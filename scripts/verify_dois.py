"""Verify DOI coverage for markdown citation files.

Examples:

    python scripts/verify_dois.py docs
    python scripts/verify_dois.py docs --crossref
    python scripts/verify_dois.py docs --csv reports/generated/doi_report.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ml_lab.citations.doi_verifier import (
    build_markdown_report,
    discover_citation_candidates,
    verify_candidates,
    write_markdown_report,
    write_results_csv,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Verify DOI coverage in markdown citation files.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["docs"],
        help="Markdown files or directories to scan. Defaults to docs.",
    )
    parser.add_argument(
        "--crossref",
        action="store_true",
        help="Query Crossref for candidate DOI matches. This requires internet access.",
    )
    parser.add_argument(
        "--markdown",
        default="reports/generated/doi_verification_report.md",
        help="Markdown report output path.",
    )
    parser.add_argument(
        "--csv",
        default="reports/generated/doi_verification_report.csv",
        help="CSV report output path.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print the markdown report to stdout.",
    )
    return parser.parse_args()


def main() -> None:
    """Run DOI verification over markdown files."""
    args = parse_args()
    scan_paths = [Path(path) for path in args.paths]
    candidates = discover_citation_candidates(scan_paths)
    results = verify_candidates(candidates, use_crossref=args.crossref)

    markdown_path = write_markdown_report(results, Path(args.markdown))
    csv_path = write_results_csv(results, Path(args.csv))

    if args.stdout:
        print(build_markdown_report(results))
    else:
        print(f"Scanned {len(candidates)} citation candidates.")
        print(f"Wrote markdown report to {markdown_path}")
        print(f"Wrote CSV report to {csv_path}")


if __name__ == "__main__":
    main()
