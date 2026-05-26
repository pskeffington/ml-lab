"""Summary metrics for synthetic ml-lab experiment logs."""

from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import fmean
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


def summarize_by_arm(events: Iterable[dict[str, str | int | float]]) -> list[ArmSummary]:
    """Summarize event-level experiment records by experimental arm."""

    grouped: dict[str, list[dict[str, str | int | float]]] = defaultdict(list)
    for event in events:
        arm = str(event.get("arm", "")).strip()
        if not arm:
            raise ValueError("each event must include a non-empty arm")
        grouped[arm].append(event)

    if not grouped:
        raise ValueError("events must not be empty")

    return [_summarize_group(arm=arm, rows=rows) for arm, rows in sorted(grouped.items())]


def summarize_event_log(path: str | Path) -> list[ArmSummary]:
    """Load a CSV event log and summarize it by arm."""

    input_path = Path(path)
    with input_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    return summarize_by_arm(rows)


def write_summary_csv(summaries: Iterable[ArmSummary], path: str | Path) -> None:
    """Write arm-level summaries to CSV."""

    summary_dicts = [summary.as_dict() for summary in summaries]
    if not summary_dicts:
        raise ValueError("summaries must not be empty")

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(summary_dicts[0].keys()))
        writer.writeheader()
        writer.writerows(summary_dicts)


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
    if field not in _NUMERIC_FIELDS:
        raise ValueError(f"unsupported numeric field: {field}")
    values: list[float] = []
    for row in rows:
        if field not in row:
            raise ValueError(f"missing field: {field}")
        values.append(float(row[field]))
    return fmean(values)


def main() -> None:
    """Summarize the default synthetic event log."""

    input_path = Path("outputs/synthetic_event_log.csv")
    output_path = Path("outputs/arm_summary.csv")
    summaries = summarize_event_log(input_path)
    write_summary_csv(summaries=summaries, path=output_path)
    for summary in summaries:
        print(summary.as_dict())
    print(f"Wrote {len(summaries)} arm summaries to {output_path}")
