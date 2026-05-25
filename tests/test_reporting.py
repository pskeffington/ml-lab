"""Tests for synthetic experiment report generation."""

from ml_lab.experiments.reporting import REPORT_TITLE, build_synthetic_report, write_synthetic_report
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment


def test_build_synthetic_report_contains_required_sections() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=3, tasks_per_learner=2, seed=23)

    report = build_synthetic_report(experiment.run())

    assert REPORT_TITLE in report
    assert "Condition-Level Results" in report
    assert "Deltas Against Unrestricted AI" in report
    assert "Independence Ranking" in report
    assert "Interpretation Guardrail" in report


def test_write_synthetic_report_creates_markdown_file(tmp_path) -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=3, tasks_per_learner=2, seed=29)
    output_path = tmp_path / "report.md"

    write_synthetic_report(experiment.run(), output_path)

    assert output_path.exists()
    assert REPORT_TITLE in output_path.read_text(encoding="utf-8")
