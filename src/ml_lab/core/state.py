"""Learner-state representation for adaptive scaffolding experiments."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class LearnerState:
    """Snapshot of a learner during a task sequence.

    The state is intentionally small for the first implementation pass. It can be
    extended as the experiment adds richer traces or cognitive-load measures.
    """

    learner_id: str
    task_id: str
    correctness: float
    confidence: float
    latency_seconds: float
    hint_count: int = 0
    error_type: str | None = None
    metadata: dict[str, str | int | float | bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not 0.0 <= self.correctness <= 1.0:
            raise ValueError("correctness must be between 0.0 and 1.0")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if self.latency_seconds < 0:
            raise ValueError("latency_seconds must be non-negative")
        if self.hint_count < 0:
            raise ValueError("hint_count must be non-negative")

    @property
    def calibration_error(self) -> float:
        """Absolute gap between confidence and observed correctness."""

        return abs(self.confidence - self.correctness)

    @property
    def needs_support(self) -> bool:
        """Return whether the learner appears to need additional support."""

        return self.correctness < 0.7 or self.calibration_error > 0.3
