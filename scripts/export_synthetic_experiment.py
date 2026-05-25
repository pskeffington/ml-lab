"""Run the synthetic experiment and export condition-level CSV results."""

from pathlib import Path

from ml_lab.experiments.export_results import export_condition_results_csv
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment, format_results_table


DEFAULT_OUTPUT_PATH = Path("outputs/synthetic_experiment_results.csv")


def main() -> None:
    """Run and export the default synthetic experiment."""
    experiment = SyntheticScaffoldingExperiment(learner_count=100, tasks_per_learner=10, seed=42)
    results = experiment.run()
    output_path = export_condition_results_csv(results, DEFAULT_OUTPUT_PATH)

    print(format_results_table(results))
    print(f"\nWrote CSV results to {output_path}")


if __name__ == "__main__":
    main()
