#!/usr/bin/env python3
"""PostToolUse hook: run the ruleset linter after an edit that it checks.

`scripts/lint_ruleset.py` is a required status check, and every failure it
reports is mechanical — a duplicate rule ID, a cross-reference to an ID that
does not exist, a missing document section, an image filename that names a rule
which is not there. Waiting for CI to report those means a push, a red check
and a second commit for something the editing session could have seen at once.

So it runs here, on every Write or Edit to `docs/` or `assets/IMAGES.md`, and
its output is returned to the agent that made the edit.

A failure is reported, not blocked. Exit code 2 shows stderr to the agent while
leaving the edit in place, which is the right shape: applying a change touches
several files, and the ruleset is legitimately inconsistent between the first
of those edits and the last. What matters is that nobody finishes a session
still believing it was clean.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

MAX_LINES = 40


def main():
    payload = json.load(sys.stdin)
    raw_path = (payload.get("tool_input") or {}).get("file_path")
    if not raw_path:
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    if project_dir:
        root = Path(project_dir)
    else:
        found = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=10,
        )
        root = Path(found.stdout.strip()) if found.returncode == 0 else Path(".")

    linter = root / "scripts" / "lint_ruleset.py"
    if not linter.is_file():
        return 0

    target = Path(raw_path)
    if not target.is_absolute():
        target = root / target

    try:
        rel = target.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return 0

    watched = (rel.startswith("docs/") and rel.endswith(".md")) or rel == "assets/IMAGES.md"
    if not watched:
        return 0

    result = subprocess.run(
        [sys.executable, str(linter)], cwd=root, capture_output=True, text=True, timeout=120
    )
    if result.returncode == 0:
        return 0

    output = (result.stdout + result.stderr).strip().splitlines()
    if len(output) > MAX_LINES:
        output = output[:MAX_LINES] + [f"... ({len(output) - MAX_LINES} more lines)"]

    print(
        "scripts/lint_ruleset.py fails after this edit:\n\n"
        + "\n".join(output)
        + "\n\nIt is a required status check, so this blocks the pull request. "
        "If you are part-way through applying a change, finish the remaining "
        "edits and run it again yourself; if you are not, fix it now. Never "
        "edit a document merely to make the check pass — that is the one rule "
        "in .claude/agents/proposal-applier.md that matters most.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # Never let the linter wrapper break an editing session.
