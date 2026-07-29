## Context

This proposal was drafted as a two-part RFC (structure, then resolution), then reviewed for duplications, omissions, and contradictions against the existing shipped ruleset before being turned into this OpenSpec change. Two things made the review non-trivial:

- `docs/13-materials.md` (MAT-001 through MAT-020) already has a component/material system that partially overlaps with this proposal's Component/Resistance model, but was never reconciled with it in the original draft.
- `docs/11-combat.md` (CBT-001 through CBT-014) predates `weapon-construction-system`'s Impact Strength (WPN-021) and still states outright that weapons never possess "Strength" — a claim this proposal's core mechanism directly depends on being false.

Neither `docs/11-combat.md` nor `docs/13-materials.md` has ever been captured as a formal OpenSpec capability (both predate this repo's OpenSpec workflow), so this change cannot express those conflicts as spec deltas — they're tracked as direct doc edits in `tasks.md` instead, with the rationale kept here.

## Goals / Non-Goals

**Goals:**
- Give every destructible object a construction-derived Resistance, replacing per-material fixed hit counts with one geometric mechanism.
- Define one combat resolution sequence (Attack Roll → Geometry Check → Damage Roll → Penetration) that every weapon/component interaction uses, with no exceptions.
- Reconcile explicitly with `13-materials.md` and `11-combat.md` instead of silently overlapping or contradicting them.

**Non-Goals:**
- Changing Range, Attack Dice, or Impact Strength (`10-weapons.md` WPN-005/006/021) — this proposal consumes those values, it doesn't touch their definitions.
- Cover (`13-materials.md` MAT-016) — explicitly deferred, unaffected by this change.
- Construction rules for rebuilding/repairing a `DESTROYED` component — Repairs (`specs/damage-resolution/spec.md`) only covers `TOUCHED → OK`; rebuilding is future work.

## Decisions

**Components use one universal three-state machine (`OK → TOUCHED → DESTROYED`), no per-type exceptions.**
Alternative considered: keep `13-materials.md`'s per-material state tracks (e.g. infantry's Operational/Wounded/Dead, glass's single-hit break). Rejected as the *only* mechanism, because it means every new material needs its own bespoke hit-count rule forever. Kept as the *description* of what happens physically (a wounded minifig sits, broken glass is removed) — Material still owns that. The universal state machine owns *how many hits it takes*, derived from Resistance.

**Resistance replaces fixed hit-counts, but is designed to reproduce the same outcomes for existing worked examples.**
A typical minifig (thin, Resistance 1) still takes two failed Damage Rolls to go from OK to DESTROYED — the same two-impact result `MAT-004` already asserted — but now because of its geometry, not because "infantry" is hard-coded to take two hits. This was a deliberate constraint during review: the new mechanism had to be able to reproduce the old, already-playtested-in-spirit outcomes, not just replace them with something unrelated.

**A second die roll (Damage Roll) is introduced, separate from the existing Attack Roll.**
Alternative considered: keep combat as a single roll (the existing `CBT-004`/`CBT-005` Attack Roll — 4+ on D6 = Impact), and let the Geometry Check alone decide the outcome deterministically. Rejected: it would make Resistance a hard binary (either an Impact always destroys-in-one-step-eventually or never affects the component at all), removing the "glancing hit" uncertainty that makes engineering a *risk-reduction* choice rather than a hard gate. The Damage Roll keeps geometry as the gate ("can this happen") and dice as the outcome ("did it happen") — mirroring the weapon system's own Attack Roll / Range split.

**Weapon Distribution: rotating mounts may split impacts across targets; fixed mounts may not.**
The original draft's "Weapon Distribution" section contradicted `CBT-007` outright (which bans splitting a weapon system's dice across targets, no exceptions). Rejected leaving the contradiction unresolved. Rejected removing the rotating-mount capability entirely, too — a turret realistically *can* track two different targets with its independent muzzles, and disallowing that would throw away a genuinely construction-derived distinction (free-rotating mount vs. fixed mount) in favor of a blanket rule. Resolution: `CBT-007` gets one explicit exception, gated on physical mount type, which is itself derivable from the model (per "The Model Is The Rules").

**`13-materials.md` and `11-combat.md` are edited directly, not through spec deltas.**
Both documents predate this repo's OpenSpec workflow and were never formalized as capabilities in `openspec/specs/`. There is nothing to write a `MODIFIED` delta against. The wording changes they need (per the Decisions above) are tracked as ordinary doc-edit tasks in `tasks.md`, same as how `weapon-construction-system` touched `docs/04-construction-standard.md` directly without a delta, since that document also isn't an OpenSpec capability.

## Risks / Trade-offs

- [Risk] Two die rolls per Impact (Attack Roll, then Damage Roll) roughly doubles dice-rolling overhead for combat compared to the current single-roll system. → Mitigation: accepted as the cost of removing per-material hard-coded hit counts; revisit only if playtesting shows it's too slow at the table.
- [Risk] `CBT-011`'s wording change (weapons may possess Impact Strength) is a visible reversal of an explicit prior statement, which could read as sloppy if not explained. → Mitigation: `tasks.md` requires the edit to explain *why* (WPN-021 postdates CBT-011; Impact Strength is geometrically derived, not a hidden stat).
- [Risk] Letting rotating mounts split impacts across targets is a new tactical capability, not just a wording clarification — it could shift vehicle-design incentives (e.g. towards turreted secondary weapons) in ways existing playtesting never accounted for. → Mitigation: flagged explicitly as **BREAKING** in the proposal; no further mitigation attempted here, this is a balance question for actual play, not a structural one.

## Open Questions

- Should `Resistance` ever be reduced by prior damage (a `TOUCHED` component being easier to penetrate further)? Deferred — no evidence yet that it's needed, and it would complicate `Penetration`'s remaining-strength formula.
- Does `13-materials.md`'s per-material *flavor* (MAT-012 "Stone usually ignores small-arms Impacts", MAT-014 "Wood is easier to damage") need to be expressed as a Resistance guideline (e.g. typical stone construction implies Resistance N) so it isn't lost? Deferred to the doc-writing task — worth a short non-normative note, not a new requirement.
