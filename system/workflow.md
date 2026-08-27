# OpenSpec Workflow

StudCraft uses OpenSpec for design proposals, decisions and historical
rationale. `docs/` holds only the current accepted rules.

**Every change to a `docs/*.md` file goes through an OpenSpec proposal first.**
A proposal is three artifacts: `proposal.md` (what and why), `design.md` (the
decisions, and what was rejected), `tasks.md` (how to apply it, in verifiable
steps). See `openspec/config.yaml` for per-artifact rules.

## When the edits came first

A rule edited at the table is proposed afterwards, not reverted. The sequence
forces the proposal's shape, so write it that way rather than improvising it:

- **Part A** — what is already in the tree. Boxes ticked, each entry naming the
  command that verifies the claim rather than asserting it.
- **Part B** — what auditing that text returns, as anchor pairs.

Every finding then costs two edits, one to `docs/` and one to the `tasks.md`
that records it. That is the price of the order, and it is why the audit order
changes too — `system/delegating-to-agents.md` ("The Order").

## Ruleset linter

`scripts/lint_ruleset.py` runs on every PR as `Docs ruleset linter`, with no
`paths:` filter — a required check that never triggers blocks the merge
forever (`system/ci-gates.md`).

What it checks is in `system/documentation-standards.md` and in the script's
own docstring. It is **structural only**: it cannot see contradicting rules,
dangling narrative references, or a rule that quietly invalidates another.
Those need a reader.

---

# Git Workflow

Mandatory rules. No exceptions.

- No document change anywhere in the repo may be committed directly to `main`
  or `develop`. Always use a branch.
- `docs/*.md` changes additionally require an OpenSpec proposal, on its own
  dedicated branch. Everything else (README, `AGENTS.md`, `system/*.md`) needs
  a branch but no proposal.
- If asked to edit a ruleset document on `main`/`develop`, or without a
  proposal: stop, make no change, and say why.
- The branch **name** is an input to CI. The table is in
  `system/repository-strategy.md` (Branch Naming).

`.claude/hooks/guard_repo_edits.py` refuses these edits locally before a push.
It mirrors the CI gates and adds nothing; where they could disagree, the gate
is authoritative.

---

# Versioning

The rule — nobody hand-edits `CHANGELOG.md` or a `**Version:**` header — lives
in `system/documentation-standards.md` (Versioning). This is the mechanism that
makes it possible.

Nothing needs to be declared. `scripts/release_cut.py` reads the latest `v*`
tag and the `docs/*.md` changes since it: no changes means nothing to release,
otherwise the bump is **minor**. Two optional overrides exist — `**Bump:**
major` in a commit message (squash-merge concatenates every commit message, so
it survives), and an explicit `severity` input at dispatch time.

## Cutting a release

1. A maintainer runs the `Release cut` action. Timing is the only judgement
   call.
2. `scripts/release_cut.py` resolves the severity, computes the version,
   rewrites `CHANGELOG.md` from the commit subjects since the last tag, and
   updates every `**Version:**` header.
3. It pushes a `release/v*` branch, writes the compare URL to the step summary
   and stops — Actions cannot open PRs here (`system/ci-gates.md`). A human
   opens and merges it.
4. `Tag release` tags the merge commit `vMAJOR.MINOR.PATCH`, the anchor for the
   next cut.

---

# Archiving

`openspec/specs/` is shared state: `openspec archive` reads a capability's
current spec and writes the result back. That is the shape `system/ci-gates.md`
("Batch, Don't Gate Per-PR") describes, applied here.

- **Archiving is a separate PR from the change that applies `docs/*.md`.** An
  apply PR merges `docs/*.md` and its own `openspec/changes/<name>/`, and never
  touches `openspec/specs/`.
- **Archiving is batched**, by the `Archive cut` action: every change whose
  `tasks.md` has no unchecked boxes is archived in one run, committed to
  `archive/batch-<date>-<run-id>`, pushed, and left for a human to open.

`OpenSpec archive must be separate from apply` enforces both directions: a PR
touching `openspec/specs/` must come from an `archive/*` branch and must not
touch `docs/*.md`; any other PR must not touch `openspec/specs/` at all.

**Run the batch after each merge, or after a small group.** Batching removes
concurrent writes; it is not permission to accumulate. A backlog is what turns
this script into a project: with sixteen changes waiting, four had modified the
same requirement and the run aborted on the first.

**Check the precondition before dispatching the run**, or it archives nothing
and exits 1:

```bash
python3 scripts/archive_cut.py --check
```

It names what is ready and, for anything blocked, the line holding it back. Ask
the script that decides rather than a grep of your own: a hand-written one
anchored at column 0, missed an indented task, and counted a checkbox quoted
inside a fenced block as real work.

A box left unticked because its work belongs in a later pull request blocks the
archive until that pull request lands and the box follows it.

## Refresh every delta against `docs/` before archiving

**A delta written a while ago is not a faithful snapshot. It is an old one.**

Deltas are written against `docs/` at proposal time, while `openspec/specs/`
may be several changes behind. Before a batch run, open each delta beside the
`docs/` rule it describes and reconcile. The tool checks structure, not truth.

`scripts/check_delta_coverage.py` mechanises one half: a delta that would drop
a scenario the living spec has fails on the PR. It cannot tell you a delta is
stale.

## When several changes modified the same requirement

Do not reconstruct a plausible sequence of deltas — the deltas were never
coherent, so that fabricates a history.

- **The last change to modify a requirement carries the authoritative delta**,
  complete and valid against the living spec.
- **Superseded deltas move to `specs-superseded/`** in their own change
  directory, with a note naming the change that now owns the requirement.

If one change's `MODIFIED` delta needs another change's capability to exist
first, note the dependency as its own task: `scripts/archive_cut.py` processes
a batch in directory order with no dependency resolution.

## Scenario names are identifiers

A `#### Scenario:` heading is matched by name, so renaming one inside a
`MODIFIED` block reads as a deletion plus an addition and is refused. When a
scenario's content becomes wrong, **keep the name and correct the body** — the
same convention a superseded rule follows in the ruleset.
