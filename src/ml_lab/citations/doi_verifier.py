"""DOI verification helpers for markdown citation files.

The verifier is intentionally lightweight and standard-library only. It can scan
repository markdown files, detect existing DOI strings, identify source rows that
need manual verification, and optionally query Crossref for candidate matches.
"""

from __future__ import annotations

import csv
import json
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DOI_PATTERN = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
MARKDOWN_TABLE_ROW_PATTERN = re.compile(r"^\|(?P<cells>.*)\|$")


@dataclass(frozen=True)
class CitationCandidate:
    """Citation-like row discovered in a markdown file."""

    path: str
    line_number: int
    raw_text: str
    extracted_doi: str | None


@dataclass(frozen=True)
class DoiVerificationResult:
    """Verification result for one citation candidate."""

    path: str
    line_number: int
    raw_text: str
    extracted_doi: str | None
    status: str
    matched_title: str | None = None
    matched_doi: str | None = None
    confidence: float | None = None
    note: str | None = None


def find_dois(text: str) -> list[str]:
    """Return DOI strings found in text."""
    return [match.group(0).rstrip(".,;)]") for match in DOI_PATTERN.finditer(text)]


def iter_markdown_files(paths: Iterable[Path]) -> Iterable[Path]:
    """Yield markdown files from paths, recursively for directories."""
    for path in paths:
        if path.is_dir():
            yield from sorted(path.rglob("*.md"))
        elif path.suffix.lower() == ".md":
            yield path


def discover_citation_candidates(paths: Iterable[Path]) -> list[CitationCandidate]:
    """Discover citation-like markdown rows and DOI-bearing lines."""
    candidates: list[CitationCandidate] = []
    for markdown_path in iter_markdown_files(paths):
        for line_number, line in enumerate(markdown_path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.strip()
            if not stripped:
                continue

            doi_matches = find_dois(stripped)
            is_table_row = bool(MARKDOWN_TABLE_ROW_PATTERN.match(stripped))
            looks_like_source_row = is_table_row and not stripped.startswith("|---")
            has_year = bool(re.search(r"\b(19|20)\d{2}\b", stripped))

            if doi_matches or (looks_like_source_row and has_year):
                candidates.append(
                    CitationCandidate(
                        path=str(markdown_path),
                        line_number=line_number,
                        raw_text=stripped,
                        extracted_doi=doi_matches[0] if doi_matches else None,
                    )
                )
    return candidates


def query_crossref(candidate_text: str, rows: int = 1) -> dict | None:
    """Query Crossref for a citation candidate and return the first item.

    This function performs a live network call. It is isolated so tests can avoid
    network dependency and so callers can disable remote verification.
    """
    query = urllib.parse.urlencode({"query.bibliographic": candidate_text, "rows": str(rows)})
    url = f"https://api.crossref.org/works?{query}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ml-lab-doi-verifier/0.1 (mailto:research@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))
    items = payload.get("message", {}).get("items", [])
    return items[0] if items else None


def verify_candidates(
    candidates: list[CitationCandidate],
    use_crossref: bool = False,
) -> list[DoiVerificationResult]:
    """Verify citation candidates locally and optionally with Crossref."""
    results: list[DoiVerificationResult] = []
    for candidate in candidates:
        if candidate.extracted_doi and not use_crossref:
            results.append(
                DoiVerificationResult(
                    path=candidate.path,
                    line_number=candidate.line_number,
                    raw_text=candidate.raw_text,
                    extracted_doi=candidate.extracted_doi,
                    status="doi_present_unverified",
                    note="DOI detected locally; run with remote verification to check metadata.",
                )
            )
            continue

        if not use_crossref:
            results.append(
                DoiVerificationResult(
                    path=candidate.path,
                    line_number=candidate.line_number,
                    raw_text=candidate.raw_text,
                    extracted_doi=candidate.extracted_doi,
                    status="needs_doi_review",
                    note="No DOI detected locally.",
                )
            )
            continue

        try:
            item = query_crossref(candidate.raw_text)
        except Exception as exc:  # pragma: no cover - defensive around network calls
            results.append(
                DoiVerificationResult(
                    path=candidate.path,
                    line_number=candidate.line_number,
                    raw_text=candidate.raw_text,
                    extracted_doi=candidate.extracted_doi,
                    status="crossref_error",
                    note=str(exc),
                )
            )
            continue

        if not item:
            results.append(
                DoiVerificationResult(
                    path=candidate.path,
                    line_number=candidate.line_number,
                    raw_text=candidate.raw_text,
                    extracted_doi=candidate.extracted_doi,
                    status="no_crossref_match",
                )
            )
            continue

        titles = item.get("title") or []
        matched_title = titles[0] if titles else None
        matched_doi = item.get("DOI")
        score = item.get("score")
        confidence = float(score) if isinstance(score, int | float) else None
        status = "crossref_candidate_found" if matched_doi else "crossref_match_without_doi"

        results.append(
            DoiVerificationResult(
                path=candidate.path,
                line_number=candidate.line_number,
                raw_text=candidate.raw_text,
                extracted_doi=candidate.extracted_doi,
                status=status,
                matched_title=matched_title,
                matched_doi=matched_doi,
                confidence=confidence,
            )
        )
    return results


def write_results_csv(results: list[DoiVerificationResult], output_path: Path) -> Path:
    """Write DOI verification results to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "path",
        "line_number",
        "status",
        "extracted_doi",
        "matched_doi",
        "matched_title",
        "confidence",
        "note",
        "raw_text",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({field: getattr(result, field) for field in fieldnames})
    return output_path


def build_markdown_report(results: list[DoiVerificationResult]) -> str:
    """Build a concise markdown DOI verification report."""
    status_counts: dict[str, int] = {}
    for result in results:
        status_counts[result.status] = status_counts.get(result.status, 0) + 1

    lines = ["# DOI Verification Report", "", "## Status Counts", ""]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`: {count}")

    lines.extend(
        [
            "",
            "## Candidate Details",
            "",
            "| File | Line | Status | Extracted DOI | Matched DOI | Matched Title |",
            "|---|---:|---|---|---|---|",
        ]
    )
    for result in results:
        lines.append(
            "| "
            f"{result.path} | "
            f"{result.line_number} | "
            f"{result.status} | "
            f"{result.extracted_doi or ''} | "
            f"{result.matched_doi or ''} | "
            f"{(result.matched_title or '').replace('|', '/')} |"
        )
    return "\n".join(lines) + "\n"


def write_markdown_report(results: list[DoiVerificationResult], output_path: Path) -> Path:
    """Write DOI verification results to markdown."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_markdown_report(results), encoding="utf-8")
    return output_path
