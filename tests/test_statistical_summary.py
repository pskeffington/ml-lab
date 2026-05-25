"""Tests for statistical summaries of scaffold experiment results."""

from ml_lab.experiments.conditions import ExperimentCondition
from ml_lab.experiments.statistical_summary import (
    compute_condition_deltas,
    format_delta_table,
    format_ranked_conditions,
    rank_conditions_for_independence,
)
from ml_lab.experiments.synthetic_experiment import SyntheticScaffoldingExperiment


def test_compute_condition_deltas_excludes_baseline() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=4, tasks_per_learner=2, seed=13)
    results = experiment.run()

    deltas = compute_condition_deltas(results, baseline=ExperimentCondition.UNRESTRICTED_AI)

    assert len(deltas) == 4
    assert all(delta.condition != ExperimentCondition.UNRESTRICTED_AI for delta in deltas)
    assert all(delta.baseline == ExperimentCondition.UNRESTRICTED_AI for delta in deltas)


def test_rank_conditions_for_independence_returns_sorted_conditions() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=4, tasks_per_learner=2, seed=17)
    results = experiment.run()

    ranked = rank_conditions_for_independence(results)

    assert len(ranked) == 5
    scores = [condition.independence_score for condition in ranked]
    assert scores == sorted(scores, reverse=True)


def test_summary_tables_include_expected_headers() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=4, tasks_per_learner=2, seed=19)
    results = experiment.run()
    deltas = compute_condition_deltas(results)
    ranked = rank_conditions_for_independence(results)

    delta_table = format_delta_table(deltas)
    ranked_table = format_ranked_conditions(ranked)

    assert "Transfer Delta" in delta_table
    assert "Overreliance Delta" in delta_table
    assert "Independence Score" in ranked_table
    assert "timing_and_fading" in ranked_table
