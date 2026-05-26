# ml-lab

Adaptive machine-learning scaffolding research lab for studying learning under cognitive load.

## Overview

`ml-lab` is a reproducible research sandbox for testing whether adaptive machine-learning scaffolds improve learning outcomes when learners face cognitively demanding tasks. The project frames instructional support as a policy problem: learner state is observed, a scaffold action is selected, and downstream learning outcomes are measured.

The initial study compares adaptive scaffolding against static scaffolding, unguided LLM assistance, and a no-AI control condition. The intended outcomes are durable learning, transfer, metacognitive calibration, and reduced hint dependency.

## Current status

The repository supports a minimal four-arm synthetic workflow:

```text
simulate learner events -> export event log -> summarize by arm -> compute pairwise comparisons
```

Synthetic output is useful for validating object interfaces, logging assumptions, policy behavior, and analysis plumbing. It should not be interpreted as evidence of real learning effectiveness.

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

## Repository map

```text
src/ml_lab/core/          Learner state, scaffold actions, policies, arms, and outcome metrics
src/ml_lab/experiments/   Synthetic task environment, learners, and experiment runner
src/ml_lab/evaluation/    Arm summaries, pairwise comparisons, and CSV analysis utilities
docs/                     Research design, workflow, pre-analysis, and literature documentation
tests/                    Unit tests for core objects, experiment running, and evaluation
outputs/                  Generated synthetic event logs and summaries, created locally
```

## Implemented object model

```text
LearnerState              Performance, confidence, latency, errors, and help use
ScaffoldAction            Hint, prompt, worked example, reflection cue, or other intervention
ScaffoldPolicy            Interface for policies that select support actions
RuleBasedScaffoldPolicy   Transparent adaptive baseline policy
StaticScaffoldPolicy      Non-adaptive comparison policy
UnguidedLLMPolicy         Synthetic proxy for unrestricted LLM assistance
TaskEnvironment           Ordered task sequence for synthetic experiments
SyntheticLearner          Synthetic learner with skill and confidence parameters
ExperimentArm             Assignment condition connecting policies and logging behavior
ExperimentRunner          Reproducible orchestration layer for synthetic trials
ArmSummary                Arm-level descriptive summary
PairwiseComparison        Mean differences and Cohen's d between arms
```

## Documentation spine

Start with [`docs/README.md`](docs/README.md). Key documents:

- [`docs/research_design.md`](docs/research_design.md)
- [`docs/researcher_guide.md`](docs/researcher_guide.md)
- [`docs/synthetic_workflow.md`](docs/synthetic_workflow.md)
- [`docs/pre_analysis_plan.md`](docs/pre_analysis_plan.md)
- [`docs/literature_matrix.md`](docs/literature_matrix.md)
- [`docs/roadmap.md`](docs/roadmap.md)

## Local setup

From a Mac terminal:

```bash
git clone https://github.com/pskeffington/ml-lab.git
cd ml-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the synthetic workflow

```bash
ml-lab-run
ml-lab-analyze
python -m pytest
```

Expected local outputs:

```text
outputs/synthetic_event_log.csv
outputs/arm_summary.csv
outputs/pairwise_comparisons.csv
```

## Development workflow

Use short-lived Git branches and clear commits.

```bash
git checkout -b feature/descriptive-name
git status
git diff
git add <files>
git commit -m "Describe the focused change"
git push origin feature/descriptive-name
```

## Reproducibility principles

- Keep research decisions documented before they are encoded in experiments.
- Promote exploratory notebook logic into scripts before treating results as final.
- Preserve random seeds, configuration files, and generated outputs needed to reproduce findings.
- Keep learner-state, scaffold-policy, experiment-runner, and outcome-metric objects independently testable.
- Distinguish synthetic workflow validation from empirical learning claims.

## Authorship

Paul Skeffington, MS, MPH  
Dartmouth College  
GitHub: [@pskeffington](https://github.com/pskeffington)  
Contact: paulskeffington@gmail.com
