#!/usr/bin/env python3
"""What a review of a change must read, and the checklist it must answer.

A review is judgement, and judgement is not scriptable. Everything around it
is: which rules to read, which Summaries and glossary entries drifted with
them, and which questions the answer has to cover. Deciding those per
invocation is what made two reviews of one change read different text and
report different things.

    python3 scripts/review_scope.py <change-name>

Prints the scope and the checklist. It reports; it judges nothing and it
answers nothing. `system/proposal-review.md` owns the checklist items and this
prints them so an auditor fills verdicts in rather than reconstructing the list.

Takes as many change names as you like, and runs once per name.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, DOCS_DIR, REPO_ROOT, RULE_ID_RE  # noqa: E402

INDEX_PATH = REPO_ROOT / ".studcraft" / "index.json"
SEPARATOR = "=" * 72

# `system/proposal-review.md` states each of these and why it recurs. Held here
# as the list an auditor must return a verdict on, so that "what I checked and
# found clean" is enumerable rather than narrative. Adding a failure class
# there means adding a line here.
CHECKLIST = [
    "Contradicts a rule that already shipped, in a document the change does not cite",
    "Dangling cross-reference — a name that exists in no artifact",
    "A retired rule ID still cited from outside docs/",
    "A changed rule's own ID never grepped, only the ones it retired",
    "A duplicate in a document that defines no rules",
    "An absolute claim left unqualified by a later exception",
    "The same rule asserted twice in two documents",
    "A task citing a spec section that was never written",
    "Requirement order not matching the described sequence",
    "Every delta describes docs/ as it now reads, not as it read when written",
    "Every file outside docs/ the change carries is named in design.md",
    "The Summary of every document touched",
    "The glossary entry of every term touched",
    "A stated count recomputed rather than trusted",
    "A number checked against every number it can be compared with",
    "A cap added where the model already bounds the value",
    "The six principles that catch most defects here",
]


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


def named_rules(change_dir: Path, index: dict) -> dict[str, set[str]]:
    """Every rule the change's own artifacts name, and where each is named."""
    found: dict[str, set[str]] = {}
    for path in sorted(change_dir.rglob("*.md")):
        for rule_id in RULE_ID_RE.findall(path.read_text()):
            if rule_id in index["rules"]:
                found.setdefault(rule_id, set()).add(path.relative_to(change_dir).as_posix())
    return found


def dead_ids(change_dir: Path, index: dict) -> list[str]:
    """Rule IDs the change names that do not exist in docs/.

    A change that retires a rule keeps naming it — in its own prose, and in the
    `tasks.md` that removed it. Those are the IDs worth a repository-wide grep,
    because the linter reads `docs/` and `assets/IMAGES.md` only and the index
    is built from `docs/`: neither can see `CODE_OF_DESIGN.md`, `README.md`,
    `system/` or `scripts/` still citing one.

    An ID under a prefix no document uses is an illustration — `AAA-001`,
    `ABC-001` — and is dropped: `system/documentation-standards.md` (Naming
    Conventions) mandates that form precisely so it names nothing.

    **An invented number under a real prefix survives the filter**, and that is
    deliberate. `VEH-099` is the third sanctioned illustration form, but so is
    every genuinely retired number, and no rule tells them apart. Two lines of
    noise cost a glance; dropping a real retirement costs what this section
    exists to prevent.
    """
    live_prefixes = {
        prefix
        for document in index["documents"].values()
        for prefix in document["prefixes"]
    }

    named: set[str] = set()
    for path in sorted(change_dir.rglob("*.md")):
        named.update(RULE_ID_RE.findall(path.read_text()))

    return sorted(
        name
        for name in named
        if name not in index["rules"] and name.rsplit("-", 1)[0] in live_prefixes
    )


def delta_files(change_dir: Path) -> list[str]:
    """Every spec delta the change ships, live and superseded.

    A delta is written against `docs/` at proposal time and archived weeks
    later, by which point `docs/` has moved — `system/workflow.md` ("Refresh
    every delta against `docs/` before archiving"). Nothing else lists these,
    so nothing else prompts anyone to re-read them.
    """
    found = [
        path.relative_to(change_dir).as_posix()
        for directory in ("specs", "specs-superseded")
        for path in sorted((change_dir / directory).rglob("*.md"))
    ]
    return found


