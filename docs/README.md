# Documentation

This directory contains the working documentation for the `ml-lab` proposed research study.

## Current direction

`ml-lab` is now centered on an auditable ML-assisted workflow for paper-format and multilingual healthcare-document ingestion, evidence review, quality checks, and human adjudication.

The current lead study question is:

```text
Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?
```

The project remains an early-stage proposal and pre-pilot research scaffold. It is not an approved clinical system, production ingestion service, human-subject protocol, or validated empirical tool.

## Core documents

- [`roadmap.md`](roadmap.md): Current phased development plan for the health-system ingestion and evidence-review direction.
- [`paper_multilingual_ingestion_workflow.md`](paper_multilingual_ingestion_workflow.md): Architecture and study-design note for paper, scanned, multilingual, OCR, translation, provenance, and adjudication workflow.
- [`dartmouth_health_study_concept.md`](dartmouth_health_study_concept.md): Dartmouth Health-facing feasibility-pilot concept note.
- [`pilot_protocol.md`](pilot_protocol.md): Existing citation-integrity pilot protocol that supports the evidence-review track.
- [`data_dictionary.md`](data_dictionary.md): Current data dictionary for citation-audit records and learner-study event records.
- [`repo_tracks.md`](repo_tracks.md): Architecture boundary between the health-system ingestion direction, citation-integrity audit workflow, and older adaptive scaffolding simulation.

## Supporting documents

- [`research_design.md`](research_design.md): Earlier adaptive-scaffolding study framing, retained as background and possible secondary simulation track.
- [`researcher_guide.md`](researcher_guide.md): Practical orientation for ML researchers who want to extend, simulate, or evaluate the project.
- [`synthetic_workflow.md`](synthetic_workflow.md): Instructions for running the four-arm synthetic adaptive-scaffolding experiment and analysis workflow.
- [`pre_analysis_plan.md`](pre_analysis_plan.md): Template for planned outcomes, comparisons, model specifications, exclusions, and interpretation boundaries.
- [`literature_matrix.md`](literature_matrix.md): Construct-to-source matrix for linking prior research to implementation and study-design decisions.
- [`evidence_roadmap.md`](evidence_roadmap.md): Publication-oriented evidence ladder, milestones, claim boundaries, and next artifacts.

## Recommended reading order

1. Read [`roadmap.md`](roadmap.md) to understand the current project direction.
2. Read [`paper_multilingual_ingestion_workflow.md`](paper_multilingual_ingestion_workflow.md) to understand the proposed ingestion and adjudication workflow.
3. Read [`dartmouth_health_study_concept.md`](dartmouth_health_study_concept.md) to understand the health-system feasibility-pilot frame.
4. Read [`repo_tracks.md`](repo_tracks.md) to understand which parts of the repository are primary, supporting, or legacy-background tracks.
5. Review [`pilot_protocol.md`](pilot_protocol.md) and [`data_dictionary.md`](data_dictionary.md) to understand the current audit workflow and data fields.
6. Use [`pre_analysis_plan.md`](pre_analysis_plan.md) and [`evidence_roadmap.md`](evidence_roadmap.md) before interpreting any outputs as research evidence.

## Documentation principles

The documentation should remain concise, reproducible, and implementation-oriented. Each document should make clear what research decision it supports, how it connects to the codebase, and what evidence or assumptions it depends on.

## Safety and governance principles

- Keep public repository examples synthetic or aggregate only.
- Do not commit PHI, private documents, identifiable student work, restricted source text, or confidential health-system materials.
- Preserve provenance for OCR, translation, extracted fields, quality flags, and human adjudication.
- Treat translation and OCR outputs as uncertain derived artifacts, not original records.
- Keep human adjudication as the source of truth for pilot evaluation.
- Avoid language implying validated clinical AI, patient-facing automation, or approved deployment.

## Style conventions

Use direct academic prose, define constructs before operationalizing them, and keep methods language aligned with the objects implemented under `src/ml_lab/`. Prefer small sections that can be maintained independently as the experimental framework matures.