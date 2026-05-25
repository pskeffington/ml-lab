"""Run synthetic experiment and print paper-facing statistical summaries."""

from ml_lab.experiments.conditions import ExperimentCondition
from ml_lab.experiments.statistical_summary import (
    compute_condition_deltas,
    format_delta_table,
    format_ranked_conditions,
    rank_conditions_for_independence,
)
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment, format_results_table


def main() -> None:
    """Run synthetic experiment and summarize condition comparisons."""
    experiment = SyntheticScaffoldingExperiment(learner_count=100, tasks_per_learner=10, seed=42)
    results = experiment.run()
    deltas = compute_condition_deltas(results, baseline=ExperimentCondition.UNRESTRICTED_AI)
    ranked = rank_conditions_for_independence(results)

    print("# Synthetic Experiment Results\n")
    print(format_results_table(results))
    print("\n# Deltas vs Unrestricted AI\n")
    print(format_delta_table(deltas))
    print("\n# Independence Ranking\n")
    print(format_ranked_conditions(ranked))


if __name__ == "__main__":
    main()
