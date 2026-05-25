"""Statistical summaries for scaffold experiment condition results."""

from __future__ import annotations

from dataclasses import dataclass

from ml_lab.experiments.conditions import ExperimentCondition
from ml_lab.experiments.synthetic_experiment import ConditionResult


@dataclass(frozen=True)
class ConditionDelta:
    """Difference between a condition and a baseline condition."""

    condition: ExperimentCondition
    baseline: ExperimentCondition
    transfer_accuracy_delta: float
    calibration_error_delta: float
    overreliance_score_delta: float
    immediate_accuracy_delta: float


@dataclass(frozen=True)
class RankedCondition:
    """Condition ranked by the project learning-independence objective."""

    condition: ExperimentCondition
    independence_score: float
    transfer_accuracy: float
    calibration_error: float
    overreliance_score: float


def compute_condition_deltas(
    results: list[ConditionResult],
    baseline: ExperimentCondition = ExperimentCondition.UNRESTRICTED_AI,
) -> list[ConditionDelta]:
    """Compute condition-level deltas against a baseline condition."""
    result_by_condition = {result.condition: result for result in results}
    if baseline not in result_by_condition:
        raise ValueError(f"Baseline condition {baseline.value!r} not found in results.")

    baseline_result = result_by_condition[baseline]
    deltas: list[ConditionDelta] = []
    for result in results:
        if result.condition == baseline:
            continue
        deltas.append(
            ConditionDelta(
                condition=result.condition,
                baseline=baseline,
                transfer_accuracy_delta=result.transfer_accuracy - baseline_result.transfer_accuracy,
                calibration_error_delta=result.calibration_error - baseline_result.calibration_error,
                overreliance_score_delta=result.overreliance_score - baseline_result.overreliance_score,
                immediate_accuracy_delta=result.immediate_accuracy - baseline_result.immediate_accuracy,
            )
        )
    return deltas


def rank_conditions_for_independence(results: list[ConditionResult]) -> list[RankedCondition]:
    """Rank conditions by transfer with penalties for miscalibration and overreliance.

    Higher scores are better. The score intentionally values independent learning
    outcomes over immediate task completion.
    """
    ranked = [
        RankedCondition(
            condition=result.condition,
            independence_score=(
                result.transfer_accuracy
                - 0.50 * result.calibration_error
                - 0.50 * result.overreliance_score
            ),
            transfer_accuracy=result.transfer_accuracy,
            calibration_error=result.calibration_error,
            overreliance_score=result.overreliance_score,
        )
        for result in results
    ]
    return sorted(ranked, key=lambda item: item.independence_score, reverse=True)


def format_delta_table(deltas: list[ConditionDelta]) -> str:
    """Format condition deltas as a markdown table."""
    rows = [
        "| Condition | Baseline | Transfer Delta | Calibration Error Delta | Overreliance Delta | Immediate Delta |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for delta in deltas:
        rows.append(
            "| "
            f"{delta.condition.value} | "
            f"{delta.baseline.value} | "
            f"{delta.transfer_accuracy_delta:.3f} | "
            f"{delta.calibration_error_delta:.3f} | "
            f"{delta.overreliance_score_delta:.3f} | "
            f"{delta.immediate_accuracy_delta:.3f} |"
        )
    return "\n".join(rows)


def format_ranked_conditions(ranked: list[RankedCondition]) -> str:
    """Format independence-ranked conditions as a markdown table."""
    rows = [
        "| Rank | Condition | Independence Score | Transfer Accuracy | Calibration Error | Overreliance |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for index, condition in enumerate(ranked, start=1):
        rows.append(
            "| "
            f"{index} | "
            f"{condition.condition.value} | "
            f"{condition.independence_score:.3f} | "
            f"{condition.transfer_accuracy:.3f} | "
            f"{condition.calibration_error:.3f} | "
            f"{condition.overreliance_score:.3f} |"
        )
    return "\n".join(rows)
