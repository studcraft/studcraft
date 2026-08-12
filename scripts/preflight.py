#!/usr/bin/env python3
"""Run, in one command, every gate that can be answered locally before a push.

Some checks read nothing but the branch name and the list of changed files, so
they can be answered here instead of a minute after a push. Others are scripts
this repository already owns. Two need something that may not be installed —
the `openspec` CLI and pytest — and are reported as skipped when it is missing.
`gh api repos/studcraft/studcraft/branches/main/protection` says which of the
mirrored gates actually block a merge.

**The gate is authoritative; this is a mirror.** `.claude/rules/tooling.md`
states that a local check and a CI gate are not alternatives — the gate runs
for everyone and is what blocks a merge. This exists to move the same refusal
earlier, and it adds no rule of its own. When a workflow under
`.github/workflows/` changes, the mirror here has to be checked against it;
where the two disagree, the workflow wins.

What it runs:

  1. scripts/lint_ruleset.py          (Docs ruleset linter)
  2. scripts/check_delta_coverage.py  (OpenSpec change is coherent, part 2)
  3. scripts/check_task_anchors.py    (no CI gate — a proposal defect, caught here)
  4. scripts/check_id_stability.py    (no CI gate — IDs are permanent across revisions)
  5. scripts/check_todo_quotes.py     (no CI gate — TODO.md must not misquote docs/)
  6. openspec validate                (OpenSpec change is coherent, part 1)
  7. pytest                           (Tests — skipped when pytest is absent)
  8. scripts/build_index.py           (no CI gate — keeps the query index current)
  9. branch name                      (Branch name follows the convention)
 10. CHANGELOG.md untouched by a ruleset PR
                                      (Docs must not edit CHANGELOG.md directly)
 11. one complete proposal per change  (Docs require OpenSpec proposal)
 12. archive is separate from apply    (OpenSpec archive must be separate from apply)

Five of those mirror no gate at all. Anchor uniqueness is a defect CI cannot
see — by the time a change is applied wrongly, the diff looks deliberate.
ID stability needs a base revision to compare against, which a single-revision
linter has not got. A TODO.md quote drifts when the rule it quotes is reworded,
so the branch that breaks it is a ruleset branch that never touches TODO.md.
The index is a local cache with nothing to enforce, and the tests cover
`scripts/` rather than the ruleset. All of them belong to the moment before a
push rather than after one, which is what this script is.

Checks 9-12 compare the working tree against the merge base with `origin/main`,
which is the closest local equivalent of the base/head pair a pull request
gives CI. Uncommitted work is included: the point is to fail before the commit,
not after it.

Exit code 0 when every check passes or is skipped, 1 otherwise. Each failing
check is named, so the output says which gate would go red rather than only
that something would.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import REPO_ROOT, git  # noqa: E402

PASS, FAIL, SKIP = "PASS", "FAIL", "SKIP"

RELEASE_BRANCH_RE = re.compile(r"^release/v\d+\.\d+\.\d+$")
ARCHIVE_BRANCH_RE = re.compile(r"^archive/[a-z0-9][a-z0-9._-]*$")
WORKING_BRANCH_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
CHANGE_DIR_RE = re.compile(r"^openspec/changes/([^/]+)")

PROPOSAL_ARTIFACTS = ("proposal.md", "design.md", "tasks.md")


class Result:
    """One check's outcome, and the lines it wants printed underneath it."""

    def __init__(self, name: str, status: str, detail: list[str] | None = None):
        self.name = name
        self.status = status
        self.detail = detail or []


def run_script(name: str, script: str) -> Result:
    """Run one of this repository's own checkers and forward its output."""
    proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / script)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    output = (proc.stdout + proc.stderr).strip().splitlines()
    if proc.returncode == 0:
        return Result(name, PASS, output[-1:])
    return Result(name, FAIL, output)


def current_branch() -> str | None:
    code, out = git("rev-parse", "--abbrev-ref", "HEAD")
    return out if code == 0 else None


