# Manuscript Draft: Methods

## Methods

This project uses a design-science and protocol-validation approach to develop best practices for adaptive machine-learning scaffolding. The goal of the current phase is not to estimate treatment effects in human learners, but to operationalize a reproducible framework that can later support a human-subject pilot study. The methods therefore combine conceptual framework development, scaffold-policy design, metric specification, synthetic trace generation, and automated reporting.

## Framework Development

The framework was developed around the principle that effective scaffolding should increase learner independence over time. The design emphasizes seven practices: preserving productive struggle, using learner-state evidence before intervention, organizing support through hint ladders, fading assistance as competence improves, requiring metacognitive work, measuring overreliance, and making scaffold decisions auditable. These practices define the conceptual criteria against which scaffold policies are evaluated.

## Learner-State Representation

The executable framework represents learner state using a small set of auditable features: estimated knowledge, confidence, cognitive load, hint dependency, attempt count, and elapsed time. These features are intentionally compact so that policy decisions remain interpretable. The learner-state representation supports three core decisions: whether the learner needs support, whether the learner is ready for scaffold fading, and whether the learner shows risk of overreliance.

## Scaffold Policy Design

The initial scaffold policy implements timing and fading rules. When a learner has not yet attempted a task, the policy provides low-intensity orientation support rather than a direct answer. When the learner shows high hint dependency with limited attempts, the policy selects a diagnostic question to require reflection before further assistance. When the learner demonstrates stronger knowledge, manageable cognitive load, and low dependency, the policy fades support. When evidence indicates genuine need, the policy provides moderate strategy support rather than high-intensity answer replacement.

## Synthetic Protocol Validation

The synthetic experiment compares five conditions: no-AI control, unrestricted AI assistance, static scaffolding, adaptive scaffold policy, and adaptive timing-and-fading scaffolding. Each condition is encoded as an explicit configuration describing scaffold access, adaptivity, timing gates, fading, metacognitive prompting, and baseline hint dependency. Synthetic learners complete repeated introductory machine-learning reasoning tasks with varying difficulty. For each learner-task interaction, the simulation estimates immediate correctness, transfer correctness, confidence, scaffold intensity, help-seeking behavior, and unsupported follow-up performance.

## Outcome Measures

The primary outcomes are transfer accuracy, calibration error, overreliance score, premature help rate, and unsupported drop rate. Immediate accuracy is also reported but treated as secondary because it can be inflated by high-intensity assistance. Calibration error is defined as the absolute difference between mean confidence and accuracy. Overreliance is measured using premature help-seeking, high-intensity scaffold use, copy-forward behavior, and performance drop-off after scaffold removal.

## Analysis Workflow

The analysis workflow produces condition-level summaries, deltas against unrestricted AI assistance, and an independence ranking. The independence ranking prioritizes transfer while penalizing calibration error and overreliance. This ranking is used as a design-validation tool rather than evidence of real-world instructional superiority. The workflow also exports CSV files and markdown reports to support reproducibility and manuscript development.

## Reproducibility Controls

The repository includes automated tests for scaffold-policy behavior, synthetic experiment outputs, result export, statistical summaries, reporting, and citation verification. The experiment uses fixed random seeds for reproducibility. Generated reports include interpretation guardrails stating that synthetic outputs validate the protocol and software pipeline but do not establish empirical learning effects.

## Transition to Empirical Study

The synthetic protocol prepares the project for a future pilot study with real learners. In that phase, participants would complete introductory machine-learning reasoning tasks under randomized support conditions. The main empirical comparison would test whether adaptive timing-and-fading scaffolding improves transfer, calibration, and independent recovery relative to unrestricted AI assistance.
