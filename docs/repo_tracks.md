# Repository Tracks

This repository currently supports two related research tracks. Both tracks use small, auditable Python objects and CSV-based workflows, but they answer different research questions and should not be interpreted as one empirical study.

## Track A: Adaptive scaffolding simulation

The adaptive scaffolding track studies whether learner-state-aware support can improve learning-relevant outcomes under cognitive load. This track is implemented through the core learner-state, scaffold-action, policy, experiment-runner, and evaluation objects.

Primary modules:

```text
src/ml_lab/core/          Learner states, scaffold actions, policies, arms, and outcome metrics
src/ml_lab/experiments/   Synthetic learners, task environments, experiment configuration, and runner
src/ml_lab/evaluation/    Arm summaries, pairwise comparisons, and CSV output helpers
```

Current workflow:

```text
simulate learner events -> export event log -> summarize by arm -> compute pairwise comparisons
```

Current interpretation boundary: synthetic events validate object interfaces, logging assumptions, policy behavior, reproducibility, and analysis plumbing. They do not demonstrate that adaptive scaffolding improves real learner outcomes.

Near-term needs:

- learner-level aggregation before research-facing arm comparisons;
- task specifications that distinguish practice, transfer, and delayed-post-test events;
- durable-learning and transfer metrics;
- uncertainty intervals for pairwise comparisons;
- clearer separation between synthetic workflow validation and empirical claims.

## Track B: Citation-integrity audit workflow

The citation-integrity audit track studies how citation claims, references, adjudicated findings, and ML-assisted review flags can be represented and summarized for audit workflows. This track is implemented under the audit package and exposed through separate command-line entry points.

Primary modules:

```text
src/ml_lab/audit/records.py   Citation claims, reference records, audit findings, and audit records
src/ml_lab/audit/io.py        CSV schema, template writing, and adjudicated-record loading
src/ml_lab/audit/metrics.py   Audit summaries and reduction estimates
src/ml_lab/audit/cli.py       Template and analysis command-line entry points
```

Current workflow:

```text
create audit template -> adjudicate citation records -> summarize audit arms -> estimate mis-citation reduction
```

Current interpretation boundary: audit summaries describe adjudicated records in the provided CSV. They do not establish external validity, general audit effectiveness, or publication-level citation quality without a defined sample, adjudication protocol, and reliability checks.

Near-term needs:

- documentation in the README and researcher guide;
- example audit CSV with synthetic records;
- inter-rater reliability support if multiple reviewers are used;
- confidence intervals for mis-citation rates and reductions;
- explicit connection between audit metrics and publication claims.

## Shared design principles

Both tracks should preserve the same engineering discipline:

- keep domain objects small and independently testable;
- validate fields at object boundaries;
- make random seeds and CSV schemas explicit;
- separate workflow validation from empirical evidence;
- document interpretation limits next to runnable commands;
- add tests before treating a workflow as stable.

## Recommended next branch

The next technical branch should focus on Track A outcome structure:

```bash
git checkout -b feature/learner-outcome-layer
```

Suggested scope:

```text
1. Add LearnerSummary for learner-level aggregation.
2. Add summarize_by_learner() and learner-level arm summaries.
3. Add TaskSpec with task_type fields for practice, transfer, and delayed post-test events.
4. Add tests for learner aggregation and task-type validation.
5. Update synthetic workflow documentation with the new output schema.
```

This branch should come before learned-policy work because policy learning should optimize against durable, learner-level outcomes rather than shallow event-level synthetic summaries.
