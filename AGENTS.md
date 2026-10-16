# AGENTS.md

Instructions for AI coding agents working in this repository.

## Project

Teaching demo for COMP5320, Chapter TODO (TODO chapter title). The code exists to demonstrate practices live in class, so clarity matters more than cleverness.

## Commands

- Install: `pip install -r requirements-dev.txt`
- Test: `make test` (pytest)
- Lint: `make lint` (ruff)
- Demo: `make demo`

## Rules

- Keep code in `src/demo_app/` and tests in `tests/`.
- Every new function needs a test. Run `make test` and `make lint` before proposing a change.
- Do not add dependencies without saying why.
- Do not modify `tutorial/solutions/` or anything in `verification/`; humans write those.
- Never commit secrets, API keys or personal data.

## Context

TODO: anything the agent must know for this chapter's demo (domain, constraints, files to read first).
