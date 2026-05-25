"""Run the configurable DOI verification pipeline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ml_lab.citations.doi_pipeline import load_pipeline_config, run_pipeline


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the DOI verification pipeline.")
    parser.add_argument(
        "--config",
        default="citation_pipeline.json",
        help="Path to citation pipeline JSON config.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return nonzero exit code if the configured policy fails.",
    )
    return parser.parse_args()


def main() -> None:
    """Run DOI pipeline from config."""
    args = parse_args()
    config = load_pipeline_config(Path(args.config))
    summary = run_pipeline(config)

    print(f"DOI candidates scanned: {summary.candidate_count}")
    print("Status counts:")
    for status, count in sorted(summary.status_counts.items()):
        print(f"  {status}: {count}")

    if summary.passed:
        print("DOI pipeline policy: passed")
    else:
        print("DOI pipeline policy: failed")
        for failure in summary.failures:
            print(f"  - {failure}")
        if args.strict:
            sys.exit(1)


if __name__ == "__main__":
    main()
