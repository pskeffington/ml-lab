"""Outcome metrics for adaptive scaffolding experiments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from statistics import fmean

from ml_lab.core.state import LearnerState


class OutcomeMetric(ABC):
    """Interface for metrics computed from learner-state traces."""

    name: str

    @abstractmethod
    def score(self, states: list[LearnerState]) -> float:
        """Compute a metric score from ordered learner states."""


@dataclass(frozen=True, slots=True)
class CalibrationMetric(OutcomeMetric):
    """Mean absolute confidence-performance gap."""

    name: str = "calibration_error"

    def score(self, states: list[LearnerState]) -> float:
        if not states:
            raise ValueError("states must not be empty")
        return fmean(state.calibration_error for state in states)


@dataclass(frozen=True, slots=True)
class HintDependencyMetric(OutcomeMetric):
    """Mean hint count across learner states."""

    name: str = "hint_dependency"

    def score(self, states: list[LearnerState]) -> float:
        if not states:
            raise ValueError("states must not be empty")
        return fmean(state.hint_count for state in states)


def main() -> None:
    """Placeholder CLI entry point for future analysis commands."""

    print("ml-lab metrics module")
