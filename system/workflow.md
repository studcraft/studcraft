# OpenSpec Workflow

StudCraft uses OpenSpec for design discussions and architectural decisions.

OpenSpec stores:

- Design proposals
- Design decisions
- Historical rationale
- Future ideas

The `/docs` directory stores only the current accepted rules — the ruleset. Every change to a ruleset file (`/docs/*.md`) must go through an OpenSpec proposal first. This is mandatory; see Git Workflow below.

See `openspec/config.yaml` for per-artifact rules.

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

- A merging PR does **not** bump any version number. It adds its change
  under the `[Unreleased]` section of `CHANGELOG.md` and leaves ruleset
  document `Version:` headers untouched.
- A version number is assigned only in a separate, later **release-cut**
  step, which happens one at a time against `main` (git merges are
  serialized), removing the collision case entirely.

## Declaring a bump

Any PR that changes `docs/*.md` must add an entry under `[Unreleased]` in
`CHANGELOG.md` that includes a line:

```
**Bump:** major|minor|patch
```

(pick one). This is enforced by the `Docs require changelog bump` GitHub
Action — it fails the PR if `docs/*.md` changed without a matching
`CHANGELOG.md` update and `**Bump:**` line. For this to actually block a
merge, `Docs require changelog bump` (and `Docs require OpenSpec
proposal`) must be configured as **required status checks** in the
branch protection rules for `main`/`develop`, with "Include
administrators" enabled — otherwise the checks only advise and can be
bypassed.

## Cutting a release

Cutting a release is manual-trigger, mechanical-execution:

1. A maintainer runs the `Release cut` GitHub Action (`workflow_dispatch`)
   whenever they decide it's time to release — this is the only human
   judgment call left (timing, and implicitly which accumulated bumps to
   include).
2. The action (`scripts/release_cut.py`) reads every `**Bump:**` entry
   under `[Unreleased]`, takes the most severe one, computes the next
   version from the latest `v*` git tag, rewrites `CHANGELOG.md` (moving
   the accumulated entries under a new `[MAJOR.MINOR.PATCH] - DATE`
   header and opening a fresh empty `[Unreleased]`), and updates the
   `**Version:**` header in every `docs/*.md` file.
3. It opens a PR with these changes (never pushes to `main` directly,
   per the Git Workflow rules above). A human reviews and merges it.
4. On merge, the `Tag release` action tags that commit `vMAJOR.MINOR.PATCH`
   automatically, so every released version is traceable to an exact
   commit in git history.
