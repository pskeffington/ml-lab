# Reporting Workflow

## Purpose

The reporting workflow turns synthetic experiment outputs into manuscript-facing markdown artifacts. These reports are designed for reproducibility, interpretation, and later integration into the paper draft.

## Command

Generate the default synthetic experiment report:

```bash
python scripts/generate_synthetic_report.py
```

Default output:

```text
reports/generated/synthetic_experiment_report.md
```

## Report Contents

The generated report includes:

- Purpose statement
- Condition-level synthetic results
- Deltas against unrestricted AI
- Independence ranking
- Interpretation guardrail

## Interpretation Standard

Reports generated from synthetic data should be treated as protocol-validation artifacts. They can support workflow validation, code review, and manuscript planning, but they should not be used to claim human learning effects.

## Manuscript Use

The report can support the synthetic methods and reproducibility sections of the manuscript. Human-subject data will be required for any empirical claims about learner outcomes.
