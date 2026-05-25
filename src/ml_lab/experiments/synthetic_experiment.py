"""Run a synthetic experiment comparing scaffold-design conditions."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random

from ml_lab.experiments.conditions import ConditionConfig, ExperimentCondition, default_conditions
from ml_lab.evaluation.calibration_metrics import CalibrationEvent, compute_calibration
from ml_lab.evaluation.overreliance_metrics import ScaffoldUseEvent, compute_overreliance


@dataclass(frozen=True)
class ConditionResult:
    """Summary result for one experimental condition."""

    condition: ExperimentCondition
    learner_count: int
    task_count: int
    immediate_accuracy: float
    transfer_accuracy: float
    calibration_error: float
    overreliance_score: float
    premature_help_rate: float
    unsupported_drop_rate: float


def _bounded(value: float) -> float:
    """Clamp values into a normalized 0.0-1.0 range."""
    return max(0.0, min(1.0, value))


class SyntheticScaffoldingExperiment:
    """Synthetic pilot experiment for scaffold best-practice comparisons."""

    def __init__(
        self,
        learner_count: int = 100,
        tasks_per_learner: int = 10,
        seed: int = 42,
        conditions: list[ConditionConfig] | None = None,
    ) -> None:
        self.learner_count = learner_count
        self.tasks_per_learner = tasks_per_learner
        self._rng = Random(seed)
        self.conditions = conditions or default_conditions()

    def run(self) -> list[ConditionResult]:
        """Run every condition and return aggregate summary results."""
        return [self._run_condition(condition) for condition in self.conditions]

    def _run_condition(self, condition: ConditionConfig) -> ConditionResult:
        calibration_events: list[CalibrationEvent] = []
        scaffold_events: list[ScaffoldUseEvent] = []
        immediate_correct: list[bool] = []
        transfer_correct: list[bool] = []

        for _learner_id in range(self.learner_count):
            knowledge = self._rng.uniform(0.25, 0.75)
            hint_dependency = condition.base_hint_dependency

            for _task_id in range(self.tasks_per_learner):
                difficulty = self._rng.uniform(0.30, 0.85)
                productive_struggle_bonus = 0.04 if condition.timing_gate else -0.02
                metacognitive_bonus = 0.05 if condition.metacognitive_prompting else 0.00
                adaptive_bonus = 0.06 if condition.adaptive else 0.00
                fading_transfer_bonus = 0.08 if condition.fading else -0.03

                help_intensity = self._help_intensity(condition, hint_dependency)
                attempted_before_help = self._attempted_before_help(condition, hint_dependency)

                immediate_probability = _bounded(
                    knowledge
                    - difficulty
                    + 0.50
                    + adaptive_bonus
                    + metacognitive_bonus
                    + (0.12 * help_intensity if condition.scaffold_access else 0.00)
                )
                immediate = self._rng.random() < immediate_probability

                transfer_probability = _bounded(
                    knowledge
                    - difficulty
                    + 0.48
                    + productive_struggle_bonus
                    + metacognitive_bonus
                    + fading_transfer_bonus
                    - (0.10 * hint_dependency)
                    - (0.06 if help_intensity >= 0.70 else 0.00)
                )
                transfer = self._rng.random() < transfer_probability

                confidence = _bounded(
                    knowledge
                    + (0.20 * help_intensity)
                    - (0.08 if difficulty > knowledge else 0.00)
                    + self._rng.uniform(-0.10, 0.12)
                )

                immediate_correct.append(immediate)
                transfer_correct.append(transfer)
                calibration_events.append(CalibrationEvent(confidence=confidence, correct=immediate))

                if condition.scaffold_access:
                    scaffold_events.append(
                        ScaffoldUseEvent(
                            attempted_before_help=attempted_before_help,
                            scaffold_intensity=help_intensity,
                            response_correct=immediate,
                            post_scaffold_correct=immediate,
                            independent_followup_correct=transfer,
                            copied_scaffold_text=self._rng.random() < max(0.01, help_intensity - 0.75),
                        )
                    )

                knowledge = _bounded(knowledge + (0.035 if transfer else -0.005))
                if condition.fading and transfer:
                    hint_dependency = _bounded(hint_dependency - 0.015)
                elif condition.scaffold_access and not attempted_before_help:
                    hint_dependency = _bounded(hint_dependency + 0.015)

        calibration = compute_calibration(calibration_events)
        overreliance = compute_overreliance(scaffold_events)

        return ConditionResult(
            condition=condition.condition,
            learner_count=self.learner_count,
            task_count=self.learner_count * self.tasks_per_learner,
            immediate_accuracy=sum(immediate_correct) / len(immediate_correct),
            transfer_accuracy=sum(transfer_correct) / len(transfer_correct),
            calibration_error=calibration.absolute_calibration_error,
            overreliance_score=overreliance.composite_overreliance_score,
            premature_help_rate=overreliance.premature_help_rate,
            unsupported_drop_rate=overreliance.unsupported_drop_rate,
        )

    def _help_intensity(self, condition: ConditionConfig, hint_dependency: float) -> float:
        if not condition.scaffold_access:
            return 0.0
        if condition.condition == ExperimentCondition.UNRESTRICTED_AI:
            return _bounded(0.75 + self._rng.uniform(-0.10, 0.15))
        if condition.condition == ExperimentCondition.STATIC_SCAFFOLDING:
            return 0.50
        if condition.condition == ExperimentCondition.ADAPTIVE_POLICY:
            return _bounded(0.45 + hint_dependency * 0.20)
        if condition.condition == ExperimentCondition.TIMING_AND_FADING:
            return _bounded(0.40 - hint_dependency * 0.10)
        return 0.0

    def _attempted_before_help(self, condition: ConditionConfig, hint_dependency: float) -> bool:
        if not condition.scaffold_access:
            return True
        if condition.timing_gate:
            return self._rng.random() < 0.88
        return self._rng.random() > hint_dependency


def format_results_table(results: list[ConditionResult]) -> str:
    """Format synthetic results as a markdown table."""
    rows = [
        "| Condition | Immediate Accuracy | Transfer Accuracy | Calibration Error | Overreliance | Premature Help | Unsupported Drop |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for result in results:
        rows.append(
            "| "
            f"{result.condition.value} | "
            f"{result.immediate_accuracy:.3f} | "
            f"{result.transfer_accuracy:.3f} | "
            f"{result.calibration_error:.3f} | "
            f"{result.overreliance_score:.3f} | "
            f"{result.premature_help_rate:.3f} | "
            f"{result.unsupported_drop_rate:.3f} |"
        )
    return "\n".join(rows)


def main() -> None:
    """Run the synthetic experiment and print a markdown summary table."""
    experiment = SyntheticScaffoldingExperiment()
    print(format_results_table(experiment.run()))


if __name__ == "__main__":
    main()
