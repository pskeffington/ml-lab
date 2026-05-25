# ml-lab

Adaptive machine-learning scaffolding research lab.

## Working research topic

**Adaptive Machine-Learning Scaffolding for Learning Under Cognitive Load**

This repository develops a reproducible experimental framework for studying whether adaptive machine-learning scaffolds improve durable learning, transfer, metacognitive calibration, and reduced hint dependency compared with static scaffolding, unguided LLM assistance, and non-AI control conditions.

## Initial research question

Does adaptive ML-driven scaffolding improve learning transfer and metacognitive calibration compared with static scaffolding, unguided LLM use, and no-AI control conditions?

## Planned structure

```text
src/ml_lab/        Python package for learner state, scaffold policies, experiments, and evaluation
docs/              Paper outline, literature matrix, and experimental design notes
tests/             Unit tests for core objects and metrics
scripts/           Reproducible command-line experiment and analysis entrypoints
notebooks/         Exploratory demonstrations and result inspection
```

## Development workflow

All work should be conducted in Git branches with clear commits.

```bash
git checkout -b scaffold-lab-init
git add .
git commit -m "Initialize adaptive scaffolding research lab"
```
