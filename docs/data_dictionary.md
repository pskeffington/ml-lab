# Data Dictionary

This dictionary defines the minimum fields needed for non-synthetic citation-audit results and future learner-study results. Field names should remain stable once real data collection begins.

## Citation-audit records

Default CSV path for pilot input:

```text
outputs/citation_audit_records.csv
```

Template command:

```bash
ml-lab-audit-template
```

Analysis command:

```bash
ml-lab-audit-analyze
```

### Required fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `claim_id` | string | yes | Unique identifier for the citation claim. |
| `document_id` | string | yes | Identifier for the document containing the claim. |
| `claim_text` | string | yes | Text of the claim being audited. |
| `citation_text` | string | yes | In-text citation or citation marker attached to the claim. |
| `reference_id` | string | yes | Identifier linking the claim to a reference record. |
| `reference_title` | string | yes | Title of the cited source. |
| `reference_authors` | string | no | Source author string. |
| `reference_year` | integer | no | Publication year. |
| `doi` | string | no | DOI when available. |
| `url` | string | no | Stable URL when available. |
| `source_available` | boolean | yes | Whether the adjudicator could access or verify the source. |
| `arm` | string | yes | Workflow condition, such as `baseline`, `ml_audit`, `human_audit`, or `ml_plus_human`. |
| `reviewer_id` | string | yes | Identifier for the adjudicator or adjudication process. |
| `is_miscitation` | boolean | yes | Final adjudicated label indicating citation error. |
| `error_type` | string | yes | Error category. Use `none` when `is_miscitation=false`. |
| `confidence` | float | yes | Reviewer confidence from 0.0 to 1.0. |
| `ml_flagged` | boolean | yes | Whether the ML audit workflow flagged the claim. |
| `review_time_seconds` | float | no | Time spent reviewing the claim. |
| `notes` | string | no | Optional adjudication notes. |

### Allowed error types

```text
none
unsupported_claim
overstated_claim
wrong_source
fabricated_source
metadata_error
quote_error
scope_error
```

### Boolean encoding

Boolean fields accept:

```text
true, false, 1, 0, yes, no, y, n
```

## Citation-audit summary output

Default summary path:

```text
outputs/citation_audit_summary.csv
```

| Field | Description |
| --- | --- |
| `arm` | Workflow condition. |
| `n_claims` | Number of audited citation claims. |
| `n_miscitations` | Number of adjudicated mis-citations. |
| `mis_citation_rate` | Mis-citations divided by audited claims. |
| `ml_flag_rate` | Share of claims flagged by ML workflow. |
| `mean_review_time_seconds` | Mean review time for records with timing data. |
| `unsupported_claim_rate` | Share of claims labeled unsupported. |
| `fabricated_source_rate` | Share of claims tied to fabricated sources. |
| `metadata_error_rate` | Share of claims with material metadata errors. |

## Learner-study event records

Default synthetic CSV path:

```text
outputs/synthetic_event_log.csv
```

| Field | Type | Description |
| --- | --- | --- |
| `learner_id` | string | Synthetic or de-identified learner identifier. |
| `arm` | string | Experimental condition. |
| `task_id` | string | Task identifier. |
| `step` | integer | Task order. |
| `correctness` | float | 0.0 to 1.0 correctness value. |
| `confidence` | float | 0.0 to 1.0 learner confidence. |
| `calibration_error` | float | Absolute confidence-performance gap. |
| `latency_seconds` | float | Task response time. |
| `hint_count` | integer | Cumulative support-use count. |
| `selected_action` | string | Scaffold or audit action selected. |
| `action_intensity` | float | 0.0 to 1.0 support intensity. |
| `support_intensity_next` | float | Support intensity applied to next attempt. |
| `learner_skill` | float | Synthetic skill parameter; not available in real data unless measured. |

## Data governance

Do not commit identifiable human-subject data. Real data should be de-identified before analysis. Public examples should use synthetic data, small fabricated examples, or aggregate outputs.
