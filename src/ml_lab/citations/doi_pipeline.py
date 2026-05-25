"""Configurable DOI verification pipeline."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from ml_lab.citations.doi_verifier import (
    DoiVerificationResult,
    discover_citation_candidates,
    verify_candidates,
    write_markdown_report,
    write_results_csv,
)


@dataclass(frozen=True)
class DoiPipelinePolicy:
    """Pass/fail policy for DOI verification results."""

    allow_missing_doi: bool = True
    allow_crossref_errors: bool = True
    fail_on_unverified_existing_doi: bool = False
    max_missing_doi_candidates: int | None = None


@dataclass(frozen=True)
class DoiPipelineOutputs:
    """Output artifact paths for the DOI pipeline."""

    markdown: str = "reports/generated/doi_verification_report.md"
    csv: str = "reports/generated/doi_verification_report.csv"
    summary_json: str = "reports/generated/doi_verification_summary.json"


@dataclass(frozen=True)
class DoiPipelineConfig:
    """Complete DOI pipeline configuration."""

    scan_paths: list[str]
    outputs: DoiPipelineOutputs
    policy: DoiPipelinePolicy
    use_crossref: bool = False


@dataclass(frozen=True)
class DoiPipelineSummary:
    """CI-friendly DOI pipeline summary."""

    candidate_count: int
    status_counts: dict[str, int]
    passed: bool
    failures: list[str]


def load_pipeline_config(path: Path) -> DoiPipelineConfig:
    """Load DOI pipeline configuration from JSON."""
    payload: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    outputs_payload = payload.get("outputs", {})
    policy_payload = payload.get("policy", {})
    remote_payload = payload.get("remote", {})

    return DoiPipelineConfig(
        scan_paths=list(payload.get("scan_paths", ["docs"])),
        outputs=DoiPipelineOutputs(**outputs_payload),
        policy=DoiPipelinePolicy(**policy_payload),
        use_crossref=bool(remote_payload.get("use_crossref", False)),
    )


def summarize_results(
    results: list[DoiVerificationResult],
    policy: DoiPipelinePolicy,
) -> DoiPipelineSummary:
    """Summarize DOI verification results and evaluate pass/fail policy."""
    status_counts: dict[str, int] = {}
    for result in results:
        status_counts[result.status] = status_counts.get(result.status, 0) + 1

    failures: list[str] = []
    missing_count = status_counts.get("needs_doi_review", 0)
    crossref_error_count = status_counts.get("crossref_error", 0)
    unverified_count = status_counts.get("doi_present_unverified", 0)

    if not policy.allow_missing_doi and missing_count > 0:
        failures.append(f"Missing DOI candidates detected: {missing_count}")

    if policy.max_missing_doi_candidates is not None and missing_count > policy.max_missing_doi_candidates:
        failures.append(
            "Missing DOI candidate count exceeds policy: "
            f"{missing_count} > {policy.max_missing_doi_candidates}"
        )

    if not policy.allow_crossref_errors and crossref_error_count > 0:
        failures.append(f"Crossref errors detected: {crossref_error_count}")

    if policy.fail_on_unverified_existing_doi and unverified_count > 0:
        failures.append(f"Existing DOI values require remote verification: {unverified_count}")

    return DoiPipelineSummary(
        candidate_count=len(results),
        status_counts=status_counts,
        passed=not failures,
        failures=failures,
    )


def write_summary_json(summary: DoiPipelineSummary, output_path: Path) -> Path:
    """Write DOI pipeline summary JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(asdict(summary), indent=2), encoding="utf-8")
    return output_path


def run_pipeline(config: DoiPipelineConfig) -> DoiPipelineSummary:
    """Run the DOI verification pipeline and write configured artifacts."""
    candidates = discover_citation_candidates([Path(path) for path in config.scan_paths])
    results = verify_candidates(candidates, use_crossref=config.use_crossref)
    summary = summarize_results(results, config.policy)

    write_markdown_report(results, Path(config.outputs.markdown))
    write_results_csv(results, Path(config.outputs.csv))
    write_summary_json(summary, Path(config.outputs.summary_json))

    return summary
