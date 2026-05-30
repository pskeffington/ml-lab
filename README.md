# ml-lab

Auditable ML-assisted document review for paper-format and multilingual healthcare-document ingestion.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** early-stage proposed research study; materials are in proposal drafting and pre-pilot infrastructure development. Generated outputs validate software plumbing only and should not be interpreted as empirical evidence or validated clinical performance.  
**Last documentation refresh:** 2026-05-29

## Project status note

`ml-lab` is an early-stage proposed research study. The current repository materials support proposal drafting, research-design development, synthetic workflow validation, and pre-pilot planning. The repository does not yet represent a completed study, validated empirical system, approved clinical system, production ingestion service, or proven intervention.

Any outputs produced at this stage should be treated as draft planning artifacts, synthetic examples, or engineering validation artifacts unless and until a formal empirical study design, governance pathway, data collection process, and analysis plan are approved and executed.

Public-facing language should describe the project as a proposed feasibility pilot, early drafting effort, pre-pilot research scaffold, or synthetic validation workflow rather than as completed empirical evidence.

## Lead study question

Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?

## Overview

`ml-lab` is being refocused as a reproducible research scaffold for auditable ML-assisted document review in health-system and rural-health research contexts. The proposed workflow addresses paper-format and multilingual documentation problems: scanned PDFs, faxed pages, handwritten or printed forms, clinical and administrative packets, discharge materials, consent documents, public-health reports, research documentation, and other documents that require traceable review.

The system is intended to support human reviewers, not replace them. The core design principle is that OCR, translation, extraction, and ML quality flags must preserve provenance, confidence, uncertainty, and human adjudication.

## Current direction

The current lead workflow is:

```text
paper document
  -> scan or image capture
  -> image quality check
  -> document classification
  -> OCR and layout extraction
  -> language identification
  -> translation when needed
  -> claim and field extraction
  -> evidence/source linking
  -> ML-assisted quality flags
  -> human adjudication
  -> structured audit record
  -> aggregate feasibility and quality metrics
```

The intended comparison is:

```text
usual manual review vs ML-assisted human-adjudicated review
```

Primary outcome domains are quality, completeness, and review efficiency.

## What this repository is not

`ml-lab` is not:

```text
autonomous clinical decision-making
patient-facing automation
diagnosis or treatment recommendation software
an approved Dartmouth Health study or deployment
a validated clinical AI system
a repository for PHI, private documents, or confidential health-system materials
```

## Repository tracks

### Primary track: health-system document ingestion and evidence review

This is the lead direction. It concerns paper-format and multilingual healthcare-document ingestion, OCR provenance, translation uncertainty, quality flags, human adjudication, and feasibility metrics.

Key documents:

- [`docs/roadmap.md`](docs/roadmap.md)
- [`docs/paper_multilingual_ingestion_workflow.md`](docs/paper_multilingual_ingestion_workflow.md)
- [`docs/dartmouth_health_study_concept.md`](docs/dartmouth_health_study_concept.md)

### Supporting track: citation-integrity audit workflow

The existing audit workflow supports claim extraction, source linkage, adjudicated error labels, audit summaries, and ML-assisted review metrics.

Current commands:

```bash
ml-lab-audit-template
ml-lab-audit-analyze
```

Expected local output:

```text
outputs/citation_audit_summary.csv
```

### Background track: adaptive scaffolding simulation

The earlier adaptive-scaffolding simulation remains available as a secondary research scaffold for future reviewer-support, simulation, or education work. It is no longer the lead roadmap.

Current commands:

```bash
ml-lab-run
ml-lab-analyze
```

Expected local outputs:

```text
outputs/synthetic_event_log.csv
outputs/arm_summary.csv
outputs/pairwise_comparisons.csv
```

## Repository map

```text
src/ml_lab/core/          Earlier learner-state and scaffold-policy objects
src/ml_lab/experiments/   Earlier synthetic adaptive-scaffolding experiment runner
src/ml_lab/evaluation/    Earlier arm summaries, pairwise comparisons, and CSV helpers
src/ml_lab/audit/         Citation-integrity audit records, CSV I/O, metrics, and CLI commands
docs/                     Proposal, roadmap, workflow, protocol, and governance documentation
tests/                    Unit tests for implemented objects and workflows
outputs/                  Generated local outputs; do not commit sensitive records
```

Planned primary modules for the health-system ingestion direction:

```text
src/ml_lab/ingest/intake.py
src/ml_lab/ingest/page_quality.py
src/ml_lab/ingest/ocr_records.py
src/ml_lab/ingest/language.py
src/ml_lab/ingest/translation.py
src/ml_lab/ingest/extraction.py
src/ml_lab/ingest/adjudication.py
src/ml_lab/ingest/metrics.py
```

## Planned ingestion object model

```text
DocumentBatch
DocumentRecord
PageImageRecord
PageQualityRecord
OcrBlockRecord
LanguageDetectionRecord
TranslationRecord
ExtractedClaimRecord
ExtractedFieldRecord
QualityFlag
HumanAdjudicationRecord
AuditSummary
```

## Documentation spine

Start with [`docs/README.md`](docs/README.md). Key documents:

- [`docs/roadmap.md`](docs/roadmap.md)
- [`docs/paper_multilingual_ingestion_workflow.md`](docs/paper_multilingual_ingestion_workflow.md)
- [`docs/dartmouth_health_study_concept.md`](docs/dartmouth_health_study_concept.md)
- [`docs/repo_tracks.md`](docs/repo_tracks.md)
- [`docs/pilot_protocol.md`](docs/pilot_protocol.md)
- [`docs/data_dictionary.md`](docs/data_dictionary.md)
- [`docs/pre_analysis_plan.md`](docs/pre_analysis_plan.md)
- [`docs/evidence_roadmap.md`](docs/evidence_roadmap.md)

## Local setup

From a Mac terminal:

```bash
git clone https://github.com/pskeffington/ml-lab.git
cd ml-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run current implemented workflows

```bash
ml-lab-audit-template
ml-lab-audit-analyze
ml-lab-run
ml-lab-analyze
python -m pytest
```

## Reproducibility and governance principles

- Keep research decisions documented before they are encoded in experiments.
- Promote exploratory notebook logic into scripts before treating results as final.
- Preserve random seeds, configuration files, and generated outputs needed to reproduce findings.
- Distinguish synthetic workflow validation, pilot feasibility evidence, and empirical study claims.
- Do not commit PHI, identifiable human-subject data, private documents, restricted source materials, confidential health-system materials, or non-public participant records.
- Treat OCR and translation as uncertain derived artifacts, not original records.
- Preserve provenance for extracted fields, claims, quality flags, and adjudication decisions.
- Keep human adjudication as the source of truth.

## Authorship

Paul Skeffington, MS, MPH  
Dartmouth College  
GitHub: [@pskeffington](https://github.com/pskeffington)  
Contact: paulskeffington@gmail.com