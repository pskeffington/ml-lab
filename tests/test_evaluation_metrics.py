"""Tests for event-log evaluation summaries."""

from __future__ import annotations

import csv

import pytest

from ml_lab.evaluation.metrics import (
    compare_arms,
    compare_event_log,
    summarize_by_arm,
    summarize_by_learner,
    summarize_event_log,
    summarize_event_log_by_learner,
    summarize_event_log_learners_by_arm,
    summarize_learners_by_arm,
    write_comparison_csv,
    write_learner_arm_summary_csv,
    write_learner_summary_csv,
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


def test_summarize_by_learner_returns_one_summary_per_learner() -> None:
    events = build_default_runner(seed=31).run(learners_per_arm=2)

    summaries = summarize_by_learner(events)

    assert len(summaries) == 8
    assert all(summary.n_events == 4 for summary in summaries)
    assert all(0.0 <= summary.mean_correctness <= 1.0 for summary in summaries)
    assert all(0.0 <= summary.final_correctness <= 1.0 for summary in summaries)
    assert all(summary.total_hints >= 0 for summary in summaries)


def test_summarize_by_learner_uses_final_step_for_final_outcomes() -> None:
    events = [
        {
            "learner_id": "learner-1",
            "arm": "adaptive_ml_scaffold",
            "step": 2,
            "correctness": 0.0,
            "confidence": 0.2,
            "calibration_error": 0.2,
            "latency_seconds": 10.0,
            "hint_count": 1,
            "action_intensity": 0.5,
        },
        {
            "learner_id": "learner-1",
            "arm": "adaptive_ml_scaffold",
            "step": 1,
            "correctness": 1.0,
            "confidence": 0.9,
            "calibration_error": 0.1,
            "latency_seconds": 5.0,
            "hint_count": 0,
            "action_intensity": 0.0,
        },
    ]

    summary = summarize_by_learner(events)[0]

    assert summary.final_correctness == pytest.approx(0.0)
    assert summary.final_confidence == pytest.approx(0.2)
    assert summary.final_calibration_error == pytest.approx(0.2)
    assert summary.total_hints == 1


def test_summarize_learners_by_arm_uses_learner_level_units() -> None:
    events = build_default_runner(seed=41).run(learners_per_arm=3)
    learner_summaries = summarize_by_learner(events)

    arm_summaries = summarize_learners_by_arm(learner_summaries)

    assert [summary.arm for summary in arm_summaries] == [
        "adaptive_ml_scaffold",
        "no_ai_control",
        "static_scaffold",
        "unguided_llm_assistance",
    ]
    assert all(summary.n_learners == 3 for summary in arm_summaries)
    assert all(0.0 <= summary.mean_final_correctness <= 1.0 for summary in arm_summaries)
    assert all(summary.mean_total_hints >= 0.0 for summary in arm_summaries)


def test_summarize_by_learner_rejects_missing_learner_id() -> None:
    with pytest.raises(ValueError, match="learner_id"):
        summarize_by_learner(
            [
                {
                    "arm": "adaptive_ml_scaffold",
                    "correctness": 1.0,
                    "confidence": 1.0,
                    "calibration_error": 0.0,
                    "latency_seconds": 5.0,
                    "hint_count": 0,
                    "action_intensity": 0.0,
                }
            ]
        )


def test_summarize_by_learner_rejects_cross_arm_learner() -> None:
    events = [
        {
            "learner_id": "learner-1",
            "arm": "adaptive_ml_scaffold",
            "correctness": 1.0,
            "confidence": 1.0,
            "calibration_error": 0.0,
            "latency_seconds": 5.0,
            "hint_count": 0,
            "action_intensity": 0.0,
        },
        {
            "learner_id": "learner-1",
            "arm": "no_ai_control",
            "correctness": 0.0,
            "confidence": 0.5,
            "calibration_error": 0.5,
            "latency_seconds": 6.0,
            "hint_count": 0,
            "action_intensity": 0.0,
        },
    ]

    with pytest.raises(ValueError, match="multiple arms"):
        summarize_by_learner(events)


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


def test_learner_summary_csv_round_trip(tmp_path) -> None:
    runner = build_default_runner(seed=47)
    events = runner.run(learners_per_arm=1)
    event_log_path = tmp_path / "events.csv"
    learner_path = tmp_path / "learner_summary.csv"
    learner_arm_path = tmp_path / "learner_arm_summary.csv"
    runner.write_csv(events=events, path=event_log_path)

    learner_summaries = summarize_event_log_by_learner(event_log_path)
    learner_arm_summaries = summarize_event_log_learners_by_arm(event_log_path)
    write_learner_summary_csv(learner_summaries, learner_path)
    write_learner_arm_summary_csv(learner_arm_summaries, learner_arm_path)

    with learner_path.open(newline="", encoding="utf-8") as file:
        learner_rows = list(csv.DictReader(file))
    with learner_arm_path.open(newline="", encoding="utf-8") as file:
        learner_arm_rows = list(csv.DictReader(file))

    assert len(learner_rows) == 4
    assert set(learner_rows[0]) == {
        "learner_id",
        "arm",
        "n_events",
        "mean_correctness",
        "final_correctness",
        "mean_confidence",
        "final_confidence",
        "mean_calibration_error",
        "final_calibration_error",
        "mean_latency_seconds",
        "total_hints",
        "mean_action_intensity",
    }
    assert len(learner_arm_rows) == 4
    assert set(learner_arm_rows[0]) == {
        "arm",
        "n_learners",
        "mean_correctness",
        "mean_final_correctness",
        "mean_confidence",
        "mean_final_confidence",
        "mean_calibration_error",
        "mean_final_calibration_error",
        "mean_latency_seconds",
        "mean_total_hints",
        "mean_action_intensity",
    }
