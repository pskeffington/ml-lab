# Documentation

This directory contains the working documentation for the `ml-lab` research project.

## Contents

- [`research_design.md`](research_design.md): Core study framing, hypotheses, experimental arms, measures, and implementation plan.
- [`researcher_guide.md`](researcher_guide.md): Practical orientation for ML researchers who want to extend, simulate, or evaluate the project.
- [`synthetic_workflow.md`](synthetic_workflow.md): Instructions for running the four-arm synthetic experiment and analysis workflow.
- [`pre_analysis_plan.md`](pre_analysis_plan.md): Template for planned outcomes, comparisons, model specifications, exclusions, and interpretation boundaries.
- [`literature_matrix.md`](literature_matrix.md): Construct-to-source matrix for linking prior research to implementation and study-design decisions.
- [`evidence_roadmap.md`](evidence_roadmap.md): Publication-oriented evidence ladder, milestones, claim boundaries, and next artifacts.
- [`roadmap.md`](roadmap.md): Phased development plan organized by research utility.

## Recommended reading order

1. Read [`research_design.md`](research_design.md) to understand the study frame.
2. Read [`researcher_guide.md`](researcher_guide.md) to understand how the codebase is meant to be extended.
3. Run the workflow in [`synthetic_workflow.md`](synthetic_workflow.md).
4. Review [`pre_analysis_plan.md`](pre_analysis_plan.md) before interpreting outputs.
5. Use [`literature_matrix.md`](literature_matrix.md) to connect claims to evidence and implementation choices.
6. Use [`evidence_roadmap.md`](evidence_roadmap.md) to decide which publication claims are currently supportable.

## Documentation principles

The documentation should remain concise, reproducible, and implementation-oriented. Each document should make clear what research decision it supports, how it connects to the codebase, and what evidence or assumptions it depends on.

## Style conventions

Use direct academic prose, define constructs before operationalizing them, and keep methods language aligned with the objects implemented under `src/ml_lab/`. Prefer small sections that can be maintained independently as the experimental framework matures.
