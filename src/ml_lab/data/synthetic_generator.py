"""Synthetic trace generation for scaffold-policy experiments."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random

from ml_lab.core.learner_state import LearnerState
from ml_lab.core.scaffold_policy import ScaffoldPolicy, TimingAndFadingPolicy
from ml_lab.evaluation.calibration_metrics import CalibrationEvent
from ml_lab.evaluation.overreliance_metrics import ScaffoldUseEvent


@dataclass(frozen=True)
class SyntheticTrace:
    """Synthetic learner trace for reproducible scaffold-policy evaluation."""

    learner_id: str
    calibration_events: list[CalibrationEvent]
    scaffold_events: list[ScaffoldUseEvent]


def _bounded(value: float) -> float:
    """Clamp a synthetic value to the normalized 0.0-1.0 range."""
    return max(0.0, min(1.0, value))


class SyntheticTraceGenerator:
    """Generate reproducible learner traces for early-stage experiments."""

    def __init__(self, seed: int = 42, policy: ScaffoldPolicy | None = None) -> None:
        self._rng = Random(seed)
        self._policy = policy or TimingAndFadingPolicy()

    def generate(self, learner_count: int = 25, tasks_per_learner: int = 8) -> list[SyntheticTrace]:
        """Generate synthetic traces for learners across repeated tasks."""
        traces: list[SyntheticTrace] = []
        for learner_index in range(learner_count):
            baseline_knowledge = self._rng.uniform(0.25, 0.80)
            hint_dependency = self._rng.uniform(0.10, 0.65)
            calibration_events: list[CalibrationEvent] = []
            scaffold_events: list[ScaffoldUseEvent] = []

            for task_index in range(tasks_per_learner):
                task_difficulty = self._rng.uniform(0.30, 0.85)
                attempts = self._rng.randint(0, 3)
                cognitive_load = _bounded(task_difficulty - baseline_knowledge + self._rng.uniform(0.25, 0.55))
                confidence = _bounded(baseline_knowledge - cognitive_load / 3 + self._rng.uniform(-0.10, 0.15))

                learner_state = LearnerState(
                    knowledge_estimate=baseline_knowledge,
                    confidence=confidence,
                    cognitive_load=cognitive_load,
                    hint_dependency=hint_dependency,
                    attempts=attempts,
                    elapsed_seconds=self._rng.uniform(30, 480),
                )
                scaffold = self._policy.select(learner_state)

                independent_probability = _bounded(baseline_knowledge - task_difficulty + 0.50)
                response_correct = self._rng.random() < independent_probability
                scaffold_gain = 0.20 * scaffold.intensity if not scaffold.is_high_intensity else 0.12
                post_scaffold_probability = _bounded(independent_probability + scaffold_gain)
                post_scaffold_correct = self._rng.random() < post_scaffold_probability

                fading_bonus = 0.10 if scaffold.intensity < 0.40 else -0.05
                followup_probability = _bounded(independent_probability + fading_bonus - hint_dependency * 0.10)
                independent_followup_correct = self._rng.random() < followup_probability

                calibration_events.append(
                    CalibrationEvent(confidence=confidence, correct=response_correct)
                )
                scaffold_events.append(
                    ScaffoldUseEvent(
                        attempted_before_help=attempts > 0,
                        scaffold_intensity=scaffold.intensity,
                        response_correct=response_correct,
                        post_scaffold_correct=post_scaffold_correct,
                        independent_followup_correct=independent_followup_correct,
                        copied_scaffold_text=self._rng.random() < max(0.02, scaffold.intensity - 0.70),
                    )
                )

                baseline_knowledge = _bounded(
                    baseline_knowledge + (0.03 if independent_followup_correct else -0.01)
                )
                hint_dependency = _bounded(
                    hint_dependency + (0.02 if scaffold.is_high_intensity else -0.01)
                )

            traces.append(
                SyntheticTrace(
                    learner_id=f"synthetic-{learner_index:03d}",
                    calibration_events=calibration_events,
                    scaffold_events=scaffold_events,
                )
            )
        return traces
