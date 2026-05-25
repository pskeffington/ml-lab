"""Tests for DOI verification utilities."""

from ml_lab.citations.doi_verifier import (
    build_markdown_report,
    discover_citation_candidates,
    find_dois,
    verify_candidates,
    write_markdown_report,
    write_results_csv,
)


def test_find_dois_extracts_doi_from_text() -> None:
    text = "Wood et al. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x."

    dois = find_dois(text)

    assert dois == ["10.1111/j.1469-7610.1976.tb00381.x"]


def test_discover_citation_candidates_finds_markdown_table_rows(tmp_path) -> None:
    markdown_file = tmp_path / "sources.md"
    markdown_file.write_text(
        "| Source | APA |\n"
        "|---|---|\n"
        "| Wood et al. (1976) | The role of tutoring in problem solving. |\n",
        encoding="utf-8",
    )

    candidates = discover_citation_candidates([markdown_file])

    assert len(candidates) == 1
    assert candidates[0].line_number == 3
    assert candidates[0].extracted_doi is None


def test_verify_candidates_marks_missing_doi_without_remote_lookup(tmp_path) -> None:
    markdown_file = tmp_path / "sources.md"
    markdown_file.write_text(
        "| Wood et al. (1976) | The role of tutoring in problem solving. |\n",
        encoding="utf-8",
    )
    candidates = discover_citation_candidates([markdown_file])

    results = verify_candidates(candidates, use_crossref=False)

    assert len(results) == 1
    assert results[0].status == "needs_doi_review"


def test_report_writers_create_files(tmp_path) -> None:
    markdown_file = tmp_path / "sources.md"
    markdown_file.write_text(
        "Wood et al. DOI: 10.1111/j.1469-7610.1976.tb00381.x\n",
        encoding="utf-8",
    )
    results = verify_candidates(discover_citation_candidates([markdown_file]))
    markdown_output = tmp_path / "report.md"
    csv_output = tmp_path / "report.csv"

    write_markdown_report(results, markdown_output)
    write_results_csv(results, csv_output)

    assert markdown_output.exists()
    assert csv_output.exists()
    assert "DOI Verification Report" in markdown_output.read_text(encoding="utf-8")


def test_build_markdown_report_includes_status_counts(tmp_path) -> None:
    markdown_file = tmp_path / "sources.md"
    markdown_file.write_text(
        "Wood et al. DOI: 10.1111/j.1469-7610.1976.tb00381.x\n",
        encoding="utf-8",
    )
    results = verify_candidates(discover_citation_candidates([markdown_file]))

    report = build_markdown_report(results)

    assert "Status Counts" in report
    assert "doi_present_unverified" in report
