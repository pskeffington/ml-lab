"""Markdown report generation for scaffold experiment outputs."""

from __future__ import annotations

from pathlib import Path

from ml_lab.experiments.conditions import ExperimentCondition
from ml_lab.experiments.statistical_summary import (
    compute_condition_deltas,
    format_delta_table,
    format_ranked_conditions,
    rank_conditions_for_independence,
)
from ml_lab.experiments.synthetic_experiment import ConditionResult, format_results_table


REPORT_TITLE = "Synthetic Scaffolding Experiment Report"


def build_synthetic_report(results: list[ConditionResult]) -> str:
    """Build a manuscript-facing markdown report from synthetic experiment results."""
    deltas = compute_condition_deltas(results, baseline=ExperimentCondition.UNRESTRICTED_AI)
    ranked = rank_conditions_for_independence(results)

    return "\n".join(
        [
            f"# {REPORT_TITLE}",
            "",
            "## Purpose",
            "",
            "This report summarizes a synthetic protocol-validation experiment for adaptive "
            "machine-learning scaffolding. The results validate the software workflow and "
            "analysis structure; they should not be interpreted as human-subject evidence.",
            "",
            "## Condition-Level Results",
            "",
            format_results_table(results),
            "",
            "## Deltas Against Unrestricted AI",
            "",
            "The unrestricted AI condition is the default comparison because the project "
            "tests whether disciplined scaffolding can improve independence beyond open-ended help.",
            "",
            format_delta_table(deltas),
            "",
            "## Independence Ranking",
            "",
            "The independence score prioritizes transfer while penalizing calibration error "
            "and overreliance.",
            "",
            format_ranked_conditions(ranked),
            "",
            "## Interpretation Guardrail",
            "",
            "Synthetic outputs are protocol-validation artifacts. Human learner data are "
            "required before making empirical claims about learning effects.",
            "",
        ]
    )


def write_synthetic_report(results: list[ConditionResult], output_path: Path) -> Path:
    """Write a synthetic experiment markdown report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_synthetic_report(results), encoding="utf-8")
    return output_path
