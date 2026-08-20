#!/usr/bin/env python3
"""The facts about this repository that more than one script needs.

Three things here were each defined in several scripts at once, which is the
thing `scripts/build_index.py` already refused to do with the citation patterns:
*"A second copy of that would drift from the first, and the drift would be
silent."* The argument does not stop at that one import.

  - **The rule-ID pattern.** `lint_ruleset.py` and `rule.py` held identical
    copies of it. It encodes a convention (`system/documentation-standards.md`,
    Naming Conventions) that can change, and a copy that misses the change
    reports nothing rather than reporting a failure. The rule-header pattern
    made the same argument once; it has since moved to
    `scripts/ruleset_ast.py`, which is where "is this heading a rule" now has
    its single answer. The ID pattern stays here because it answers a
    different question — is a rule ID present anywhere in prose — that no AST
    replaces.
  - **Which directories under `openspec/changes/` are changes.** Four scripts
    each spelled out that `archive` is not one. A fifth that forgot would
    quietly audit archived work.
  - **A read-only `git` call.** Two scripts had the same five lines.

`scripts/open_pr.py` deliberately keeps its own runner: it also runs `gh`, and
it stops the process on a non-zero exit rather than returning one. Scripts that
need nothing else from here keep their own one-line `REPO_ROOT`; a path spelled
once is not a rule that can drift.

Import it the way `build_index.py` already does:

    sys.path.insert(0, str(Path(__file__).resolve().parent))

    from repo import CHANGES_DIR, RULE_ID_RE  # noqa: E402
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CHANGES_DIR = REPO_ROOT / "openspec" / "changes"
SPECS_DIR = REPO_ROOT / "openspec" / "specs"

# A rule ID wherever it appears — in a citation, a table cell, a glossary entry.
RULE_ID_RE = re.compile(r"[A-Z]{2,6}-\d{3}")


def unarchived_changes() -> list[str]:
    """Every OpenSpec change directory that has not been archived yet.

    `openspec/changes/archive/` holds completed changes and is not one of them.
    """
    if not CHANGES_DIR.is_dir():
        return []
    return sorted(
        path.name
        for path in CHANGES_DIR.iterdir()
        if path.is_dir() and path.name != "archive"
    )


def git(*args: str) -> tuple[int, str]:
    """Run git in the repository root. Returns (exit code, stripped stdout).

    Read-only by convention rather than by construction: every caller here
    passes an inspection subcommand, and anything that writes belongs in
    `scripts/open_pr.py`, which is the one script allowed to change history.
    """
    proc = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    return proc.returncode, proc.stdout.strip()
