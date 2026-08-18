## 0. Setup

- [x] 0.1 Create and switch to a dedicated branch named `damage-resolution-drops-legacy-state-names` (`openspec/config.yaml` requires one per proposal), created off an up-to-date `main` (`git fetch origin`, `git checkout main`, `git merge --ff-only origin/main`, `git checkout -b damage-resolution-drops-legacy-state-names`).

This change edits no `docs/*.md` file — the ruleset already reads `Operational` / `Wounded` / `Dead` throughout (`DMG-005`, `DMG-015`, `DMG-019`). There is nothing here for `scripts/check_task_anchors.py` to anchor against, and no section 1 replacement-block preamble is needed. The only content this change carries is the spec delta below, already written in this change directory, plus its own verification.

## 1. Spec delta

Already written at `specs/damage-resolution/spec.md` in this change directory. Verify only — do not rewrite it.

- [x] 1.1 `MODIFIED Requirements` contains exactly two requirements, `Damage Roll` and `Repairs`, matching the living spec's requirement names exactly.
- [x] 1.2 Neither requirement's scenario headings differ from the living spec's: `Successful damage roll leaves the component unchanged`, `Failed damage roll advances the component's state`, `Repairing a touched component`, `Destroyed components cannot be repaired` — all four carried through unrenamed, per `system/workflow.md` ("Scenario names are identifiers").
- [x] 1.3 Every occurrence of `OK`, `TOUCHED`, and `DESTROYED` in both requirement bodies is replaced with `Operational`, `Wounded`, and `Dead` respectively, and nothing else in either requirement's wording changed.
- [x] 1.4 No other requirement in the delta file. `Attack Roll`, `Select Target Component`, `Composite Vehicle Targeting`, `Geometry Check`, `Multiple Independent Impacts`, `Penetration`, and `Weapon Distribution` are untouched by this change and carry no delta.

## 2. Verify

- [x] 2.1 Run `grep -c -e OK -e TOUCHED -e DESTROYED openspec/specs/damage-resolution/spec.md` — before this change is archived: **5** (the living spec still carries the stale names; only the Archive cut writes `openspec/specs/`).
- [x] 2.2 Run `grep -c -e OK -e TOUCHED -e DESTROYED openspec/changes/damage-resolution-drops-legacy-state-names/specs/damage-resolution/spec.md` — the delta itself: **0**.
- [x] 2.3 Run `grep -c "^#### Scenario:" openspec/changes/damage-resolution-drops-legacy-state-names/specs/damage-resolution/spec.md` — the delta carries all four scenarios the living spec has for the two `MODIFIED` requirements: **4**.
- [x] 2.4 Run `python3 scripts/check_delta_coverage.py` — confirms the delta drops no scenario the living spec already has for `Damage Roll` or `Repairs`.
- [x] 2.5 Run `python3 scripts/check_task_anchors.py damage-resolution-drops-legacy-state-names` — confirms this file, which has no replacement-block anchors, raises no anchor error and instructs no release-cut-only edit.
- [x] 2.6 Run `python3 scripts/preflight.py` — confirms this change does not put any required CI gate into a failing state before push.

Task 2.6 above is deliberately not `scripts/verify_tasks.py` re-running this same file: that command is itself on `verify_tasks.py`'s own allowlist, so a task naming it verbatim would have the tool execute itself recursively against its own unfinished output. It was tried once, by hand rather than as a task, and timed out at 120s for exactly that reason. `scripts/preflight.py` already covers the same ground (it runs both checker scripts) without the recursion.
