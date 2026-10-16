.PHONY: install test lint demo check

install:
	pip install -r requirements-dev.txt

test:
	python -m pytest -q

lint:
	ruff check src tests

demo:
	PYTHONPATH=src python -m demo_app.core

check:
	python scripts/check_submission.py
