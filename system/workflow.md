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
3. It opens a PR with these changes (never pushes to `main` directly,
   per the Git Workflow rules above) from a `release/v*` branch — that
   branch naming is what tells `Docs must not edit CHANGELOG.md directly`
   to skip its check for this one PR. A human reviews and merges it.
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
- Archiving happens afterward, one change at a time, in whatever order
  dependencies require (check other open changes' `tasks.md` for
  `MODIFIED`/dependency notes before archiving). It is its own PR:
  `openspec archive <name>` run against an up-to-date `main`, then
  commit and PR that result — never pushed to `main` directly, per the
  Git Workflow rules above.
- If a change's delta depends on another capability that hasn't been
  archived yet, wait. Don't force it — see `weapon-construction-system`
  (PR #7) / `gameplay-visual-geometry` (PR #11) for a real example of
  this dependency.

This isn't just policy — it's enforced. Push the archive result from a
branch named `archive/<name>` (mirrors `release/v*`). The `OpenSpec
archive must be separate from apply` GitHub Action then requires:

- Any PR touching `openspec/specs/` **must** come from an `archive/*`
  branch, and must not touch `docs/*.md`.
- Any PR **not** from an `archive/*` branch must not touch
  `openspec/specs/` at all.

So an apply PR that also tries to archive gets rejected, and an archive
PR that also tries to sneak in a ruleset edit gets rejected too. For this
to actually block a merge, `OpenSpec archive must be separate from
apply` must be added to the **required status checks** in branch
protection for `main`/`develop`, alongside the other required checks.
