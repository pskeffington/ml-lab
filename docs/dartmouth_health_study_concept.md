# Dartmouth Health Study Concept

## Project status

This is an early-stage proposed research study concept. It is a drafting artifact for shaping `ml-lab` into a study that could be relevant to Dartmouth Health, Dartmouth Hitchcock Medical Center, Geisel School of Medicine, The Dartmouth Institute, and related rural-health and learning-health-system research partners. It does not represent an approved study, funded project, IRB protocol, clinical implementation, or validated empirical system.

## Working concept

**A learning-health-system pilot for auditable ML-assisted review of clinical, educational, and research documentation in rural healthcare delivery.**

The current repository already contains two related tracks:

```text
Track A: Adaptive scaffolding simulation
Track B: Citation-integrity audit workflow
```

For Dartmouth Health relevance, the near-term proposal should emphasize Track B as the health-system-facing pilot and preserve Track A as a supporting simulation and training scaffold. The strongest health-system use case is not a broad claim that AI improves learning. The stronger, more practical claim is that auditable ML-assisted review may improve documentation quality, citation integrity, protocol preparation, or evidence-use reliability in clinical and rural-health research workflows.

## Why Dartmouth Health might care

Dartmouth Health publicly emphasizes research and innovation, clinical expertise, clinical trials, HRPP/IRB infrastructure, rural health equity, and rural healthcare delivery science. A viable proposal should therefore connect `ml-lab` to practical problems that matter in an academic health system:

- reducing avoidable documentation and citation errors in research-facing materials;
- improving trustworthiness of evidence summaries used in pilot proposals, quality improvement, and clinical research planning;
- supporting rural healthcare delivery science with lightweight, auditable workflows;
- improving trainee and early-career researcher support without replacing expert review;
- creating a learning-health-system feedback loop where errors, corrections, and review outcomes become reusable quality-improvement data.

## Proposed Dartmouth Health-facing study title

**Auditable ML-Assisted Evidence Review for Rural Healthcare Delivery Research: A Feasibility Pilot**

Alternative titles:

- **ML-Assisted Citation and Evidence Integrity Review for Health-System Research Drafting**
- **A Learning-Health-System Pilot for Safer AI-Assisted Research Documentation**
- **Improving Evidence-Use Reliability in Rural Health Research Proposals with Auditable ML Review**

## Core research question

Can an auditable ML-assisted evidence-review workflow improve the quality, completeness, and review efficiency of health-system research documentation compared with usual manual review?

## Proposed pilot aim

Evaluate whether an ML-assisted citation and evidence audit workflow can feasibly identify unsupported claims, citation mismatches, source metadata errors, and overstatements in early-stage research documents relevant to rural healthcare delivery, quality improvement, or clinical research proposal development.

## Specific aims

### Aim 1: Feasibility

Assess whether a structured ML-assisted audit workflow can be applied to early-stage health-system research documents without exposing private patient data or restricted materials.

Candidate feasibility measures:

- number of documents processed;
- number of citation claims extracted;
- percentage of claims with identifiable sources;
- completion time per claim;
- missing-field rate in audit records;
- reviewer completion burden.

### Aim 2: Documentation quality

Estimate whether ML-assisted review improves detection of citation and evidence-use problems compared with baseline review.

Candidate quality measures:

- adjudicated mis-citation rate;
- unsupported-claim rate;
- overstated-claim rate;
- metadata-error rate;
- wrong-source rate;
- fabricated-source rate;
- quote-error rate;
- scope-error rate.

### Aim 3: Reviewer support and learning-health feedback

Assess whether the workflow produces reusable feedback that can improve future proposal drafting, training, and documentation standards.

Candidate feedback measures:

- recurring error types;
- error clusters by document section;
- reviewer confidence;
- reviewer time;
- proportion of ML flags confirmed by adjudication;
- correction patterns that can inform future templates and training materials.

## Candidate study design

### Design type

Feasibility pilot with adjudicated document-level and citation-claim-level outcomes.

### Units of analysis

Primary unit:

```text
citation_claim
```

Secondary units:

```text
document
reviewer
document_section
source_record
```

### Candidate arms

| Arm | Description |
| --- | --- |
| baseline | Review using existing manual process without ML-assisted flagging. |
| ml_audit | Review after ML-assisted claim extraction, source checking, and issue flagging. |
| ml_plus_human | ML flags likely issues, then human adjudicator verifies and classifies errors. |

