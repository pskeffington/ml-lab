# OCR and Translation Boundary

## Project status

This document supports proposal drafting and pre-pilot architecture. It is not an institutional approval, security assessment, or authorization to process real health-system documents.

## Purpose

Paper-format and multilingual healthcare-document ingestion depends on OCR, layout extraction, language identification, and translation. These steps are useful but risky. OCR and translation outputs can contain errors, can alter meaning, and can reproduce sensitive source text. This boundary document defines how the project should treat OCR and translation before any real health-system use.

## Core principle

OCR and translation are uncertain derived artifacts.

They are not the original record, not final truth, and not a substitute for human review.

## OCR boundary

OCR output must preserve provenance.

Minimum OCR fields:

```text
document_id
page_number
block_id
text
ocr_confidence
bounding_box
reading_order
source_image_hash
data_sensitivity_class
```

Rules:

- Do not trust OCR text without source-image traceability.
- Do not overwrite or discard the original page image.
- Do not merge low-confidence OCR into final extracted fields without review.
- Do not commit OCR output from real governed documents to the public repo.
- Treat OCR text as having the same sensitivity level as the source image.

## Translation boundary

Translation output must preserve the original source text and translation provenance.

Minimum translation fields:

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
data_sensitivity_class
```

Rules:

- Do not replace source text with translated text.
- Do not treat translation as adjudicated meaning unless human-reviewed.
- Do not send governed text to an unapproved translation service.
- Do not commit translations of governed real documents to the public repo.
- Treat translated text as having the same sensitivity level as the source text.

## Language identification boundary

Language detection should occur at page or block level, not only document level.

Minimum fields:

```text
document_id
page_number
block_id
language_code
language_confidence
mixed_language_flag
```

Mixed-language content should be escalated when confidence is low or when the content affects evidence review, patient-facing instructions, consent language, medication instructions, referral information, or follow-up instructions.

## Quality flags

OCR and translation should generate quality flags rather than final conclusions.

Candidate flags:

```text
low_ocr_confidence
low_translation_confidence
mixed_language_uncertainty
handwriting_detected
page_cutoff_detected
layout_uncertainty
requires_human_translation_review
requires_source_image_review
```

Each flag should include:

```text
flag_id
record_id
flag_type
confidence
reason
source_pointer
review_required
```

## Human review requirements

Human review is required when:

- OCR confidence is below threshold;
- translation confidence is below threshold;
- the page contains handwriting;
- the document is mixed-language;
- the field affects safety, consent, referral, medication, diagnosis, treatment, or eligibility interpretation;
- the output will be used in a research or quality-improvement finding;
- the reviewer cannot trace the extracted value back to the source image.

## Public repo rule

Only synthetic OCR and synthetic translation records may be committed to this repository unless a public real document is legally reusable and explicitly marked as public-safe.

## Proposal language

Use:

```text
OCR-assisted extraction
translation-assisted review
human-adjudicated multilingual review
provenance-preserving OCR and translation records
low-confidence output escalation
```

Avoid:

```text
automated translation as ground truth
autonomous multilingual clinical review
fully automated OCR-based document understanding
clinically validated translation pipeline
```

## Implementation implication

Future ingestion objects should make OCR confidence, source-image provenance, language confidence, translation provenance, and human-review status required fields. Any missing provenance should fail validation before the record is eligible for analysis.