"""Experiment-arm definitions for adaptive scaffolding studies."""

from __future__ import annotations

from dataclasses import dataclass

from ml_lab.core.policies import ScaffoldPolicy


@dataclass(frozen=True, slots=True)
class ExperimentArm:
    """Assignment condition for an experiment participant or simulation."""

    name: str
    description: str
    policy: ScaffoldPolicy | None = None
    uses_ai: bool = False
    adaptive: bool = False

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name must not be empty")
        if self.adaptive and self.policy is None:
            raise ValueError("adaptive arms require a scaffold policy")
