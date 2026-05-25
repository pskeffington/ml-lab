# Contribution Map

## Project Claim

The project argues that best-practice ML scaffolding should maximize learner independence, not merely provide more assistance.

## Contribution 1: Best-Practices Framework

The framework defines practical design rules for scaffold timing, fading, metacognitive prompting, hint laddering, and overreliance prevention.

### Paper Role

This is the conceptual contribution.

### Repo Evidence

- `docs/scaffolding_best_practices.md`
- `docs/result_interpretation.md`

## Contribution 2: Auditable Scaffold Policy

The system treats scaffolding as a policy problem. A policy observes learner state and selects scaffold type, intensity, and rationale.

### Paper Role

This is the system-design contribution.

### Repo Evidence

- `src/ml_lab/core/learner_state.py`
- `src/ml_lab/core/scaffold.py`
- `src/ml_lab/core/scaffold_policy.py`

## Contribution 3: Evaluation Metrics

The project defines metrics for overreliance, calibration, immediate performance, transfer performance, premature help-seeking, and unsupported drop-off.

### Paper Role

This is the measurement contribution.

### Repo Evidence

- `src/ml_lab/evaluation/overreliance_metrics.py`
- `src/ml_lab/evaluation/calibration_metrics.py`

## Contribution 4: Reproducible Synthetic Experiment

The synthetic experiment validates the experimental structure before human-subject data collection.

### Paper Role

This is the reproducibility and protocol-validation contribution.

### Repo Evidence

- `src/ml_lab/experiments/conditions.py`
- `src/ml_lab/experiments/synthetic_experiment.py`
- `scripts/run_synthetic_experiment.py`
- `docs/synthetic_experiment_methods.md`

## Contribution 5: Pathway to Human-Subject Study

The repository establishes a protocol that can be extended into a pilot study with real learners completing introductory ML reasoning tasks.

### Paper Role

This is the future empirical contribution.

### Repo Evidence

- `docs/experimental_protocol.md`
- `docs/paper_outline.md`

## Target Venue Fit

### Learning Analytics and Knowledge

Strong fit for measurement, learner traces, calibration, and overreliance metrics.

### Artificial Intelligence in Education

Strong fit for adaptive scaffold policies and intelligent learning systems.

### Educational Data Mining

Strong fit if the project emphasizes policy evaluation, learner modeling, and trace data.

### Computers and Education: Artificial Intelligence

Strong fit if the paper emphasizes human-AI learning design and educational AI governance.
