# Researcher Guide

## What this repository is useful for

`ml-lab` is designed as a lightweight research scaffold for studying adaptive instructional support. It is most useful for researchers who want to compare scaffold policies, simulate learner trajectories, define reproducible outcome metrics, or prepare an empirical study of AI-supported learning.

The repository is not yet a full experimental platform. Its current value is in the object model, documentation structure, and early tests that make later extensions easier to review and reproduce.

## Research workflows supported

### 1. Policy prototyping

Researchers can implement scaffold policies that map learner state to instructional support actions. The current baseline is `RuleBasedScaffoldPolicy`, which provides a transparent comparison point for learned policies.

Useful extension points:

```text
src/ml_lab/core/state.py       Learner-state features
src/ml_lab/core/actions.py     Scaffold-action definitions
src/ml_lab/core/policies.py    Policy interface and baseline policies
```

### 2. Simulation studies

The project can be extended into a simulation environment where synthetic learners move through task sequences. This is useful before collecting human-subject data because policy behavior, logging requirements, and metric definitions can be tested under controlled assumptions.

A simulation workflow should specify:

- learner-state initialization rules;
- task sequence and feedback rules;
- policy assignment by experimental arm;
- state-transition assumptions;
- random seeds and configuration files;
- expected output tables.

### 3. Empirical study preparation

The object model can support a later human-subject study by defining what must be logged at each task event. Before collecting data, researchers should align the implementation with the study protocol, consent language, institutional review requirements, and data-retention plan.

Minimum event-level fields are described in [`research_design.md`](research_design.md).

### 4. Outcome analysis

The initial metric objects support calibration and hint-dependency scoring. Future work should add durable-learning and transfer metrics once assessment timing and task design are fixed.

Useful extension points:

```text
src/ml_lab/core/metrics.py     Outcome metric interface and metric implementations
tests/test_core.py             Unit tests for expected metric behavior
```

## Suggested researcher path

A new researcher should read the repository in this order:

1. [`README.md`](../README.md) for the project overview.
2. [`research_design.md`](research_design.md) for the study frame.
3. `src/ml_lab/core/state.py` to understand the learner-state representation.
4. `src/ml_lab/core/policies.py` to understand how scaffold decisions are selected.
5. `tests/test_core.py` to see the expected behavior of the current objects.

## Near-term improvements that would increase research utility

- Add a `TaskEnvironment` object for problem sequences and feedback rules.
- Add an `ExperimentRunner` that can execute a small simulated study.
- Add config files for reproducible experimental arms.
- Add durable-learning and transfer metrics.
- Add an example script that produces a small synthetic event log.
- Add a pre-analysis plan template under `docs/`.
- Add a literature matrix connecting constructs to measurement choices.

## Boundaries and cautions

This repository should distinguish clearly between simulated learners and empirical learners. Simulation results can validate code paths and assumptions, but they should not be described as evidence of learning effectiveness. Human-subject claims require an approved protocol, documented recruitment and assignment procedures, and a transparent analysis plan.
