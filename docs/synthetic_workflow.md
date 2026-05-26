# Synthetic Workflow

This workflow shows how to run the current four-arm synthetic experiment and summarize the results.

## Install

From a Mac terminal:

```bash
git clone https://github.com/pskeffington/ml-lab.git
cd ml-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the synthetic experiment

```bash
ml-lab-run
```

This writes:

```text
outputs/synthetic_event_log.csv
```

The default runner includes four research-design conditions:

```text
adaptive_ml_scaffold
static_scaffold
unguided_llm_assistance
no_ai_control
```

Each event row records the learner, assigned arm, task, correctness, confidence, calibration error, latency, selected action, action intensity, next-step support intensity, and synthetic learner skill.

## Summarize by experimental arm

```bash
ml-lab-analyze
```

This writes:

```text
outputs/arm_summary.csv
```

The summary file reports arm-level means for correctness, confidence, calibration error, latency, hint count, and action intensity.

## Run tests

```bash
python -m pytest
```

The tests verify deterministic output under fixed seeds, expected event schema, CSV writing, grouped summaries, and validation behavior.

## Research interpretation caution

The synthetic workflow is an engineering scaffold, not evidence of learning effectiveness. Its purpose is to test object interfaces, logging assumptions, policy behavior, and analysis plumbing before empirical data collection.
