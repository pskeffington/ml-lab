# Experimental Protocol: Evaluating Best Practices in ML Scaffolding

## Study Aim

Evaluate whether best-practice adaptive scaffolding improves durable learning, transfer, metacognitive calibration, and independent performance compared with static scaffolding and unrestricted AI assistance.

## Research Question

Which scaffolding practices in ML-supported learning environments best improve transfer and independent problem solving while minimizing overreliance?

## Hypotheses

### H1: Transfer

Learners receiving adaptive timing-and-fading scaffolds will outperform learners receiving unrestricted AI assistance on unsupported transfer tasks.

### H2: Calibration

Learners receiving metacognitive scaffolds will show better confidence-correctness calibration than learners receiving direct answer support.

### H3: Dependency

Learners receiving faded scaffolds will show lower hint dependency than learners receiving static or unrestricted assistance.

### H4: Productive Struggle

Moderate productive struggle before intervention will predict stronger delayed learning outcomes than immediate high-intensity support.

## Experimental Conditions

### Condition 1: No-AI Control

Learners complete tasks using standard instructional materials only.

### Condition 2: Unrestricted AI Assistance

Learners may ask an AI assistant for help at any time. No scaffold timing, fading, or hint laddering is enforced.

### Condition 3: Static Scaffolding

Learners receive fixed scaffold prompts that do not adapt to performance, confidence, or prior help use.

### Condition 4: Adaptive Scaffold Policy

Learners receive scaffolds selected from learner-state evidence. The policy uses attempts, error patterns, confidence, time on task, and prior scaffold use.

### Condition 5: Adaptive Timing-and-Fading Policy

Learners receive adaptive scaffolds with explicit productive-struggle thresholds and fading as competence improves.

## Task Domain

Initial implementation should use introductory machine-learning reasoning tasks, such as:

- Selecting an appropriate model for a problem
- Interpreting train-test splits
- Diagnosing overfitting and underfitting
- Choosing evaluation metrics
- Understanding bias-variance tradeoffs
- Explaining feature leakage

This domain is appropriate because tasks can be generated, scored, and varied for transfer while remaining relevant to ML education.

## Outcome Measures

### Immediate Performance

Score on scaffolded learning tasks.

### Delayed Performance

Score on similar tasks after a delay or simulated delay condition.

### Transfer Performance

Score on novel task variants requiring the same concept but different surface features.

### Calibration

Difference between learner confidence and correctness.

### Hint Dependency

Frequency and intensity of scaffold use, especially before independent attempts.

### Productive Struggle

Time and attempts before intervention, bounded so that struggle remains constructive rather than frustrating.

### Independent Recovery

Performance after scaffolds are removed.

## Minimum Data Schema

Each learning event should include:

```text
learner_id
task_id
condition
concept
task_difficulty
attempt_number
response_correct
confidence
elapsed_seconds
scaffold_requested
scaffold_type
scaffold_intensity
policy_reason
post_scaffold_correct
transfer_task_id
```

## Analysis Plan

Primary comparisons:

- Adaptive timing-and-fading vs unrestricted AI assistance
- Adaptive timing-and-fading vs static scaffolding
- Static scaffolding vs unrestricted AI assistance
- All scaffolded conditions vs no-AI control

Primary models:

- Regression models for transfer performance
- Mixed-effects models for repeated learner-task observations
- Calibration error analysis
- Mediation analysis for whether reduced hint dependency explains transfer gains

## Reproducibility Standard

The repository should support synthetic trace generation before human data collection. Synthetic traces allow the scaffold policy, metric definitions, and analysis pipeline to be tested before any IRB-dependent study.
