"""Generate a markdown report for the synthetic scaffolding experiment."""

from pathlib import Path

from ml_lab.experiments.reporting import write_synthetic_report
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment


DEFAULT_REPORT_PATH = Path("reports/generated/synthetic_experiment_report.md")


def main() -> None:
    """Run the default synthetic experiment and write a markdown report."""
    experiment = SyntheticScaffoldingExperiment(learner_count=100, tasks_per_learner=10, seed=42)
    output_path = write_synthetic_report(experiment.run(), DEFAULT_REPORT_PATH)
    print(f"Wrote synthetic experiment report to {output_path}")


if __name__ == "__main__":
    main()
