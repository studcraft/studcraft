# CI Gates

This repo relies on required GitHub Actions status checks to enforce process
rules mechanically instead of trusting anyone (human or agent) to remember
them. Building and debugging those gates surfaced a few non-obvious pitfalls
worth writing down before adding another one.

---

# Which Checks Are Required Right Now

A check that exists is not a check that blocks. Marking one **required** is a
branch-protection setting in the GitHub UI, done by hand, and nothing in this
repository can do it for you — so a workflow can ship, pass on every PR, and
still stop nothing.

Required on `main`, with `enforce_admins` enabled so the single maintainer
cannot merge past them:

- `Docs require OpenSpec proposal`
- `Docs must not edit CHANGELOG.md directly`
- `OpenSpec archive must be separate from apply`
- `Docs ruleset linter`
- `OpenSpec change is coherent`

**Not required, and therefore advisory only:**

- `Branch name follows the convention` — passes on every PR since it landed;
  add it to branch protection to make it block.

Branch protection also sets `allow_force_pushes: false`, `allow_deletions:
false`, `required_linear_history: true` and `strict: true` (a branch must be
up to date before merging). Those cover `main` only. **No feature branch is
protected**, so the force-push and rebase prohibitions in
`system/repository-strategy.md` are rules someone keeps, not rules git
enforces.

Read the live state rather than trusting this list, which is a snapshot:

```bash
gh api repos/studcraft/studcraft/branches/main/protection \
  --jq '.required_status_checks.contexts[]'
```

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

## The branch name alone is not enough — constrain by content too

Matching on the prefix and stopping there is a bypass, and it stays invisible
for exactly as long as one person can push branches. `Docs require OpenSpec
proposal` originally read:

```bash
if [[ "$branch" == release/v* ]]; then exit 0; fi
```

Anyone able to push could name their branch `release/v9` and land arbitrary
ruleset changes with no proposal at all. The gate trusted a string the author
chose.

**Every branch-prefix exemption must also assert what the diff is allowed to
contain.** The automation's output is narrow and known, so the constraint is
easy to state and impossible to forge:

- `release/v*` — the `docs/` diff may change nothing except `**Version:**`
  header lines. A real release cut rewrites that one line and nothing else.
- `archive/*` — the diff may touch nothing outside `openspec/`. A real archive
  cut moves changes and writes capability specs, and never edits a rule.

The check is on content, not on the label, so a maliciously or carelessly
named branch fails anyway. Add the same treatment to any future exemption
before merging it.

### One gate was fixed and the other two were not

Writing the rule down did not apply it everywhere. `Docs require OpenSpec
proposal` and `OpenSpec archive must be separate from apply` were both
tightened; `Docs must not edit CHANGELOG.md directly` kept the bare
`exit 0` for months afterwards, while this document already described the
fix as the pattern used throughout the repo.

What that leaves open is narrower than the original bypass but real: a branch
called `release/v9` that touches only `**Version:**` headers satisfies the
proposal gate, and the CHANGELOG gate waves it through on the name alone —
so `CHANGELOG.md` can be written by hand, which is the one thing the gate
exists to prevent. It now asserts the same content constraint as the other
two: nothing outside `CHANGELOG.md` and `docs/*.md`, and inside `docs/`,
nothing but the `**Version:**` line.

**When a lesson is written here, grep for every gate it applies to and fix
them in the same PR.** A rule recorded in `system/` and applied to one of
three call sites reads, later, exactly like a rule that was applied
everywhere.

---

# The Branch Name Is Itself an Input, So Validate It

Three gates change their behaviour based on `github.head_ref`. That makes the
branch name an untrusted input on the same footing as the diff, and until
`Branch name follows the convention` was added, nothing checked its shape —
only whether it started with a reserved prefix. `archive/anything-at-all`
matched the archive exemption; `release/v9` matched the release one.

Content constraints (above) already stop such a branch from *landing* anything
it should not. The naming gate handles the other half: it rejects the
ambiguous name outright, so no gate has to guess what a half-formed
`release/` branch was meant to be.

It also enforces one thing no content check can. `openspec/config.yaml`
requires each proposal to live on its own dedicated branch, and `Docs require
OpenSpec proposal` verifies a PR carries exactly one change — but nothing tied
the branch to *that* change. The naming gate requires them to be equal.

**Test a naming rule against the merged history before shipping it**, per the
last section of this document. This one was: of the 22 merged PRs touching
`docs/`, 21 already had `branch == change name`, and the single exception
carried two proposals, which `Docs require OpenSpec proposal` rejects on its
own. A convention that the repo's own history fails is a convention that needs
changing, not a history that needs excusing.

---

# Anything Mutating Shared State Needs a Concurrency Group

`Release cut` and `Archive cut` both write files that everything else reads —
`CHANGELOG.md`, the `**Version:**` headers, `openspec/specs/`. Neither had a
`concurrency:` block, so two dispatches could run at once, each branching from
its own snapshot of `main`, producing two branches that both claim to archive
the same changes.

Every `workflow_dispatch` action that writes repository state gets:

```yaml
concurrency:
  group: <workflow-name>
  cancel-in-progress: false
```

`cancel-in-progress` must be **false**. These scripts commit and push partway
through; cancelling one mid-run leaves a branch pushed with an incomplete
batch. Queueing is correct, cancelling is not.

