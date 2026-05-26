# Pre-Analysis Plan Template

This template separates planned research claims from exploratory engineering work. Complete it before treating synthetic or empirical results as evidence.

## Study title

Adaptive Machine-Learning Scaffolding for Learning Under Cognitive Load

## Study purpose

State whether the analysis uses simulated learners, pilot learners, or a full empirical sample. Synthetic results should be described as validation of code paths and assumptions, not as evidence of learning effectiveness.

## Primary research question

Does adaptive ML-driven scaffolding improve learning transfer and metacognitive calibration compared with static scaffolding, unguided LLM use, and no-AI control conditions?

## Experimental arms

- Adaptive ML scaffold
- Static scaffold
- Unguided LLM assistance
- No-AI control

## Primary outcomes

Define each outcome before analysis begins.

| Outcome | Operational definition | Timing | Primary comparison |
| --- | --- | --- | --- |
| Durable learning | Delayed post-test performance | To be specified | Adaptive ML scaffold vs. each comparison arm |
| Transfer | Performance on related but non-identical tasks | To be specified | Adaptive ML scaffold vs. each comparison arm |
| Metacognitive calibration | Absolute confidence-performance gap | During and after task sequence | Adaptive ML scaffold vs. each comparison arm |
| Hint dependency | Frequency and intensity of support use | During task sequence | Adaptive ML scaffold vs. unguided LLM assistance |

## Secondary outcomes

- Latency or time-on-task.
- Help-seeking frequency.
- Action intensity.
- Error-type transitions.
- Learner-state stability across tasks.

## Planned comparisons

Primary pairwise comparisons:

- Adaptive ML scaffold vs. static scaffold.
- Adaptive ML scaffold vs. unguided LLM assistance.
- Adaptive ML scaffold vs. no-AI control.

Secondary pairwise comparisons:

- Static scaffold vs. no-AI control.
- Unguided LLM assistance vs. no-AI control.
- Static scaffold vs. unguided LLM assistance.

## Statistical summaries

At minimum, report:

- arm-level means;
- mean differences;
- Cohen's d for pairwise comparisons;
- sample size by arm;
- missing-data counts when empirical data are used.

## Model specifications

For synthetic runs, start with descriptive summaries and pairwise effect-size comparisons. For empirical data, specify models before analysis begins.

Candidate empirical models:

- ordinary least squares for continuous outcomes;
- logistic regression for binary correctness outcomes;
- mixed-effects models for repeated task observations nested within learners;
- robustness checks using learner-level aggregated outcomes.

## Exclusion rules

Specify exclusion rules before running empirical analysis. Examples may include incomplete task sequences, failed attention checks, duplicate learner identifiers, or missing confidence ratings.

## Missing data

Document whether missing data will be excluded, imputed, or modeled directly. For empirical work, report missingness by arm and outcome.

## Multiple comparisons

State whether p-values will be adjusted when inferential tests are added. Synthetic comparisons should emphasize engineering diagnostics rather than statistical significance.

## Reproducibility requirements

- Record random seeds.
- Preserve configuration files.
- Commit analysis scripts.
- Keep generated outputs separate from source code unless outputs are part of a release artifact.
- Report any deviations from this plan.

## Interpretation boundaries

Synthetic learner results can demonstrate that the experiment runner, logging schema, and analysis pipeline behave as expected. They cannot establish that adaptive scaffolding improves real learner outcomes. Empirical claims require appropriate study design, human-subject review where applicable, and transparent reporting.
