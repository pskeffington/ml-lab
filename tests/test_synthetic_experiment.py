"""Tests for the synthetic scaffolding experiment."""

from ml_lab.experiments.conditions import ExperimentCondition
from ml_lab.experiments.synthetic_experiment import (
    SyntheticScaffoldingExperiment,
    format_results_table,
)


def test_synthetic_experiment_returns_all_default_conditions() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=5, tasks_per_learner=3, seed=7)

    results = experiment.run()

    assert len(results) == 5
    assert {result.condition for result in results} == {
        ExperimentCondition.NO_AI_CONTROL,
        ExperimentCondition.UNRESTRICTED_AI,
        ExperimentCondition.STATIC_SCAFFOLDING,
        ExperimentCondition.ADAPTIVE_POLICY,
        ExperimentCondition.TIMING_AND_FADING,
    }


def test_synthetic_experiment_result_values_are_normalized() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=5, tasks_per_learner=3, seed=11)

    results = experiment.run()

    for result in results:
        assert 0.0 <= result.immediate_accuracy <= 1.0
        assert 0.0 <= result.transfer_accuracy <= 1.0
        assert 0.0 <= result.calibration_error <= 1.0
        assert 0.0 <= result.overreliance_score <= 1.0
        assert 0.0 <= result.premature_help_rate <= 1.0
        assert 0.0 <= result.unsupported_drop_rate <= 1.0


def test_format_results_table_contains_core_metrics() -> None:
    experiment = SyntheticScaffoldingExperiment(learner_count=3, tasks_per_learner=2, seed=3)

    table = format_results_table(experiment.run())

    assert "Immediate Accuracy" in table
    assert "Transfer Accuracy" in table
    assert "Calibration Error" in table
    assert "Overreliance" in table
    assert ExperimentCondition.TIMING_AND_FADING.value in table
