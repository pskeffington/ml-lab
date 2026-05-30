# Specific Aims Draft

## Project status

This is an early-stage draft for a proposed feasibility pilot. It is not an approved study, funded project, clinical deployment, or validated empirical claim.

## Working title

Auditable ML-Assisted Review of Paper-Format and Multilingual Healthcare Documents: A Feasibility Pilot

## Significance

Healthcare organizations continue to rely on paper-format, scanned, faxed, multilingual, and semi-structured documents in referral, discharge, consent, administrative, research, and quality-improvement workflows. These documents can be difficult to search, translate, verify, and review consistently. Manual review is often slow and can miss low-quality scans, incomplete pages, uncertain translations, unsupported claims, missing fields, and source-linkage problems.

ML-assisted document review may help identify quality and completeness problems, but opaque automation is not appropriate for high-trust health-system workflows. A safer approach is an auditable workflow that preserves provenance, records uncertainty, flags low-confidence outputs, and keeps human adjudication as the source of truth.

## Overall objective

The objective of this proposed feasibility pilot is to evaluate whether an auditable ML-assisted workflow can convert paper-format and multilingual healthcare documents into traceable structured review records and improve document review quality, completeness, and efficiency compared with usual manual review.

## Central hypothesis

A provenance-preserving ML-assisted workflow with human adjudication will improve detection of document-quality, completeness, OCR, translation, and evidence-linkage issues while reducing reviewer burden compared with usual manual review.

## Aim 1: Establish feasibility of traceable document ingestion

Evaluate whether paper-format and multilingual documents can be represented as structured records that preserve page-level provenance, OCR confidence, language identification, translation status, and review eligibility.

### Candidate outcomes

- percentage of pages with complete image-quality records;
- percentage of OCR blocks with source-image provenance;
- percentage of text blocks with language identification;
- percentage of translated blocks with source-text preservation;
- percentage of extracted fields or claims linked back to source page evidence.

## Aim 2: Compare review quality and completeness

Compare usual manual review with ML-assisted human-adjudicated review for detecting quality and completeness problems.

### Candidate outcomes

- missing-field detection rate;
- low-OCR-confidence detection rate;
- low-translation-confidence detection rate;
- unsupported-claim detection rate;
- wrong-source or source-linkage error rate;
- adjudicated error-type distribution;
- manual escalation rate.

## Aim 3: Assess review efficiency and reviewer burden

Estimate whether ML-assisted human-adjudicated review changes reviewer time, confidence, and workload compared with usual manual review.

### Candidate outcomes

- review time per document;
- review time per page;
- review time per extracted field or claim;
- reviewer confidence;
- number of records reviewed per hour;
- reviewer escalation frequency.

## Proposed study design

The proposed pilot will use a public-safe synthetic demonstration dataset first. If institutional governance permits, later phases may use approved, de-identified, or governed documents in an approved environment. The initial comparison should be feasibility-oriented rather than powered for definitive effectiveness claims.

Candidate arms:

```text
usual_manual_review
ml_assisted_human_adjudicated_review
```

## Innovation

The project does not position ML as an autonomous clinical decision-maker. Its innovation is a provenance-preserving, human-adjudicated workflow for reviewing messy paper-format and multilingual health-system documents. The workflow treats OCR and translation as uncertain derived artifacts, not ground truth.

## Expected contribution

The expected contribution is a public-safe, reproducible feasibility scaffold that defines how health-system document ingestion, OCR, translation, evidence review, quality flags, and human adjudication can be measured before any real clinical or research documents are used.

## Boundary statement

This proposed pilot does not diagnose, recommend treatment, replace clinicians, make patient-facing decisions, or modify records autonomously. It evaluates document review quality, completeness, efficiency, provenance, and feasibility.