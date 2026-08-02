# OpenSpec Workflow

StudCraft uses OpenSpec for design discussions and architectural decisions.

OpenSpec stores:

- Design proposals
- Design decisions
- Historical rationale
- Future ideas

The `/docs` directory stores only the current accepted rules — the ruleset. Every change to a ruleset file (`/docs/*.md`) must go through an OpenSpec proposal first. This is mandatory; see Git Workflow below.

See `openspec/config.yaml` for per-artifact rules.

## Ruleset linter

`scripts/lint_ruleset.py` runs on every PR (see `Docs ruleset linter`) —
not filtered to PRs touching `docs/**`, because it's a required status
check: a `paths:`-filtered trigger never creates a check run at all for
non-matching PRs, which GitHub then treats as permanently pending and
blocks the merge. It is a **structural** check only:

- Rule IDs (`WPN-001`, `CORE-007`, ...) are unique and strictly
  increasing within their document.
- Cross-document rule references (e.g. `` `10-weapons.md` (WPN-002) ``)
  point at an ID that actually exists in the target document.
- Every `docs/*.md` file that defines rule IDs has a `**Version:**`
  header, and all such headers agree with each other.

It does **not** catch semantic problems — contradicting rules, dangling
narrative references, a rule that quietly invalidates another. That
still requires a human (or an explicit review pass) reading the diff
against the existing ruleset, the way the `weapon-construction-system`
proposal was reviewed before being applied.

---

# Git Workflow

Mandatory rules. No exceptions.

