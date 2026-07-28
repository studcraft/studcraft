# Repository Strategy

BLOCKER rules. No exceptions, ever — not for "my own branch," not to fix an out-of-date branch, not under user time pressure.

---

# Git History

- Never force-push (`git push --force`, `--force-with-lease`, or any variant) to any branch — including a branch only you have touched — unless the user explicitly authorizes that exact push, for that exact branch, at that moment.
- Never rewrite existing commit history: no `git rebase` on a branch that has already been pushed, no `git commit --amend` on a pushed commit, no interactive rebase, no squashing after push.
- History only grows. New commits append; they never replace, reorder, or drop existing ones.
- Only linear git: a branch moves forward by adding commits on top of what's already there. Nothing already pushed is ever recommitted under a new SHA.

---

# Keeping a branch up to date with main/develop

If GitHub shows "This branch is out-of-date with the base branch":

- Merge the base branch into the feature branch (`git merge origin/main`, or GitHub's own "Update branch" button). This adds a merge commit and is always safe — nothing is rewritten, no force push required.
- Do **not** rebase the branch onto the base and do **not** force-push to "fix" this, even though it produces a cleaner-looking log. Rebasing changes every commit's SHA on a branch that may already have an open PR, review comments, or CI runs tied to the old commits.

---

# Why

Force-pushing or rewriting published history silently breaks things that look fine until someone hits them:

- PR review comments can become orphaned or hard to re-map to the new commits.
- CI check results are tied to a specific SHA; rewriting history invalidates them even if the content is identical.
- Any collaborator (or agent) with a local checkout based on the old commits now has a diverged, hard-to-reconcile branch.

Example: a branch fell behind `main` after a sibling PR merged. The correct fix is `git merge origin/main` (or GitHub's "Update branch" button) — not `git rebase origin/main` followed by `git push --force-with-lease`, even though the rebase result looks tidier.

A regular merge commit costs one extra line in the log. That's a good trade — this repo's git history doubles as the audit trail for how the ruleset evolved (see `system/workflow.md`).
