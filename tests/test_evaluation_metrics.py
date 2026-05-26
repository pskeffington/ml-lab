"""Tests for event-log evaluation summaries."""

from __future__ import annotations

import csv

import pytest

from ml_lab.evaluation.metrics import (
    compare_arms,
    compare_event_log,
    summarize_by_arm,
    summarize_event_log,
    write_comparison_csv,
    write_summary_csv,
)
from ml_lab.experiments.runner import build_default_runner


def test_summarize_by_arm_returns_one_summary_per_arm() -> None:
    events = build_default_runner(seed=31).run(learners_per_arm=2)

    summaries = summarize_by_arm(events)

    assert [summary.arm for summary in summaries] == [
        "adaptive_ml_scaffold",
        "no_ai_control",
        "static_scaffold",
        "unguided_llm_assistance",
    ]
    assert all(summary.n_events == 8 for summary in summaries)
    assert all(0.0 <= summary.mean_correctness <= 1.0 for summary in summaries)
    assert all(0.0 <= summary.mean_calibration_error <= 1.0 for summary in summaries)


def test_compare_arms_returns_pairwise_effect_sizes() -> None:
    events = build_default_runner(seed=41).run(learners_per_arm=3)

    comparisons = compare_arms(events, outcomes=("correctness", "calibration_error"))

    assert len(comparisons) == 6 * 2
    assert {comparison.outcome for comparison in comparisons} == {
        "correctness",
        "calibration_error",
    }
    assert all(isinstance(comparison.cohens_d, float) for comparison in comparisons)


def test_summarize_by_arm_rejects_empty_events() -> None:
    with pytest.raises(ValueError, match="events must not be empty"):
        summarize_by_arm([])


def test_summarize_by_arm_rejects_missing_arm() -> None:
    with pytest.raises(ValueError, match="non-empty arm"):
        summarize_by_arm(
            [
                {
                    "correctness": 1.0,
                    "confidence": 1.0,
                    "calibration_error": 0.0,
                    "latency_seconds": 5.0,
                    "hint_count": 0,
                    "action_intensity": 0.0,
                }
            ]
        )


def test_summary_and_comparison_csv_round_trip(tmp_path) -> None:
    runner = build_default_runner(seed=37)
    events = runner.run(learners_per_arm=1)
    event_log_path = tmp_path / "events.csv"
    summary_path = tmp_path / "summary.csv"
    comparison_path = tmp_path / "comparisons.csv"
    runner.write_csv(events=events, path=event_log_path)

    summaries = summarize_event_log(event_log_path)
    comparisons = compare_event_log(event_log_path)
    write_summary_csv(summaries=summaries, path=summary_path)
    write_comparison_csv(comparisons=comparisons, path=comparison_path)

    with summary_path.open(newline="", encoding="utf-8") as file:
        summary_rows = list(csv.DictReader(file))
    with comparison_path.open(newline="", encoding="utf-8") as file:
        comparison_rows = list(csv.DictReader(file))

    assert len(summary_rows) == 4
    assert set(summary_rows[0]) == {
        "arm",
        "n_events",
        "mean_correctness",
        "mean_confidence",
        "mean_calibration_error",
        "mean_latency_seconds",
        "mean_hint_count",
        "mean_action_intensity",
    }
    assert len(comparison_rows) == 18
    assert set(comparison_rows[0]) == {
        "arm_a",
        "arm_b",
        "outcome",
        "mean_a",
        "mean_b",
        "mean_difference",
        "cohens_d",
    }
