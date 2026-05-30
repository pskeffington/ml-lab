# Health-System Pilot Protocol Draft

## Project status

This is an early-stage protocol draft for a proposed feasibility pilot. It is not an approved study, clinical deployment, production workflow, or authorization to process real health-system documents.

## Working title

Auditable ML-Assisted Review of Paper-Format and Multilingual Healthcare Documents: A Feasibility Pilot

## Study purpose

The purpose of this proposed pilot is to evaluate whether an auditable ML-assisted workflow can improve the quality, completeness, and efficiency of reviewing paper-format and multilingual healthcare documents compared with usual manual review.

The pilot is designed to test feasibility, traceability, review workflow, and measurement quality. It is not designed to make autonomous clinical decisions or to replace expert review.

## Study question

Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?

## Study design

Feasibility pilot using document-level, page-level, text-block-level, extracted-field-level, and adjudication-level records.

Initial phase:

```text
public-safe synthetic demonstration
```

Possible later phase after institutional review:

```text
governed real-document pilot in approved environment
```

## Candidate arms

| Arm | Description |
| --- | --- |
| `usual_manual_review` | Human reviewer evaluates documents using the usual unassisted or minimally structured process. |
| `ml_assisted_human_adjudicated_review` | Workflow provides OCR, language detection, translation status, extracted fields or claims, quality flags, provenance pointers, and review forms. Human adjudicator makes the final label. |

## Candidate document types

Synthetic or approved documents may represent:

```text
referral_packet
discharge_instruction
consent_form
public_health_report
research_protocol
administrative_form
literature_summary
multilingual_patient_instruction
```

## Exclusion criteria

Exclude documents that:

- contain PHI unless processed only after approval in a governed environment;
- contain identifiable private information not approved for study use;
- depend on restricted source material;
- cannot be classified for sensitivity;
- cannot be lawfully processed by the proposed OCR or translation workflow;
- cannot be reviewed by authorized adjudicators.

## Data records

Minimum record tables:

```text
document_manifest
page_quality_records
ocr_block_records
language_detection_records
translation_records
extracted_field_records
quality_flag_records
human_adjudication_records
audit_summary
```

## Primary feasibility outcomes

- document intake completion rate;
- page-quality record completion rate;
- OCR provenance completion rate;
- language identification completion rate;
- translation status completion rate;
- human adjudication completion rate;
- manual escalation rate;
- public-safe export eligibility for synthetic outputs.

## Primary quality outcomes

- missing-field detection rate;
- low-OCR-confidence detection rate;
- low-translation-confidence detection rate;
- unsupported-claim detection rate;
- source-linkage error rate;
- page-loss or page-cutoff detection rate;
- adjudicated error-type distribution.

## Primary efficiency outcomes

- review time per document;
- review time per page;
- review time per extracted field or claim;
- reviewer confidence;
- records reviewed per hour;
- reviewer escalation burden.

## Human adjudication

Human adjudication is the source of truth. The ML-assisted workflow may flag candidate problems, but it does not make final determinations.

Minimum adjudication labels:

```text
no_error
ocr_error
translation_error
missing_required_field
unsupported_claim
wrong_source
source_document_error
reviewer_uncertainty
true_document_defect
```

## Governance boundary

Before real documents are used, the project requires determination of:

```text
PHI status
human-subject status
quality-improvement versus research status
IRB or HRPP requirements
data-use permissions
storage and processing environment
OCR service approval
translation service approval
adjudicator authorization
export rules
```

## Public repository rule

The public repository may contain only:

```text
code
schemas
documentation
synthetic examples
public-safe test fixtures
aggregate non-sensitive outputs
```

It must not contain real PHI, patient records, confidential health-system documents, unapproved OCR output, unapproved translations, or restricted source text.

## Analysis plan sketch

The first analysis should be descriptive:

- count documents, pages, OCR blocks, extracted fields, flags, and adjudications;
- summarize completion rates by stage;
- summarize error-type distribution;
- compare review time by arm;
- compare detection and escalation rates by arm;
- report uncertainty intervals when sample size allows;
- identify workflow bottlenecks and missing-data points.

## Interpretation boundary

The pilot can support feasibility, workflow, measurement, and process-quality claims. It cannot support broad claims of clinical effectiveness, autonomous AI performance, patient outcome improvement, or institutional deployment readiness without additional approved study design and evidence.

## Next protocol tasks

- Define synthetic document set.
- Define adjudicator instructions.
- Define review-time capture method.
- Define confidence rating scale.
- Define sample size for synthetic and governed phases.
- Define export and reporting rules.
- Define adverse event or incident reporting for data exposure or governance failures.