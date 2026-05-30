# Roadmap

This roadmap refocuses `ml-lab` around the proposed health-system study direction: an auditable ML-assisted workflow for paper-format and multilingual healthcare-document ingestion, evidence review, quality checks, and human adjudication.

## Current project direction

`ml-lab` is an early-stage proposed research study and pre-pilot infrastructure project. The main research direction is now:

```text
Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?
```

This is not an approved clinical system, production ingestion service, human-subject protocol, or validated empirical tool. The repo should remain public-safe and should contain only code, schemas, documentation, synthetic examples, and aggregate non-sensitive outputs.

## Primary track: health-system document ingestion and evidence review

The main ecosystem-facing track is a governed workflow for messy health-system documentation:

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

The intended value is not autonomous clinical decision-making. The intended value is safer, faster, more transparent document review for research, quality improvement, rural healthcare delivery science, language-access review, and learning-health-system workflows.

## Supporting tracks

### Citation-integrity audit workflow

The existing audit workflow remains directly relevant. It provides the first working pattern for claim extraction, source linkage, adjudicated error labels, audit summaries, and ML-assisted review metrics.

### Adaptive scaffolding simulation

The adaptive scaffolding simulation remains a secondary research scaffold. It may support training, simulation, and reviewer-support experiments, but it is no longer the lead ecosystem-facing roadmap.

## Phase 1: Proposal and governance spine

Goal: make the project safe to discuss with health-system, academic, IRB/HRPP, quality-improvement, and data-governance stakeholders.

Status: active priority.

Key outputs:

- `docs/dartmouth_health_study_concept.md`.
- `docs/paper_multilingual_ingestion_workflow.md`.
- `docs/governance_checklist.md`.
- `docs/data_classification_policy.md`.
- `docs/phi_handling_boundary.md`.
- `docs/translation_service_boundary.md`.
- `docs/ecosystem_readiness_review.md`.
- One-page specific aims draft.
- Health-system pilot protocol draft.

Research utility:

- Defines the project as a proposed feasibility pilot rather than an app launch.
- Separates public-safe synthetic work from governed real-document work.
- Prevents premature claims about clinical deployment or empirical effectiveness.
- Gives potential partners a concrete review package.

## Phase 2: Traceable ingestion schema

Goal: define small, auditable objects for document intake, page quality, OCR provenance, language detection, translation, field extraction, quality flags, and human adjudication.

Planned objects:

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

Planned modules:

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

Research utility:

- Makes provenance mandatory for every extracted field or claim.
- Keeps OCR, translation, and adjudication uncertainty explicit.
- Creates the data spine required for feasibility metrics.
- Allows synthetic demonstrations without using real patient data.

## Phase 3: Public-safe synthetic demonstration package

Goal: provide a realistic but fully synthetic demonstration of paper-format and multilingual healthcare-document review.

Planned outputs:

```text
examples/synthetic_paper_docs/README.md
examples/synthetic_paper_docs/document_manifest.csv
examples/synthetic_paper_docs/page_quality_records.csv
examples/synthetic_paper_docs/ocr_block_records.csv
examples/synthetic_paper_docs/language_detection_records.csv
examples/synthetic_paper_docs/translation_records.csv
examples/synthetic_paper_docs/quality_flag_records.csv
examples/synthetic_paper_docs/human_adjudication_records.csv
examples/synthetic_paper_docs/audit_summary.csv
```

Research utility:

- Lets reviewers understand the workflow without exposing PHI or confidential records.
- Provides test fixtures for ingestion and audit metrics.
- Demonstrates how paper, OCR, multilingual, and adjudication uncertainty are represented.
- Supports early proposal review and technical critique.

## Phase 4: Feasibility metrics and comparison layer

Goal: support transparent comparison between usual manual review and ML-assisted human-adjudicated review.

Primary metric domains:

```text
Quality:
  error_detection_rate
  missing_field_detection_rate
  unsupported_claim_detection_rate
  ocr_issue_detection_rate
  translation_issue_detection_rate

Completeness:
  required_field_completion_rate
  source_linkage_rate
  page_recovery_rate
  language_identification_completion_rate
  adjudication_completion_rate

Efficiency:
  review_time_per_document
  review_time_per_page
  review_time_per_extracted_field
  reviewer_confidence
  escalation_rate
```

Planned outputs:

- confidence intervals for detection and completion rates;
- reviewer-burden summaries;
- inter-rater reliability support;
- audit-arm comparisons;
- feasibility report template.

Research utility:

- Prevents vague claims about AI improvement.
- Keeps outcomes tied to measurable review quality, completeness, and efficiency.
- Supports a feasibility pilot rather than premature effectiveness claims.

## Phase 5: Health-system pilot package

Goal: create a partner-facing package that can be reviewed by research, quality-improvement, data-governance, and health-system stakeholders.

Planned outputs:

- One-page concept note.
- Specific aims page.
- Governance checklist.
- Pilot protocol.
- Data dictionary.
- Synthetic workflow diagram.
- Public-safe synthetic demo.
- Risk and boundary statement.
- Evaluation metric table.

Research utility:

- Makes the project legible to Dartmouth Health-style stakeholders.
- Clarifies what approval would be needed before real documents are used.
- Identifies where IRB/HRPP, QI, data-use, translation, and security review may apply.

## Phase 6: Governed real-world pilot readiness

Goal: prepare for a possible feasibility pilot using approved, governed, non-public documents only after appropriate review.

Planned outputs:

- governed storage and access plan;
- data-use permissions checklist;
- PHI/non-PHI determination workflow;
- review environment requirements;
- human adjudicator training guide;
- de-identification and export rules;
- reporting templates for aggregate outputs only.

Research utility:

- Moves the project toward a real health-system study without exposing sensitive records.
- Preserves human adjudication as the source of truth.
- Keeps the system away from autonomous diagnosis, treatment recommendation, or patient-facing decision-making.

## Phase 7: Secondary simulation and training layer

Goal: preserve the adaptive scaffolding simulation as a supporting research track rather than the lead roadmap.

Potential outputs:

- reviewer-training simulation;
- synthetic adjudicator workload simulation;
- adaptive reviewer-support policy experiments;
- learner or trainee feedback experiments using public-safe examples.

Research utility:

- Keeps earlier work available for future education or reviewer-support studies.
- Avoids mixing adaptive-learning claims with the health-system ingestion pilot.

## Current near-term priority

Do not build a production app yet. The immediate priority is to harden the health-system study package and schema:

```text
1. Update README and docs navigation to lead with the health-system ingestion direction.
2. Add governance and data-boundary documents.
3. Add ingestion object schemas.
4. Add synthetic paper/multilingual example records.
5. Add feasibility metrics and tests.
6. Keep all public repo artifacts synthetic or aggregate only.
```

## Claim boundary

Use:

```text
proposed feasibility pilot
pre-pilot research scaffold
auditable ML-assisted document review
paper-format and multilingual healthcare-document ingestion
human-adjudicated evidence-review workflow
```

Avoid:

```text
validated clinical AI
approved health-system deployment
autonomous clinical document review
patient-facing decision system
proven intervention effectiveness
```