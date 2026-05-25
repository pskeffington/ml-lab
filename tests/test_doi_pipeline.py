"""Tests for the configurable DOI verification pipeline."""

import json

from ml_lab.citations.doi_pipeline import (
    DoiPipelinePolicy,
    load_pipeline_config,
    run_pipeline,
    summarize_results,
)
from ml_lab.citations.doi_verifier import DoiVerificationResult


def test_load_pipeline_config_reads_json(tmp_path) -> None:
    config_path = tmp_path / "citation_pipeline.json"
    config_path.write_text(
        json.dumps(
            {
                "scan_paths": ["docs"],
                "outputs": {
                    "markdown": "reports/doi.md",
                    "csv": "reports/doi.csv",
                    "summary_json": "reports/doi.json",
                },
                "policy": {
                    "allow_missing_doi": False,
                    "allow_crossref_errors": True,
                    "fail_on_unverified_existing_doi": False,
                    "max_missing_doi_candidates": 2,
                },
                "remote": {"use_crossref": False},
            }
        ),
        encoding="utf-8",
    )

    config = load_pipeline_config(config_path)

    assert config.scan_paths == ["docs"]
    assert config.outputs.markdown == "reports/doi.md"
    assert config.policy.allow_missing_doi is False
    assert config.policy.max_missing_doi_candidates == 2
    assert config.use_crossref is False


def test_summarize_results_fails_when_missing_dois_not_allowed() -> None:
    results = [
        DoiVerificationResult(
            path="docs/source.md",
            line_number=1,
            raw_text="Wood et al. (1976)",
            extracted_doi=None,
            status="needs_doi_review",
        )
    ]

    summary = summarize_results(results, DoiPipelinePolicy(allow_missing_doi=False))

    assert summary.passed is False
    assert summary.failures


def test_run_pipeline_writes_configured_outputs(tmp_path) -> None:
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    source_file = docs_dir / "sources.md"
    source_file.write_text(
        "| Source | APA |\n"
        "|---|---|\n"
        "| Wood et al. (1976) | The role of tutoring in problem solving. |\n",
        encoding="utf-8",
    )
    config_path = tmp_path / "citation_pipeline.json"
    markdown_path = tmp_path / "reports" / "doi.md"
    csv_path = tmp_path / "reports" / "doi.csv"
    summary_path = tmp_path / "reports" / "doi.json"
    config_path.write_text(
        json.dumps(
            {
                "scan_paths": [str(docs_dir)],
                "outputs": {
                    "markdown": str(markdown_path),
                    "csv": str(csv_path),
                    "summary_json": str(summary_path),
                },
                "policy": {"allow_missing_doi": True},
                "remote": {"use_crossref": False},
            }
        ),
        encoding="utf-8",
    )

    summary = run_pipeline(load_pipeline_config(config_path))

    assert summary.passed is True
    assert markdown_path.exists()
    assert csv_path.exists()
    assert summary_path.exists()
