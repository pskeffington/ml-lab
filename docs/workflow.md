# Project Workflow

## Purpose

This workflow keeps the project aligned across code, experiments, and manuscript development. Every change should support the central research claim: effective ML scaffolding should improve learner independence, not merely increase assistance.

## Branching Model

Use focused branches for each unit of work.

Recommended branch names:

```text
feature/scaffold-policy
feature/synthetic-experiment
feature/evaluation-metrics
docs/manuscript-framework
docs/pilot-protocol
```

## Commit Standard

Each commit should do one thing and use a clear imperative message.

Examples:

```text
Add timing and fading scaffold policy
Add overreliance evaluation metrics
Document synthetic experiment methods
Add manuscript contribution map
```

## Development Loop

1. Define the research purpose of the change.
2. Add or update the smallest useful code or document component.
3. Add tests for executable behavior.
4. Run the test suite.
5. Commit with a clear message.
6. Update documentation if the public workflow changes.

## Code Workflow

### Install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .[dev]
```

### Test

```bash
pytest
```

### Lint

```bash
ruff check src tests scripts
```

## Experiment Workflow

Run the default synthetic scaffolding experiment:

```bash
python scripts/run_synthetic_experiment.py
```

Expected output is a markdown table with condition-level summary metrics:

- Immediate accuracy
- Transfer accuracy
- Calibration error
- Overreliance score
- Premature help rate
- Unsupported drop rate

## Interpretation Workflow

When reviewing results, prioritize outcomes in this order:

1. Transfer accuracy
2. Unsupported follow-up performance
3. Calibration error
4. Overreliance score
5. Immediate accuracy

Immediate task success should not be treated as sufficient evidence of learning.

## Manuscript Workflow

Manuscript development should proceed in this order:

1. `docs/paper_outline.md`
2. Introduction draft
3. Best-practices framework section
4. System-design section
5. Synthetic experiment methods section
6. Limitations and human-subject pilot pathway

## Pull Request Checklist

Before merging a change, confirm:

- The change supports the scaffolding research claim.
- Tests pass when code is modified.
- Documentation is updated when workflows change.
- Synthetic results are not overclaimed as human-learning evidence.
- New metrics are interpretable from 0.0 to 1.0 unless otherwise documented.

## Research Discipline

Do not optimize for a system that gives more help by default. Optimize for scaffold timing, fading, transfer, calibration, and independent recovery.
