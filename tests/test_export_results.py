"""Tests for experiment result export utilities."""

import csv

from ml_lab.experiments.export_results import CSV_FIELDS, export_condition_results_csv
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment


def test_export_condition_results_csv_writes_expected_fields(tmp_path) -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=3, tasks_per_learner=2, seed=5)
    results = experiment.run()
    output_path = tmp_path / "synthetic_results.csv"

    export_condition_results_csv(results, output_path)

    assert output_path.exists()
    with output_path.open("r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert reader.fieldnames == CSV_FIELDS
    assert len(rows) == 5
    assert {row["condition"] for row in rows}
