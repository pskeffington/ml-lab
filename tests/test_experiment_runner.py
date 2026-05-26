"""Tests for synthetic experiment runner."""

from __future__ import annotations

import csv

import pytest

from ml_lab.experiments import ExperimentRunner, TaskEnvironment
from ml_lab.experiments.runner import ExperimentConfig, build_default_arms, build_default_runner


def test_default_runner_produces_expected_number_of_events() -> None:
    runner = build_default_runner(seed=11)

    events = runner.run(learners_per_arm=3)

    assert len(events) == 4 * 3 * 4
    assert set(events[0]) == {
        "learner_id",
        "arm",
        "task_id",
        "step",
        "correctness",
        "confidence",
        "calibration_error",
        "latency_seconds",
        "hint_count",
        "selected_action",
        "action_intensity",
        "support_intensity_next",
        "learner_skill",
    }


def test_default_arms_match_research_design_conditions() -> None:
    arms = build_default_arms()

    assert [arm.name for arm in arms] == [
        "adaptive_ml_scaffold",
        "static_scaffold",
        "unguided_llm_assistance",
        "no_ai_control",
    ]


def test_runner_is_deterministic_under_fixed_seed() -> None:
    first = build_default_runner(seed=19).run(learners_per_arm=2)
    second = build_default_runner(seed=19).run(learners_per_arm=2)

    assert first == second


def test_task_environment_requires_tasks() -> None:
    with pytest.raises(ValueError, match="task_ids"):
        TaskEnvironment(task_ids=())


def test_experiment_config_requires_positive_learners() -> None:
    with pytest.raises(ValueError, match="learners_per_arm"):
        ExperimentConfig(learners_per_arm=0)


def test_runner_requires_positive_learners_per_arm() -> None:
    runner = build_default_runner()

    with pytest.raises(ValueError, match="learners_per_arm"):
        runner.run(learners_per_arm=0)


def test_runner_writes_csv(tmp_path) -> None:
    runner = build_default_runner(seed=23)
    events = runner.run(learners_per_arm=1)
    output_path = tmp_path / "event_log.csv"

    ExperimentRunner.write_csv(events=events, path=output_path)

    with output_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == len(events)
    assert rows[0]["learner_id"] == events[0]["learner_id"]
