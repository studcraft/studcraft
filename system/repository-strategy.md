# Repository Strategy

BLOCKER rules. No exceptions, ever — not for "my own branch," not to fix an out-of-date branch, not under user time pressure.

---

# Git History

- Never force-push (`--force`, `--force-with-lease`, any variant) to any branch, including one only you have touched, unless the user authorizes that exact push, for that exact branch, at that moment.
- Never rewrite existing history: no `git rebase` on a pushed branch, no `--amend` on a pushed commit, no interactive rebase, no squashing after push.
- History only grows. New commits append; nothing pushed is ever recommitted under a new SHA.

Rewriting published history breaks things that look fine until someone hits them: review comments orphaned from their commits, CI results tied to SHAs that no longer exist, and every collaborator's checkout diverged. A merge commit costs one line in the log — this history doubles as the audit trail for how the ruleset evolved.

---

# Staging — never `git add -A`

- **Never run `git add -A` or `git add .`.** Stage the specific paths you edited, by name, every time.
- **A deletion is staged with `git update-index --remove -- <path>`.** `git add` cannot express one — the path matches nothing on disk — and the flag that would fix that is the one forbidden above. `scripts/open_pr.py` does this itself: delete the file, pass its path like any other, and do not `git rm` first.

Both commands take one path and can touch nothing else, which is the property the rule protects.

---

# Creating a new branch

- Every branch is created from current `main`: `git fetch origin`, `git checkout main`, `git pull origin main --ff-only`, then branch. Never from another feature branch or a stale local `main`.

---

# Branch Naming

Branch names are an input to CI: three gates read `github.head_ref` and change what they allow. `Branch name follows the convention` enforces this table on every PR.

| Name | Who creates it | What it may touch |
|---|---|---|
| `release/v<major>.<minor>.<patch>` | `Release cut` workflow, never by hand | `CHANGELOG.md` and the `**Version:**` header in `docs/*.md` — nothing else |
| `archive/batch-<date>-<run-id>` | `Archive cut` workflow, never by hand | `openspec/` only |
| `<change-name>` — the directory under `openspec/changes/`, exactly | you, for a ruleset proposal | `docs/*.md` plus that one change, plus what its `design.md` names as knowingly broken otherwise |
| `<what-it-does>` in kebab-case | you, for anything else | anything except `docs/` and `openspec/specs/` |

A ruleset branch may also carry a non-`docs/` file only if its `design.md`
says which and why — #119, #123 and #126 each did. Shipping a pointer the
change knows is broken so the file set stays pure is worse, and nobody has
chosen it.

`release/` and `archive/` are **reserved prefixes**, not descriptive ones — they are how the automation's PRs identify themselves to the gates that would otherwise block them.

A ruleset branch takes its proposal's name because `openspec/config.yaml` requires one dedicated branch per proposal, and a matching name is the only way to check that mechanically.

Everything else is lowercase kebab-case. No slashes, no underscores, no uppercase.

---

# Keeping a branch up to date with main

If GitHub reports "out-of-date with the base branch": **merge the base into the branch** (`git merge origin/main`, or the "Update branch" button). Nothing is rewritten and no force-push is needed.

Do **not** rebase and force-push to fix it, even though the log looks tidier.

---

# This Repo Squash-Merges, and That Has Two Consequences

Every PR lands on `main` as one new commit, so a branch's own commits are never ancestors of `main`.

## `git branch --merged` is useless here — never delete branches by it

After 34 merged PRs it reported **zero** merged branches. Use what GitHub records instead:

```bash
gh pr list --state merged --limit 100 --json headRefName --jq '.[].headRefName'
```

Compare that against `git branch --format='%(refname:short)'`; a local branch on both lists is safe to delete, one on neither needs inspecting first.

## Concurrent branches conflict artificially after one of them merges

Two branches editing the same file conflict on **every line the first one changed**, because the squash commit discards their shared ancestry. Two proposal branches whose real difference was six lines conflicted across every hunk.

The resolution is usually to take the feature branch's version of the file wholesale — it already equals `main` plus its own edits — but **verify that afterwards** by diffing against `main` and confirming only the expected lines remain. Where one branch's text cites wording another introduces, land the branch that introduces the wording first.
