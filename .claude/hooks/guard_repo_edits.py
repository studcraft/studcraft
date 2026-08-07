#!/usr/bin/env python3
"""PreToolUse guard for Write and Edit, for every agent in this repository.

`system/workflow.md` and `system/repository-strategy.md` state rules that were
trusted rather than enforced locally: branch before editing a document, propose
before editing the ruleset, never hand-edit `CHANGELOG.md` or a `**Version:**`
header, keep archiving off an apply branch. CI enforces all of them, but only
after a push, and only for whoever reads the red check.

This hook refuses the same edits at the moment they are attempted. It does not
invent a rule: every refusal below mirrors a required status check under
`.github/workflows/` and names the document that owns the rule. Where the two
could disagree, the gate is authoritative — see `system/ci-gates.md`.

It fails open. An unrecognised path, a detached HEAD, a missing git binary or
any unexpected exception allows the edit: a guard that blocks work it does not
understand gets switched off, and then nothing is enforced at all.

Input is the PreToolUse JSON payload on stdin. Output is either nothing (allow)
or a deny decision whose reason is what the agent reads instead of the edit.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

VERSION_HEADER = re.compile(r"^\*\*Version:\*\*", re.MULTILINE)

# Anything here is a repository document in the sense system/workflow.md means:
# it may not be changed directly on a long-lived branch.
DOCUMENT_DIRS = {"docs", "system", "openspec", "scripts", ".github", ".claude", "assets", "site"}

# Machine-local permission list. Personal, not a document about the project.
TRUNK_EXEMPT = {".claude/settings.local.json"}


def allow():
    sys.exit(0)


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def git(root, *args):
    result = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, timeout=10
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def active_changes(root):
    changes = root / "openspec" / "changes"
    if not changes.is_dir():
        return []
    return sorted(
        d.name for d in changes.iterdir() if d.is_dir() and d.name != "archive"
    )


def main():
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input") or {}

    raw_path = tool_input.get("file_path")
    if not raw_path:
        allow()

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    root = Path(project_dir) if project_dir else Path(
        git(Path.cwd(), "rev-parse", "--show-toplevel") or "."
    )
    if not (root / "AGENTS.md").is_file():
        allow()  # Not this repository. Not this hook's business.

    target = Path(raw_path)
    if not target.is_absolute():
        target = root / target

    try:
        rel = target.resolve().relative_to(root.resolve())
    except ValueError:
        allow()  # Outside the repository.

    rel_posix = rel.as_posix()
    parts = rel.parts
    top = parts[0] if parts else ""

    new_text = tool_input.get("content") or tool_input.get("new_string") or ""

    branch = git(root, "rev-parse", "--abbrev-ref", "HEAD")
    if not branch or branch == "HEAD":
        allow()  # Detached or unreadable. Fail open.

    on_trunk = branch in ("main", "develop")
    is_release = branch.startswith("release/v")
    is_archive = branch.startswith("archive/")
    is_ruleset = top == "docs" and rel.suffix == ".md"

    # --- Generated output -------------------------------------------------
    if rel_posix.startswith("site/docs/"):
        deny(
            f"{rel_posix} is generated. `scripts/generate_site_docs.py` builds "
            "site/docs/ from docs/, and .gitignore excludes it — an edit here is "
            "overwritten by the next build and never committed. Edit the source "
            "under docs/ instead (which needs an OpenSpec proposal), or change "
            "the generator."
        )

    # --- CHANGELOG.md is release-cut-only ---------------------------------
    if rel_posix == "CHANGELOG.md" and not is_release:
        deny(
            "Nobody edits CHANGELOG.md by hand, agents least of all. It is "
            "written by the Release cut workflow, which computes the version "
            "from git history and rewrites every header in one pass — see "
            "system/documentation-standards.md (Versioning) for why several "
            "branches in flight make a hand-written entry collide. The `Docs "
            "must not edit CHANGELOG.md directly` check blocks the pull request "
            "that tries."
        )

    # --- The ruleset ------------------------------------------------------
    if is_ruleset:
        if on_trunk:
            deny(
                f"You are on `{branch}`. No document change may be committed "
                "directly to main or develop, and a ruleset change additionally "
                "needs its own proposal branch — system/workflow.md (Git "
                "Workflow). Create the branch first: it is named for the "
                "OpenSpec change it carries (system/repository-strategy.md, "
                "Branch Naming), and it is branched from an up-to-date main."
            )

        if is_archive:
            deny(
                f"Branch `{branch}` is an archive batch, and an archive pull "
                "request must not touch docs/*.md. Applying a change and "
                "archiving it are separate pull requests — system/workflow.md "
                "(Archiving). The `OpenSpec archive must be separate from apply` "
                "check rejects this combination."
            )

        if is_release and not VERSION_HEADER.search(new_text):
            deny(
                f"Branch `{branch}` is named like a release cut, and a release "
                f"cut only ever rewrites the `**Version:**` header line — this "
                f"edit to {rel_posix} writes something else. The name alone does "
                "not grant the exemption: `Docs require OpenSpec proposal` reads "
                "the release/v* diff and fails it on any other changed line, "
                "precisely so the prefix cannot be used to land ruleset changes "
                "with no proposal. Open a normal proposal branch instead."
            )

        if VERSION_HEADER.search(new_text) and not is_release:
            deny(
                f"This edit writes a `**Version:**` header into {rel_posix}. "
                "That line belongs to the Release cut, which rewrites it in "
                "every docs/*.md file at once — system/documentation-standards.md "
                "(Versioning). A ruleset change declares nothing about its own "
                "version. If a tasks.md instructed you to bump it, that task is "
                "one the workflow forbids: leave it unticked and report it."
            )

        if not is_release:
            changes = active_changes(root)
            if branch not in changes:
                listed = ", ".join(changes) if changes else "none"
                deny(
                    f"Branch `{branch}` does not name an OpenSpec change, so this "
                    f"edit to {rel_posix} has no proposal behind it. Every ruleset "
                    "change is proposed first, on a branch named exactly for the "
                    "change directory it carries — system/workflow.md (OpenSpec "
                    "Workflow) and system/repository-strategy.md (Branch Naming). "
                    "Both `Docs require OpenSpec proposal` and `Branch name "
                    f"follows the convention` reject this. Active changes: {listed}."
                )

            missing = [
                f for f in ("proposal.md", "design.md", "tasks.md")
                if not (root / "openspec" / "changes" / branch / f).is_file()
            ]
            if missing:
                deny(
                    f"openspec/changes/{branch}/ is missing {', '.join(missing)}. "
                    "A proposal is three artifacts, not a directory with something "
                    "in it: proposal.md (what and why), design.md (the decisions "
                    "and what was rejected), tasks.md (how to apply it, in "
                    "verifiable steps). Write the missing one before editing the "
                    "ruleset — `Docs require OpenSpec proposal` checks for all "
                    "three."
                )

    # --- Shared spec state ------------------------------------------------
    if rel_posix.startswith("openspec/specs/") and not is_archive:
        deny(
            f"openspec/specs/ is written only by the Archive cut, from an "
            f"`archive/*` branch — you are on `{branch}`. `openspec archive` "
            "reads a capability's current spec and writes the result back, so "
            "two branches editing it clobber each other; system/workflow.md "
            "(Archiving) is the reasoning. Run the `Archive cut` workflow "
            "instead of writing this file. The `OpenSpec archive must be "
            "separate from apply` check rejects it either way."
        )

    if is_release and rel_posix != "CHANGELOG.md" and not is_ruleset:
        deny(
            f"Branch `{branch}` is a release cut and may touch CHANGELOG.md and "
            f"the `**Version:**` header in docs/*.md — nothing else, and "
            f"{rel_posix} is neither. `release/` is a reserved prefix, not a "
            "descriptive one (system/repository-strategy.md, Branch Naming); it "
            "is how the automation's own pull request identifies itself to the "
            "gates that would otherwise block it. Use a working branch."
        )

    if is_archive and top not in ("openspec", ""):
        deny(
            f"Branch `{branch}` is an archive batch and may touch openspec/ only "
            f"— {rel_posix} is outside it. system/workflow.md (Archiving), "
            "enforced by `OpenSpec archive must be separate from apply`."
        )

    # --- Everything else, on a long-lived branch --------------------------
    if on_trunk and rel_posix not in TRUNK_EXEMPT:
        if top in DOCUMENT_DIRS or rel.suffix == ".md":
            deny(
                f"You are on `{branch}`. No document change anywhere in this "
                "repository may be committed directly to main or develop — "
                "system/workflow.md (Git Workflow). Non-ruleset files need a "
                "branch but no proposal, so: fetch, pull main --ff-only, then "
                "create a lowercase kebab-case branch off it "
                "(system/repository-strategy.md) and make the edit there."
            )

    allow()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)  # Fail open, deliberately. See the module docstring.
