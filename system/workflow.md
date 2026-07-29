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

`scripts/lint_ruleset.py` runs on every PR touching `docs/**` (see
`Docs ruleset linter`). It is a **structural** check only:

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
section in `CHANGELOG.md`. That still let two concurrent PRs collide —
both inserting a new entry at the same point in the same file is a
textbook merge conflict. Since this repo always squash-merges (one
commit per PR on `main`, confirmed by `git log --merges` showing zero
merge commits), git itself already gives every PR a natural, per-PR
"why did this change" record with no shared file to collide on: the
squash commit message. So the mechanism moved there instead.

## Declaring a bump

Any PR that changes `docs/*.md` must include a line in one of its
**commit messages** (not in `CHANGELOG.md` — see above):

```
**Bump:** major|minor|patch
```

(pick one). Since this repo squash-merges, every commit message on the
branch is concatenated into the one commit that lands on `main`, so the
marker survives the merge automatically. This is enforced by the `Docs
require changelog bump` GitHub Action — it fails the PR if `docs/*.md`
changed without a `**Bump:**` line in the commit range, and separately
fails the PR if it edits `CHANGELOG.md` directly (that file is now
release-cut-only — see below). For this to actually block a merge,
`Docs require changelog bump` (and `Docs require OpenSpec proposal`)
must be configured as **required status checks** in the branch
protection rules for `main`/`develop`, with "Include administrators"
enabled — otherwise the checks only advise and can be bypassed.

## Cutting a release

Cutting a release is manual-trigger, mechanical-execution:

1. A maintainer runs the `Release cut` GitHub Action (`workflow_dispatch`)
   whenever they decide it's time to release — this is the only human
   judgment call left (timing, and implicitly which accumulated commits
   to include).
2. The action (`scripts/release_cut.py`) finds the latest `v*` git tag,
   walks every commit merged since (`git log <tag>..HEAD`), collects
   every `**Bump:**` marker across those commit messages, and takes the
   most severe one. It computes the next version, rewrites
   `CHANGELOG.md` (auto-building the new `[MAJOR.MINOR.PATCH] - DATE`
   entry from the commit subjects, opening a fresh empty `[Unreleased]`
   above it), and updates the `**Version:**` header in every
   `docs/*.md` file.
3. It opens a PR with these changes (never pushes to `main` directly,
   per the Git Workflow rules above) from a `release/v*` branch — that
   branch naming is what tells `Docs require changelog bump` to skip its
   normal checks for this one PR. A human reviews and merges it.
4. On merge, the `Tag release` action tags that commit `vMAJOR.MINOR.PATCH`
   automatically, so every released version is traceable to an exact
   commit in git history, and becomes the new anchor for the next cut.
