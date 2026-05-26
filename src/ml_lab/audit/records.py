"""Core records for citation-claim auditing."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class CitationErrorType(StrEnum):
    """Supported citation-error categories."""

    NONE = "none"
    UNSUPPORTED_CLAIM = "unsupported_claim"
    OVERSTATED_CLAIM = "overstated_claim"
    WRONG_SOURCE = "wrong_source"
    FABRICATED_SOURCE = "fabricated_source"
    METADATA_ERROR = "metadata_error"
    QUOTE_ERROR = "quote_error"
    SCOPE_ERROR = "scope_error"


@dataclass(frozen=True, slots=True)
class CitationClaim:
    """A claim in a document that depends on one or more citations."""

    claim_id: str
    document_id: str
    claim_text: str
    citation_text: str
    reference_id: str

    def __post_init__(self) -> None:
        for field_name in ("claim_id", "document_id", "claim_text", "citation_text", "reference_id"):
            if not str(getattr(self, field_name)).strip():
                raise ValueError(f"{field_name} must not be empty")


@dataclass(frozen=True, slots=True)
class ReferenceRecord:
    """Bibliographic record attached to a citation claim."""

    reference_id: str
    title: str
    authors: str = ""
    year: int | None = None
    doi: str | None = None
    url: str | None = None
    source_available: bool = False

    def __post_init__(self) -> None:
        if not self.reference_id.strip():
            raise ValueError("reference_id must not be empty")
        if not self.title.strip():
            raise ValueError("title must not be empty")


@dataclass(frozen=True, slots=True)
class AuditFinding:
    """Machine or human finding for a citation claim."""

    claim_id: str
    reviewer_id: str
    is_miscitation: bool
    error_type: CitationErrorType = CitationErrorType.NONE
    confidence: float = 1.0
    notes: str = ""
    metadata: dict[str, str | int | float | bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.claim_id.strip():
            raise ValueError("claim_id must not be empty")
        if not self.reviewer_id.strip():
            raise ValueError("reviewer_id must not be empty")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if not self.is_miscitation and self.error_type != CitationErrorType.NONE:
            raise ValueError("non-miscitations must use error_type=none")
        if self.is_miscitation and self.error_type == CitationErrorType.NONE:
            raise ValueError("miscitations require a non-none error_type")


@dataclass(frozen=True, slots=True)
class AuditRecord:
    """Adjudicated audit result for a citation claim under one workflow arm."""

    claim: CitationClaim
    reference: ReferenceRecord
    arm: str
    adjudicated_finding: AuditFinding
    ml_flagged: bool = False
    review_time_seconds: float | None = None

    def __post_init__(self) -> None:
        if self.claim.reference_id != self.reference.reference_id:
            raise ValueError("claim reference_id must match reference reference_id")
        if self.claim.claim_id != self.adjudicated_finding.claim_id:
            raise ValueError("claim_id must match adjudicated finding")
        if not self.arm.strip():
            raise ValueError("arm must not be empty")
        if self.review_time_seconds is not None and self.review_time_seconds < 0:
            raise ValueError("review_time_seconds must be non-negative")

    @property
    def is_miscitation(self) -> bool:
        """Return whether the adjudicated finding marks this claim as miscited."""

        return self.adjudicated_finding.is_miscitation

    @property
    def error_type(self) -> CitationErrorType:
        """Return the adjudicated citation-error type."""

        return self.adjudicated_finding.error_type
