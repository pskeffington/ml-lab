"""Citation and evidence-audit utilities for ml-lab."""

from ml_lab.audit.io import read_audit_records, write_audit_summary_csv, write_audit_template_csv
from ml_lab.audit.metrics import (
    AuditSummary,
    estimate_absolute_reduction,
    estimate_relative_reduction,
    summarize_audit_records,
)
from ml_lab.audit.records import (
    AuditFinding,
    AuditRecord,
    CitationClaim,
    CitationErrorType,
    ReferenceRecord,
)

__all__ = [
    "AuditFinding",
    "AuditRecord",
    "AuditSummary",
    "CitationClaim",
    "CitationErrorType",
    "ReferenceRecord",
    "estimate_absolute_reduction",
    "estimate_relative_reduction",
    "read_audit_records",
    "summarize_audit_records",
    "write_audit_summary_csv",
    "write_audit_template_csv",
]
