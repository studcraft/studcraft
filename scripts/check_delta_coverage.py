#!/usr/bin/env python3
"""Catch spec-delta drift at pull-request time instead of at archive time.

`openspec archive` refuses a `## MODIFIED Requirements` block that omits a
scenario the living spec already has, because applying it would silently drop
that scenario. That refusal is correct, but it fires whenever someone next
runs the archive batch — which may be weeks after the proposal merged, long
after the person who could explain the delta has moved on. This repo hit that
exactly once and it cost two dedicated PRs to untangle (see
`system/workflow.md`, Archiving).

`openspec validate` does not catch it: it checks that a change parses and is
structurally complete, not that its deltas are coherent with what is currently
in `openspec/specs/`. Verified by deliberately stripping a scenario from a
delta — validate passed.

This script runs the archive-time coherence check early, on every PR:

  For every `## MODIFIED Requirements` block in every unarchived change, if
  the targeted requirement already exists in the living spec, every scenario
  the living spec has for it must also appear in the delta block.

Renaming a scenario therefore fails here rather than at archive time. That is
intended: a scenario heading is an identifier. When its content becomes wrong,
keep the name and correct the body — the same stable-identifier convention
MEL-010 and CBT-011 follow in the ruleset itself.

Exit code 0 if every delta is coherent (or there are no deltas), 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import CHANGES_DIR, SPECS_DIR, unarchived_changes  # noqa: E402

OP_HEADER_RE = re.compile(r"^## (ADDED|MODIFIED|REMOVED|RENAMED) Requirements\s*$", re.M)
REQ_RE = re.compile(r"^### Requirement:\s*(.+?)\s*$", re.M)
SCENARIO_RE = re.compile(r"^#### Scenario:\s*(.+?)\s*$", re.M)


def modified_blocks(text: str) -> dict[str, set[str]]:
    """Requirement name -> scenario names, for MODIFIED sections only."""
    out: dict[str, set[str]] = {}
    sections = list(OP_HEADER_RE.finditer(text))
    for i, m in enumerate(sections):
        if m.group(1) != "MODIFIED":
            continue
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        body = text[m.end():end]
        reqs = list(REQ_RE.finditer(body))
        for j, r in enumerate(reqs):
            r_end = reqs[j + 1].start() if j + 1 < len(reqs) else len(body)
            # Merged, not replaced: one delta file may carry two MODIFIED
            # sections naming the same requirement, and assignment would drop
            # the scenarios of the first — the exact silent deletion this
            # script exists to catch.
            out.setdefault(r.group(1), set()).update(
                SCENARIO_RE.findall(body[r.start():r_end])
            )
    return out


def living_requirements(text: str) -> dict[str, set[str]]:
    """Requirement name -> scenario names, for a whole living spec file."""
    out: dict[str, set[str]] = {}
    reqs = list(REQ_RE.finditer(text))
    for j, r in enumerate(reqs):
        end = reqs[j + 1].start() if j + 1 < len(reqs) else len(text)
        out[r.group(1)] = set(SCENARIO_RE.findall(text[r.start():end]))
    return out


def main() -> int:
    if not CHANGES_DIR.exists():
        print("No openspec/changes/ directory. Nothing to check.")
        return 0

    errors: list[str] = []
    checked = 0

    for name in unarchived_changes():
        change_dir = CHANGES_DIR / name
        specs_root = change_dir / "specs"
        if not specs_root.exists():
            continue

        for delta_file in sorted(specs_root.glob("*/spec.md")):
            capability = delta_file.parent.name
            living_file = SPECS_DIR / capability / "spec.md"
            deltas = modified_blocks(delta_file.read_text())
            if not deltas:
                continue
            if not living_file.exists():
                # MODIFIED against a capability that does not exist yet. Not this
                # script's problem — openspec archive reports it, and the change
                # may legitimately depend on another landing first.
                continue

            living = living_requirements(living_file.read_text())
            for req_name, delta_scenarios in deltas.items():
                checked += 1
                if req_name not in living:
                    continue
                missing = living[req_name] - delta_scenarios
                if missing:
                    errors.append(
                        f"{change_dir.name} / {capability} / "
                        f'"{req_name}"\n'
                        + "".join(f"    missing scenario: {s}\n" for s in sorted(missing))
                    )

    if errors:
        print("Spec delta would drop scenarios the living spec already has.\n")
        for e in errors:
            print("  " + e)
        print(
            "A MODIFIED block replaces the whole requirement, so any scenario it\n"
            "omits is deleted at archive time. If you renamed a scenario, keep the\n"
            "original heading and correct its body instead — a scenario name is an\n"
            "identifier. If the living spec has drifted from docs/, refresh the\n"
            "delta against the rule as it now reads.\n\n"
            "See system/workflow.md (Archiving) for why this is checked here rather\n"
            "than being discovered weeks later during an archive batch."
        )
        return 1

    print(f"Checked {checked} MODIFIED requirement(s) across all changes. No dropped scenarios.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
