#!/usr/bin/env python3
"""Place the images `assets/IMAGES.md` specifies, in the sections that specify them.

That file has named example images since it was added, and named where each one
belongs: a `## docs/<file>.md` heading, and a rule or heading inside it. What it
never had was anything that acts on it. Twenty images were specified and none
was placed, because placing one was a job nobody had written down.

It is a mechanical job. Which rule, which file, which line — every answer is
already in the index, which is the shape of work `scripts/apply_tasks.py` exists
for elsewhere in this repository: the deciding is a person's, the transcribing
is not.

## One rule

    An embed exists in docs/ exactly when the file exists in assets/images/
    and assets/IMAGES.md lists it for that section.

Both halves fail differently and both are reported:

  - **listed and drawn, but not embedded** — the image exists and no reader of
    the rule ever sees it;
  - **embedded, but not drawn** — a broken image in the rulebook;
  - **embedded, but not listed** — an image whose argument for existing was
    never written. `assets/IMAGES.md` keeps entries selective on purpose, and
    the *Why text alone is not enough* column is what a reviewer reads when
    deciding whether one belongs at all. An embed with no entry skipped that.

A drawn file that no entry lists is reported the same way, since it is the same
gap seen from the disk.

## Where an image goes

After the section's own prose, before its first sub-heading — **not** at the end
of its span. A `#` heading that groups rules ends after the last of them, and an
image belonging to the group would land under a rule it does not illustrate.
For a leaf rule the two are the same line.

Several entries may name one section. They are placed in the order the table
lists them: ordering entries is an editorial act, and it belongs to whoever
edits the index.

## What it refuses, and why

`--write` edits `docs/`, and `.claude/rules/tooling.md` is explicit that a
`PreToolUse` hook sees `Write` and `Edit` but not a script writing through
`Bash`. So this restates for itself what the hook would have refused:

  - **`main` and `develop`.** No document change anywhere in this repository is
    committed to either directly (`system/workflow.md`, Git Workflow).
  - **A branch that is not an unarchived change.** Editing `docs/*.md` requires
    a proposal on a branch named for it (`system/repository-strategy.md`,
    Branch Naming). `apply_tasks.py` compares against the change it was handed;
    this script is handed none, so it requires the branch to name one.

`--check` writes nothing and refuses nothing. It is what runs in CI, where the
branch is a pull-request head and reporting is the whole job.

Usage:

    python3 scripts/insert_images.py            report, write nothing
    python3 scripts/insert_images.py --check    the same, said out loud
    python3 scripts/insert_images.py --write    place, re-place and remove

Exit code 0 when `docs/`, `assets/images/` and `assets/IMAGES.md` agree, 1
otherwise. After a successful `--write`, a second run exits 0.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import images_index  # noqa: E402
from repo import DOCS_DIR, REPO_ROOT, git, unarchived_changes  # noqa: E402
from ruleset_ast import Section, parse_text  # noqa: E402

# An embed as this script writes it, and as it recognises one already placed:
# a whole line, holding only the image. The path is what identifies it — alt
# text is generated and may be rewritten, so it cannot be the identity.
EMBED_RE = re.compile(r"^!\[[^\]]*\]\((\.\./assets/images/[^)]+)\)\s*$")

# Where the rejected candidates start. An embed whose rule is below this line
# was considered and turned down once, and re-proposing it has a ritual of its
# own — struck through, marked, with what changed.
REJECTED_HEADING = "Rules considered and rejected"


class Finding:
    """One disagreement between the three places an image lives."""

    def __init__(self, where: str, summary: str, remedy: str = ""):
        self.where = where
        self.summary = summary
        self.remedy = remedy

    def render(self) -> str:
        text = f"{self.where}: {self.summary}"
        if self.remedy:
            text += "\n" + "\n".join(f"  {line}" for line in self.remedy.splitlines())
        return text


def embed_line(entry: images_index.Entry) -> str:
    """The one line this script writes for an entry.

    The path is relative because `docs/` is read as Markdown from inside its own
    directory, on GitHub and in any renderer; an absolute repository path
    resolves for neither.
    """
    return f"![{entry.alt}](../{entry.path})"


def own_region(section: Section) -> tuple[int, int]:
    """The lines a section owns itself, as (start, end), 1-indexed inclusive.

    Everything after its heading and before its first child's. `Section.line_end`
    covers descendants, which is right for citation scanning and wrong here.
    """
    start = section.line + 1
    end = section.children[0].line - 1 if section.children else section.line_end
    return start, max(start - 1, end)


def resolve(document, anchor: str) -> Section | None:
    """The section an entry's Rule cell names, or None when nothing matches it.

    A rule ID matches the rule; anything else matches a heading by its text.
    Two headings of one title in one document would be ambiguous, so that
    returns None as well and is reported rather than guessed at.
    """
    matches = [
        section for section in document.root.walk()
        if section.rule_id == anchor or (section.level and section.title == anchor)
    ]
    return matches[0] if len(matches) == 1 else None


def strip_embeds(region: list[str]) -> tuple[list[str], list[str]]:
    """The region without its embed lines, and the embed lines removed.

    An embed is written as a blank line and then the image, so removing one
    takes the blank that introduced it as well. Nothing else about the region's
    whitespace is touched: a general "collapse blank runs" pass here rewrote
    four documents this change never proposed to edit, silently, because every
    document with an entry goes through this function whether an image lands in
    it or not.
    """
    kept: list[str] = []
    removed: list[str] = []

    for line in region:
        if EMBED_RE.match(line):
            removed.append(line)
            if kept and not kept[-1].strip():
                kept.pop()
            continue
        kept.append(line)

    return kept, removed


def rebuild(region: list[str], entries: list[images_index.Entry]) -> list[str]:
    """A section's own lines, with exactly the embeds its drawn entries call for.

    The trailing run of blanks and thematic breaks is held back and re-attached,
    so an image lands under the prose rather than under the `---` that closes
    the rule.
    """
    kept, _ = strip_embeds(region)
    if not entries:
        return kept

    tail = len(kept)
    while tail and (not kept[tail - 1].strip() or kept[tail - 1].strip() == "---"):
        tail -= 1

    placed: list[str] = []
    for entry in entries:
        placed.extend(("", embed_line(entry)))

    return kept[:tail] + placed + kept[tail:]


def rejected_at(index_text: str, anchor: str) -> int | None:
    """The line where the rejected list turns this rule down, if it does."""
    lines = index_text.splitlines()
    start = next(
        (number for number, line in enumerate(lines) if REJECTED_HEADING in line),
        None,
    )
    if start is None:
        return None
    for number in range(start, len(lines)):
        if anchor in lines[number]:
            return number + 1
    return None


def row_for(path: str, anchor: str, doc: str) -> str:
    """The `assets/IMAGES.md` row that would make an embed legitimate."""
    return (
        f"Add to assets/IMAGES.md, under ## docs/{doc}:\n"
        f"| {anchor} | `{path}` | TODO: what it must show | "
        f"TODO: why text alone is not enough |"
    )


def plan_document(doc: str, text: str, entries: list[images_index.Entry],
                  index_text: str) -> tuple[str, list[Finding]]:
    """This document as it should read, and every disagreement found on the way."""
    document = parse_text(doc, text)
    lines = text.splitlines()
    findings: list[Finding] = []

    wanted: dict[int, list[images_index.Entry]] = {}
    for entry in entries:
        section = resolve(document, entry.anchor)
        if section is None:
            findings.append(Finding(
                f"assets/IMAGES.md:{entry.lineno}",
                f"no single section in docs/{doc} is {entry.anchor!r}, so the image "
                f"has nowhere to go",
            ))
            continue
        if entry.exists:
            wanted.setdefault(section.line, []).append(entry)

    sections = sorted(
        (section for section in document.root.walk() if section.level),
        key=lambda section: section.line,
        reverse=True,
    )

    for section in sections:
        start, end = own_region(section)
        region = lines[start - 1:end]
        calls_for = wanted.get(section.line, [])
        _, present = strip_embeds(region)

        present_paths = {EMBED_RE.match(line).group(1)[len("../"):] for line in present}
        wanted_paths = {entry.path for entry in calls_for}

        for path in sorted(present_paths - wanted_paths):
            anchor = section.rule_id or section.title
            listed = any(entry.path == path for entry in entries)
            if listed:
                summary = f"{path} is embedded and listed, but is not in assets/images/"
                remedy = "Draw it, or remove the entry and this embed together."
            else:
                summary = f"{path} is embedded but no entry in assets/IMAGES.md lists it"
                remedy = row_for(path, anchor, doc)
                rejected = rejected_at(index_text, anchor)
                if rejected:
                    remedy += (
                        f"\n{anchor} is in the rejected list (assets/IMAGES.md:{rejected}). "
                        f"Reclassify it as assets/IMAGES.md requires — struck through, "
                        f"marked, and saying what changed."
                    )
            findings.append(Finding(f"docs/{doc}:{section.line}", summary, remedy))

        for entry in calls_for:
            if entry.path not in present_paths:
                findings.append(Finding(
                    f"docs/{doc}:{section.line}",
                    f"{entry.path} is drawn and listed, but {section.rule_id or section.title} "
                    f"does not embed it",
                    "python3 scripts/insert_images.py --write",
                ))

        rebuilt = rebuild(region, calls_for)
        if rebuilt != region:
            lines[start - 1:end] = rebuilt

    # Alt text produces no finding of its own. It is generated from the entry,
    # so a difference is one definition catching up with itself rather than two
    # intentions disagreeing — `--write` rewrites it and the diff shows it.
    #
    # The trailing newline is whatever the file already had. Seven documents in
    # docs/ end without one, and "fix" them here and this script writes to files
    # it was not asked to touch — which is a docs/ edit no proposal describes.
    rebuilt = "\n".join(lines)
    return (rebuilt + "\n" if text.endswith("\n") else rebuilt), findings


def orphan_files(entries: list[images_index.Entry]) -> list[Finding]:
    """Every drawn file no entry names."""
    listed = {entry.path for entry in entries}
    findings: list[Finding] = []

    for path in images_index.drawn_files():
        relative = path.relative_to(REPO_ROOT).as_posix()
        if relative in listed:
            continue
        findings.append(Finding(
            relative,
            "is in assets/images/ and no entry in assets/IMAGES.md names it",
            "Add its entry, or delete the file. assets/IMAGES.md is the only "
            "place an image's specification is written.",
        ))

    return findings


def branch_refusal() -> str | None:
    """Why this branch must not write to `docs/`, or None.

    `apply_tasks.branch_refusal` compares the branch against the change it was
    told to apply. This script is told nothing, so it asks the weaker question
    the gate actually asks: is this branch a change that exists?
    """
    code, branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0:
        return "could not read the current branch"

    if branch in ("main", "develop"):
        return (
            f"on {branch}. No document change anywhere in this repository is "
            f"committed to {branch} directly — system/workflow.md (Git Workflow)."
        )

    if branch not in unarchived_changes():
        return (
            f"on branch {branch}, which names no unarchived change. Editing "
            f"docs/*.md needs a proposal on a branch named for it — "
            f"system/repository-strategy.md (Branch Naming)."
        )

    return None


def silent_rewrite(doc: str, found: list[Finding]) -> Finding | None:
    """A rewrite of `doc` that none of `found` accounts for, as a finding.

    `--check` is only a guard if it is green exactly when `--write` is a no-op.
    An early version normalised whitespace on its way through every document
    with an entry, and `--check` reported none of it: the gate was green on a
    tree where `--write` edited four documents no proposal named. What produced
    a rewrite is not the question — that it was not reported is.
    """
    if any(finding.where.startswith(f"docs/{doc}") for finding in found):
        return None

    return Finding(
        f"docs/{doc}",
        "would be rewritten with nothing to report. Placing an image is not the "
        "cause, so this is a document the script was not asked to touch",
    )


def survey() -> tuple[list[images_index.Entry], list[Finding], dict[Path, str]]:
    """Every entry, everything wrong, and the documents that would change."""
    entries = images_index.entries()
    index_text = images_index.IMAGES_INDEX.read_text() if entries else ""

    findings = orphan_files(entries)
    rewrites: dict[Path, str] = {}

    by_doc: dict[str, list[images_index.Entry]] = {}
    for entry in entries:
        by_doc.setdefault(entry.doc, []).append(entry)

    for doc, group in sorted(by_doc.items()):
        path = DOCS_DIR / doc
        if not path.is_file():
            findings.append(Finding(
                f"assets/IMAGES.md:{group[0].lineno}",
                f"section names docs/{doc}, which does not exist",
            ))
            continue

        text = path.read_text()
        rebuilt, found = plan_document(doc, text, group, index_text)
        findings.extend(found)
        if rebuilt != text:
            rewrites[path] = rebuilt

        if rebuilt != text:
            unexplained = silent_rewrite(doc, found)
            if unexplained:
                findings.append(unexplained)

    return entries, findings, rewrites


def main(argv: list[str]) -> int:
    mode = argv[0] if argv else "--check"
    if mode not in ("--check", "--write") or len(argv) > 1:
        print(__doc__.split("Usage:")[1].strip(), file=sys.stderr)
        return 2

    entries, findings, rewrites = survey()

    for finding in findings:
        print(finding.render())

    if mode == "--write" and rewrites:
        refusal = branch_refusal()
        if refusal:
            print(f"\nRefusing: {refusal}", file=sys.stderr)
            return 1

        for path, text in rewrites.items():
            path.write_text(text)
        names = ", ".join(sorted(path.name for path in rewrites))
        print(f"\nWrote {len(rewrites)} document(s): {names}")

        # What is left is what writing could not fix — a file nobody listed, an
        # entry pointing at a section that is not there. Re-surveying says so
        # rather than leaving the exit code to speak for a run that half worked.
        entries, findings, rewrites = survey()
        for finding in findings:
            print(finding.render())

    if not findings:
        drawn = sum(1 for entry in entries if entry.exists)
        print(
            f"Checked {len(entries)} image entr(ies), {drawn} drawn. "
            f"docs/, assets/images/ and assets/IMAGES.md agree."
        )
        return 0

    print(f"\n{len(findings)} disagreement(s).", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
