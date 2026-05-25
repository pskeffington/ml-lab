"""Export experiment results to durable analysis artifacts."""

from __future__ import annotations

import csv
from pathlib import Path

from ml_lab.experiments.synthetic_experiment import ConditionResult


CSV_FIELDS = [
    "condition",
    "learner_count",
    "task_count",
    "immediate_accuracy",
    "transfer_accuracy",
    "calibration_error",
    "overreliance_score",
    "premature_help_rate",
    "unsupported_drop_rate",
]


def export_condition_results_csv(results: list[ConditionResult], output_path: Path) -> Path:
    """Export condition-level synthetic experiment results to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    "condition": result.condition.value,
                    "learner_count": result.learner_count,
                    "task_count": result.task_count,
                    "immediate_accuracy": result.immediate_accuracy,
                    "transfer_accuracy": result.transfer_accuracy,
                    "calibration_error": result.calibration_error,
                    "overreliance_score": result.overreliance_score,
                    "premature_help_rate": result.premature_help_rate,
                    "unsupported_drop_rate": result.unsupported_drop_rate,
                }
            )

    return output_path