def changed_files() -> tuple[list[str], str | None]:
    """Every path this branch changes, committed or not.

    The base is the merge base with `origin/main`, which is what the pull
    request would diff against. Falls back to `main` when there is no remote
    ref locally, and reports the failure rather than silently checking nothing.
    """
    base = None
    for ref in ("origin/main", "main"):
        code, out = git("merge-base", ref, "HEAD")
        if code == 0:
            base = out
            break
    if base is None:
        return [], None

    paths: set[str] = set()
    for args in (
        ("diff", "--name-only", base, "HEAD"),
        ("diff", "--name-only", "HEAD"),
        ("diff", "--name-only", "--cached"),
    ):
        code, out = git(*args)
        if code == 0 and out:
            paths.update(out.splitlines())

    code, out = git("ls-files", "--others", "--exclude-standard")
    if code == 0 and out:
        paths.update(out.splitlines())

    return sorted(paths), base


def touched_changes(changed: list[str]) -> list[str]:
    """The OpenSpec change directories this branch touches. `archive` is not one."""
    names = set()
    for path in changed:
        match = CHANGE_DIR_RE.match(path)
        if match and match.group(1) != "archive":
            names.add(match.group(1))
    return sorted(names)


def touches_docs(changed: list[str]) -> bool:
    return any(re.match(r"^docs/.*\.md$", p) for p in changed)


def check_branch_name(branch: str, changed: list[str]) -> Result:
    """Mirror of .github/workflows/branch-naming.yml."""
    name = "Branch name follows the convention"

    if branch in ("main", "develop"):
        return Result(name, SKIP, [f"On {branch}; the convention applies to working branches."])

    if branch.startswith("release/"):
        if not RELEASE_BRANCH_RE.match(branch):
            return Result(name, FAIL, [
                f"{branch} wears the reserved release/ prefix but is not "
                f"release/v<major>.<minor>.<patch>. Three gates key their exemption "
                f"on that exact shape."
            ])
        return Result(name, PASS, ["Release-cut branch; name OK."])

    if branch.startswith("archive/"):
        if not ARCHIVE_BRANCH_RE.match(branch):
            return Result(name, FAIL, [
                f"{branch} wears the reserved archive/ prefix but the rest is empty "
                f"or not lowercase kebab-case."
            ])
        return Result(name, PASS, ["Archive-cut branch; name OK."])

    if not WORKING_BRANCH_RE.match(branch):
        return Result(name, FAIL, [
            f"{branch} is not lowercase kebab-case. No slashes (release/ and "
            f"archive/ are reserved for automation), no underscores, no uppercase. "
            f"See system/repository-strategy.md (Branch Naming)."
        ])

    if not touches_docs(changed):
        return Result(name, PASS, ["Working branch, no docs/*.md changes. Name OK."])

    touched = touched_changes(changed)
    if len(touched) != 1:
        return Result(name, PASS, [
            f"Touches {len(touched)} OpenSpec changes — nothing to match a name "
            f"against here; 'Docs require OpenSpec proposal' owns that error."
        ])

    if branch != touched[0]:
        return Result(name, FAIL, [
            f"Branch {branch} carries the OpenSpec change '{touched[0]}' but is not "
            f"named for it. A proposal lives on its own dedicated branch and takes "
            f"the change's name so the two cannot drift. Rename to {touched[0]}."
        ])

    return Result(name, PASS, [f"Branch matches its OpenSpec change ({touched[0]})."])