- No document changes anywhere in the repo (`/docs`, `README.md`, `CODE_OF_DESIGN.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `AGENTS.md`, `system/*.md`) may be committed directly to `main` or `develop`. Always use a branch.
- Ruleset changes (`/docs/*.md`) additionally require an OpenSpec proposal first, on its own dedicated branch (see `openspec/config.yaml`). Non-ruleset docs (README, AGENTS.md, `system/*.md`, etc.) need a branch but not a proposal.
- If asked to edit a ruleset document directly on `main`/`develop`, or without a proposal: stop, do not make the change, and tell the user why.

---

# Versioning

Multiple proposal branches can be in flight at the same time. Assigning a
version number (e.g. bumping a `docs/*.md` header from 0.1.0 to 0.2.0) on
a branch risks two branches picking the same next version and colliding
at merge time.

To avoid this:

- A merging PR does **not** bump any version number, and does **not**
  edit `CHANGELOG.md` at all. Ruleset document `Version:` headers stay
  untouched too.
- A version number is assigned only in a separate, later **release-cut**
  step, which happens one at a time against `main` (git merges are
  serialized), removing the collision case entirely.

Earlier versions of this workflow had PRs hand-edit a `[Unreleased]`
section in `CHANGELOG.md`, then later a required `**Bump:**` marker in
a commit message. Both still depended on a human or agent remembering
to write something, every single time, or a PR would get blocked. The
current mechanism requires **nothing to be written, ever**, for the
routine case — see Declaring a bump below.

## Declaring a bump

Nothing needs to be declared. `scripts/release_cut.py` finds the latest
`v*` git tag and checks whether any `docs/*.md` file changed since —
purely from git history, no commit message or file edit required:

- If nothing under `docs/*.md` changed since the last tag, there is
  nothing to release.
- Otherwise the bump defaults to **minor**, automatically, always.

The only thing a PR must never do is edit `CHANGELOG.md` directly — that
file is release-cut-only (see below), enforced by the `Docs must not
edit CHANGELOG.md directly` GitHub Action. For this to actually block a
merge, that check (and `Docs require OpenSpec proposal`) must be
configured as **required status checks** in the branch protection rules
for `main`/`develop`, with "Include administrators" enabled — otherwise
the checks only advise and can be bypassed.

Two fully optional escape hatches exist for the rare case that isn't
"routine minor bump":

- A commit message may include `**Bump:** major` to self-flag as
  breaking. Since this repo squash-merges, every commit message on a
  branch is concatenated into the one commit that lands on `main`, so
  the marker survives automatically if anyone bothers to add it. It is
  never required, and its absence never blocks anything.
- Whoever triggers `Release cut` can pass an explicit `severity` input
  (`auto` / `patch` / `minor` / `major`), overriding both the default
  and any marker, for when they know better at cut time.

## Cutting a release

Cutting a release is manual-trigger, mechanical-execution:

1. A maintainer runs the `Release cut` GitHub Action (`workflow_dispatch`)
   whenever they decide it's time to release — this is the only human
   judgment call left (timing, and optionally an explicit severity
   override).
2. The action (`scripts/release_cut.py`) finds the latest `v*` git tag,
   confirms `docs/*.md` changed since it, and resolves severity (explicit
   override, else `major` if any commit self-flagged it, else `minor`).
   It computes the next version, rewrites `CHANGELOG.md` (auto-building
   the new `[MAJOR.MINOR.PATCH] - DATE` entry from every commit subject
   since the last tag, opening a fresh empty `[Unreleased]` above it),
   and updates the `**Version:**` header in every `docs/*.md` file.
3. It commits these changes to a `release/v*` branch and pushes it, then
   stops — it never pushes to `main` directly, per the Git Workflow rules
   above, and it does **not** open the PR. The org blocks Actions from
   creating pull requests, and the setting that would allow it also allows
   Actions to approve them (see `system/ci-gates.md`). The run writes the
   compare URL to its step summary; a human opens the PR from there,
   reviews and merges it. The `release/v*` branch naming is what tells
   `Docs must not edit CHANGELOG.md directly` to skip its check for this
   one PR — and that exemption additionally verifies the `docs/` diff
   contains nothing but `**Version:**` header lines.
4. On merge, the `Tag release` action tags that commit `vMAJOR.MINOR.PATCH`
   automatically, so every released version is traceable to an exact
   commit in git history, and becomes the new anchor for the next cut.

---

# Archiving

`openspec/specs/` is shared state: `openspec archive` reads a capability's
*current* spec there and writes the result back. Same problem as
`CHANGELOG.md` — if two proposal PRs both archive against it at merge
time, whichever merges second either conflicts or, worse, silently
clobbers what the first one just wrote (e.g. a `MODIFIED` delta applied
against a capability that doesn't exist yet, or against a stale copy of
it). Multiple proposals can be in flight at once, and some may depend on
another's capability existing first (e.g. a change with a `MODIFIED`
delta on `weapon-construction` needs `weapon-construction` to already be
archived).

To avoid this, **archiving is decoupled from the PR that applies a
change's `docs/*.md` edits**:

- A proposal's apply/implementation PR merges `docs/*.md`,
  `docs/14-glossary.md`, and its own `openspec/changes/<name>/` files to
  `main`. It does **not** touch `openspec/specs/` and does **not**
  archive.
- Archiving happens afterward, as its own PR, never pushed to `main`
  directly, per the Git Workflow rules above.

**Archiving is batched, not one PR per merged proposal.** Doing it
per-PR would mean the same "concurrent writes to shared state" problem
this section opened with, just shifted from apply-time to archive-time —
and with several proposal branches landing on `main` around the same
time (see Versioning above), that's a lot of archive-PR churn for a
mechanical step. Instead, archiving accumulates: any change with a
fully-checked `tasks.md` is a candidate, and they all get archived
together the next time someone runs the batch.

## Cutting an archive batch

1. A maintainer runs the `Archive cut` GitHub Action (`workflow_dispatch`)
   whenever they decide it's time — this is the only human judgment
   call left (timing).
2. The action (`scripts/archive_cut.py`) walks every directory under
   `openspec/changes/` (excluding `archive/`), and runs `openspec
   archive <name> --yes` for every change whose `tasks.md` has no
   remaining unchecked boxes. Changes with incomplete tasks are left
   alone and reported, not archived — archiving is only safe once a
   proposal's `docs/*.md` edits have actually landed on `main`. If a
   change's `MODIFIED` delta depends on another capability that isn't
   archived yet, it simply won't have a target to delta against; check
   dependency notes in `tasks.md` before relying on ordering within one
   batch run.
3. It commits every archived change's result to a branch named
   `archive/batch-<date>-<run-id>`, pushes it, writes the compare URL to
   its step summary, and stops — a human opens the PR from there, for the
   same reason the release cut does (see `system/ci-gates.md`). Any
   `archive/*` prefix satisfies the branch-naming convention the `OpenSpec
   archive must be separate from apply` gate checks for; it isn't tied to
   a single change's name. That exemption additionally verifies the diff
   touches nothing outside `openspec/`.

This isn't just policy — it's enforced. The `OpenSpec archive must be
separate from apply` GitHub Action requires:

- Any PR touching `openspec/specs/` **must** come from an `archive/*`
  branch, and must not touch `docs/*.md`.
- Any PR **not** from an `archive/*` branch must not touch
  `openspec/specs/` at all.

So an apply PR that also tries to archive gets rejected, and an archive
PR that also tries to sneak in a ruleset edit gets rejected too. For this
to actually block a merge, `OpenSpec archive must be separate from
apply` must be added to the **required status checks** in branch
protection for `main`/`develop`, alongside the other required checks.

## Archive close to the merge, not in batches of seventeen

Batching exists to remove concurrent writes to `openspec/specs/`, not to let
changes pile up. Sixteen unarchived changes accumulated once, and the batch
run aborted on the first one — four merged changes had each modified the same
requirement, and none of their deltas was valid against the living spec.
Fixing it took two dedicated PRs and a set of judgement calls that a
mechanical step should never require.

Run the batch after each merge, or after a small group. The concurrency
protection is unchanged; the backlog is what turns a script into a project.

## Refresh every delta against `docs/` before archiving

**A delta written a while ago is not a faithful snapshot. It is an old one.**

Deltas in this repo are written against `docs/` at the time of the proposal,
while `openspec/specs/` may already be several changes behind. That is the
root cause of every archive failure so far: the deltas were never coherent
with the living spec, so they could not form a valid chain no matter what
order they were applied in.

Two concrete examples, both caught only because someone re-read the delta
against current `docs/` immediately before archiving:

- `gameplay-visual-geometry`'s `geometry-layers` delta omitted `Resistance`
  from the measured-value list, lacked GEO-002's structural-cross-section
  carve-out, and still described Cover as gradual after `CORE-010` became
  binary. Archiving it unrefreshed would have created a brand-new capability
  carrying exactly the drift the previous PR had just finished removing.
- Four changes' `component-damage` deltas each modified `Geometry Defines
  Resistance` and disagreed with each other and with the living spec.

Before running the batch, for every change it will archive: open its delta and
the `docs/` rule it describes, side by side, and reconcile. The tool checks
structure, not truth.

One half of this is now mechanised: `OpenSpec change is coherent` runs
`scripts/check_delta_coverage.py` on every PR, so a delta that would drop a
scenario the living spec has fails immediately instead of at archive time.
It cannot tell you a delta is *stale* — only that it is not destructive.
Reading it against `docs/` is still yours.

## When several changes modified the same requirement

`openspec archive` refuses a `MODIFIED` block that omits a scenario the living
spec already has, because applying it would drop that scenario silently. With
a backlog, several changes commonly modify the same requirement, and their
deltas conflict.

Do not reconstruct a plausible sequence of deltas — that fabricates a history
that never happened, since the deltas were never coherent in the first place.
Instead:

- **The last change to modify a requirement carries the authoritative delta**,
  complete and valid against the living spec.
- **Superseded deltas move to `specs-superseded/`** inside their own change
  directory, with a note naming the change that now owns the requirement.
  Nothing is deleted; the reasoning behind each still lives in its own
  `proposal.md`, `design.md` and git history.

## Scenario names are identifiers

A `#### Scenario:` heading is matched by name. Renaming one in a `MODIFIED`
block reads as deleting the old scenario and adding a new one, and the archive
tool will refuse the block for exactly that reason.

When a scenario's content becomes wrong, **keep its name and correct the
body** — the same stable-identifier convention `MEL-010` and `CBT-011` follow
in the ruleset itself. `Resistance read from a single-brick cross-section` kept
its name when a brick stopped meaning Resistance 1 and started meaning 3.
