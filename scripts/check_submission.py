"""List files that still contain TODO placeholders or required files that are missing.

Usage: python scripts/check_submission.py
Exit code 1 if anything remains, so it can be used before submitting.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md",
    "CONTRIBUTIONS.md",
    "demo/DEMO_SCRIPT.md",
    "presentation/DISCUSSION.md",
    "tutorial/TUTORIAL.md",
    "verification/VERIFICATION_LOG.md",
    "verification/AI_USAGE_LOG.md",
]
SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "node_modules"}
SKIP_FILES = {"check_submission.py", "CHECKLIST.md"}
TEXT_SUFFIXES = {".md", ".py", ".toml", ".txt", ".yml", ".yaml"}


def main() -> int:
    problems = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            problems.append(f"missing: {rel}")
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name in SKIP_FILES or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        count = path.read_text(encoding="utf-8", errors="ignore").count("TODO")
        if count:
            problems.append(f"{count:3d} TODO  {path.relative_to(ROOT)}")
    if not any((ROOT / "slides").glob("*.pdf")):
        problems.append("missing: slides/*.pdf")
    if problems:
        print("Still to do before submission:")
        print("\n".join(f"  {p}" for p in problems))
        return 1
    print("All set: no TODOs left and all required files present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
