# Ecosystem Readiness Review

## Project status

This review supports an early-stage proposed research study and pre-pilot infrastructure project. It is not an approval for clinical deployment, patient-facing use, production ingestion, real-document processing, or empirical claims.

## Readiness judgment

`ml-lab` is ready to be discussed as a proposed feasibility pilot and synthetic demonstration package. It is not ready to be presented as a deployed application or validated health-system tool.

The project should enter the ecosystem as:

```text
proposal package + governed workflow design + synthetic demonstration scaffold
```

It should not enter the ecosystem as:

```text
clinical AI app
production OCR pipeline
autonomous translation system
approved health-system deployment
validated intervention
```

## Lead ecosystem thesis

Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?

## Why the concept is ecosystem-relevant

The project addresses problems that health-system, rural-health, quality-improvement, clinical-research, and learning-health-system stakeholders can recognize:

- paper documents remain common in referral, consent, discharge, administrative, and historical record workflows;
- scanned and faxed records are difficult to search, verify, translate, and audit;
- multilingual materials introduce language-access and translation-quality concerns;
- manual review is labor-intensive and inconsistent;
- research and quality-improvement documents need stronger evidence-use and citation-integrity review;
- stakeholders need provenance-preserving systems, not opaque AI outputs.

## Minimum package before partner discussion

Before any external partner review, the repo should contain:

```text
README.md with early-proposal status
roadmap focused on health-system ingestion
governance checklist
data classification policy
OCR and translation boundary
ingestion workflow architecture
Dartmouth Health-facing concept note
specific aims draft
health-system pilot protocol draft
public-safe synthetic example plan
```

## Current strengths

- The project question is now specific and measurable.
- The repo clearly states that it is an early proposal, not a validated system.
- The roadmap now prioritizes governance, traceability, synthetic examples, feasibility metrics, and pilot readiness.
- OCR and translation are framed as uncertain derived artifacts.
- Human adjudication remains the source of truth.
- The public repository boundary is explicit.

## Current gaps

### Governance gaps

- No completed partner-specific approval map.
- No HRPP/IRB/QI determination memo template.
- No data-use or storage-environment plan.
- No export-review process for aggregate outputs.

### Technical gaps

- No implemented `src/ml_lab/ingest/` object layer yet.
- No synthetic paper-document example package yet.
- No ingestion CLI yet.
- No page-quality, OCR, language, translation, or adjudication schema tests yet.

### Research-design gaps

- No finalized pilot sample plan.
- No finalized usual-review comparator workflow.
- No adjudicator training protocol.
- No inter-rater reliability plan for multilingual or OCR-derived records.
- No feasibility report template.

## Recommended sequence

### Step 1: Finish proposal spine

```text
specific_aims_draft.md
health_system_pilot_protocol.md
pilot_feasibility_report_template.md
```

### Step 2: Build synthetic demonstration package

```text
examples/synthetic_paper_docs/document_manifest.csv
examples/synthetic_paper_docs/page_quality_records.csv
examples/synthetic_paper_docs/ocr_block_records.csv
examples/synthetic_paper_docs/language_detection_records.csv
examples/synthetic_paper_docs/translation_records.csv
examples/synthetic_paper_docs/quality_flag_records.csv
examples/synthetic_paper_docs/human_adjudication_records.csv
```

### Step 3: Implement minimal ingestion objects

```text
DocumentBatch
DocumentRecord
PageQualityRecord
OcrBlockRecord
LanguageDetectionRecord
TranslationRecord
QualityFlag
HumanAdjudicationRecord
```

### Step 4: Add feasibility metrics

```text
quality flag rate
low OCR confidence rate
low translation confidence rate
adjudication completion rate
manual escalation rate
review time per document
review time per extracted field
```

### Step 5: Prepare partner-facing package

```text
one-page concept
specific aims
workflow diagram
synthetic output example
governance boundary
metric table
ask for review of synthetic demo and pilot feasibility
```

## Go / no-go criteria

### Ready for internal project review

Ready when:

- roadmap and README match the health-system direction;
- governance documents exist;
- specific aims and pilot protocol exist;
- synthetic demo plan exists.

### Ready for external partner conversation

Ready when:

- synthetic records can be loaded and summarized;
- no real sensitive data are in the repo;
- governance questions are explicit;
- proposed pilot is framed as feasibility, not deployment;
- human adjudication is central.

### Ready for real-document pilot planning

Ready only when:

- institutional pathway is determined;
- data class is known;
- storage and processing environment are approved;
- OCR and translation services are approved for the data class;
- adjudicators are authorized;
- export rules are defined;
- public outputs are restricted to approved aggregate results.

## Suggested ecosystem ask

The first partner-facing ask should be narrow:

> Review a synthetic demonstration of an auditable ML-assisted workflow for paper-format and multilingual healthcare-document review, and advise whether the feasibility-pilot design aligns with health-system research, quality-improvement, data-governance, and language-access priorities.

Do not ask for real documents first. Ask for review of the synthetic workflow and governance design.