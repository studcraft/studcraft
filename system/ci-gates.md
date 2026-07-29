# CI Gates

This repo relies on required GitHub Actions status checks to enforce process
rules mechanically instead of trusting anyone (human or agent) to remember
them. Building and debugging those gates surfaced a few non-obvious pitfalls
worth writing down before adding another one.

---

# A Required Check Must Trigger on Every PR, Unconditionally

`Docs ruleset linter` was originally scoped with `paths: docs/**` at the
workflow's `on:` trigger level. That seemed right — why run a docs linter on
a PR that doesn't touch `docs/`? But once it was marked as a **required**
status check in branch protection, an archive-only PR (touching only
`openspec/specs/`) never triggered the workflow at all — no check run was
ever created for it. GitHub does not treat "this check never ran because it
was filtered out" the same as "this check passed" or "this check was
skipped" — it shows the required check as permanently pending, and blocks
the merge indefinitely.

**Every required check's workflow must trigger on every PR event, with no
`paths:` filter at the `on:` level.** If the check should only meaningfully
apply to some PRs, do that filtering *inside* the job (read the diff, decide
to pass/skip, always produce a check-run result), the way `Docs require
OpenSpec proposal`, `Docs must not edit CHANGELOG.md directly`, and `OpenSpec
archive must be separate from apply` already do. Only non-required,
purely-advisory checks are safe to gate with a `paths:` filter, because
nothing blocks on their absence.

---

# Branch-Naming Exemptions for Automation

Some gates need an escape hatch for the automation that's supposed to do the
thing the gate normally forbids — e.g. `Docs must not edit CHANGELOG.md
directly` has to let the `Release cut` action's own PR edit `CHANGELOG.md`.
The pattern used throughout this repo: the automation always opens its PR
from a branch matching a fixed prefix (`release/v*`, `archive/*`), and the
gate's script checks `github.head_ref` against that prefix as its first
step, exiting success immediately if matched.

This only works if the exemption is scoped as narrowly as the prefix allows
— `archive/*` matches any archive-related branch name, which is why
`scripts/archive_cut.py` could switch from one-branch-per-change
(`archive/<name>`) to one-branch-per-batch (`archive/batch-<date>-<run-id>`)
without needing any change to the gate itself.

---

# Batch, Don't Gate Per-PR, for Anything Writing to Shared State

Any file or directory that multiple concurrent PRs might all want to modify
(`CHANGELOG.md`'s version entries, `openspec/specs/`) has the same underlying
problem: two PRs editing it independently either collide at merge time, or
worse, one silently clobbers what the other just wrote (e.g. a `MODIFIED`
delta applied against a stale copy of a capability). This repo hit that
problem twice — versioning, then archiving — and solved it the same way both
times:

1. No individual PR touches the shared state directly. A gate enforces this
   (`Docs must not edit CHANGELOG.md directly`, `OpenSpec archive must be
   separate from apply`).
2. A separate, manually-triggered `workflow_dispatch` action
   (`Release cut`, `Archive cut`) does the actual write, in one batch,
   whenever a human decides it's time. Batching means the collision case
   never happens — there's only ever one writer, running at one point in
   time, from a script that reads the current state of `main` fresh.
3. The action commits the batch result to its own exempted branch (see
   above) and opens a PR — never pushes to `main` directly.

If a third kind of shared state ever needs this treatment, reuse this shape
rather than inventing a new one: gate + batch script + `workflow_dispatch`
action + branch-naming exemption.

---

# Test Any Repo-Mutating Script in an Isolated Worktree

Both `release_cut.py` and `archive_cut.py` mutate real repository files
(`CHANGELOG.md`, `docs/*.md` version headers, `openspec/specs/`,
`openspec/changes/`). Never run a first test of a script like this directly
against your real working directory — use `git worktree add <path> HEAD`,
run the script there, inspect the result, then `git worktree remove <path>
--force`. This showed its value directly: an early test of `release_cut.py`
against the real working directory, followed by `git reset --hard` to clean
up, wiped out a real uncommitted fix in the same working tree that had
nothing to do with the test. Committing work before testing helps, but a
worktree removes the risk entirely — the real working directory is never
touched, so there's nothing to accidentally reset away. See
`system/repository-strategy.md` for the related rule against destructive git
operations on work that hasn't been reviewed.
