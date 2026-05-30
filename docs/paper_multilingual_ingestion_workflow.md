# Paper and Multilingual Healthcare Document Ingestion Workflow

## Project status

This document is an early-stage architecture and study-design note. It supports proposal drafting for an auditable ML-assisted evidence-review workflow. It is not an approved clinical system, production ingestion service, human-subject protocol, or validated empirical tool.

## Core scenario

A health system may hold or receive large volumes of healthcare-related documents in paper format. Some documents may be scanned PDFs, faxed pages, handwritten forms, printed clinical notes, discharge instructions, consent materials, referral packets, public-health reports, research documentation, or administrative records. These documents may appear in multiple languages and may vary in scan quality, structure, terminology, and completeness.

The proposed workflow asks whether an auditable ML-assisted evidence-review pipeline can improve the quality, completeness, and review efficiency of health-system research documentation compared with usual manual review.

## Refined study question

Can an auditable ML-assisted workflow ingest paper-format and multilingual healthcare documents, convert them into traceable structured records, and improve document review quality, completeness, and efficiency compared with usual manual review?

## Why paper and multilingual ingestion matters

Paper and multilingual documentation create several health-system problems:

- important information can be locked in non-searchable paper or scanned image files;
- manual review is slow and inconsistent;
- translation adds another layer of uncertainty;
- OCR errors can change meaning;
- low-quality scans can hide missing pages, signatures, dates, or source details;
- reviewers may not know which extracted claims are reliable and which require human verification;
- research and quality-improvement teams need an audit trail showing where each extracted field came from.

The value of `ml-lab` is not to replace expert review. The value is to create a structured, auditable intake and review workflow where each step preserves provenance, confidence, uncertainty, and human adjudication.

## Proposed pipeline

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

## Pipeline stages

### Stage 1: Intake and chain of custody

Every document batch should receive a batch identifier before scanning or review.

Minimum metadata:

```text
batch_id
document_id
page_count_expected
page_count_observed
source_context
ingestion_date
intake_operator_id
data_sensitivity_class
allowed_processing_environment
```

Purpose:

- prevent silent document loss;
- separate public-safe test documents from governed real documents;
- preserve a chain of custody;
- support later audit and reproducibility.

### Stage 2: Scan and image capture

Paper documents are converted into image files or scanned PDFs.

Quality checks should include:

```text
resolution
blur_score
skew_angle
contrast_score
page_orientation
page_cutoff_flag
blank_page_flag
duplicate_page_flag
handwriting_flag
```

Low-quality pages should be routed to manual review before downstream extraction is trusted.

### Stage 3: Document classification

Documents should be classified before field extraction.

Candidate classes:

```text
clinical_note
discharge_summary
referral_packet
consent_form
public_health_report
research_protocol
literature_summary
administrative_form
unknown
```

Classification should be probabilistic and auditable. The system should record the predicted class, confidence, and reason codes or trace fields when possible.

### Stage 4: OCR and layout extraction

OCR should preserve page-level and text-region provenance.

Minimum OCR record:

```text
document_id
page_number
block_id
text
ocr_confidence
bounding_box
reading_order
source_image_hash
```

This is essential because reviewers need to trace every extracted claim or field back to the page image that produced it.

### Stage 5: Language identification

Each page or text block should receive a language label.

Minimum language record:

```text
document_id
page_number
block_id
language_code
language_confidence
mixed_language_flag
```

Mixed-language documents should be expected. A single document may contain English administrative text, Spanish patient instructions, French research material, or other language segments.

### Stage 6: Translation layer

Translation should be treated as an uncertain derived artifact, not as the original record.

Minimum translation record:

```text
document_id
page_number
block_id
source_language
target_language
source_text
translated_text
translation_model_or_service
translation_confidence
human_translation_review_status
```

The original text must remain preserved. Human reviewers should be able to compare the source text, OCR output, translated text, and page image.

### Stage 7: Field and claim extraction

The system extracts candidate claims or fields depending on document type.

For research and evidence-review documents:

```text
claim_id
claim_text
citation_text
reference_id
reference_title
reference_authors
reference_year
source_available
```

For health-system document review, possible fields include:

```text
patient_identifier_present_flag
date_present_flag
signature_present_flag
language_access_issue_flag
missing_page_flag
unclear_instruction_flag
medication_instruction_present_flag
follow_up_instruction_present_flag
referral_reason_present_flag
```

If real clinical documents are used, extracted values should not be committed to the public repository. Only synthetic examples, schemas, and aggregate metrics belong in the repo.

### Stage 8: ML-assisted quality flags

