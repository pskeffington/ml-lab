# ml-lab

Adaptive machine-learning scaffolding research lab for studying learning under cognitive load.

## Overview

`ml-lab` is a reproducible research sandbox for testing whether adaptive machine-learning scaffolds improve learning outcomes when learners face cognitively demanding tasks. The project frames instructional support as a policy problem: learner state is observed, a scaffold action is selected, and downstream learning outcomes are measured.

The initial study compares adaptive scaffolding against static scaffolding, unguided LLM assistance, and a no-AI control condition. The intended outcomes are durable learning, transfer, metacognitive calibration, and reduced hint dependency.

## Working title

**Adaptive Machine-Learning Scaffolding for Learning Under Cognitive Load**

## Research question

Does adaptive ML-driven scaffolding improve learning transfer and metacognitive calibration compared with static scaffolding, unguided LLM use, and no-AI control conditions?

## Experimental conditions

| Condition | Description | Purpose |
| --- | --- | --- |
| Adaptive ML scaffold | Learner support changes in response to estimated learner state. | Tests whether state-aware support improves learning. |
| Static scaffold | Learners receive pre-specified support that does not adapt. | Separates scaffolding from adaptation. |
| Unguided LLM assistance | Learners may use LLM help without structured scaffold controls. | Tests whether unrestricted AI help supports durable learning or creates dependency. |
| No-AI control | Learners complete tasks without AI-mediated support. | Establishes a baseline comparison. |

## Core outcomes

- **Durable learning:** delayed post-test performance after the initial learning task.
- **Transfer:** performance on related but non-identical tasks.
- **Metacognitive calibration:** alignment between confidence and observed performance.
- **Hint dependency:** frequency, timing, and depth of support-seeking behavior.

## Repository map

```text
src/ml_lab/        Python package for learner state, scaffold policies, experiments, and evaluation
docs/              Research design notes, literature matrix, and paper-development materials
tests/             Unit tests for core objects, policies, and metrics
scripts/           Reproducible command-line experiment and analysis entry points
notebooks/         Exploratory demonstrations, diagnostics, and result inspection
```

## Planned object model

The implementation should remain small, modular, and testable.

```text
LearnerState        Current representation of performance, confidence, latency, errors, and help use
ScaffoldPolicy      Rule-based or learned policy that selects the next support action
ScaffoldAction      Hint, prompt, worked example, reflection cue, or other intervention
TaskEnvironment     Problem sequence, feedback rules, task metadata, and assessment timing
ExperimentArm       Assignment condition connecting policies, task rules, and logging behavior
OutcomeMetric       Reusable metric object for learning, transfer, calibration, and dependency
ExperimentRunner    Reproducible orchestration layer for simulation or empirical trials
```

## Documentation

Start with [`docs/README.md`](docs/README.md) for the documentation index. The core design document is [`docs/research_design.md`](docs/research_design.md).

## Local setup

From a Mac terminal:

```bash
git clone https://github.com/pskeffington/ml-lab.git
cd ml-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

When package metadata is added, install the project in editable mode:

```bash
python -m pip install -e .
```

## Development workflow

Use short-lived Git branches and clear commits.

```bash
git checkout -b docs-polish
git add README.md docs/
git commit -m "Polish project documentation"
git push origin docs-polish
```

Before merging implementation work, run the test suite once tests are available:

```bash
python -m pytest
```

## Reproducibility principles

- Keep research decisions documented before they are encoded in experiments.
- Promote exploratory notebook logic into scripts before treating results as final.
- Preserve random seeds, configuration files, and generated outputs needed to reproduce findings.
- Keep learner-state, scaffold-policy, and outcome-metric objects independently testable.

## Authorship

Paul Skeffington, MS, MPH  
Dartmouth College  
GitHub: [@pskeffington](https://github.com/pskeffington)  
Contact: paulskeffington@gmail.com
