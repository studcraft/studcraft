#!/usr/bin/env python3
"""Compare the ruleset's rule IDs against a base revision. IDs are permanent.

`system/documentation-standards.md` makes rule identifiers stable: they are
never renumbered and never reused. A superseded rule keeps its number and
carries a note saying so — `MEL-010`, `CBT-011` and `WPN-021` are the
precedents, and the `13-*.md` gap in `docs/` exists for the same reason.

That invariant is enforced by nobody. `scripts/lint_ruleset.py` checks IDs
within a single revision — duplicates, and ordering inside a document — which
cannot see a rule that quietly changed number or moved to another document
between two revisions. Only a comparison against the base can.

**This has never fired.** Scanning the last twenty-five commits on `main` found
no renumbering, no reuse and no disappearance, which is the honest case for
running it: it is insurance on an invariant that is cheap to check and expensive
to break, not a tool that finds things. An ID is cited from other documents,
from `docs/14-glossary.md` and from `assets/IMAGES.md`, so a silent renumber
breaks references in places nothing points at.

Three things are reported:

  disappeared   an ID present in the base and absent now. A rule may be
                superseded, but its number stays and carries a note.
  moved         an ID that changed document. Each document owns its prefix
                namespace, so this is a renumbering wearing the same number.
  reused        an ID absent from the base, present now, and whose number is
                below the highest its document already had. New rules append.

Usage:

    python3 scripts/check_id_stability.py              against origin/main
    python3 scripts/check_id_stability.py <revision>   against anything else
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

RULE_HEADER_RE = re.compile(r"^#{1,2} ([A-Z]{2,6})-(\d{3}) — ", re.MULTILINE)
DEFAULT_BASE = "origin/main"


def git(*args: str) -> tuple[int, str]:
    proc = subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout


def ids_at_revision(revision: str) -> dict[str, str] | None:
    """Every rule ID in docs/ at `revision`, mapped to the document holding it."""
    code, listing = git("ls-tree", "-r", "--name-only", revision, "docs/")
    if code != 0:
        return None

    found: dict[str, str] = {}
    for path in listing.split():
        if not path.endswith(".md"):
            continue
        code, text = git("show", f"{revision}:{path}")
        if code != 0:
            continue
        for prefix, number in RULE_HEADER_RE.findall(text):
            found[f"{prefix}-{number}"] = path[len("docs/"):]
    return found


def ids_in_worktree() -> dict[str, str]:
    """The same, from the files on disk — so uncommitted work is checked too."""
    found: dict[str, str] = {}
    for path in sorted(DOCS_DIR.glob("*.md")):
        for prefix, number in RULE_HEADER_RE.findall(path.read_text()):
            found[f"{prefix}-{number}"] = path.name
    return found


def main(argv: list[str]) -> int:
    base = argv[0] if argv else DEFAULT_BASE

    before = ids_at_revision(base)
    if before is None:
        print(f"Cannot read {base}; nothing to compare against. Skipping.")
        return 0

    after = ids_in_worktree()
    errors: list[str] = []

    for rule_id in sorted(set(before) - set(after)):
        errors.append(
            f"{rule_id} was in {before[rule_id]} at {base} and is gone. Rule IDs are "
            f"never removed — a superseded rule keeps its number and carries a note "
            f"saying so (MEL-010, CBT-011, WPN-021 are the precedents)."
        )

    for rule_id in sorted(set(before) & set(after)):
        if before[rule_id] != after[rule_id]:
            errors.append(
                f"{rule_id} moved from {before[rule_id]} to {after[rule_id]}. Each "
                f"document owns its prefix namespace, so this is a renumbering."
            )

    highest: dict[tuple[str, str], int] = {}
    for rule_id, document in before.items():
        prefix = rule_id.split("-")[0]
        key = (document, prefix)
        highest[key] = max(highest.get(key, 0), int(rule_id.split("-")[1]))

    for rule_id in sorted(set(after) - set(before)):
        prefix, number = rule_id.split("-")
        ceiling = highest.get((after[rule_id], prefix))
        if ceiling is not None and int(number) < ceiling:
            errors.append(
                f"{rule_id} is new in {after[rule_id]} but sits below "
                f"{prefix}-{ceiling:03d}, which that document already had at {base}. "
                f"New rules append; a number below the ceiling is a reused one."
            )

    if errors:
        for error in errors:
            print(f"::error::{error}")
        print(f"\n{len(errors)} rule-ID stability issue(s) against {base}.")
        return 1

    added = len(set(after) - set(before))
    print(
        f"Compared {len(after)} rule ID(s) against {base}: none renumbered, reused or "
        f"removed{f', {added} appended' if added else ''}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