def scope(change: str, index: dict) -> int:
    change_dir = CHANGES_DIR / change
    if not change_dir.is_dir():
        available = sorted(
            p.name for p in CHANGES_DIR.iterdir() if p.is_dir() and p.name != "archive"
        )
        print(f"No change {change}. Unarchived: {', '.join(available) or 'none'}", file=sys.stderr)
        return 1

    named = named_rules(change_dir, index)

    # A rule that cites a changed rule may read differently once it changed,
    # and nothing in the change reveals it. That is the half a prompt forgets.
    citers = {
        citer
        for rule_id in named
        for citer in index["rules"][rule_id]["cited_by"]
        if citer not in named
    }

    documents = sorted({index["rules"][rule_id]["doc"] for rule_id in named})

    entries = [
        entry
        for entry in index["glossary"]
        if any(cited in named for cited in entry["cites"])
    ]

    deltas = delta_files(change_dir)
    dead = dead_ids(change_dir, index)

    print(f"# Review scope — {change}\n")

    if not named:
        print("Names no rule that exists in docs/. Read the change's own artifacts,")
        print("then answer the checklist below against them.\n")
    else:
        print(f"## Read in full — {len(named)} rule(s) the change names\n")
        print("Named, not necessarily edited: a rule a `design.md` argues against")
        print("is here too, and reading it is how you find out which it was.\n")
        for rule_id in sorted(named, key=lambda r: (index["rules"][r]["doc"], index["rules"][r]["line"])):
            rule = index["rules"][rule_id]
            print(f"  {rule_id:10s} {rule['doc']}:{rule['line']:<5d} {rule['title']}")
            print(f"             named in: {', '.join(sorted(named[rule_id]))}")

        print(f"\n## Read also — {len(citers)} rule(s) that cite one of those\n")
        if citers:
            for rule_id in sorted(citers, key=lambda r: (index["rules"][r]["doc"], index["rules"][r]["line"])):
                rule = index["rules"][rule_id]
                print(f"  {rule_id:10s} {rule['doc']}:{rule['line']:<5d} {rule['title']}")
        else:
            print("  none")

        print(f"\n## Summaries — {len(documents)} document(s) whose rules changed\n")
        for name in documents:
            print(f"  {name}  # Summary")

        print(f"\n## Glossary — {len(entries)} entry pointing at a changed rule\n")
        if entries:
            for entry in entries:
                print(f"  14-glossary.md:{entry['line']:<5d} {entry['term']}")
        else:
            print("  none")

    print(f"\n## Deltas — {len(deltas)} spec delta(s) this change ships\n")
    if deltas:
        print("Written against docs/ at proposal time and archived later, by which")
        print("point docs/ has moved. Read each beside the rule it describes.\n")
        for name in deltas:
            print(f"  {name}")
    else:
        print("  none")

    print(f"\n## Retired IDs — {len(dead)} named here and absent from docs/\n")
    if dead:
        print("Grep the whole repository for each. The linter reads docs/ and")
        print("assets/IMAGES.md only, and the index is built from docs/, so neither")
        print("sees CODE_OF_DESIGN.md, README.md, system/ or scripts/ still citing one.")
        print("A high number under a real prefix is an illustration, not a retirement —")
        print("it is listed because no rule tells the two apart.\n")
        for name in dead:
            print(f"  git grep -n \"{name}\"")
    else:
        print("  none")

    print(f"\n## Checklist — answer every line\n")
    print("CLEAN, FINDING or N/A with the reason. No line is skipped in silence:")
    print("an item nobody answered is indistinguishable from an item nobody checked.\n")
    for number, item in enumerate(CHECKLIST, start=1):
        print(f"  {number:2d}. [ ] {item}")

    print("\nA finding names where, what, why it is a defect and what would fix it.")
    print("One that cannot name what it violates is a preference — drop it, or")
    print("label it an observation. system/proposal-review.md has the whole of it.")
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip())
        return 1

    index = load_index()
    status = 0
    for position, change in enumerate(argv):
        if position:
            print(f"\n{SEPARATOR}\n")
        status |= scope(change, index)
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
