#!/usr/bin/env python3
"""Query the ruleset without reading it.

The index built by `scripts/build_index.py` answers, in one command each, the
questions an audit otherwise answers by opening fifteen documents:

  rule.py show <ID>           the rule itself, as it reads in docs/
  rule.py refs <ID>           every rule that cites it — the inverse graph
  rule.py neighbors <ID>      what sits either side of it in its document
  rule.py touched <change>    every rule an OpenSpec change names
  rule.py orphans             rules nothing cites and no glossary entry defines
  rule.py glossary            glossary entries that point at no rule
  rule.py doc <document.md>   a document's chapters and rules, first sentence too

**Every command except `orphans` and `glossary` takes as many arguments as you
like**, and runs once per argument:

  rule.py show <ID> <ID> <ID> <ID> <ID>

Use that rather than a shell loop. A loop needs `$id`, and a command carrying a
shell expansion cannot be matched by any permission rule — it interrupts to ask,
every time, however the allowlist is written. One command with seven arguments
never asks.

`show` prints from `docs/` rather than from the index: the index tells it
where a rule's body starts and ends, but the text printed is read fresh from
the file every time, never from a stored copy. The index holds a summary, and
a summary is a thing to decide with, never a thing to audit against.
Everything else reads the index, which is rebuilt automatically whenever a
file in `docs/` is newer than it.

`orphans` is a prompt, not a verdict. A rule nothing cites may be a genuinely
standalone rule; it may equally be a rule the ruleset forgot to connect. The
command narrows 225 rules to the handful worth a human look.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, DOCS_DIR, REPO_ROOT, RULE_ID_RE  # noqa: E402

INDEX_PATH = REPO_ROOT / ".studcraft" / "index.json"


def load_index() -> dict:
    """Read the index, rebuilding it first if any document is newer."""
    stale = not INDEX_PATH.exists()
    if not stale:
        built = INDEX_PATH.stat().st_mtime
        stale = any(path.stat().st_mtime > built for path in DOCS_DIR.glob("*.md"))

    if stale:
        subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "build_index.py")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

    return json.loads(INDEX_PATH.read_text())


def need(index: dict, rule_id: str) -> dict:
    rule = index["rules"].get(rule_id.upper())
    if rule is None:
        print(f"No rule {rule_id.upper()} in docs/.", file=sys.stderr)
        raise SystemExit(1)
    return rule


def cmd_show(index: dict, rule_id: str) -> int:
    rule = need(index, rule_id)
    lines = (DOCS_DIR / rule["doc"]).read_text().splitlines()

    print(f"{rule['doc']}:{rule['line']}")
    # `line_end` already reaches through the rule's own sub-headings — it is
    # computed once, in scripts/build_index.py, from the same AST section
    # this print would otherwise have to re-walk with a pattern of its own.
    body = lines[rule["line"] - 1:rule["line_end"]]

    while body and not body[-1].strip():
        body.pop()
    print("\n".join(body))

    if rule["cites"]:
        print(f"\ncites: {', '.join(rule['cites'])}")
    if rule["cited_by"]:
        print(f"cited by: {', '.join(rule['cited_by'])}")
    return 0


def cmd_refs(index: dict, rule_id: str) -> int:
    rule = need(index, rule_id)
    if not rule["cited_by"]:
        print(f"{rule['id']} is cited by nothing.")
        return 0

    print(f"{rule['id']} — {rule['title']} is cited by:")
    for other_id in rule["cited_by"]:
        other = index["rules"][other_id]
        print(f"  {other_id:10s} {other['doc']}:{other['line']}  {other['title']}")

    terms = [entry["term"] for entry in index["glossary"] if rule["id"] in entry["cites"]]
    if terms:
        print(f"\nglossary: {', '.join(terms)}")
    return 0


def cmd_neighbors(index: dict, rule_id: str) -> int:
    rule = need(index, rule_id)
    order = index["documents"][rule["doc"]]["rules"]
    position = order.index(rule["id"])

    print(f"{rule['doc']}, rules {position + 1} of {len(order)}\n")
    for offset in (-1, 0, 1):
        spot = position + offset
        if spot < 0 or spot >= len(order):
            continue
        other = index["rules"][order[spot]]
        marker = ">" if offset == 0 else " "
        print(f"{marker} {other['id']:10s} {other['title']}")
        if other["summary"]:
            print(f"    {other['summary']}")
    return 0


def cmd_touched(index: dict, change: str) -> int:
    change_dir = CHANGES_DIR / change
    if not change_dir.is_dir():
        available = sorted(
            p.name for p in CHANGES_DIR.iterdir() if p.is_dir() and p.name != "archive"
        )
        print(f"No change {change}. Unarchived: {', '.join(available) or 'none'}", file=sys.stderr)
        return 1

    found: dict[str, set[str]] = {}
    for path in sorted(change_dir.rglob("*.md")):
        for rule_id in RULE_ID_RE.findall(path.read_text()):
            if rule_id in index["rules"]:
                found.setdefault(rule_id, set()).add(path.relative_to(change_dir).as_posix())

    if not found:
        print(f"{change} names no rule that exists in docs/.")
        return 0

    print(f"{change} names {len(found)} rule(s):\n")
    for rule_id in sorted(found, key=lambda r: (index["rules"][r]["doc"], index["rules"][r]["line"])):
        rule = index["rules"][rule_id]
        print(f"  {rule_id:10s} {rule['doc']}:{rule['line']:<5d} {rule['title']}")
        print(f"             named in: {', '.join(sorted(found[rule_id]))}")
        if rule["cited_by"]:
            print(f"             read also: {', '.join(rule['cited_by'])}")
    return 0


def cmd_orphans(index: dict) -> int:
    glossed = {rid for entry in index["glossary"] for rid in entry["cites"]}
    orphans = [
        rule
        for rule in index["rules"].values()
        if not rule["cited_by"] and rule["id"] not in glossed
    ]

    if not orphans:
        print("Every rule is cited by another rule or by the glossary.")
        return 0

    print(f"{len(orphans)} rule(s) cited by nothing and defined in no glossary entry.")
    print("Standalone is legitimate; disconnected is a defect. This is a shortlist,")
    print("not a verdict.\n")
    for rule in sorted(orphans, key=lambda r: (r["doc"], r["line"])):
        print(f"  {rule['id']:10s} {rule['doc']}:{rule['line']:<5d} {rule['title']}")
    return 0


def cmd_glossary(index: dict) -> int:
    """Glossary entries that point at no rule.

    `.claude/agents/ruleset-auditor.md` expects each entry to cite its owning
    document and rule ID. Twelve of forty-seven do not, which is why this
    reports rather than fails: a gate that is red on arrival gets switched off,
    and this is pre-existing debt that a tooling change has no business fixing
    in passing — correcting the ruleset takes an OpenSpec proposal.

    An entry citing an ID that does not exist is *not* checked here, because
    `scripts/lint_ruleset.py` already checks it across every file in docs/,
     14-glossary.md included, and a second implementation would drift.
    """
    uncited = [entry for entry in index["glossary"] if not entry["cites"]]

    print(f"{len(index['glossary'])} glossary entries, {len(uncited)} citing no rule.\n")
    for entry in uncited:
        print(f"  14-glossary.md:{entry['line']:<5d} {entry['term']}")

    if uncited:
        print("\nAn entry a reader cannot trace to a rule is a definition with no owner.")
    return 0


def _rules_held(outline: list[dict], position: int, level: int) -> int:
    """How many rules sit under `outline[position]`, a non-rule section at
    `level`: every following entry at a deeper level, up to the next one at
    `level` or shallower.
    """
    count = 0
    for entry in outline[position + 1:]:
        if entry["level"] <= level:
            break
        if entry["rule_id"] is not None:
            count += 1
    return count


def cmd_doc(index: dict, name: str) -> int:
    document = index["documents"].get(name)
    if document is None:
        print(f"No document {name}. Have: {', '.join(sorted(index['documents']))}", file=sys.stderr)
        return 1

    outline = document["outline"]
    # A chapter is a level-1, non-rule section holding at least one rule —
    # `system/documentation-standards.md`'s definition. A level-1 section
    # holding none (Purpose, Summary, ...) is prose, not a chapter, and does
    # not count.
    chapters = sum(
        1 for position, entry in enumerate(outline)
        if entry["level"] == 1 and entry["rule_id"] is None
        and _rules_held(outline, position, 1)
    )
    print(f"{name} — {len(document['rules'])} rule(s), {chapters} chapter(s)\n")

    for position, entry in enumerate(outline):
        indent = "  " if entry["level"] == 1 else "    "
        # `#`/`##` states the heading level, exactly as `scripts/parse_ruleset.py`
        # prints it and as the documents themselves are written — a rule inside a
        # chapter is `##`, everything else here is `#`. The two tools are meant to
        # agree on this column; the line/inbound/summary that follow are this
        # tool's own addition, not a disagreement with it.
        prefix = "#" * entry["level"]

        if entry["rule_id"] is None:
            held = _rules_held(outline, position, entry["level"])
            marker = f"[{held} rules]" if held else "[prose]"
            print(f"{indent}{prefix} {entry['title']}  {marker}")
            continue

        rule = index["rules"][entry["rule_id"]]
        inbound = len(rule["cited_by"])
        print(f"{indent}{prefix} {entry['rule_id']:10s} {entry['line']:<5d} {entry['title']}  ({inbound} inbound)")
        if rule["summary"]:
            print(f"{indent}  {rule['summary']}")
    return 0


# arity: 0 takes none, 1 takes exactly one, "+" takes one or more and is run
# once per argument. The variadic forms exist so that reading seven rules is one
# command rather than a shell loop — a loop needs `$id`, and a command carrying a
# shell expansion cannot be matched by any permission rule, so it prompts every
# time however the allowlist is written. Removing the reason to write the loop is
# the only fix that survives.
COMMANDS = {
    "show": (cmd_show, "+"),
    "refs": (cmd_refs, "+"),
    "neighbors": (cmd_neighbors, "+"),
    "touched": (cmd_touched, "+"),
    "orphans": (cmd_orphans, 0),
    "glossary": (cmd_glossary, 0),
    "doc": (cmd_doc, "+"),
}

SEPARATOR = "=" * 72


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COMMANDS:
        print(__doc__.strip())
        return 1

    handler, arity = COMMANDS[argv[0]]
    args = argv[1:]
    index = load_index()

    if arity == 0:
        if args:
            print(f"{argv[0]} takes no arguments, got {len(args)}.", file=sys.stderr)
            return 1
        return handler(index)

    if not args:
        print(f"{argv[0]} needs at least one argument.", file=sys.stderr)
        return 1

    status = 0
    for position, argument in enumerate(args):
        if position:
            print(f"\n{SEPARATOR}\n")
        try:
            status |= handler(index, argument)
        except SystemExit as exit_signal:
            # `need()` exits on an unknown rule. With several arguments, report it
            # and carry on: stopping on the third of seven wastes the other four.
            status |= exit_signal.code or 1
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
