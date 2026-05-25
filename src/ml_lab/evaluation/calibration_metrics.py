"""Calibration metrics for scaffolded learning experiments."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalibrationEvent:
    """Confidence-correctness observation for a learner response."""

    confidence: float
    correct: bool


@dataclass(frozen=True)
class CalibrationReport:
    """Aggregate confidence calibration indicators."""

    mean_confidence: float
    accuracy: float
    absolute_calibration_error: float
    overconfidence: float


def compute_calibration(events: list[CalibrationEvent]) -> CalibrationReport:
    """Compute simple calibration metrics from learner confidence events."""
    if not events:
        return CalibrationReport(
            mean_confidence=0.0,
            accuracy=0.0,
            absolute_calibration_error=0.0,
            overconfidence=0.0,
        )

    mean_confidence = sum(event.confidence for event in events) / len(events)
    accuracy = sum(event.correct for event in events) / len(events)
    calibration_error = abs(mean_confidence - accuracy)
    overconfidence = max(0.0, mean_confidence - accuracy)

    return CalibrationReport(
        mean_confidence=mean_confidence,
        accuracy=accuracy,
        absolute_calibration_error=calibration_error,
        overconfidence=overconfidence,
    )