def check_changelog(branch: str, changed: list[str]) -> Result:
    """Mirror of .github/workflows/docs-changelog-hands-off.yml.

    The release/v* exemption is deliberately not reimplemented here: verifying
    it means diffing docs/*.md line by line to prove nothing but the
    **Version:** header moved, and a release cut is pushed by a workflow rather
    than typed on a laptop. Report it as skipped so the gap is visible instead
    of looking like a pass.
    """
    name = "Docs must not edit CHANGELOG.md directly"

    if branch.startswith("release/"):
        return Result(name, SKIP, [
            "Release-cut branch; the content-constrained exemption is checked in CI only."
        ])

    if not touches_docs(changed):
        return Result(name, PASS, ["No docs/*.md changes; CHANGELOG.md is free to edit."])

    if "CHANGELOG.md" in changed:
        return Result(name, FAIL, [
            "This branch changes docs/*.md and also edits CHANGELOG.md. CHANGELOG.md "
            "is written only by the Release cut workflow — that is what stops "
            "concurrent proposal branches colliding on it. No branch needs to declare "
            "a bump either: docs/*.md changes default to a minor release. "
            "See system/workflow.md."
        ])

    return Result(name, PASS, ["CHANGELOG.md untouched."])


def check_proposal(branch: str, changed: list[str]) -> Result:
    """Mirror of .github/workflows/docs-require-proposal.yml."""
    name = "Docs require OpenSpec proposal"

    if branch.startswith("release/"):
        return Result(name, SKIP, [
            "Release-cut branch; the content-constrained exemption is checked in CI only."
        ])

    touched = touched_changes(changed)

    if touches_docs(changed) and not touched:
        return Result(name, FAIL, [
            "This branch changes docs/ (the ruleset) but includes no OpenSpec "
            "proposal under openspec/changes/. Ruleset changes are proposed before "
            "they are made — system/workflow.md (OpenSpec Workflow)."
        ])

    if not touched:
        return Result(name, PASS, ["No proposal touched, and no docs/ change."])

    if len(touched) > 1:
        return Result(name, FAIL, [
            f"This branch touches {len(touched)} OpenSpec changes "
            f"({', '.join(touched)}). One proposal per pull request, on its own "
            f"branch — openspec/config.yaml."
        ])

    change_dir = REPO_ROOT / "openspec" / "changes" / touched[0]
    missing = [f for f in PROPOSAL_ARTIFACTS if not (change_dir / f).is_file()]
    if missing:
        return Result(name, FAIL, [
            f"openspec/changes/{touched[0]} is missing: {' '.join(missing)}. A "
            f"proposal needs all three — proposal.md (what and why), design.md (the "
            f"decisions and what was rejected), tasks.md (how to apply it)."
        ])

    return Result(name, PASS, [f"Proposal {touched[0]} is complete."])


def check_archive_separate(branch: str, changed: list[str]) -> Result:
    """Mirror of .github/workflows/openspec-archive-separate.yml."""
    name = "OpenSpec archive must be separate from apply"

    specs = [p for p in changed if p.startswith("openspec/specs/")]

    if branch.startswith("archive/"):
        outside = [p for p in changed if not p.startswith("openspec/")]
        if outside:
            return Result(name, FAIL, [
                f"Archive branch changes files outside openspec/: {', '.join(outside)}. "
                f"Archiving only moves changes and writes capability specs."
            ])
        if touches_docs(changed):
            return Result(name, FAIL, [
                "Archive branch changes docs/*.md. An archive PR touches "
                "openspec/specs/** and openspec/changes/** only."
            ])
        if not specs:
            return Result(name, FAIL, [
                "Archive branch does not touch openspec/specs/. Nothing to archive here."
            ])
        return Result(name, PASS, ["Archive-only branch."])

    if specs:
        return Result(name, FAIL, [
            "This branch changes openspec/specs/ but is not an archive/* branch. "
            "Archiving happens in its own PR, separate from the change that applies "
            "docs/*.md — system/workflow.md (Archiving)."
        ])

    return Result(name, PASS, ["No openspec/specs/ changes outside an archive/* branch."])


