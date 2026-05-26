"""Summary and comparison metrics for synthetic ml-lab experiment logs."""

from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from statistics import fmean, stdev
from typing import Iterable


_NUMERIC_FIELDS = (
    "correctness",
    "confidence",
    "calibration_error",
    "latency_seconds",
    "hint_count",
    "action_intensity",
)


@dataclass(frozen=True, slots=True)
class ArmSummary:
    """Aggregate summary for one experimental arm."""

    arm: str
    n_events: int
    mean_correctness: float
    mean_confidence: float
    mean_calibration_error: float
    mean_latency_seconds: float
    mean_hint_count: float
    mean_action_intensity: float

    def as_dict(self) -> dict[str, str | int | float]:
        """Return a CSV-friendly dictionary representation."""

        return {
            "arm": self.arm,
            "n_events": self.n_events,
            "mean_correctness": self.mean_correctness,
            "mean_confidence": self.mean_confidence,
            "mean_calibration_error": self.mean_calibration_error,
            "mean_latency_seconds": self.mean_latency_seconds,
            "mean_hint_count": self.mean_hint_count,
            "mean_action_intensity": self.mean_action_intensity,
        }


@dataclass(frozen=True, slots=True)
class PairwiseComparison:
    """Pairwise arm comparison for one numeric outcome."""

    arm_a: str
    arm_b: str
    outcome: str
    mean_a: float
    mean_b: float
    mean_difference: float
    cohens_d: float

    def as_dict(self) -> dict[str, str | float]:
        """Return a CSV-friendly dictionary representation."""

        return {
            "arm_a": self.arm_a,
            "arm_b": self.arm_b,
            "outcome": self.outcome,
            "mean_a": self.mean_a,
            "mean_b": self.mean_b,
            "mean_difference": self.mean_difference,
            "cohens_d": self.cohens_d,
        }


def summarize_by_arm(events: Iterable[dict[str, str | int | float]]) -> list[ArmSummary]:
    """Summarize event-level experiment records by experimental arm."""

    grouped = _group_by_arm(events)
    return [_summarize_group(arm=arm, rows=rows) for arm, rows in sorted(grouped.items())]


def compare_arms(
    events: Iterable[dict[str, str | int | float]],
    outcomes: tuple[str, ...] = ("correctness", "calibration_error", "hint_count"),
) -> list[PairwiseComparison]:
    """Compute pairwise mean differences and Cohen's d by outcome."""

    grouped = _group_by_arm(events)
    comparisons: list[PairwiseComparison] = []

    for arm_a, arm_b in combinations(sorted(grouped), 2):
        rows_a = grouped[arm_a]
        rows_b = grouped[arm_b]
        for outcome in outcomes:
            values_a = _values(rows_a, outcome)
            values_b = _values(rows_b, outcome)
            mean_a = fmean(values_a)
            mean_b = fmean(values_b)
            comparisons.append(
                PairwiseComparison(
                    arm_a=arm_a,
                    arm_b=arm_b,
                    outcome=outcome,
                    mean_a=mean_a,
                    mean_b=mean_b,
                    mean_difference=mean_a - mean_b,
                    cohens_d=_cohens_d(values_a, values_b),
                )
            )

    return comparisons


def summarize_event_log(path: str | Path) -> list[ArmSummary]:
    """Load a CSV event log and summarize it by arm."""

    return summarize_by_arm(_read_event_log(path))


def compare_event_log(path: str | Path) -> list[PairwiseComparison]:
    """Load a CSV event log and compute pairwise arm comparisons."""

    return compare_arms(_read_event_log(path))


def write_summary_csv(summaries: Iterable[ArmSummary], path: str | Path) -> None:
    """Write arm-level summaries to CSV."""

    _write_dicts([summary.as_dict() for summary in summaries], path, "summaries")


def write_comparison_csv(comparisons: Iterable[PairwiseComparison], path: str | Path) -> None:
    """Write pairwise comparisons to CSV."""

    _write_dicts([comparison.as_dict() for comparison in comparisons], path, "comparisons")


def _read_event_log(path: str | Path) -> list[dict[str, str]]:
    input_path = Path(path)
    with input_path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def _write_dicts(rows: list[dict[str, str | int | float]], path: str | Path, label: str) -> None:
    if not rows:
        raise ValueError(f"{label} must not be empty")

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _group_by_arm(
    events: Iterable[dict[str, str | int | float]],
) -> dict[str, list[dict[str, str | int | float]]]:
    grouped: dict[str, list[dict[str, str | int | float]]] = defaultdict(list)
    for event in events:
        arm = str(event.get("arm", "")).strip()
        if not arm:
            raise ValueError("each event must include a non-empty arm")
        grouped[arm].append(event)

    if not grouped:
        raise ValueError("events must not be empty")
    return grouped


def _summarize_group(arm: str, rows: list[dict[str, str | int | float]]) -> ArmSummary:
    return ArmSummary(
        arm=arm,
        n_events=len(rows),
        mean_correctness=_mean(rows, "correctness"),
        mean_confidence=_mean(rows, "confidence"),
        mean_calibration_error=_mean(rows, "calibration_error"),
        mean_latency_seconds=_mean(rows, "latency_seconds"),
        mean_hint_count=_mean(rows, "hint_count"),
        mean_action_intensity=_mean(rows, "action_intensity"),
    )


def _mean(rows: list[dict[str, str | int | float]], field: str) -> float:
    return fmean(_values(rows, field))


def _values(rows: list[dict[str, str | int | float]], field: str) -> list[float]:
    if field not in _NUMERIC_FIELDS:
        raise ValueError(f"unsupported numeric field: {field}")
    values: list[float] = []
    for row in rows:
        if field not in row:
            raise ValueError(f"missing field: {field}")
        values.append(float(row[field]))
    return values


def _cohens_d(values_a: list[float], values_b: list[float]) -> float:
    if len(values_a) < 2 or len(values_b) < 2:
        return 0.0
    variance_a = stdev(values_a) ** 2
    variance_b = stdev(values_b) ** 2
    pooled_numerator = (len(values_a) - 1) * variance_a + (len(values_b) - 1) * variance_b
    pooled_denominator = len(values_a) + len(values_b) - 2
    if pooled_denominator <= 0:
        return 0.0
    pooled_sd = (pooled_numerator / pooled_denominator) ** 0.5
    if pooled_sd == 0:
        return 0.0
    return (fmean(values_a) - fmean(values_b)) / pooled_sd


def main() -> None:
    """Summarize and compare the default synthetic event log."""

    input_path = Path("outputs/synthetic_event_log.csv")
    summary_path = Path("outputs/arm_summary.csv")
    comparison_path = Path("outputs/pairwise_comparisons.csv")
    summaries = summarize_event_log(input_path)
    comparisons = compare_event_log(input_path)
    write_summary_csv(summaries=summaries, path=summary_path)
    write_comparison_csv(comparisons=comparisons, path=comparison_path)
    for summary in summaries:
        print(summary.as_dict())
    print(f"Wrote {len(summaries)} arm summaries to {summary_path}")
    print(f"Wrote {len(comparisons)} pairwise comparisons to {comparison_path}")
