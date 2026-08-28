#!/usr/bin/env python3
"""Compare the ruleset's rule IDs against a base revision. IDs are never reissued.

`system/documentation-standards.md` makes rule identifiers stable: they are
never renumbered and never reused. A rule may be deleted once another document
owns what it said, and its number is then retired rather than handed to a new
rule — the `13-*.md` gap in `docs/` is the same thing at document scale.

That invariant is enforced by nobody. `scripts/lint_ruleset.py` checks IDs
within a single revision — duplicates, and ordering inside a document — which
cannot see a rule that quietly changed number or moved to another document
between two revisions. Only a comparison against the base can. A rule heading
written inside a fenced block is not a rule, and both checks below rely on
`scripts/ruleset_ast.py` to leave it uncounted — a phantom ID is exactly the
sort of thing that would otherwise be reported as reused.

An ID is cited from other documents, from `docs/14-glossary.md` and from
`assets/IMAGES.md`, so a silent renumber breaks references in places nothing
points at. This is insurance on an invariant that is cheap to check and
expensive to break, not a tool that finds things.

Two things are reported:

  moved         an ID that changed document. Each document owns its prefix
                namespace, so this is a renumbering wearing the same number.
  reused        an ID absent from the base, present now, and whose number is
                below the highest its document already had. New rules append.

An ID present in the base and absent now is **not** reported. Deleting a rule is
an ordinary edit. Its one failure mode is a stranded citation, and
`scripts/lint_ruleset.py` catches that only within `docs/` and
`assets/IMAGES.md` — it reads nothing else, while `README.md`,
`CODE_OF_DESIGN.md`, `TODO.md` and `system/` all cite rule IDs too. A proposal
retiring an ID therefore greps the whole repository for it, which
`system/proposal-review.md` states as a step. What this script adds is the case
no grep would think to look for: a number reappearing on a different rule.

Usage:

    python3 scripts/check_id_stability.py              against origin/main
    python3 scripts/check_id_stability.py <revision>   against anything else

A revision passed explicitly and unreadable is an error rather than a skip: CI
names the pull request's base, and a base that is not there would otherwise
report every identifier stable without comparing it to anything.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import DOCS_DIR, git  # noqa: E402
from ruleset_ast import parse_text  # noqa: E402

DEFAULT_BASE = "origin/main"


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
        name = path[len("docs/"):]
        for section in parse_text(name, text).root.rules():
            found[section.rule_id] = name
    return found


def ids_in_worktree() -> dict[str, str]:
    """The same, from the files on disk — so uncommitted work is checked too."""
    found: dict[str, str] = {}
    for path in sorted(DOCS_DIR.glob("*.md")):
        for section in parse_text(path.name, path.read_text()).root.rules():
            found[section.rule_id] = path.name
    return found


def main(argv: list[str]) -> int:
    base = argv[0] if argv else DEFAULT_BASE

    before = ids_at_revision(base)
    if before is None:
        # A base that was *asked for* and cannot be read is a wrong answer, not
        # a missing one: in CI it would report every rule ID stable without
        # comparing them against anything. `origin/main` failing is different —
        # a fresh clone with no remote legitimately has nothing to compare to.
        if argv:
            print(
                f"::error::Cannot read {base}, which was named explicitly. "
                f"Refusing to report the rule IDs stable without comparing them "
                f"against anything.",
                file=sys.stderr,
            )
            return 1
        print(f"Cannot read {base}; nothing to compare against. Skipping.")
        return 0

    after = ids_in_worktree()
    errors: list[str] = []

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
    retired = len(set(before) - set(after))
    tail = "".join(
        (
            f", {added} appended" if added else "",
            f", {retired} retired" if retired else "",
        )
    )
    print(f"Compared {len(after)} rule ID(s) against {base}: none renumbered or reused{tail}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
