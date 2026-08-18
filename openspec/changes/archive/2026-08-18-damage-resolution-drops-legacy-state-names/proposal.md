# Damage resolution drops legacy state names

## Why

`openspec/specs/damage-resolution/spec.md` names the same three Component States with two different vocabularies. Its *Attack Roll* requirement, recently updated, reads `Wounded`. Further down the same file, *Damage Roll* still reads:

> A result of 1, 2, or 3 SHALL advance the component's state by exactly one step (`OK` to `TOUCHED`, or `TOUCHED` to `DESTROYED`).

and *Repairs* still reads:

> Repairing a component SHALL consume Action Points and SHALL restore exactly one state, from `TOUCHED` to `OK`. A `DESTROYED` component SHALL NOT be repairable.

`OK` / `TOUCHED` / `DESTROYED` is not a vocabulary any rule in `docs/` uses. `docs/16-damage-system.md` (`DMG-005`) names the three states `Operational`, `Wounded` and `Dead`, and both `DMG-015` (Damage Roll) and `DMG-019` (Repairs) read against those names. `openspec/specs/component-damage/spec.md` — the sibling capability that owns the state machine itself — already uses `Operational` / `Wounded` / `Dead` throughout. The living `damage-resolution` spec is the one place still carrying the legacy names, and it carries them in two requirements at once, contradicting the *Attack Roll* requirement in the same file.

This is drift in `openspec/specs/`, not in `docs/`: the ruleset itself has been correct and consistent since `DMG-005` was written. Nothing here corrects a rule — it corrects a spec that fell behind the rule it is supposed to mirror.

## What Changes

- **`damage-resolution`'s *Damage Roll* requirement** — `OK` / `TOUCHED` / `DESTROYED` become `Operational` / `Wounded` / `Dead` in the requirement text. Neither of its two scenario bodies names a state, so neither needs a wording change; both are carried through unrenamed per `system/workflow.md` ("Scenario names are identifiers").
- **`damage-resolution`'s *Repairs* requirement** — same substitution, in the requirement text and in both scenario bodies. The two scenario headings — `Repairing a touched component` and `Destroyed components cannot be repaired` — keep their exact wording; only the body of each is corrected.
- **One `MODIFIED` delta**, at `specs/damage-resolution/spec.md` in this change directory, covering both requirements. Every scenario the living spec currently has for either requirement is carried through, per `scripts/check_delta_coverage.py`.

## What Does Not Change

- **`docs/`.** `16-damage-system.md` already reads `Operational` / `Wounded` / `Dead` throughout (`DMG-005`, `DMG-015`, `DMG-019`). No `docs/*.md` file is touched by this change.
- **No rule ID moves.** `DMG-015` and `DMG-019` are unaffected; this change touches only `openspec/specs/damage-resolution/spec.md`, which has no rule IDs of its own.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only, per `system/documentation-standards.md` (Versioning). No `**Bump:**` line: this is a spec-only correction with no `docs/*.md` change to bump.
- **Every other requirement in `damage-resolution`.** *Attack Roll*, *Select Target Component*, *Composite Vehicle Targeting*, *Geometry Check*, *Multiple Independent Impacts*, *Penetration*, and *Weapon Distribution* already read `Operational` / `Wounded` / `Dead` (or name no state at all) and are left alone.
- **Scenario names.** No scenario in either modified requirement is renamed; only the two that named a stale state get their body corrected.

## Checked elsewhere

`grep -rn "OK\|TOUCHED\|DESTROYED" openspec/specs/` was run against the whole `openspec/specs/` tree before writing this proposal. Every hit is inside `openspec/specs/damage-resolution/spec.md`, in the two requirements this change corrects. No other capability (`action-economy`, `component-damage`, `geometry-layers`, `unit-base`, `weapon-capacity`, `weapon-construction`) carries this vocabulary — `component-damage`'s own state-machine requirement already reads `Operational` / `Wounded` / `Dead` throughout. No second delta is needed.

## Out of Scope

- **Any mechanical change to the Damage Roll or to Repairs.** `DMG-015`'s 4-5-6 / 1-2-3 threshold and `DMG-019`'s Action Point cost are unchanged; only the names of the states are corrected.
- **Restating `DMG-019`'s "1 Action Point, once per activation" into the Repairs requirement.** The living requirement does not carry that detail today and this change does not add it.
- **Adding, removing or renaming any scenario.** Both requirements keep exactly the scenarios the living spec already has for them.
