# Repository Strategy

BLOCKER rules. No exceptions, ever — not for "my own branch," not to fix an out-of-date branch, not under user time pressure.

---

# Git History

- Never force-push (`git push --force`, `--force-with-lease`, or any variant) to any branch — including a branch only you have touched — unless the user explicitly authorizes that exact push, for that exact branch, at that moment.
- Never rewrite existing commit history: no `git rebase` on a branch that has already been pushed, no `git commit --amend` on a pushed commit, no interactive rebase, no squashing after push.
- History only grows. New commits append; they never replace, reorder, or drop existing ones.
- Only linear git: a branch moves forward by adding commits on top of what's already there. Nothing already pushed is ever recommitted under a new SHA.

---

# Creating a new branch

- Before creating any new branch, update local `main` first: `git fetch origin` then `git checkout main` then `git pull origin main --ff-only` (or branch directly off `origin/main`). Never branch off a stale local `main`.
- Every new branch is created from `main`. Not from another feature branch, not from an old local checkout — from current `main`, every time.
- Skipping this step is exactly what causes the "out-of-date with the base branch" state this document already tells you not to fix with rebase + force-push. Doing it right the first time avoids needing the fix at all.

---

# Keeping a branch up to date with main/develop

If GitHub shows "This branch is out-of-date with the base branch":

- Merge the base branch into the feature branch (`git merge origin/main`, or GitHub's own "Update branch" button). This adds a merge commit and is always safe — nothing is rewritten, no force push required.
- Do **not** rebase the branch onto the base and do **not** force-push to "fix" this, even though it produces a cleaner-looking log. Rebasing changes every commit's SHA on a branch that may already have an open PR, review comments, or CI runs tied to the old commits.

---

# This Repo Squash-Merges, and That Has Two Consequences

Every PR lands on `main` as a single new commit. The branch's own commits are
never ancestors of `main`, which breaks two things people reach for by reflex.

## `git branch --merged` is useless here — never delete branches by it

After 34 merged PRs, `git branch --merged main` reported **zero** merged
branches. Deleting by that criterion would have deleted nothing; trusting its
inverse would have deleted everything.

Use the authoritative source instead — which branches GitHub records as having
a merged PR:

```bash
gh pr list --state merged --limit 100 --json headRefName --jq '.[].headRefName' | sort -u > /tmp/merged.txt
git branch --format='%(refname:short)' | grep -v '^main$' | sort > /tmp/local.txt
comm -12 /tmp/local.txt /tmp/merged.txt        # safe to delete
comm -23 /tmp/local.txt /tmp/merged.txt        # inspect before deleting
```

## Concurrent branches conflict artificially after one of them merges

Two branches that both edit the same file will conflict on **every line the
first one changed**, not just on the lines they genuinely disagree about,
because the squash commit discards the ancestry they shared.

This happened between two proposal branches whose real content difference was
six lines: `git merge origin/main` reported a conflict across every hunk the
sibling PR had touched. The resolution is usually to take the feature branch's
version of the file wholesale — it already equals `main` plus its own edits —
but **verify that after resolving**, by diffing against `main` and confirming
only the expected lines remain.

Merge, never rebase, per the rules above. And where one branch's text cites
wording another branch introduces, the merge order is not a preference: land
the branch that introduces the wording first.

---

# Why

Force-pushing or rewriting published history silently breaks things that look fine until someone hits them:

- PR review comments can become orphaned or hard to re-map to the new commits.
- CI check results are tied to a specific SHA; rewriting history invalidates them even if the content is identical.
- Any collaborator (or agent) with a local checkout based on the old commits now has a diverged, hard-to-reconcile branch.

Example: a branch fell behind `main` after a sibling PR merged. The correct fix is `git merge origin/main` (or GitHub's "Update branch" button) — not `git rebase origin/main` followed by `git push --force-with-lease`, even though the rebase result looks tidier.

A regular merge commit costs one extra line in the log. That's a good trade — this repo's git history doubles as the audit trail for how the ruleset evolved (see `system/workflow.md`).
