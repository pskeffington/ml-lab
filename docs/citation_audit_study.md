# Citation Audit Study Design

This document defines a non-synthetic study path for testing whether ML-assisted auditing reduces mis-citations in research writing.

## Candidate publishable claim

ML-assisted citation auditing reduces the mis-citation rate by a measurable amount compared with unaudited or manually reviewed citation workflows.

The value of `N` should not be assumed. It should be estimated from a controlled study and reported as an absolute percentage-point reduction, a relative reduction, and an uncertainty interval.

## Primary estimand

Let:

```text
p_control = mis-citation rate under the baseline workflow
p_audit   = mis-citation rate after ML-assisted citation auditing
```

The primary estimand is:

```text
N = p_control - p_audit
```

Where `N` is the absolute reduction in mis-citations measured in percentage points.

A secondary estimand is relative reduction:

```text
relative_reduction = (p_control - p_audit) / p_control
```

## Unit of analysis

The preferred unit of analysis is the individual citation claim, not the whole paper.

A citation claim is a sentence, clause, paragraph, table note, or method statement that relies on one or more references.

## Mis-citation definition

A citation should be coded as a mis-citation if one or more of the following is true:

| Error type | Definition |
| --- | --- |
| Unsupported claim | The cited source does not support the claim. |
| Overstated claim | The claim is stronger than the source permits. |
| Wrong source | The source is real but about a different finding, method, population, or context. |
| Fabricated source | The cited source does not exist or cannot be verified. |
| Metadata error | Author, year, title, journal, DOI, or URL is materially incorrect. |
| Quote error | A quoted phrase is inaccurate or not present in the source. |
| Scope error | The source is cited outside its population, setting, or methodological scope. |

## Study arms

| Arm | Description |
| --- | --- |
| Baseline | Citation claims are written and reviewed without ML-assisted auditing. |
| ML audit | Citation claims are checked with an ML-assisted audit workflow before final review. |
| Human audit only | Citation claims are checked by a human reviewer without ML assistance. Optional comparator. |
| ML plus human audit | ML flags likely errors, then a human adjudicates. Strongest practical workflow. |

## Primary outcome

The primary outcome is the citation-level mis-citation rate.

```text
mis_citation_rate = number_of_miscited_claims / number_of_audited_citation_claims
```

## Secondary outcomes

- Fabricated-source rate.
- Unsupported-claim rate.
- Metadata-error rate.
- Overstatement rate.
- Time required per citation claim.
- Reviewer confidence.
- False-positive flag rate from the audit system.
- False-negative rate after human adjudication.

## Gold-standard adjudication

A non-synthetic study requires a gold-standard review process. Recommended structure:

1. Extract citation claims from documents.
2. Retrieve cited sources.
3. Have two independent reviewers code each claim.
4. Resolve disagreements through adjudication.
5. Record final labels and error types.

The gold standard should be blinded to study arm when practical.

## Minimal viable dataset

A practical first study could use:

```text
10 to 20 documents
200 to 500 citation claims
2 independent human adjudicators
2 study conditions: baseline vs ML audit
```

For a stronger publication, increase the number of documents, diversify domains, and include human-only and ML-plus-human arms.

## Analysis plan

Report:

- citation claims reviewed by arm;
- mis-citation rate by arm;
- absolute percentage-point reduction;
- relative reduction;
- confidence interval for the reduction;
- error-type distribution;
- false positives and false negatives;
- time cost per claim.

For document-level clustering, use cluster-robust intervals or a mixed-effects model with citation claims nested within documents.

## Example result language

Do not write:

> ML auditing reduces mis-citations by N amount.

Write:

> In this sample, ML-assisted citation auditing reduced the citation-level mis-citation rate from `p_control` to `p_audit`, an absolute reduction of `N` percentage points and a relative reduction of `R%`, using human-adjudicated source verification as the reference standard.

## Integration with `ml-lab`

This study can be represented using the same science-abstract machine structure:

```text
DocumentState       Claims, references, source availability, metadata completeness
AuditPolicy         ML audit, human audit, or combined audit workflow
AuditAction         Flag unsupported claim, verify metadata, retrieve source, request adjudication
AuditEnvironment    Corpus, source-access rules, claim-extraction rules
OutcomeMetric       Mis-citation rate, false-positive rate, false-negative rate, time cost
ExperimentRunner    Randomized or retrospective comparison workflow
```

## Required implementation additions

- `CitationClaim` object.
- `ReferenceRecord` object.
- `AuditFinding` object.
- Citation-claim CSV schema.
- Mis-citation scoring utilities.
- Pairwise comparison functions for citation-error outcomes.
- Human adjudication import format.

## Interpretation boundary

The claim is only valid for the documents, fields, citation styles, source-access conditions, and audit workflow tested. A reduction in mis-citations does not imply that the writing is substantively correct; it means citation support improved under the adjudication criteria.
