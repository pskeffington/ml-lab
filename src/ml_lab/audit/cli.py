"""Command-line utilities for citation-audit pilot workflows."""

from __future__ import annotations

from pathlib import Path

from ml_lab.audit.io import read_audit_records, write_audit_summary_csv, write_audit_template_csv
from ml_lab.audit.metrics import (
    estimate_absolute_reduction,
    estimate_relative_reduction,
    summarize_audit_records,
)


def template_main() -> None:
    """Write an empty citation-audit CSV template."""

    output_path = Path("outputs/citation_audit_template.csv")
    write_audit_template_csv(output_path)
    print(f"Wrote citation-audit template to {output_path}")


def analyze_main() -> None:
    """Analyze an adjudicated citation-audit CSV file."""

    input_path = Path("outputs/citation_audit_records.csv")
    summary_path = Path("outputs/citation_audit_summary.csv")
    records = read_audit_records(input_path)
    summaries = summarize_audit_records(records)
    write_audit_summary_csv(summaries, summary_path)

    for summary in summaries:
        print(summary.as_dict())

    arms = {summary.arm for summary in summaries}
    if {"baseline", "ml_audit"}.issubset(arms):
        absolute = estimate_absolute_reduction(summaries, "baseline", "ml_audit")
        relative = estimate_relative_reduction(summaries, "baseline", "ml_audit")
        print({"absolute_reduction": absolute, "relative_reduction": relative})

    print(f"Wrote citation-audit summary to {summary_path}")
