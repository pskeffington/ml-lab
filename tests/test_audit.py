"""Tests for citation-audit records, metrics, and CSV helpers."""

from __future__ import annotations

import csv

import pytest

from ml_lab.audit import (
    AuditFinding,
    AuditRecord,
    CitationClaim,
    CitationErrorType,
    ReferenceRecord,
    estimate_absolute_reduction,
    estimate_relative_reduction,
    read_audit_records,
    summarize_audit_records,
    write_audit_summary_csv,
    write_audit_template_csv,
)


def _record(
    claim_id: str,
    arm: str,
    is_miscitation: bool,
    error_type: CitationErrorType = CitationErrorType.NONE,
    ml_flagged: bool = False,
    review_time_seconds: float = 30.0,
) -> AuditRecord:
    claim = CitationClaim(
        claim_id=claim_id,
        document_id="doc-1",
        claim_text="A claim requiring citation support.",
        citation_text="(Example, 2024)",
        reference_id="ref-1",
    )
    reference = ReferenceRecord(
        reference_id="ref-1",
        title="Example source",
        authors="Example Author",
        year=2024,
        source_available=True,
    )
    finding = AuditFinding(
        claim_id=claim_id,
        reviewer_id="reviewer-1",
        is_miscitation=is_miscitation,
        error_type=error_type,
    )
    return AuditRecord(
        claim=claim,
        reference=reference,
        arm=arm,
        adjudicated_finding=finding,
        ml_flagged=ml_flagged,
        review_time_seconds=review_time_seconds,
    )


def test_audit_finding_requires_error_type_for_miscitation() -> None:
    with pytest.raises(ValueError, match="miscitations require"):
        AuditFinding(
            claim_id="claim-1",
            reviewer_id="reviewer-1",
            is_miscitation=True,
            error_type=CitationErrorType.NONE,
        )


def test_summarize_audit_records_by_arm() -> None:
    records = [
        _record("claim-1", "baseline", True, CitationErrorType.UNSUPPORTED_CLAIM),
        _record("claim-2", "baseline", False),
        _record("claim-3", "ml_audit", False, ml_flagged=True),
        _record("claim-4", "ml_audit", False, ml_flagged=True),
    ]

    summaries = summarize_audit_records(records)

    assert [summary.arm for summary in summaries] == ["baseline", "ml_audit"]
    assert summaries[0].mis_citation_rate == pytest.approx(0.5)
    assert summaries[1].mis_citation_rate == pytest.approx(0.0)
    assert summaries[1].ml_flag_rate == pytest.approx(1.0)


def test_estimate_absolute_and_relative_reduction() -> None:
    summaries = summarize_audit_records(
        [
            _record("claim-1", "baseline", True, CitationErrorType.WRONG_SOURCE),
            _record("claim-2", "baseline", False),
            _record("claim-3", "ml_audit", False),
            _record("claim-4", "ml_audit", False),
        ]
    )

    assert estimate_absolute_reduction(summaries, "baseline", "ml_audit") == pytest.approx(0.5)
    assert estimate_relative_reduction(summaries, "baseline", "ml_audit") == pytest.approx(1.0)


def test_audit_csv_round_trip(tmp_path) -> None:
    template_path = tmp_path / "audit_template.csv"
    audit_path = tmp_path / "audit_records.csv"
    summary_path = tmp_path / "audit_summary.csv"
    write_audit_template_csv(template_path)

    with template_path.open(newline="", encoding="utf-8") as file:
        fieldnames = list(csv.DictReader(file).fieldnames or [])

    rows = [
        {
            "claim_id": "claim-1",
            "document_id": "doc-1",
            "claim_text": "A claim requiring citation support.",
            "citation_text": "(Example, 2024)",
            "reference_id": "ref-1",
            "reference_title": "Example source",
            "reference_authors": "Example Author",
            "reference_year": "2024",
            "doi": "",
            "url": "",
            "source_available": "true",
            "arm": "baseline",
            "reviewer_id": "reviewer-1",
            "is_miscitation": "true",
            "error_type": "unsupported_claim",
            "confidence": "1.0",
            "ml_flagged": "false",
            "review_time_seconds": "45.0",
            "notes": "",
        }
    ]
    with audit_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    records = read_audit_records(audit_path)
    summaries = summarize_audit_records(records)
    write_audit_summary_csv(summaries, summary_path)

    assert len(records) == 1
    assert records[0].is_miscitation is True
    assert summaries[0].n_miscitations == 1
    assert summary_path.exists()
