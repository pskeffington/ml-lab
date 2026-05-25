"""Tests for scaffold timing and fading behavior."""

from ml_lab.core.learner_state import LearnerState
from ml_lab.core.scaffold import ScaffoldType
from ml_lab.core.scaffold_policy import TimingAndFadingPolicy


def test_policy_preserves_productive_struggle_before_first_attempt() -> None:
    policy = TimingAndFadingPolicy()
    state = LearnerState(
        knowledge_estimate=0.50,
        confidence=0.50,
        cognitive_load=0.50,
        hint_dependency=0.20,
        attempts=0,
        elapsed_seconds=45.0,
    )

    scaffold = policy.select(state)

    assert scaffold.scaffold_type == ScaffoldType.ORIENTATION
    assert scaffold.intensity < 0.30
    assert scaffold.requires_reflection


def test_policy_uses_diagnostic_question_for_overreliance_risk() -> None:
    policy = TimingAndFadingPolicy()
    state = LearnerState(
        knowledge_estimate=0.60,
        confidence=0.65,
        cognitive_load=0.35,
        hint_dependency=0.85,
        attempts=1,
        elapsed_seconds=60.0,
    )

    scaffold = policy.select(state)

    assert scaffold.scaffold_type == ScaffoldType.DIAGNOSTIC_QUESTION
    assert scaffold.intensity <= 0.30
    assert "hint dependency" in scaffold.policy_reason.lower()


def test_policy_fades_support_when_learner_is_ready() -> None:
    policy = TimingAndFadingPolicy()
    state = LearnerState(
        knowledge_estimate=0.80,
        confidence=0.70,
        cognitive_load=0.30,
        hint_dependency=0.20,
        attempts=2,
        elapsed_seconds=120.0,
    )

    scaffold = policy.select(state)

    assert scaffold.scaffold_type == ScaffoldType.ORIENTATION
    assert scaffold.intensity < 0.20
    assert "fading" in scaffold.policy_reason.lower()
