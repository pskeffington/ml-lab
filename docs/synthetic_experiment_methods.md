# Synthetic Experiment Methods

## Purpose

The synthetic experiment provides a reproducible pilot framework for comparing scaffolding design conditions before collecting human-subject data. It is not intended to estimate real-world effect sizes. Its purpose is to validate the experimental structure, metrics, code path, and expected directional behavior of the scaffold-policy framework.

## Conditions

The experiment compares five conditions:

1. No-AI control
2. Unrestricted AI assistance
3. Static scaffolding
4. Adaptive scaffold policy
5. Adaptive timing-and-fading policy

## Simulated Learner Process

Each learner receives a baseline knowledge estimate and completes repeated introductory machine-learning reasoning tasks. Each task has a difficulty value, and the simulation estimates immediate correctness, transfer correctness, confidence, scaffold intensity, and help-seeking behavior.

## Core Assumptions

The simulation encodes the paper's theoretical expectations:

- Unrestricted high-intensity help may improve immediate performance while increasing overreliance.
- Metacognitive prompting improves calibration and transfer.
- Timing gates preserve productive struggle.
- Fading improves independent follow-up performance.
- Excessive hint dependency reduces transfer.

## Primary Outcomes

The synthetic experiment reports:

- Immediate accuracy
- Transfer accuracy
- Calibration error
- Composite overreliance score
- Premature help rate
- Unsupported drop rate

## Interpretation

Results should be interpreted as a software and protocol validation artifact, not as empirical evidence about human learners. The synthetic layer supports reproducibility by ensuring that all conditions, metrics, and outputs are defined before pilot data collection.

## Command

```bash
python scripts/run_synthetic_experiment.py
```

## Paper Use

The synthetic experiment can support a methods or reproducibility section by demonstrating that the framework is operationalized in code. Human learner data would be required for causal claims about real learning outcomes.
