# Governance Checklist

## Project status

This checklist supports an early-stage proposed research study and pre-pilot infrastructure project. It is not a substitute for institutional review, legal review, privacy review, information-security review, HRPP/IRB determination, or health-system operational approval.

## Purpose

The purpose of this checklist is to prevent premature use of real health-system documents, patient records, multilingual clinical materials, or restricted source text before the project has the necessary governance pathway.

## Non-negotiable public repository boundary

The public repository may contain:

```text
source code
schemas
documentation
synthetic examples
public-safe test fixtures
aggregate non-sensitive outputs
```

The public repository must not contain:

```text
PHI
identifiable patient records
private clinical documents
confidential health-system materials
identifiable student or trainee work
restricted source text
internal operational documents
unapproved scanned records
raw OCR from real governed documents
translations of real governed documents
```

## Intake governance questions

Before any real document is processed, answer:

| Question | Required before real use |
| --- | --- |
| What is the source of the document batch? | yes |
| Does the batch contain PHI or identifiable private information? | yes |
| Is the activity research, quality improvement, operations, education, or mixed? | yes |
| Is HRPP/IRB determination required? | yes |
| Is data-use authorization or agreement required? | yes |
| Is the processing environment approved for the sensitivity class? | yes |
| Are translation or OCR services permitted for this data class? | yes |
| Who can access source images, OCR text, translations, and adjudication records? | yes |
| What can be exported from the governed environment? | yes |
| What may be committed to the public repository? | yes |

## Data sensitivity classification

Each document batch must be assigned one of the following classes before processing:

```text
public_synthetic
public_real
internal_non_phi
restricted_non_phi
phi_or_identifiable
unknown_sensitive
```

Processing rule:

```text
unknown_sensitive -> stop and escalate
phi_or_identifiable -> governed environment only
restricted_non_phi -> governed environment only unless approved for public-safe transformation
internal_non_phi -> internal environment unless approved for public release
public_real -> public-safe processing allowed if licensing permits
public_synthetic -> public repository allowed
```

## Review pathway classification

Before real documents are used, classify the activity:

```text
software_development_only
synthetic_validation
quality_improvement
human_subjects_research
non_human_subjects_research
education_or_training
operations_review
mixed_or_uncertain
```

Rule:

```text
mixed_or_uncertain -> request institutional determination before processing real documents
```

## OCR and translation governance

Before OCR or translation is performed on real documents, confirm:

- the OCR tool is approved for the document sensitivity class;
- the translation service is approved for the document sensitivity class;
- no real sensitive text is sent to unapproved third-party services;
- source images remain in the approved environment;
- derived OCR and translation outputs inherit the sensitivity class of the source document;
- low-confidence OCR or translation is flagged for human review;
- original text is preserved and not replaced by translated text.

## Human adjudication governance

Before adjudication begins, confirm:

- adjudicators are authorized for the document sensitivity class;
- adjudicators understand the difference between OCR error, translation error, document error, and reviewer uncertainty;
- adjudication records do not expose unnecessary sensitive text;
- reviewer notes are governed as potentially sensitive data;
- aggregate outputs are checked before export.

## Public release checklist

Before publishing or committing any output, confirm:

- the artifact contains no PHI;
- the artifact contains no identifiable private information;
- the artifact contains no restricted source text;
- the artifact contains no real unapproved OCR or translation output;
- the artifact is synthetic, public, or aggregate;
- the artifact cannot reasonably be linked back to a real patient or confidential document;
- the artifact is labeled with its source class and intended use.

## Approval gates

| Gate | Required before |
| --- | --- |
| Public-safe synthetic validation | public repo examples |
| Data classification | any real document intake |
| HRPP/IRB or QI determination | real health-system study activity |
| Privacy/security review | processing restricted or identifiable documents |
| Translation service approval | translating real sensitive content |
| Export review | moving outputs out of governed environment |
| Partner approval | describing work as affiliated, approved, or deployed |

## Stop conditions

Stop processing and escalate if:

- document sensitivity is unknown;
- PHI is discovered in a public-safe workflow;
- real OCR or translation output is about to be committed;
- a third-party tool is not approved for the sensitivity class;
- reviewers disagree about whether data may be exported;
- project language implies clinical deployment or validated effectiveness before approval.

## Repository implementation implication

Every future ingestion record should include:

```text
data_sensitivity_class
allowed_processing_environment
source_document_status
public_release_status
governance_review_status
```

These fields should be required before any real-data extension of the project.