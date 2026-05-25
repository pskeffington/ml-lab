"""Scaffold primitives and best-practice categories."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ScaffoldType(StrEnum):
    """Pedagogical scaffold categories ordered from light to heavy support."""

    ORIENTATION = "orientation"
    CONCEPT_ACTIVATION = "concept_activation"
    DIAGNOSTIC_QUESTION = "diagnostic_question"
    STRATEGY_HINT = "strategy_hint"
    MICRO_EXAMPLE = "micro_example"
    PARTIAL_SOLUTION = "partial_solution"
    FULL_EXPLANATION = "full_explanation"


@dataclass(frozen=True)
class Scaffold:
    """A scaffold selected by a policy for a learner-task state."""

    scaffold_type: ScaffoldType
    intensity: float
    message: str
    requires_reflection: bool
    policy_reason: str

    @property
    def is_high_intensity(self) -> bool:
        """Return whether this scaffold risks replacing learner work."""
        return self.intensity >= 0.70
