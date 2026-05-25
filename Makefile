.PHONY: install test lint experiment export clean

install:
	python -m pip install --upgrade pip
	python -m pip install -e .[dev]

test:
	pytest

lint:
	ruff check src tests scripts

experiment:
	python scripts/run_synthetic_experiment.py

export:
	python scripts/export_synthetic_experiment.py

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache outputs
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
