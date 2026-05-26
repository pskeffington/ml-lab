# Dartmouth Study Packet

## Project identity

`ml-lab` is a science-abstract machine-learning system for auditable learning and citation-integrity research. It translates research questions into modular ML objects, study arms, event logs, outcome metrics, and interpretation boundaries.

## Near-term study

The near-term non-synthetic study tests whether ML-assisted citation auditing reduces mis-citations in research writing.

## Research question

Does ML-assisted citation auditing reduce the citation-level mis-citation rate compared with baseline review?

## Primary outcome

```text
mis_citation_rate = n_miscitations / n_audited_citation_claims
```

## Primary estimand

```text
absolute_reduction = p_baseline - p_ml_audit
relative_reduction = (p_baseline - p_ml_audit) / p_baseline
```

## Why this matters

AI-assisted research writing creates a need for workflows that verify whether claims are actually supported by cited sources. A system that reduces unsupported, overstated, wrong-source, fabricated-source, or metadata citation errors would contribute to research integrity, reproducibility, and responsible AI use.

## What is already implemented

The repository currently includes:

- core science-abstract ML objects for learning-scaffold experiments;
- four-arm synthetic learner workflow;
- event-log export and arm-level summaries;
- pairwise effect-size comparisons;
- citation-audit objects and metrics;
- citation-audit CSV template generation;
- citation-audit CSV analysis;
- data dictionary;
- pilot protocol;
- publication evidence roadmap;
- tests for core, experiment, evaluation, and audit modules.

## Terminal workflow

From a Mac terminal:

```bash
git clone https://github.com/pskeffington/ml-lab.git
cd ml-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Synthetic learning workflow:

```bash
ml-lab-run
ml-lab-analyze
```

Citation-audit pilot workflow:

```bash
ml-lab-audit-template
# fill outputs/citation_audit_records.csv with adjudicated records
ml-lab-audit-analyze
python -m pytest
```

## Expected outputs

```text
outputs/synthetic_event_log.csv
outputs/arm_summary.csv
outputs/pairwise_comparisons.csv
outputs/citation_audit_template.csv
outputs/citation_audit_records.csv
outputs/citation_audit_summary.csv
```

## Pilot design summary

| Element | Design choice |
| --- | --- |
| Unit of analysis | Citation claim |
| Minimum sample | 200 to 500 citation claims |
| Core arms | `baseline`, `ml_audit` |
| Optional arms | `human_audit`, `ml_plus_human` |
| Gold standard | Human adjudication of source support |
| Primary metric | Mis-citation rate |
| Main comparison | Baseline vs. ML audit |
| Interpretation | Pilot evidence, not universal causal proof |

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

## Publication path

The project is staged for three publication shapes:

1. System/protocol paper: reproducible ML research architecture for auditable learning and citation integrity.
2. Pilot citation-audit paper: non-synthetic estimate of mis-citation reduction from ML-assisted auditing.
3. Future learner study: adaptive scaffolding effects on calibration, transfer, and durable learning.

## Collaboration ask

The immediate collaboration need is a small corpus of research documents or citation claims suitable for adjudication, plus guidance on domain scope, adjudication standards, and appropriate governance for de-identified research-writing data.

## Claim boundary

The repository is ready to support a pilot estimate of citation-audit performance. It is not yet claiming that ML auditing universally reduces mis-citations or that adaptive scaffolding improves real learner outcomes. Those claims require the evidence milestones defined in `docs/evidence_roadmap.md`.
