# CI Gates

Required GitHub Actions status checks enforce this repo's process rules
mechanically. What follows is what to get right before adding another one.

---

# Which Checks Are Required Right Now

A check that exists is not a check that blocks. Marking one **required** is a
branch-protection setting done by hand in the GitHub UI.

Read the live list rather than trusting a snapshot:

```bash
gh api repos/studcraft/studcraft/branches/main/protection --jq '.required_status_checks.contexts[]'
```

Branch protection on `main` also sets `enforce_admins`, no force-push, no
deletions, linear history and `strict: true`. **No feature branch is
protected**, so the prohibitions in `system/repository-strategy.md` are rules
someone keeps, not rules git enforces.

---

# A Required Check Must Trigger on Every PR, Unconditionally

**No `paths:` filter at a required workflow's `on:` level.** GitHub does not
treat "filtered out" as passed or skipped — the check stays pending and blocks
the merge forever. Filter inside the job instead: read the diff, decide to
pass or skip, always produce a result. Only advisory checks may use `paths:`.

---

# Branch-Naming Exemptions for Automation

Automation opens its PRs from a fixed prefix (`release/v*`, `archive/*`), and a
gate that must let it through checks `github.head_ref` first.

**Every branch-prefix exemption must also assert what the diff may contain.**
The name is a string the author chose; `release/v9` is otherwise a free pass.

- `release/v*` — the `docs/` diff may change nothing but `**Version:**` lines,
  and nothing outside `CHANGELOG.md` and `docs/*.md`.
- `archive/*` — the diff may touch nothing outside `openspec/`.

Scope the prefix no more narrowly than needed: `archive/*` matches any archive
branch, which is why `archive_cut.py` could move from one branch per change to
one per batch without touching a gate.

**When a lesson is recorded here, grep for every gate it applies to and fix
them in the same PR.** A rule applied to one of three call sites reads later
exactly like a rule applied everywhere.

---

# The Branch Name Is Itself an Input, So Validate It

Three gates change behaviour based on `github.head_ref`, which makes the name
untrusted input. `Branch name follows the convention` rejects an ambiguous name
outright, and enforces the one thing no content check can: a ruleset branch
must equal the name of the change it carries.

**Test a naming rule against merged history before shipping it.** A convention
the repo's own history fails is a convention that needs changing.

---

# Anything Mutating Shared State Needs a Concurrency Group

Every `workflow_dispatch` action that writes repository state gets:

```yaml
concurrency:
  group: <workflow-name>
  cancel-in-progress: false
```

`cancel-in-progress` must be **false**. These scripts commit and push partway
through; cancelling mid-run leaves a branch pushed with an incomplete batch.

---

# GitHub Actions Cannot Open Pull Requests Here

Org policy blocks `GITHUB_TOKEN` from creating pull requests:

```
GitHub Actions is not permitted to create or approve pull requests
```

The setting that would permit it governs *create* **and** *approve*, so
enabling it would let workflows approve PRs across every repo in the org.

**Both cut workflows therefore push their branch, write the compare URL to
`$GITHUB_STEP_SUMMARY`, and stop.** Do not reintroduce `gh pr create`, and do
not route around the policy with a personal access token. They request
`contents: write` only.

---

# Required Reviews With One Maintainer

Raising `required_approving_review_count` **in branch protection** is a trap
with one maintainer: `enforce_admins` is on and GitHub forbids self-approval,
so every PR becomes unmergeable, including the one that undoes the setting.

**A repository ruleset escapes this** because it takes a `bypass_actors` list.
What is live: ruleset `Require PR review except jujorie` on `refs/heads/main`
(1 approval, `require_code_owner_review: true`, bypass `jujorie`), alongside
branch protection with 0 required reviews and `enforce_admins: true`. The two
are evaluated together and the more restrictive wins.

- **Anyone but the bypass actor** needs one `CODEOWNERS` approval to merge.
- **The bypass actor** merges with no approval, and still cannot merge red —
  `enforce_admins` belongs to branch protection, which a ruleset bypass does
  not reach.

`file_path_restriction` is unavailable: it is a **push** rule, and the API
refuses push rulesets on public repositories (`422 "Source public repos cannot
have push rules"`). Review is the mechanism, so `.github/CODEOWNERS` must cover
every sensitive path completely.

## The day a non-admin collaborator appears

- **Do they go in `CODEOWNERS`?** That is the moment "code owner" and "admin"
  stop being the same set.
- **Does the `jujorie` bypass stay?** With a second reviewer it is no longer
  load-bearing.
- A path-guard CI gate becomes worth reconsidering then, and **blocks nothing
  `CODEOWNERS` does not already block** before then.

---

# Check Late-Firing Failures Early

**If a mechanical check exists only inside a manually triggered batch step, it
is not a gate — it is a landmine.** Move it to the PR that can still fix it
cheaply.

Two checks used to fire only inside `Archive cut`, weeks after the proposal
merged. Both now run per-PR as `OpenSpec change is coherent`:

- `openspec validate --all` — structural: does everything parse, does each
  change carry a delta, does every requirement have a scenario.
- `scripts/check_delta_coverage.py` — semantic, and the one that matters: a
  `MODIFIED` block must keep every scenario the living spec already has.
  Verified, not assumed: stripping a scenario left `validate` passing.

## A new gate must be tested against work it should let through

`OpenSpec change is coherent` shipped as required, then failed its first real
proposal for having no delta — which `system/proposal-review.md` (Delta vs.
Direct Edit) documents as correct here. It now validates a change only when it
ships a `specs/` directory.

**Testing that a gate fails on bad input is half the work.** Test that it
passes on every shape of legitimate work first, including the shapes `system/`
documents as correct.

---

# A Gate That Checks Presence Is Not Checking Substance

`Docs require OpenSpec proposal` originally passed on *any* path under
`openspec/changes/`; an empty file satisfied it. It now requires all three
artifacts (checked against the working tree, since an apply-only PR
legitimately touches `tasks.md` alone) and one change per PR.

**When adding a gate, ask what the cheapest way to satisfy it without doing the
work is.** If that way exists, the gate is checking the wrong thing.

---

# Error Messages Are Documentation for People Who Have Not Read Any

A contributor meets this process for the first time through a red check. Every
gate's `::error::` says what is wrong, what the rule is, and where to read
more. Where a failure mode is unobvious, it also says how to fix it — a renamed
scenario reads as a deletion, so the fix is to restore the heading, not keep
the new name.

---

# Batch, Don't Gate Per-PR, for Anything Writing to Shared State

Any file several concurrent PRs might modify (`CHANGELOG.md`,
`openspec/specs/`) gets the same shape, and reuse it rather than inventing a
third:

1. A gate stops individual PRs touching it.
2. A manually-triggered `workflow_dispatch` script does the write in one batch,
   reading `main` fresh, so there is only ever one writer.
3. The action commits to its own exempted branch and never pushes to `main`.

---

# Test Any Repo-Mutating Script in an Isolated Worktree

Never run a first test of a script that writes repository files against your
real working directory: `git worktree add <path> HEAD`, run it there, inspect,
then `git worktree remove <path> --force`. An early `release_cut.py` test
followed by `git reset --hard` wiped an unrelated uncommitted fix.
