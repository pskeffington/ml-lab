"""Scaffold policy interfaces and baseline implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ml_lab.core.actions import ScaffoldAction
from ml_lab.core.state import LearnerState


class ScaffoldPolicy(ABC):
    """Interface for policies that choose scaffold actions from learner state."""

    @abstractmethod
    def select_action(self, state: LearnerState) -> ScaffoldAction:
        """Select the next support action for a learner state."""


@dataclass(frozen=True, slots=True)
class RuleBasedScaffoldPolicy(ScaffoldPolicy):
    """Transparent baseline policy for early experiments and tests."""

    high_support_threshold: float = 0.5
    calibration_threshold: float = 0.3

    def select_action(self, state: LearnerState) -> ScaffoldAction:
        if state.correctness < self.high_support_threshold:
            return ScaffoldAction(
                name="worked_example",
                description="Provide a worked example before the learner retries.",
                intensity=0.9,
            )
        if state.calibration_error > self.calibration_threshold:
            return ScaffoldAction(
                name="reflection_prompt",
                description="Ask the learner to compare confidence against evidence.",
                intensity=0.6,
            )
        if state.needs_support:
            return ScaffoldAction(
                name="strategic_hint",
                description="Provide a targeted hint while preserving productive effort.",
                intensity=0.5,
            )
        return ScaffoldAction(
            name="continue",
            description="Allow the learner to continue without additional support.",
            intensity=0.0,
        )