The most defensible initial pilot is `baseline` versus `ml_plus_human`, because it keeps human adjudication as the source of truth and avoids claiming autonomous AI performance.

## Candidate document sources

Use public-safe, non-identifiable, low-risk documents first:

- synthetic research-proposal excerpts;
- public clinical-trial summaries;
- public health-policy briefs;
- de-identified training documents;
- mock rural-health research proposals;
- public literature summaries created for the study.

Do not use patient records, identifiable student work, restricted internal documents, or confidential grant/protocol drafts without explicit governance approval.

## Exclusion rules

Exclude any document or claim that:

- includes protected health information;
- contains identifiable private information;
- depends on restricted or unavailable source material;
- cannot be linked to a reference record;
- is outside the selected pilot domain;
- would require committing private source text to the public repository.

## Data governance boundary

This repository should contain only code, synthetic examples, public-safe templates, aggregate outputs, and de-identified records approved for public use. Real study data should be stored outside the repository in an approved governed environment.

Before any real Dartmouth Health or Dartmouth-affiliated data are used, the project needs determination of:

- whether the activity is quality improvement, non-human-subject research, or human-subject research;
- whether HRPP/IRB review is required;
- where source documents and adjudication records may be stored;
- who may access the data;
- what may be exported or committed;
- whether a data-use agreement, security review, or operational approval is required.

## Dartmouth Health alignment map

| Dartmouth Health-facing priority | How this concept aligns |
| --- | --- |
| Research and innovation | Builds an auditable AI-assisted workflow for research-document quality. |
| Clinical-trials and protocol readiness | Helps detect unsupported claims, metadata errors, and source mismatches before submission. |
| Rural healthcare delivery science | Applies to rural-health proposals, evidence summaries, and implementation documents. |
| Rural health equity | Supports clearer, more reliable evidence use in projects serving rural communities. |
| Learning health system | Converts review errors and corrections into structured feedback for future quality improvement. |
| Patient safety and trust | Avoids autonomous clinical recommendations and focuses first on documentation integrity. |

## Minimal viable pilot

A minimal pilot could be completed with:

```text
10 to 20 public-safe documents
200 to 500 citation claims
2 workflow arms: baseline and ml_plus_human
1 to 2 adjudicators
1 structured CSV audit dataset
1 aggregate summary table
1 feasibility report
```

## Analysis plan sketch

Primary descriptive outputs:

- number of documents;
- number of citation claims;
- claims per document;
- source-availability rate;
- adjudicated mis-citation rate by arm;
- error-type distribution;
- mean review time by arm;
- reviewer confidence by arm;
- ML flag confirmation rate.

Primary comparative outputs:

- absolute difference in mis-citation detection rate;
- relative difference in mis-citation detection rate;
- false-positive and false-negative rates when adjudicated labels are available;
- confidence intervals for arm-level rates when sample size allows.

The first pilot should emphasize feasibility and measurement quality, not definitive causal claims.

## Repository build implications

To make this workable, the next code and documentation work should add:

```text
examples/citation_audit_records_synthetic.csv
docs/dartmouth_health_study_concept.md
docs/governance_checklist.md
src/ml_lab/audit/reliability.py
src/ml_lab/audit/intervals.py
tests/test_audit_reliability.py
tests/test_audit_intervals.py
```

## Next implementation milestones

1. Add a public-safe synthetic audit dataset.
2. Add confidence intervals for mis-citation rates and reductions.
3. Add inter-rater reliability measures for multiple adjudicators.
4. Add a governance checklist for Dartmouth Health-style review.
5. Add a one-page specific-aims draft.
6. Add a pilot feasibility report template.
7. Keep the README clear that this is an early proposal and not approved or validated empirical work.

## Public-facing positioning

Use:

```text
proposed feasibility pilot
pre-pilot research scaffold
auditable ML-assisted evidence review
rural healthcare delivery research documentation
human-adjudicated citation integrity workflow
```

Avoid:

```text
validated clinical AI
approved Dartmouth Health study
proven improvement in research quality
autonomous clinical documentation system
patient-facing AI tool
```

## Source alignment notes

This concept was drafted to align with public Dartmouth Health pages describing its research and innovation ecosystem, rural health equity work, rural healthcare delivery science center, clinical trials, HRPP/IRB resources, and Promise Partnership Learning Health System resources. These sources should be reviewed and cited in any formal proposal narrative rather than treated as institutional endorsement.