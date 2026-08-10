#!/usr/bin/env python3
"""Stage named paths, commit, push, and open or update a pull request.

`.claude/agents/git-operator.md` describes a fixed sequence, a list of commands
that must never run, and a set of conditions to stop on. It says of itself: *You
run git. You do not decide anything.* A procedure that decides nothing is a
script, and every rule in that document is expressible as one.

**This does not replace `git-operator`.** The agent still calls it, reads what it
printed, and reports. What moves here is the part that must never vary: the
BLOCKER rules in `system/repository-strategy.md` stop being instructions an agent
is trusted to follow and become things it has no way to do. What stays with the
agent is the part a script is bad at — noticing that something is off in a way
nobody anticipated, and saying so instead of continuing.

Consequences of that split, in order of how much they matter:

- **The forbidden commands are unreachable.** No `--force`, no `--amend`, no
  `rebase`, no `reset --hard`, no `git add -A`. Not because the caller was told
  not to, but because this issues `git add <path>` once per path it was given
  and nothing else.
- **The staged set is verified against the given set** before committing. A
  change to a file nobody named stops the run.
- **Pull requests are opened through `gh api`, not `gh pr create`.** `gh pr edit`
  and parts of `gh pr create` resolve organisation-level fields and fail on a
  token without `read:org` — which is exactly what happened here, mid-run, after
  the commit had already landed. The REST endpoint needs no such scope.

Every step prints what it did. A failure prints why and stops; it never tries a
second approach.

Usage:

    python3 scripts/open_pr.py \\
        --branch <name> \\
        --message-file <path> \\
        --pr-title <title> \\
        --pr-body-file <path> \\
        --path docs/08-vehicles.md --path openspec/changes/x/tasks.md

    --existing-pr <number>   push to an open PR and replace its body instead
                             of opening a new one
    --dry-run                print the plan and touch nothing

## The one thing it will not do

**It cannot update a pull request's description on its own.** `--path` is
required and it stops when nothing is staged, because it commits, and a commit
needs a change. So correcting a description after the fact — the body file was
stale, a reviewer asked for a clarification — is not this script's job, and the
one command for it is:

    gh api repos/<owner>/<repo>/pulls/<number> -X PATCH -F body=@<path>

That is deliberate rather than missing. Adding a body-only mode would give this
script a second purpose and a path through it that skips every guarantee the
rest of the file exists to make — the staged-set check, the branch check, one
commit per run. A separate command that does one thing is the smaller risk.

It was hit once, immediately: a third commit was pushed to an open pull request
with a body file that still described the first two.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PROTECTED_BRANCHES = ("main", "develop")


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True)
    if check and proc.returncode != 0:
        stop(f"`{' '.join(args)}` exited {proc.returncode}:\n{(proc.stdout + proc.stderr).strip()}")
    return proc


def stop(reason: str) -> None:
    """Report and exit. Never repair, never retry, never improvise a fix.

    `system/repository-strategy.md`: a stuck branch costs a minute of somebody's
    attention, and a branch unstuck by guessing costs a rewritten history this
    repository forbids anyone to fix.
    """
    print(f"\nSTOPPED: {reason}", file=sys.stderr)
    sys.exit(1)


def repo_slug() -> str:
    proc = run("git", "remote", "get-url", "origin")
    url = proc.stdout.strip()
    if url.endswith(".git"):
        url = url[: -len(".git")]
    if ":" in url and "//" not in url:
        return url.split(":", 1)[1]
    return "/".join(url.split("/")[-2:])


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--message-file", required=True, type=Path)
    parser.add_argument("--pr-title")
    parser.add_argument("--pr-body-file", type=Path)
    parser.add_argument("--path", action="append", default=[], dest="paths")
    parser.add_argument("--base", default="main")
    parser.add_argument("--existing-pr")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if not args.paths:
        stop("no --path given. Stage paths by name; never a pattern, never everything.")
    if not args.message_file.is_file():
        stop(f"--message-file {args.message_file} does not exist")
    if not args.existing_pr and not (args.pr_title and args.pr_body_file):
        stop("opening a new pull request needs --pr-title and --pr-body-file")
    if args.pr_body_file and not args.pr_body_file.is_file():
        stop(f"--pr-body-file {args.pr_body_file} does not exist")

    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if branch != args.branch:
        stop(f"on branch {branch!r}, was told {args.branch!r}. Not switching branches.")
    if branch in PROTECTED_BRANCHES:
        stop(f"{branch} is protected — no document change may be committed to it directly.")

    for path in args.paths:
        if not (REPO_ROOT / path).exists():
            stop(f"{path} does not exist. Nothing here guesses at what was meant.")

    if args.dry_run:
        print(f"branch      {branch}")
        print(f"base        {args.base}")
        print(f"paths       {len(args.paths)}")
        for path in args.paths:
            print(f"            {path}")
        print(f"pull request {'update #' + args.existing_pr if args.existing_pr else 'open new'}")
        return 0

    for path in args.paths:
        run("git", "add", "--", path)

    staged = [
        line.split("\t", 1)[-1]
        for line in run("git", "diff", "--cached", "--name-only").stdout.splitlines()
        if line.strip()
    ]
    unexpected = sorted(set(staged) - set(args.paths))
    if unexpected:
        stop(
            "the staged set is not the set given. Unexpected: "
            + ", ".join(unexpected)
            + ". Nothing was committed."
        )
    if not staged:
        stop("nothing staged — the named paths hold no changes.")

    print(f"Staged {len(staged)} path(s):")
    for path in staged:
        print(f"  {path}")

    run("git", "commit", "-F", str(args.message_file.resolve()))
    print("\n" + run("git", "show", "--stat", "HEAD").stdout.strip())

    push = run("git", "push", "-u", "origin", branch)
    print("\n" + (push.stdout + push.stderr).strip())

    slug = repo_slug()

    if args.existing_pr:
        if args.pr_body_file:
            run(
                "gh", "api", f"repos/{slug}/pulls/{args.existing_pr}",
                "-X", "PATCH", "-F", f"body=@{args.pr_body_file.resolve()}",
            )
            print(f"\nUpdated the description of pull request #{args.existing_pr}.")
        print(f"https://github.com/{slug}/pull/{args.existing_pr}")
        return 0

    created = run(
        "gh", "api", f"repos/{slug}/pulls",
        "-X", "POST",
        "-f", f"title={args.pr_title}",
        "-f", f"head={branch}",
        "-f", f"base={args.base}",
        "-F", f"body=@{args.pr_body_file.resolve()}",
    )
    try:
        print("\n" + json.loads(created.stdout)["html_url"])
    except (json.JSONDecodeError, KeyError):
        stop(f"the pull request call returned something unreadable:\n{created.stdout[:400]}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
