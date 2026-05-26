"""CSV input and output helpers for citation-audit studies."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from ml_lab.audit.metrics import AuditSummary
from ml_lab.audit.records import (
    AuditFinding,
    AuditRecord,
    CitationClaim,
    CitationErrorType,
    ReferenceRecord,
)

AUDIT_CSV_FIELDS = (
    "claim_id",
    "document_id",
    "claim_text",
    "citation_text",
    "reference_id",
    "reference_title",
    "reference_authors",
    "reference_year",
    "doi",
    "url",
    "source_available",
    "arm",
    "reviewer_id",
    "is_miscitation",
    "error_type",
    "confidence",
    "ml_flagged",
    "review_time_seconds",
    "notes",
)


def read_audit_records(path: str | Path) -> list[AuditRecord]:
    """Read adjudicated citation-audit records from CSV."""

    input_path = Path(path)
    with input_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    return [audit_record_from_row(row) for row in rows]


def audit_record_from_row(row: dict[str, str]) -> AuditRecord:
    """Build an audit record from one CSV row."""

    _require_fields(row)
    claim = CitationClaim(
        claim_id=row["claim_id"],
        document_id=row["document_id"],
        claim_text=row["claim_text"],
        citation_text=row["citation_text"],
        reference_id=row["reference_id"],
    )
    reference = ReferenceRecord(
        reference_id=row["reference_id"],
        title=row["reference_title"],
        authors=row.get("reference_authors", ""),
        year=_optional_int(row.get("reference_year", "")),
        doi=_optional_str(row.get("doi", "")),
        url=_optional_str(row.get("url", "")),
        source_available=_parse_bool(row.get("source_available", "false")),
    )
    finding = AuditFinding(
        claim_id=row["claim_id"],
        reviewer_id=row["reviewer_id"],
        is_miscitation=_parse_bool(row["is_miscitation"]),
        error_type=CitationErrorType(row.get("error_type", "none") or "none"),
        confidence=float(row.get("confidence", "1.0") or 1.0),
        notes=row.get("notes", ""),
    )
    return AuditRecord(
        claim=claim,
        reference=reference,
        arm=row["arm"],
        adjudicated_finding=finding,
        ml_flagged=_parse_bool(row.get("ml_flagged", "false")),
        review_time_seconds=_optional_float(row.get("review_time_seconds", "")),
    )


def write_audit_summary_csv(summaries: Iterable[AuditSummary], path: str | Path) -> None:
    """Write audit summaries to CSV."""

    rows = [summary.as_dict() for summary in summaries]
    if not rows:
        raise ValueError("summaries must not be empty")
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_audit_template_csv(path: str | Path) -> None:
    """Write an empty citation-audit CSV template."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(AUDIT_CSV_FIELDS))
        writer.writeheader()


def _require_fields(row: dict[str, str]) -> None:
    missing = [field for field in AUDIT_CSV_FIELDS if field not in row]
    if missing:
        raise ValueError(f"missing audit CSV fields: {', '.join(missing)}")


def _parse_bool(value: str) -> bool:
    normalized = str(value).strip().lower()
    if normalized in {"true", "1", "yes", "y"}:
        return True
    if normalized in {"false", "0", "no", "n", ""}:
        return False
    raise ValueError(f"invalid boolean value: {value}")


def _optional_str(value: str) -> str | None:
    stripped = str(value).strip()
    return stripped or None


def _optional_int(value: str) -> int | None:
    stripped = str(value).strip()
    return int(stripped) if stripped else None


def _optional_float(value: str) -> float | None:
    stripped = str(value).strip()
    return float(stripped) if stripped else None
