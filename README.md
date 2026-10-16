<!--
=====================================================================
HOW TO USE THIS TEMPLATE (delete this block once your repo is set up)
=====================================================================
1. Click "Use this template" → "Create a new repository".
   Name it: comp5320-w<WEEK>-g<GROUP>-<short-topic>
   e.g.  comp5320-w06-g03-design-patterns
2. Add every team member and the instructor as collaborators.
3. Replace every "TODO" in this repository. `make check` lists what is left.
4. Follow CHECKLIST.md for what is due at the consultation and after class.
=====================================================================
-->

# COMP5320 · Week TODO · Chapter TODO: TODO chapter title

**Team:** Group TODO · **Leader:** TODO · **Presentation date:** TODO
**Textbook:** *Agentic Software Engineering: A Practical Guide for the AI-Native Engineer* (Tantithamthavorn, 2026), [book.agentic-swe.dev](https://book.agentic-swe.dev)

| Member | Main responsibility |
|---|---|
| TODO | TODO (e.g. slides on sections X.1–X.3) |
| TODO | TODO (e.g. live demo) |
| TODO | TODO (e.g. tutorial handout) |
| TODO | TODO (e.g. online participants & chat) |
| TODO | TODO |

## What is in this repository

| Folder / file | Contents |
|---|---|
| `slides/` | Final slides (PDF + PPTX), built on the COMP5320 slide template |
| `presentation/` | Review questions, discussion points and the research link |
| `demo/DEMO_SCRIPT.md` | Step-by-step script of the live demo, including the agent mistake |
| `src/`, `tests/` | Demo code and its tests |
| `tutorial/` | Tutorial handout, starter files and sample solutions |
| `verification/` | Verification log and AI usage log for the demo and tutorial |
| `AGENTS.md` | Instructions for AI coding agents working in this repo |
| `CONTRIBUTIONS.md` | Who did what |

## Run the demo

Requirements: Python 3.11+, Git, Docker (optional), and the AI coding agent named below.

```bash
git clone <this-repo-url>
cd <repo>
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
make test        # run the tests
make demo        # TODO: describe what this runs
```

Or with Docker:

```bash
docker build -t comp5320-demo .
docker run --rm comp5320-demo
```

**AI agent and model used in the demo:** TODO (e.g. Claude Code with model X, Cursor, Gemini CLI, Codex)

**Backup recording of the demo:** TODO (link)

## Tutorial

Start with [`tutorial/TUTORIAL.md`](tutorial/TUTORIAL.md). Every team other than the presenting team completes it on **its own project** and submits the artefacts plus a verification log before the next tutorial.

## Attribution

Chapter content is summarised from the textbook above (CC BY-NC-ND 4.0). Do not copy text from the book; teach it in your own words and examples. Any code or figures reused from other sources must be cited here:

- TODO (source, licence, what was reused)
