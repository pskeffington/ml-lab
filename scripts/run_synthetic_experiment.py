"""Command-line entrypoint for the synthetic scaffolding experiment."""

from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment, format_results_table


def main() -> None:
    """Run the default synthetic experiment and print markdown results."""
    experiment = SyntheticScaffoldingExperiment(learner_count=100, tasks_per_learner=10, seed=42)
    results = experiment.run()
    print(format_results_table(results))


if __name__ == "__main__":
    main()
