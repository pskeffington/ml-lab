# Statistical Summary Workflow

## Purpose

The statistical summary workflow converts synthetic condition results into paper-facing comparisons. It is designed to support interpretation, not to overclaim empirical effects from synthetic data.

## Commands

Run the summary workflow:

```bash
python scripts/summarize_synthetic_experiment.py
```

The script prints:

1. Condition-level synthetic experiment results
2. Deltas against unrestricted AI assistance
3. Independence ranking across conditions

## Baseline Comparison

The default baseline is unrestricted AI assistance. This comparison is central because the paper argues that better scaffolding is not equivalent to more available help.

Useful interpretation:

- Positive transfer delta is desirable.
- Negative calibration error delta is desirable.
- Negative overreliance delta is desirable.
- Immediate accuracy delta is secondary and should not dominate interpretation.

## Independence Score

The independence score is a synthetic ranking objective:

```text
transfer_accuracy - 0.50 * calibration_error - 0.50 * overreliance_score
```

Higher values indicate a better balance of transfer, calibration, and low overreliance.

## Interpretation Warning

The ranking is a design-validation tool. It should not be described as evidence that one real-world instructional condition is superior without human learner data.
