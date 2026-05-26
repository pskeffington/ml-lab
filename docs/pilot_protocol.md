# Pilot Protocol

## Study title

ML-Assisted Citation Auditing for Reducing Mis-Citations in Research Writing

## Purpose

This pilot estimates whether an ML-assisted citation-audit workflow reduces citation-level mis-citations compared with a baseline review workflow. The pilot is designed to produce non-synthetic, adjudicated evidence while keeping claims appropriately bounded.

## Primary research question

Does ML-assisted citation auditing reduce the citation-level mis-citation rate compared with baseline review?

## Primary estimand

```text
absolute_reduction = p_baseline - p_ml_audit
relative_reduction = (p_baseline - p_ml_audit) / p_baseline
```

Where `p_baseline` is the adjudicated mis-citation rate in the baseline arm and `p_ml_audit` is the adjudicated mis-citation rate after ML-assisted audit.

## Study design

The minimum pilot uses citation claims extracted from research documents and assigns claims or documents to one of two workflow arms:

| Arm | Description |
| --- | --- |
| `baseline` | Citation claims are reviewed without ML-assisted audit. |
| `ml_audit` | Citation claims are reviewed after ML-assisted flagging or verification support. |

Optional expanded arms:

| Arm | Description |
| --- | --- |
| `human_audit` | Human review without ML support. |
| `ml_plus_human` | ML flags likely issues, then a human adjudicates. |

## Unit of analysis

The unit of analysis is the citation claim. A citation claim is a claim, sentence, clause, table note, or methodological assertion that depends on one or more cited sources.

## Sample target

Minimum pilot target:

```text
10 to 20 documents
200 to 500 citation claims
2 independent adjudicators where feasible
```

The pilot is feasibility-oriented and should not be described as a definitive treatment-effect study unless sample size, assignment, and analysis are designed for that purpose.

## Inclusion criteria

- Document contains scholarly or technical citations.
- Cited source can be identified from the reference list or citation metadata.
- Citation claim can be isolated and reviewed.
- Claim can be assigned to a workflow arm.

## Exclusion criteria

- Claim does not rely on a citation.
- Source cannot be identified from available metadata.
- Claim requires confidential or unavailable source material.
- Duplicate claim already represented in the dataset.
- Claim is outside the pilot domain if a domain-restricted pilot is used.

## Adjudication procedure

1. Extract citation claims from documents.
2. Link each claim to a reference record.
3. Apply the assigned workflow arm.
4. Have adjudicator label whether the claim is miscited.
5. Assign an error type if miscited.
6. Record reviewer confidence and review time.
7. Resolve disagreements if multiple adjudicators are used.

## Mis-citation categories

```text
unsupported_claim
overstated_claim
wrong_source
fabricated_source
metadata_error
quote_error
scope_error
```

Use `none` when `is_miscitation=false`.

## Primary outcome

Citation-level mis-citation rate:

```text
mis_citation_rate = n_miscitations / n_claims
```

## Secondary outcomes

- unsupported-claim rate;
- fabricated-source rate;
- metadata-error rate;
- ML flag rate;
- mean review time;
- reviewer confidence;
- false-positive and false-negative rates if independent ML flags and adjudicated labels are available.

## Analysis workflow

From a Mac terminal:

```bash
python -m pip install -e ".[dev]"
ml-lab-audit-template
```

Fill the generated file or save adjudicated records to:

```text
outputs/citation_audit_records.csv
```

Then run:

```bash
ml-lab-audit-analyze
python -m pytest
```

Expected output:

```text
outputs/citation_audit_summary.csv
```

If both `baseline` and `ml_audit` arms are present, the CLI reports absolute and relative mis-citation reduction.

## Interpretation boundaries

The pilot can support statements about the observed citation-claim sample and workflow tested. It cannot support broad claims about all fields, all citation styles, all LLM systems, or all research-writing contexts.

## Governance

Do not commit private documents, identifiable student work, or restricted source material. Store only de-identified claim records, source metadata, adjudication labels, and aggregate outputs unless permission and governance requirements allow otherwise.

## Walk-in readiness checklist

- Repository installs from `pyproject.toml`.
- CLI writes a citation-audit template.
- CLI analyzes adjudicated citation records.
- Data dictionary defines fields and error categories.
- Pilot protocol defines the estimand and adjudication process.
- Tests cover audit records, metrics, reductions, and CSV helpers.
- Documentation distinguishes pilot evidence from full causal claims.
