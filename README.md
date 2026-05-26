# ml-lab

Adaptive machine-learning scaffolding research lab for studying learning under cognitive load.

## Research focus

**Adaptive Machine-Learning Scaffolding for Learning Under Cognitive Load**

This repository supports a reproducible research framework for testing whether adaptive machine-learning scaffolds improve durable learning, transfer, metacognitive calibration, and efficient help-seeking relative to static scaffolding, unguided LLM assistance, and non-AI control conditions.

## Initial research question

Does adaptive ML-driven scaffolding improve learning transfer and metacognitive calibration compared with static scaffolding, unguided LLM use, and no-AI control conditions?

## Repository map

```text
src/ml_lab/        Python package for learner state, scaffold policies, experiments, and evaluation
docs/              Research design notes, literature matrix, and paper-development materials
tests/             Unit tests for core objects, policies, and metrics
scripts/           Reproducible command-line experiment and analysis entry points
notebooks/         Exploratory demonstrations, diagnostics, and result inspection
```

## Documentation

Start with [`docs/README.md`](docs/README.md) for the documentation index. The core design document is [`docs/research_design.md`](docs/research_design.md).

## Development workflow

Use short-lived Git branches and clear commits.

```bash
git checkout -b docs-polish
git add README.md docs/
git commit -m "Polish project documentation"
```

Recommended local setup from a Mac terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Authorship

Paul Skeffington, MS, MPH  
Dartmouth College  
GitHub: [@pskeffington](https://github.com/pskeffington)  
Contact: paulskeffington@gmail.com
