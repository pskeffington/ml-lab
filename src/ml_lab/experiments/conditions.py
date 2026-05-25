"""Experimental conditions for scaffold-policy comparisons."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ExperimentCondition(StrEnum):
    """Study arms for scaffolding experiments."""

    NO_AI_CONTROL = "no_ai_control"
    UNRESTRICTED_AI = "unrestricted_ai"
    STATIC_SCAFFOLDING = "static_scaffolding"
    ADAPTIVE_POLICY = "adaptive_policy"
    TIMING_AND_FADING = "timing_and_fading"


@dataclass(frozen=True)
class ConditionConfig:
    """Configuration parameters for a study condition."""

    condition: ExperimentCondition
    scaffold_access: bool
    adaptive: bool
    timing_gate: bool
    fading: bool
    metacognitive_prompting: bool
    base_hint_dependency: float


def default_conditions() -> list[ConditionConfig]:
    """Return the default experimental condition set."""
    return [
        ConditionConfig(
            condition=ExperimentCondition.NO_AI_CONTROL,
            scaffold_access=False,
            adaptive=False,
            timing_gate=False,
            fading=False,
            metacognitive_prompting=False,
            base_hint_dependency=0.05,
        ),
        ConditionConfig(
            condition=ExperimentCondition.UNRESTRICTED_AI,
            scaffold_access=True,
            adaptive=False,
            timing_gate=False,
            fading=False,
            metacognitive_prompting=False,
            base_hint_dependency=0.65,
        ),
        ConditionConfig(
            condition=ExperimentCondition.STATIC_SCAFFOLDING,
            scaffold_access=True,
            adaptive=False,
            timing_gate=False,
            fading=False,
            metacognitive_prompting=True,
            base_hint_dependency=0.45,
        ),
        ConditionConfig(
            condition=ExperimentCondition.ADAPTIVE_POLICY,
            scaffold_access=True,
            adaptive=True,
            timing_gate=False,
            fading=False,
            metacognitive_prompting=True,
            base_hint_dependency=0.35,
        ),
        ConditionConfig(
            condition=ExperimentCondition.TIMING_AND_FADING,
            scaffold_access=True,
            adaptive=True,
            timing_gate=True,
            fading=True,
            metacognitive_prompting=True,
            base_hint_dependency=0.25,
        ),
    ]