def check_openspec_validate() -> Result:
    """Mirror of the first step of .github/workflows/openspec-change-coherent.yml.

    Not `openspec validate --all`: that treats a delta-free change as an error,
    and this repository has legitimate delta-free changes — several docs/
    documents predate the OpenSpec workflow and were never formalised as
    capabilities. So validate the living specs always, and validate a change
    only when it actually ships deltas.
    """
    name = "openspec validate"

    if shutil.which("openspec") is None:
        return Result(name, SKIP, ["openspec is not on PATH (npm i -g @fission-ai/openspec)."])

    targets: list[str] = []
    specs_dir = REPO_ROOT / "openspec" / "specs"
    changes_dir = REPO_ROOT / "openspec" / "changes"

    if specs_dir.is_dir():
        targets += [p.name for p in sorted(specs_dir.iterdir()) if p.is_dir()]
    if changes_dir.is_dir():
        targets += [
            p.name
            for p in sorted(changes_dir.iterdir())
            if p.is_dir() and p.name != "archive" and (p / "specs").is_dir()
        ]

    if not targets:
        return Result(name, PASS, ["Nothing with deltas to validate."])

    failures: list[str] = []
    for target in targets:
        proc = subprocess.run(
            ["openspec", "validate", target],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            failures.append(f"{target}: {(proc.stdout + proc.stderr).strip()}")

    if failures:
        return Result(name, FAIL, failures)
    return Result(name, PASS, [f"Validated {len(targets)} spec(s) and change(s)."])


def check_tests() -> Result:
    """Run the pytest suite over `scripts/`, if pytest is installed.

    pytest is a development dependency (`requirements-dev.txt`) and `scripts/`
    stays stdlib-only, so this is the one check that can be unavailable on a
    working machine. It reports SKIP rather than PASS when it is: a suite that
    did not run is not a suite that passed.
    """
    name = "Tests"

    venv_python = REPO_ROOT / ".venv" / "bin" / "python3"
    interpreter = str(venv_python) if venv_python.is_file() else sys.executable

    probe = subprocess.run(
        [interpreter, "-c", "import pytest"], cwd=REPO_ROOT, capture_output=True
    )
    if probe.returncode != 0:
        return Result(name, SKIP, [
            "pytest is not installed. python3 -m venv .venv && "
            ".venv/bin/pip install -r requirements-dev.txt"
        ])

    proc = subprocess.run(
        [interpreter, "-m", "pytest", "-q"], cwd=REPO_ROOT, capture_output=True, text=True
    )
    output = (proc.stdout + proc.stderr).strip().splitlines()
    if proc.returncode == 0:
        return Result(name, PASS, output[-1:])
    return Result(name, FAIL, output)


def main() -> int:
    results: list[Result] = [
        run_script("Docs ruleset linter", "lint_ruleset.py"),
        run_script("Deltas must not drop scenarios", "check_delta_coverage.py"),
        run_script("Task anchors are unique", "check_task_anchors.py"),
        run_script("Rule IDs are stable", "check_id_stability.py"),
        run_script("TODO.md quotes the ruleset verbatim", "check_todo_quotes.py"),
        check_openspec_validate(),
        check_tests(),
        # Last, and always: rebuilding the index cannot fail the run, but a stale
        # index is a wrong answer given confidently, which is worse than no index.
        run_script("Ruleset index is current", "build_index.py"),
    ]

    branch = current_branch()
    changed, base = changed_files()

    if branch is None or base is None:
        results.append(Result(
            "Branch and diff gates",
            SKIP,
            ["Could not resolve the branch or a merge base with origin/main."],
        ))
    else:
        results += [
            check_branch_name(branch, changed),
            check_changelog(branch, changed),
            check_proposal(branch, changed),
            check_archive_separate(branch, changed),
        ]

    width = max(len(r.name) for r in results)
    print()
    for result in results:
        print(f"  {result.status:<4}  {result.name.ljust(width)}")
        for line in result.detail:
            if result.status == FAIL:
                print(f"        {line}")
    print()

    failed = [r for r in results if r.status == FAIL]
    skipped = [r for r in results if r.status == SKIP]

    if failed:
        print(f"{len(failed)} check(s) would go red: " + ", ".join(r.name for r in failed))
        return 1

    summary = f"All {len(results) - len(skipped)} check(s) pass"
    if skipped:
        summary += f", {len(skipped)} skipped ({', '.join(r.name for r in skipped)})"
    print(summary + ".")
    return 0


if __name__ == "__main__":
    sys.exit(main())
