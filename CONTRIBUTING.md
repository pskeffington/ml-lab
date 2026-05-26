# Contributing

This repository is an active research codebase. Contributions should keep the project reproducible, modular, and aligned with the adaptive scaffolding study design.

## Workflow

Create a short-lived branch for each focused change.

```bash
git checkout -b feature/descriptive-name
```

Before committing, review the changed files and keep commits focused.

```bash
git status
git diff
git add <files>
git commit -m "Describe the focused change"
```

## Code standards

- Keep objects small and testable.
- Separate learner state, scaffold policies, task environments, and outcome metrics.
- Prefer explicit configuration over hidden defaults.
- Keep source files and generated outputs separate.
- Do not commit secrets, credentials, private data, local exports, or generated build artifacts.
- Promote stable notebook logic into scripts or package modules.

## Documentation standards

- Document research decisions before encoding them in experiments.
- Define constructs before operationalizing them.
- Keep method notes tied to code objects under `src/ml_lab/`.
- Update `docs/research_design.md` when experimental assumptions change.

## Testing

When tests are available, run:

```bash
python -m pytest
```

New implementation work should include focused tests for the object, policy, or metric being added. For code or document changes, mention any checks that could not be run.
