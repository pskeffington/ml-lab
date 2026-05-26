# Roadmap

This roadmap organizes future work by research utility rather than implementation difficulty alone.

## Phase 1: Research scaffold

Goal: make the repository understandable, auditable, and safe to extend.

Status: in progress.

Key outputs:

- Project README with research framing.
- Research design document.
- Researcher guide.
- Core object model for learner state, scaffold actions, policies, arms, and metrics.
- Unit tests for core behavior.

Research utility:

- Gives new researchers a fast orientation path.
- Makes the initial theoretical claim visible before implementation expands.
- Keeps code objects aligned with the study design.

## Phase 2: Simulated experiment loop

Goal: let researchers run a small end-to-end simulated study.

Planned outputs:

- `TaskEnvironment` object for task sequences and feedback rules.
- `ExperimentRunner` object for assigning arms and executing learner traces.
- Synthetic learner generator.
- Event-log schema and example output.
- Scripted simulation entry point under `scripts/`.
- Tests for reproducibility under fixed random seeds.

Research utility:

- Validates policy behavior before empirical deployment.
- Makes logging assumptions visible.
- Provides a benchmark for comparing rule-based and learned scaffold policies.

## Phase 3: Analysis layer

Goal: support transparent comparison across experimental arms.

Planned outputs:

- Durable-learning metric.
- Transfer metric.
- Calibration and hint-dependency reporting functions.
- Arm-level summary tables.
- Basic regression or mixed-effects analysis script.
- Pre-analysis plan template.

Research utility:

- Helps prevent post-hoc metric drift.
- Makes planned comparisons explicit.
- Creates a bridge from simulation to empirical study analysis.

## Phase 4: Learned policies

Goal: replace or augment the rule-based policy with learned scaffold policies.

Planned outputs:

- Supervised policy baseline.
- Contextual-bandit policy prototype.
- Offline evaluation utilities.
- Policy comparison report.
- Tests that ensure learned policies respect scaffold-action constraints.

Research utility:

- Tests whether adaptation adds value beyond static or heuristic support.
- Allows policy behavior to be audited before human-subject deployment.
- Separates model performance from learning-outcome claims.

## Phase 5: Manuscript and dissemination layer

Goal: make the project useful for paper development and external review.

Planned outputs:

- Introduction draft.
- Best-practices framework section.
- System-design section.
- Synthetic methods section.
- Limitations and pilot-study section.
- Contribution map linking repository objects to manuscript claims.

Research utility:

- Helps reviewers understand the connection between code, theory, and claims.
- Supports manuscript drafting without disconnecting from implementation.
- Creates a reusable structure for future ML education research projects.

## Phase 6: Human-subject pilot readiness

Goal: prepare the repository to support a human-subject learning study.

Planned outputs:

- Study protocol notes.
- Data dictionary.
- Consent-aware logging plan.
- De-identification plan.
- Reproducible analysis pipeline.
- Final reporting templates.

Research utility:

- Makes the platform easier to review, audit, and replicate.
- Reduces ambiguity between engineering outputs and research evidence.
- Supports later empirical claims about learning effectiveness.

## Near-term priority

The next technical priority is to add a minimal synthetic experiment loop with CSV export and statistical summaries. The next documentation priority is to add a pre-analysis plan template and literature matrix so future researchers can connect constructs, measures, and hypotheses before running experiments.
