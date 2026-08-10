#!/usr/bin/env python3
"""PostToolUse hook: run the ruleset linter after anything that changed the ruleset.

`scripts/lint_ruleset.py` is a required status check, and every failure it
reports is mechanical — a duplicate rule ID, a cross-reference to an ID that
does not exist, a missing document section, an image filename that names a rule
which is not there. Waiting for CI to report those means a push, a red check
and a second commit for something the editing session could have seen at once.

A failure is reported, not blocked. Exit code 2 shows stderr to the agent while
leaving the edit in place, which is the right shape: applying a change touches
several files, and the ruleset is legitimately inconsistent between the first
of those edits and the last. What matters is that nobody finishes a session
still believing it was clean.

## Why this watches `Bash` too, and why by mtime

It used to match `Write|Edit` only, and read `tool_input.file_path` to decide
whether the file was one it cared about. A shell command that writes — a
`python3 - <<'PY'` heredoc, a `sed -i`, a redirection — has no `file_path`, so
it edited the ruleset with the linter switched off.

Measured across fifty sessions, that happened two or three times: the great
majority of heredocs in this repository's history edited `openspec/` task files,
which the linter does not check anyway. So this closes a small hole, not a large
one — worth doing because it is cheap, not because it was common.

Cheap is the operative word, and it is why this compares **modification times**
rather than guessing from the command text whether it looks like a write.
Deciding intent from a shell string is a losing game: a first attempt at it
matched a commit message quoting the word `docs/` and this hook's own analysis
scripts. An mtime cannot be fooled, needs no allowlist, and costs sixteen
`stat` calls. The stamp lives in `.studcraft/`, which is gitignored and already
holds the generated index.

The first run after the stamp is missing records the current state and lints
nothing — a fresh checkout should not open with a linter report about work
somebody else did.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

MAX_LINES = 40
STAMP = Path(".studcraft") / "ruleset-mtime.json"


def watched_files(root: Path) -> list[Path]:
    files = sorted((root / "docs").glob("*.md"))
    images = root / "assets" / "IMAGES.md"
    if images.is_file():
        files.append(images)
    return files


def fingerprint(root: Path) -> dict[str, float]:
    return {
        path.relative_to(root).as_posix(): path.stat().st_mtime
        for path in watched_files(root)
    }


def ruleset_changed(root: Path) -> bool:
    """Whether anything the linter reads has been written since the last check.

    Records the new state either way, so a change is reported once rather than
    on every tool call that follows it.
    """
    current = fingerprint(root)
    stamp = root / STAMP

    previous = None
    if stamp.is_file():
        try:
            previous = json.loads(stamp.read_text())
        except (json.JSONDecodeError, OSError):
            previous = None

    try:
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.write_text(json.dumps(current))
    except OSError:
        pass  # A hook that cannot write its own cache still has a job to do.

    if previous is None:
        return False

    return current != previous


def main():
    payload = json.load(sys.stdin)
    tool = payload.get("tool_name") or ""
    raw_path = (payload.get("tool_input") or {}).get("file_path")

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

    if raw_path:
        # Write and Edit name their target, so the cheapest correct answer is to
        # read it. The mtime stamp is still refreshed, so an edit the linter
        # ignores does not leave the stamp claiming the ruleset is unchanged.
        target = Path(raw_path)
        if not target.is_absolute():
            target = root / target

        try:
            rel = target.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            return 0

        watched = (rel.startswith("docs/") and rel.endswith(".md")) or rel == "assets/IMAGES.md"
        ruleset_changed(root)
        if not watched:
            return 0
    elif tool == "Bash":
        if not ruleset_changed(root):
            return 0
    else:
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
