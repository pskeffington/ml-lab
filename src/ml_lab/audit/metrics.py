"""Metrics for citation-audit studies."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from statistics import fmean
from typing import Iterable

from ml_lab.audit.records import AuditRecord, CitationErrorType


@dataclass(frozen=True, slots=True)
class AuditSummary:
    """Aggregate audit results for one workflow arm."""

    arm: str
    n_claims: int
    n_miscitations: int
    mis_citation_rate: float
    ml_flag_rate: float
    mean_review_time_seconds: float | None
    unsupported_claim_rate: float
    fabricated_source_rate: float
    metadata_error_rate: float

    def as_dict(self) -> dict[str, str | int | float | None]:
        """Return a CSV-friendly summary."""

        return {
            "arm": self.arm,
            "n_claims": self.n_claims,
            "n_miscitations": self.n_miscitations,
            "mis_citation_rate": self.mis_citation_rate,
            "ml_flag_rate": self.ml_flag_rate,
            "mean_review_time_seconds": self.mean_review_time_seconds,
            "unsupported_claim_rate": self.unsupported_claim_rate,
            "fabricated_source_rate": self.fabricated_source_rate,
            "metadata_error_rate": self.metadata_error_rate,
        }


def summarize_audit_records(records: Iterable[AuditRecord]) -> list[AuditSummary]:
    """Summarize adjudicated citation-audit records by study arm."""

    grouped: dict[str, list[AuditRecord]] = defaultdict(list)
    for record in records:
        grouped[record.arm].append(record)

    if not grouped:
        raise ValueError("records must not be empty")

    return [_summarize_arm(arm, arm_records) for arm, arm_records in sorted(grouped.items())]


def estimate_absolute_reduction(
    summaries: Iterable[AuditSummary],
    control_arm: str,
    audit_arm: str,
) -> float:
    """Estimate percentage-point reduction in mis-citation rate."""

    by_arm = {summary.arm: summary for summary in summaries}
    if control_arm not in by_arm:
        raise ValueError(f"missing control arm: {control_arm}")
    if audit_arm not in by_arm:
        raise ValueError(f"missing audit arm: {audit_arm}")
    return by_arm[control_arm].mis_citation_rate - by_arm[audit_arm].mis_citation_rate


def estimate_relative_reduction(
    summaries: Iterable[AuditSummary],
    control_arm: str,
    audit_arm: str,
) -> float:
    """Estimate relative reduction in mis-citation rate."""

    by_arm = {summary.arm: summary for summary in summaries}
    if control_arm not in by_arm:
        raise ValueError(f"missing control arm: {control_arm}")
    if audit_arm not in by_arm:
        raise ValueError(f"missing audit arm: {audit_arm}")
    control_rate = by_arm[control_arm].mis_citation_rate
    if control_rate == 0:
        return 0.0
    return (control_rate - by_arm[audit_arm].mis_citation_rate) / control_rate


def _summarize_arm(arm: str, records: list[AuditRecord]) -> AuditSummary:
    n_claims = len(records)
    if n_claims == 0:
        raise ValueError("arm records must not be empty")

    n_miscitations = sum(record.is_miscitation for record in records)
    ml_flags = sum(record.ml_flagged for record in records)
    error_counts = Counter(record.error_type for record in records)
    review_times = [record.review_time_seconds for record in records if record.review_time_seconds is not None]

    return AuditSummary(
        arm=arm,
        n_claims=n_claims,
        n_miscitations=n_miscitations,
        mis_citation_rate=n_miscitations / n_claims,
        ml_flag_rate=ml_flags / n_claims,
        mean_review_time_seconds=fmean(review_times) if review_times else None,
        unsupported_claim_rate=error_counts[CitationErrorType.UNSUPPORTED_CLAIM] / n_claims,
        fabricated_source_rate=error_counts[CitationErrorType.FABRICATED_SOURCE] / n_claims,
        metadata_error_rate=error_counts[CitationErrorType.METADATA_ERROR] / n_claims,
    )