The workflow should flag review problems rather than make final determinations.

Candidate flags:

```text
low_ocr_confidence
low_translation_confidence
missing_required_field
possible_wrong_source
unsupported_claim
overstated_claim
metadata_error
possible_duplicate_document
possible_page_missing
language_access_issue
requires_human_review
```

Each flag should include a reason, confidence score, and trace link back to source evidence.

### Stage 9: Human adjudication

Human adjudication remains the source of truth.

Minimum adjudication record:

```text
record_id
reviewer_id
review_stage
field_or_claim_id
ml_flagged
human_label
error_type
confidence
review_time_seconds
notes
```

For multilingual content, adjudication should distinguish:

```text
ocr_error
translation_error
source_document_error
reviewer_uncertainty
true_document_defect
```

### Stage 10: Structured audit output

The final dataset should support feasibility and quality analysis.

Candidate output tables:

```text
document_intake_records.csv
page_quality_records.csv
ocr_block_records.csv
translation_records.csv
claim_or_field_records.csv
ml_flag_records.csv
human_adjudication_records.csv
audit_summary.csv
```

Public repo examples should be synthetic and should not include PHI, confidential documents, or restricted source text.

## Study arms

A realistic pilot could compare:

| Arm | Description |
| --- | --- |
| usual_manual_review | Existing human review process without structured ML support. |
| ml_assisted_review | OCR, translation, extraction, and ML flags are provided to the reviewer. |
| ml_plus_human_adjudication | ML flags candidate issues, then a human adjudicator verifies and classifies them. |

The strongest initial comparison is `usual_manual_review` versus `ml_plus_human_adjudication`.

## Primary outcomes

Quality outcomes:

```text
error_detection_rate
missing_field_detection_rate
unsupported_claim_detection_rate
wrong_source_detection_rate
translation_issue_detection_rate
ocr_issue_detection_rate
```

Completeness outcomes:

```text
required_field_completion_rate
page_recovery_rate
source_linkage_rate
language_identification_completion_rate
translation_review_completion_rate
```

Efficiency outcomes:

```text
review_time_per_document
review_time_per_page
review_time_per_claim
reviewer_confidence
number_of_documents_reviewed_per_hour
```

Safety and governance outcomes:

```text
phi_exposure_flag_count
restricted_document_flag_count
manual_review_escalation_rate
low_confidence_extraction_rate
```

## Feasibility pilot design

A minimal public-safe pilot should use synthetic or public documents first.

Candidate sample:

```text
20 to 50 synthetic or public-safe documents
100 to 300 scanned pages
200 to 500 extracted claims or fields
2 workflow arms
1 to 2 reviewers
```

The first pilot should answer:

- Can the workflow ingest paper-format documents consistently?
- Can it identify language and translation needs?
- Can it preserve traceability from extracted fields back to page images?
- Can reviewers adjudicate ML flags efficiently?
- Can the system produce aggregate metrics without exposing sensitive records?

## Governance boundary

Before using real health-system documents, the project needs formal determination of:

```text
PHI status
human-subject status
quality-improvement versus research classification
IRB or HRPP requirements
data-use permissions
storage environment
access controls
translation-service rules
retention and deletion policy
public-output restrictions
```

No real patient documents, identifiable records, confidential health-system materials, or restricted source text should be committed to this public repository.

## Technical build implications

The repository should evolve toward small auditable objects:

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

Near-term modules:

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

Near-term tests:

```text
tests/test_ingest_records.py
tests/test_page_quality_records.py
tests/test_language_records.py
tests/test_translation_records.py
tests/test_adjudication_records.py
```

## Public-safe synthetic examples

The repo should include only synthetic examples such as:

```text
examples/synthetic_paper_docs/README.md
examples/synthetic_paper_docs/scanned_page_manifest.csv
examples/synthetic_paper_docs/ocr_blocks.csv
examples/synthetic_paper_docs/translation_records.csv
examples/synthetic_paper_docs/adjudication_records.csv
```

Synthetic examples should simulate multilingual and paper-format problems without using real patient records.

## Proposal framing

Use this language:

> This proposed feasibility pilot evaluates whether an auditable ML-assisted workflow can convert paper-format and multilingual healthcare documents into traceable structured review records, while improving quality, completeness, and review efficiency compared with usual manual review. The system is designed to support human adjudication, preserve provenance, and identify low-confidence OCR, translation, and evidence-linkage problems rather than replace expert review.

## Interpretation boundary

This workflow can support feasibility, data-quality, and review-process claims. It should not be framed as autonomous clinical decision-making, diagnosis, treatment recommendation, or patient-facing automation.