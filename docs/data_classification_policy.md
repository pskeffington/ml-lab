# Data Classification Policy

## Project status

This policy supports proposal drafting and pre-pilot infrastructure design. It does not replace institutional data-governance, privacy, legal, IRB/HRPP, or information-security requirements.

## Purpose

`ml-lab` must distinguish synthetic public examples from real health-system documents before any ingestion, OCR, translation, extraction, or adjudication occurs. This policy defines the minimum classification scheme for public-safe development and future governed pilots.

## Classification levels

### `public_synthetic`

Fabricated records, mock documents, synthetic OCR text, synthetic translations, and synthetic adjudication outputs created for public testing.

Allowed in public repo:

```text
yes
```

### `public_real`

Publicly available real documents that are lawfully accessible and permitted for reuse. Examples may include public health reports, public trial summaries, public policy documents, or public guidance documents.

Allowed in public repo:

```text
only if licensing, terms, and copyright constraints permit
```

### `internal_non_phi`

Internal materials that do not contain PHI or identifiable private information but are not approved for public release.

Allowed in public repo:

```text
no
```

### `restricted_non_phi`

Non-PHI materials with contractual, operational, educational, institutional, or confidentiality restrictions.

Allowed in public repo:

```text
no
```

### `phi_or_identifiable`

Any record containing protected health information, identifiable patient information, or private identifiable information.

Allowed in public repo:

```text
no
```

### `unknown_sensitive`

Any document or batch whose sensitivity is not yet known.

Allowed in public repo:

```text
no
```

Processing rule:

```text
unknown_sensitive -> stop
```

## Required classification fields

Each document batch should include:

```text
batch_id
document_id
data_sensitivity_class
classification_method
classified_by
classification_date
allowed_processing_environment
public_release_status
governance_review_status
```

## Derived artifact inheritance

Derived artifacts inherit the source document's sensitivity class unless explicitly approved for public release.

Derived artifacts include:

```text
page images
OCR text
layout blocks
language detection records
translations
extracted fields
extracted claims
quality flags
adjudication notes
reviewer comments
summary tables with small cells
```

## Public release status

Every artifact should be assigned one of:

```text
public_allowed
public_after_review
internal_only
governed_environment_only
not_reviewed
```

Rule:

```text
not_reviewed -> do not export or commit
```

## Minimum safe defaults

When uncertain, classify conservatively:

```text
unknown -> unknown_sensitive
real clinical document -> phi_or_identifiable until proven otherwise
real OCR text -> inherits source sensitivity
real translation -> inherits source sensitivity
reviewer free-text notes -> restricted until reviewed
small-cell aggregate output -> restricted until reviewed
```

## Repository implications

The public repo should prioritize:

```text
synthetic fixtures
schema tests
aggregate mock outputs
redacted examples generated from synthetic data
```

The public repo should exclude:

```text
real scanned documents
real OCR output from governed documents
real translations from governed documents
real adjudication notes tied to governed records
unreviewed aggregate outputs from governed records
```

## Development implication

Future ingestion models should validate that `data_sensitivity_class`, `allowed_processing_environment`, and `public_release_status` are present before writing records. Public example generators should default to `public_synthetic`.