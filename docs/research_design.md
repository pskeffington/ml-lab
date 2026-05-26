# Research Design

## Working title

Adaptive Machine-Learning Scaffolding for Learning Under Cognitive Load

## Purpose

This project evaluates whether adaptive machine-learning scaffolds can improve learning outcomes when learners work under cognitive load. The central comparison is between support that responds to learner state and support conditions that do not adapt in the same way.

## Research question

Does adaptive ML-driven scaffolding improve learning transfer and metacognitive calibration compared with static scaffolding, unguided LLM use, and no-AI control conditions?

## Conceptual model

The study treats learning support as a policy problem. A learner enters a task with a changing state that may include performance history, response latency, confidence, hint use, error type, and indicators of cognitive load. A scaffold policy observes that state and selects an intervention.

The expected mechanism is not simply that more help improves performance. The stronger claim is that well-timed, state-aware help can preserve productive effort while reducing unproductive cognitive burden.

## Experimental arms

| Arm | Description | Primary contrast |
| --- | --- | --- |
| Adaptive ML scaffold | Learner support changes in response to estimated learner state. | Tests the value of adaptive policy selection. |
| Static scaffold | Learners receive pre-specified support that does not respond to state. | Separates adaptation from scaffolding in general. |
| Unguided LLM assistance | Learners may use LLM help without structured scaffold constraints. | Tests whether unrestricted AI help produces durable learning or dependency. |
| No-AI control | Learners complete tasks without AI-mediated assistance. | Establishes a baseline for unsupported learning. |

## Primary outcomes

- Durable learning: delayed post-test performance after the initial learning task.
- Transfer: performance on related but non-identical problems.
- Metacognitive calibration: alignment between learner confidence and observed performance.
- Hint dependency: frequency, timing, and depth of support requests or scaffold use.

## Core implementation objects

The codebase should keep the research design object-oriented and modular.

```text
LearnerState        Current representation of performance, confidence, latency, errors, and help use.
ScaffoldPolicy      Rule-based or learned policy that selects the next support action.
ScaffoldAction      A concrete intervention, hint, prompt, worked example, or reflection cue.
TaskEnvironment     Problem sequence, feedback rules, task metadata, and assessment timing.
ExperimentArm       Assignment condition that binds a policy to task rules and logging behavior.
OutcomeMetric       Reusable metric object for learning, transfer, calibration, and dependency.
ExperimentRunner    Reproducible orchestration layer for simulation or empirical trials.
```

## Minimal viable experiment

The first working version should prioritize a small, auditable experiment over a complex adaptive system. A practical initial build can use simulated learner states, deterministic scaffold policies, and transparent outcome metrics. Once the interfaces are stable, the adaptive policy can be replaced with a learned model.

## Data logging requirements

Each task event should preserve enough information to reconstruct the learner trajectory.

```text
learner_id
experiment_arm
task_id
timestamp
observed_state
selected_action
learner_response
correctness
confidence
latency_seconds
hint_count
post_action_state
```

## Analysis plan

The initial analysis should estimate differences between experimental arms on each primary outcome. Model choice should depend on the data-generating process, but the planned structure should support ordinary least squares, generalized linear models, mixed-effects models, and repeated-measures designs.

Key comparisons:

- Adaptive ML scaffold versus static scaffold.
- Adaptive ML scaffold versus unguided LLM assistance.
- Adaptive ML scaffold versus no-AI control.
- Unguided LLM assistance versus no-AI control.

## Reproducibility standards

All simulations, experiments, and analyses should be runnable from scripts committed to the repository. Random seeds, configuration files, and generated outputs should be documented. Exploratory notebooks are acceptable for inspection, but final analyses should be promoted into scripts when results become part of the research record.

## Open design decisions

- Which learner-state features are observable without excessive instrumentation?
- How should cognitive load be measured or proxied?
- What domain tasks are appropriate for the first experiment?
- Should the first adaptive policy be rule-based, supervised, contextual-bandit, or reinforcement-learning based?
- What delay interval is sufficient to measure durable learning?
