"""Metrics for measuring AI-scaffold overreliance."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class ScaffoldUseEvent:
    """Minimal event record for scaffold-dependency analysis."""

    attempted_before_help: bool
    scaffold_intensity: float
    response_correct: bool
    post_scaffold_correct: bool
    independent_followup_correct: bool
    copied_scaffold_text: bool = False


@dataclass(frozen=True)
class OverrelianceReport:
    """Aggregate indicators of scaffold overreliance."""

    premature_help_rate: float
    high_intensity_help_rate: float
    copy_forward_rate: float
    unsupported_drop_rate: float
    composite_overreliance_score: float


def _rate(values: list[bool]) -> float:
    """Return the share of true values, guarding against empty inputs."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def compute_overreliance(events: list[ScaffoldUseEvent]) -> OverrelianceReport:
    """Compute scaffold overreliance indicators from scaffold-use events.

    The composite score intentionally emphasizes behaviors that threaten durable
    learning: premature help-seeking, heavy support, copy-forward behavior, and
    performance collapse after scaffolds are removed.
    """
    if not events:
        return OverrelianceReport(
            premature_help_rate=0.0,
            high_intensity_help_rate=0.0,
            copy_forward_rate=0.0,
            unsupported_drop_rate=0.0,
            composite_overreliance_score=0.0,
        )

    premature_help_rate = _rate([not event.attempted_before_help for event in events])
    high_intensity_help_rate = _rate([event.scaffold_intensity >= 0.70 for event in events])
    copy_forward_rate = _rate([event.copied_scaffold_text for event in events])
    unsupported_drop_rate = _rate(
        [event.post_scaffold_correct and not event.independent_followup_correct for event in events]
    )

    composite = mean(
        [
            premature_help_rate,
            high_intensity_help_rate,
            copy_forward_rate,
            unsupported_drop_rate,
        ]
    )

    return OverrelianceReport(
        premature_help_rate=premature_help_rate,
        high_intensity_help_rate=high_intensity_help_rate,
        copy_forward_rate=copy_forward_rate,
        unsupported_drop_rate=unsupported_drop_rate,
        composite_overreliance_score=composite,
    )
