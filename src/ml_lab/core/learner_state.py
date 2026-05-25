"""Learner-state primitives for adaptive scaffolding policies."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LearnerState:
    """Observable learner state used by scaffold policies.

    The fields are intentionally compact so policies remain auditable and testable.
    Values are normalized to 0.0-1.0 where practical.
    """

    knowledge_estimate: float
    confidence: float
    cognitive_load: float
    hint_dependency: float
    attempts: int
    elapsed_seconds: float

    def needs_support(self) -> bool:
        """Return whether the learner likely needs some scaffold."""
        low_knowledge = self.knowledge_estimate < 0.55
        high_load = self.cognitive_load > 0.70
        repeated_attempts = self.attempts >= 2
        return low_knowledge or high_load or repeated_attempts

    def is_ready_for_fading(self) -> bool:
        """Return whether support should be reduced rather than increased."""
        return (
            self.knowledge_estimate >= 0.70
            and self.confidence >= 0.55
            and self.cognitive_load <= 0.55
            and self.hint_dependency <= 0.40
        )

    def has_overreliance_risk(self) -> bool:
        """Return whether learner behavior suggests dependence on help."""
        return self.hint_dependency >= 0.70 and self.attempts <= 1
