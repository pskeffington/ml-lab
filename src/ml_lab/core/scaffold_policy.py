"""Auditable scaffold policy interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod

from ml_lab.core.learner_state import LearnerState
from ml_lab.core.scaffold import Scaffold, ScaffoldType


class ScaffoldPolicy(ABC):
    """Base class for scaffold-selection policies."""

    @abstractmethod
    def select(self, learner_state: LearnerState) -> Scaffold:
        """Select a scaffold from observable learner evidence."""


class TimingAndFadingPolicy(ScaffoldPolicy):
    """Best-practice scaffold policy using timing, fading, and overreliance checks."""

    def select(self, learner_state: LearnerState) -> Scaffold:
        """Select a scaffold according to best-practice rules."""
        if learner_state.has_overreliance_risk():
            return Scaffold(
                scaffold_type=ScaffoldType.DIAGNOSTIC_QUESTION,
                intensity=0.30,
                message="Before receiving another hint, explain which concept you think applies and why.",
                requires_reflection=True,
                policy_reason="High hint dependency with limited independent attempts.",
            )

        if learner_state.is_ready_for_fading():
            return Scaffold(
                scaffold_type=ScaffoldType.ORIENTATION,
                intensity=0.15,
                message="Try the next step independently, then compare your reasoning against the target concept.",
                requires_reflection=True,
                policy_reason="Learner appears ready for scaffold fading.",
            )

        if learner_state.attempts == 0:
            return Scaffold(
                scaffold_type=ScaffoldType.ORIENTATION,
                intensity=0.20,
                message="Make an initial attempt before requesting detailed help.",
                requires_reflection=True,
                policy_reason="Preserve productive struggle before intervention.",
            )

        if learner_state.needs_support():
            return Scaffold(
                scaffold_type=ScaffoldType.STRATEGY_HINT,
                intensity=0.55,
                message="Identify the target concept, then state which evidence in the problem supports your choice.",
                requires_reflection=True,
                policy_reason="Evidence indicates support is needed without direct answer-giving.",
            )

        return Scaffold(
            scaffold_type=ScaffoldType.CONCEPT_ACTIVATION,
            intensity=0.35,
            message="Name the relevant concept and check whether your answer is consistent with it.",
            requires_reflection=True,
            policy_reason="Moderate support for concept activation.",
        )
