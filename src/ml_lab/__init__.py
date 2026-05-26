"""Adaptive machine-learning scaffolding research package."""

from ml_lab.core.actions import ScaffoldAction
from ml_lab.core.arms import ExperimentArm
from ml_lab.core.metrics import CalibrationMetric, HintDependencyMetric, OutcomeMetric
from ml_lab.core.policies import RuleBasedScaffoldPolicy, ScaffoldPolicy
from ml_lab.core.state import LearnerState

__all__ = [
    "CalibrationMetric",
    "ExperimentArm",
    "HintDependencyMetric",
    "LearnerState",
    "OutcomeMetric",
    "RuleBasedScaffoldPolicy",
    "ScaffoldAction",
    "ScaffoldPolicy",
]