---

# GitHub Actions Cannot Open Pull Requests Here

The org policy blocks `GITHUB_TOKEN` from creating pull requests:

```
GitHub Actions is not permitted to create or approve pull requests
```

Both cut workflows originally ended with `gh pr create`, so both reported a
**red run despite having done all of their actual work** — computing the
version, updating the files, pushing the branch. Only the final convenience
step failed.

The setting that would permit it is one flag governing *create* **and**
*approve*; GitHub does not split them. Enabling it would let a workflow
approve pull requests, which quietly hollows out any future review requirement
across every repo in the org, permanently, to save one click per release.

**The workflows therefore push their branch and stop.** Each writes the
compare URL to `$GITHUB_STEP_SUMMARY`, so opening the PR is one click from the
run page, and the run reports success when it succeeded. Do not reintroduce
`gh pr create`, and do not route around the policy with a personal access
token stored as a secret — that recreates exactly the risk the org disabled.

While you are there: both workflows requested `pull-requests: write` for those
steps and nothing else. They now request `contents: write` only, which is what
pushing a branch actually needs.

---

# Do Not Require Approving Reviews While There Is One Maintainer

Raising `required_approving_review_count` to 1 looks like the obvious hardening
step and is currently a trap. `enforce_admins` is enabled, there is one
maintainer, and GitHub does not allow approving your own pull request — so
requiring one approval makes **every PR unmergeable, including the one that
undoes the setting.**

`.github/CODEOWNERS` exists and routes review requests, which is the useful
half. It also records the exact pair of settings to flip on the day a second
maintainer joins:

1. add them to `CODEOWNERS`,
2. set required reviews to 1 and enable `require_code_owner_reviews`.

Both at once, never the second alone.

---

# Check Late-Firing Failures Early

Two checks used to fire only inside `Archive cut`, which runs whenever a
maintainer decides it is time — potentially weeks after the proposal merged,
long after the person who could explain a delta has moved on. This repo hit
that once and untangling it cost two dedicated PRs.

Both now also run per-PR, as `OpenSpec change is coherent`:

- **`openspec validate --all`** — structural. Does every change and spec parse,
  does each change carry at least one delta, does every requirement have a
  scenario.
- **`scripts/check_delta_coverage.py`** — semantic, and the one that matters.
  For every `## MODIFIED Requirements` block, if the targeted requirement
  already exists in the living spec, every scenario the living spec has for it
  must also appear in the delta. Otherwise archiving would delete it silently.

**`openspec validate` does not catch the second problem.** That was verified,
not assumed: deliberately stripping a scenario from a delta left validate
passing. The check lives inside `openspec archive`, which is exactly the thing
that fires too late. `check_delta_coverage.py` reimplements it so it fires on
the PR that introduces the drift.

The general lesson: **if a mechanical check exists only inside a manually
triggered batch step, it is not a gate — it is a landmine.** Move it to the PR
that can still fix it cheaply.

## A new gate must be tested against work it should let through

`OpenSpec change is coherent` originally ran `openspec validate --all`, and
was made a required check the same day. Its first encounter with a real
proposal failed it:

```
✗ change/vehicle-minimum-footprint
[ERROR] Change must have at least one delta. No deltas found.
```

The change was correct. `system/proposal-review.md` (Delta vs. Direct Edit)
states this repo's own policy: several `docs/` documents predate the OpenSpec
workflow and were never formalised as capabilities, so there is nothing to
delta against, and inventing one is explicitly wrong. A required check had
been shipped that blocks the repo's documented practice — and would have
blocked most future ruleset work, since the un-formalised documents include
core rules, combat, transport, movement and construction.

The gate now validates the living specs always, and validates a change only
when it actually ships a `specs/` directory.

**Testing that a gate fails on bad input is half the work.** Test that it
passes on every shape of legitimate work first — including the shapes
documented elsewhere in `system/` as correct.

---

# A Gate That Checks Presence Is Not Checking Substance

`Docs require OpenSpec proposal` originally passed if the diff contained *any*
path under `openspec/changes/`. An empty file satisfied it. With one
maintainer that is a formality; with contributors it is a rule that can be
complied with without being followed.

It now additionally requires:

- **All three artifacts exist** — `proposal.md`, `design.md`, `tasks.md`.
  Checked against the working tree, not the diff, because a PR that only
  applies an already-merged proposal legitimately touches `tasks.md` alone.
- **One change per PR.** `openspec/config.yaml` has always required one branch
  per proposal and nothing enforced it. Archive batches move many changes at
  once and are exempt, by having no non-`archive/` change directory in their
  diff at all.

When adding a gate, ask what the cheapest way to satisfy it without doing the
work is. If that way exists, the gate is checking the wrong thing.

---

# Error Messages Are Documentation for People Who Have Not Read Any

A contributor meets this repo's process for the first time through a red
check. Every gate's `::error::` says what is wrong, what the rule is, and where
to read more — `system/workflow.md`, `CONTRIBUTING.md`, or a worked example
under `openspec/changes/archive/`.

`scripts/check_delta_coverage.py` goes further and explains the fix, because
its failure mode is genuinely unobvious: a renamed scenario reads as a
deletion, so the correct response is to restore the original heading and
correct its body rather than to keep the new name.

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
