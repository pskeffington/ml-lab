"""Tests for core adaptive scaffolding objects."""

from __future__ import annotations

import pytest

from ml_lab.core import (
    CalibrationMetric,
    ExperimentArm,
    HintDependencyMetric,
    LearnerState,
    RuleBasedScaffoldPolicy,
    ScaffoldAction,
)


def test_learner_state_computes_calibration_error() -> None:
    state = LearnerState(
        learner_id="learner-1",
        task_id="task-1",
        correctness=0.5,
        confidence=0.9,
        latency_seconds=12.0,
    )

    assert state.calibration_error == pytest.approx(0.4)
    assert state.needs_support is True


def test_learner_state_validates_probability_bounds() -> None:
    with pytest.raises(ValueError, match="correctness"):
        LearnerState(
            learner_id="learner-1",
            task_id="task-1",
            correctness=1.5,
            confidence=0.9,
            latency_seconds=12.0,
        )


def test_scaffold_action_validates_intensity() -> None:
    with pytest.raises(ValueError, match="intensity"):
        ScaffoldAction(name="bad", description="Invalid action", intensity=1.5)


def test_rule_based_policy_selects_worked_example_for_low_correctness() -> None:
    policy = RuleBasedScaffoldPolicy()
    state = LearnerState(
        learner_id="learner-1",
        task_id="task-1",
        correctness=0.2,
        confidence=0.4,
        latency_seconds=20.0,
    )

    action = policy.select_action(state)

    assert action.name == "worked_example"
    assert action.intensity == pytest.approx(0.9)


def test_rule_based_policy_selects_reflection_for_miscalibration() -> None:
    policy = RuleBasedScaffoldPolicy()
    state = LearnerState(
        learner_id="learner-1",
        task_id="task-1",
        correctness=0.8,
        confidence=0.3,
        latency_seconds=8.0,
    )

    action = policy.select_action(state)

    assert action.name == "reflection_prompt"


def test_adaptive_experiment_arm_requires_policy() -> None:
    with pytest.raises(ValueError, match="adaptive arms require"):
        ExperimentArm(
            name="adaptive",
            description="Adaptive arm without a policy should fail.",
            adaptive=True,
        )


def test_metrics_score_state_traces() -> None:
    states = [
        LearnerState(
            learner_id="learner-1",
            task_id="task-1",
            correctness=1.0,
            confidence=0.8,
            latency_seconds=5.0,
            hint_count=0,
        ),
        LearnerState(
            learner_id="learner-1",
            task_id="task-2",
            correctness=0.0,
            confidence=0.6,
            latency_seconds=10.0,
            hint_count=2,
        ),
    ]

    assert CalibrationMetric().score(states) == pytest.approx(0.4)
    assert HintDependencyMetric().score(states) == pytest.approx(1.0)
