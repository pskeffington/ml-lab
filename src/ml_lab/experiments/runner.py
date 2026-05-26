"""Synthetic experiment runner for adaptive scaffolding studies."""

from __future__ import annotations

import csv
import random
from dataclasses import dataclass, field
from pathlib import Path

from ml_lab.core import (
    ExperimentArm,
    LearnerState,
    RuleBasedScaffoldPolicy,
    ScaffoldAction,
    StaticScaffoldPolicy,
    UnguidedLLMPolicy,
)


@dataclass(frozen=True, slots=True)
class TaskEnvironment:
    """Ordered task sequence for a synthetic experiment."""

    task_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.task_ids:
            raise ValueError("task_ids must not be empty")


@dataclass(frozen=True, slots=True)
class ExperimentConfig:
    """Configuration for a synthetic scaffold experiment."""

    learners_per_arm: int = 5
    seed: int = 7
    task_ids: tuple[str, ...] = ("task-1", "task-2", "task-3", "task-4")

    def __post_init__(self) -> None:
        if self.learners_per_arm < 1:
            raise ValueError("learners_per_arm must be positive")
        if not self.task_ids:
            raise ValueError("task_ids must not be empty")


@dataclass(slots=True)
class SyntheticLearner:
    """Simple synthetic learner with skill and confidence parameters."""

    learner_id: str
    skill: float
    confidence_bias: float = 0.0
    rng: random.Random = field(default_factory=random.Random, repr=False)

    def __post_init__(self) -> None:
        if not 0.0 <= self.skill <= 1.0:
            raise ValueError("skill must be between 0.0 and 1.0")
        if not -1.0 <= self.confidence_bias <= 1.0:
            raise ValueError("confidence_bias must be between -1.0 and 1.0")

    def attempt_task(self, task_id: str, support_intensity: float = 0.0) -> LearnerState:
        """Generate a learner-state observation for one task attempt."""

        support_bonus = min(max(support_intensity, 0.0), 1.0) * 0.18
        correctness_probability = min(max(self.skill + support_bonus, 0.0), 1.0)
        correctness = 1.0 if self.rng.random() < correctness_probability else 0.0
        confidence_noise = self.rng.uniform(-0.1, 0.1)
        confidence = min(max(self.skill + self.confidence_bias + confidence_noise, 0.0), 1.0)
        latency_seconds = max(1.0, self.rng.gauss(mu=20.0 - 8.0 * self.skill, sigma=3.0))

        return LearnerState(
            learner_id=self.learner_id,
            task_id=task_id,
            correctness=correctness,
            confidence=confidence,
            latency_seconds=latency_seconds,
            hint_count=0,
            metadata={"skill": self.skill, "support_intensity": support_intensity},
        )


@dataclass(slots=True)
class ExperimentRunner:
    """Run a small synthetic scaffold experiment and return event records."""

    environment: TaskEnvironment
    arms: tuple[ExperimentArm, ...]
    seed: int = 7

    def __post_init__(self) -> None:
        if not self.arms:
            raise ValueError("arms must not be empty")

    def run(self, learners_per_arm: int = 5) -> list[dict[str, str | int | float]]:
        """Run a deterministic synthetic experiment under the configured seed."""

        if learners_per_arm < 1:
            raise ValueError("learners_per_arm must be positive")

        rng = random.Random(self.seed)
        events: list[dict[str, str | int | float]] = []

        for arm in self.arms:
            for index in range(learners_per_arm):
                learner_rng = random.Random(rng.randint(0, 1_000_000))
                learner = SyntheticLearner(
                    learner_id=f"{arm.name}-{index + 1}",
                    skill=learner_rng.uniform(0.25, 0.85),
                    confidence_bias=learner_rng.uniform(-0.15, 0.2),
                    rng=learner_rng,
                )
                events.extend(self._run_learner(arm=arm, learner=learner))

        return events

    def _run_learner(
        self,
        arm: ExperimentArm,
        learner: SyntheticLearner,
    ) -> list[dict[str, str | int | float]]:
        records: list[dict[str, str | int | float]] = []
        support_intensity = 0.0
        cumulative_hint_count = 0

        for step, task_id in enumerate(self.environment.task_ids, start=1):
            state = learner.attempt_task(task_id=task_id, support_intensity=support_intensity)
            action = self._select_action(arm=arm, state=state)
            cumulative_hint_count = self._next_hint_count(
                hint_count=cumulative_hint_count,
                action=action,
            )
            records.append(
                {
                    "learner_id": state.learner_id,
                    "arm": arm.name,
                    "task_id": state.task_id,
                    "step": step,
                    "correctness": state.correctness,
                    "confidence": state.confidence,
                    "calibration_error": state.calibration_error,
                    "latency_seconds": state.latency_seconds,
                    "hint_count": cumulative_hint_count,
                    "selected_action": action.name,
                    "action_intensity": action.intensity,
                    "support_intensity_next": action.intensity,
                    "learner_skill": float(state.metadata["skill"]),
                }
            )
            support_intensity = action.intensity

        return records

    @staticmethod
    def _select_action(arm: ExperimentArm, state: LearnerState) -> ScaffoldAction:
        if arm.policy is None:
            return ScaffoldAction(
                name="none",
                description="No scaffold action selected for this arm.",
                intensity=0.0,
            )
        return arm.policy.select_action(state)

    @staticmethod
    def _next_hint_count(hint_count: int, action: ScaffoldAction) -> int:
        if action.intensity > 0:
            return hint_count + 1
        return hint_count

    @staticmethod
    def write_csv(events: list[dict[str, str | int | float]], path: str | Path) -> None:
        """Write experiment events to CSV."""

        if not events:
            raise ValueError("events must not be empty")
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=list(events[0].keys()))
            writer.writeheader()
            writer.writerows(events)


def build_default_arms() -> tuple[ExperimentArm, ...]:
    """Build the four default experimental arms from the research design."""

    return (
        ExperimentArm(
            name="adaptive_ml_scaffold",
            description="Rule-based adaptive scaffold baseline.",
            policy=RuleBasedScaffoldPolicy(),
            uses_ai=True,
            adaptive=True,
        ),
        ExperimentArm(
            name="static_scaffold",
            description="Non-adaptive scaffold with constant support.",
            policy=StaticScaffoldPolicy(),
            uses_ai=False,
            adaptive=False,
        ),
        ExperimentArm(
            name="unguided_llm_assistance",
            description="Proxy for unrestricted LLM help without scaffold constraints.",
            policy=UnguidedLLMPolicy(),
            uses_ai=True,
            adaptive=False,
        ),
        ExperimentArm(
            name="no_ai_control",
            description="Unsupported baseline condition.",
            policy=None,
            uses_ai=False,
            adaptive=False,
        ),
    )


def build_default_runner(seed: int = 7) -> ExperimentRunner:
    """Build the default synthetic experiment runner."""

    config = ExperimentConfig(seed=seed)
    return build_runner_from_config(config)


def build_runner_from_config(config: ExperimentConfig) -> ExperimentRunner:
    """Build a runner from an experiment configuration."""

    return ExperimentRunner(
        environment=TaskEnvironment(task_ids=config.task_ids),
        arms=build_default_arms(),
        seed=config.seed,
    )


def main() -> None:
    """Run a small synthetic experiment and export the event log."""

    config = ExperimentConfig()
    runner = build_runner_from_config(config)
    events = runner.run(learners_per_arm=config.learners_per_arm)
    output_path = Path("outputs/synthetic_event_log.csv")
    runner.write_csv(events=events, path=output_path)
    print(f"Wrote {len(events)} events to {output_path}")
