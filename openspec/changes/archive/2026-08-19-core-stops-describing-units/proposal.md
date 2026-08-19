# CORE stops describing units

## Why

`docs/02-core-rules.md` is the document a player prints and keeps on the table. It owns the Unit Base, the Action Point economy, Line of Sight, Cover and the physical-representation principle — the anchors every other document reads.

It also still says what an infantry base is built from, which edge of it faces front, how a vehicle's front is decided, and how many hands a minifigure has.

Those are unit rules, and both unit domains now exist to hold them. `docs/17-infantry.md` was created for exactly this, `docs/08-vehicles.md` has held vehicle construction since it was written, and `docs/10-weapons.md` already states which weapons need one hand and which need two — today by citing `CORE-015` as though CORE owned the answer.

The narrow purpose this change enforces:

> **CORE defines the universal anchors every system consumes. What a unit is, how it is built and what it carries belong to that unit's domain.**

`CODE_OF_DESIGN.md` Principle 10 states it as one clear responsibility per document, and Principle 12 as consistency: `CORE-003` and `CORE-004` already defer to their domains, and the rules around them do not.

## What Changes

Five documents. **One rule is retired; nothing is renumbered.**

- **`CORE-001`** — loses one sentence, the one describing the physical base an infantry model is built on. The volume, the plate-layer conversion, the height datum and the `W × D` footprint reading all stay: sixteen rules cite `CORE-001` and every one of them reads it for those.
- **`CORE-002`** — becomes one universal rule. Every model must have an obvious front, and facing is read from the model. The infantry block ("the 4-stud side of the base") and the vehicle block ("determined by the vehicle construction") go to the domains that already own them. The six-item **Facing determines** list goes too: `MOVE-001` owns which directions a unit has, and firing arcs are Combat's.
- **`CORE-004`** — reworded to match `CORE-003`. Both now name their domain and stop there. The pointer at `08-vehicles.md` stays; it is the vehicle half of the symmetry.
- **`CORE-009`** — keeps the principle and nothing else. "If you can see it, you can shoot it."
- **`CORE-015`** — **retired.** Its number is never reissued and no stub replaces it.
- **`INF-001`** — states the base an infantry model is built on and which edge is its front, instead of deferring both to CORE and getting an infantry-specific answer back. It also gains the hand count, because hands belong to the minifigure and the minifigure is Infantry's; `CMP-014` and `WPN-010` cite it rather than each asserting "two hands" separately. `17-infantry.md`'s Summary moves with it.
- **`docs/14-glossary.md`, the *Facing* entry** — reproduces the six-item list `CORE-002` loses, "the left and right sides" included, which `MOVE-001` already established is not universal. A glossary entry is a restatement and is checked in the same pass as the rule (`system/proposal-review.md`).
- **`CMP-014`** — owns a shield occupying one hand. A shield is not a weapon; it is cover, and cover is a component.
- **`WPN-010`** — states one-handed and two-handed weapons on its own authority instead of borrowing CORE's.

## What Does Not Change

- **No gameplay value.** The Unit Base is still `4 × 3 × 13`. An infantry base is still `4 × 3` studs and one plate. The 4-stud edge is still the front. A shield still occupies one hand, a rifle still occupies two. Nothing about facing, visibility or cover resolves differently.
- **`CORE-006`'s allotment.** Three Action Points per activation, the action list, and that no unit gains AP through its profile. Eight rules cite `CORE-006` for those and none is affected.

  **Its size paragraph does not stay**, though an earlier draft of this proposal said it would. The maintainer decided it goes: a prohibition on pricing by size guards against something no rule does, and an exception cannot be made to a scheme that is never established. `TRN-005` and `TRN-006` keep their flat cost and stop sourcing it from CORE. This is the change's only capability delta — `design.md`, Decision 8.
- **`CORE-014`.** It is the equipment anchor: equipment must be physically represented, and a unit cannot use what is not on the model. That is universal and stays.
- **`CORE-005`, `CORE-007`, `CORE-008`, `CORE-010`, `CORE-016`** and the `Universal Rule` section.
- **No rule ID is renumbered or reused.** `CORE-015` is retired and `CORE-016` is not moved into the gap.
- **`openspec/specs/`** — one `REMOVED` delta against `action-economy`, and only that. The scope cleanup that is the rest of this change owes none: it moves sentences between documents and no requirement or scenario stops being true (`design.md`, Decisions 6 and 8).
- **`CHANGELOG.md` and every version header.** Release-cut-only.

## Checked elsewhere

- `python3 scripts/rule.py refs CORE-001 CORE-002 CORE-015 CBT-014` — every inbound citation was read against the text that survives. `CORE-001`'s sixteen citers read it for the volume, the conversion or the footprint; only `INF-001` read it for the base, and this change moves that. `CORE-002`'s citers read it for facing existing, not for how each domain decides one. `CORE-015` has exactly two citers, `CMP-014` and `WPN-010`, and both are re-aimed.
- `grep -rn "CORE-015" README.md TODO.md CODE_OF_DESIGN.md system/ assets/` — no hit outside `docs/`. Retiring the ID strands nothing.

## The one thing that gets quieter

**`CBT-014` ends this change cited by nothing.** `CORE-009` was its only citer, through the sentence this change removes.

That is the intended result rather than a side effect. Whether StudCraft has reaction fire is a combat question, and `11-combat.md` answers it by listing Reaction Fire among the extensions it does not yet have. `system/proposal-review.md` distinguishes the two cases: standalone is legitimate, disconnected is a defect. `CBT-014` is standalone — it is the list of things Combat has not built, and nothing needs to point at a list of absences.

## Out of Scope

- **Emptying CORE further.** It stops describing units; it does not stop being the anchor. The Unit Base, the Action Point economy and the physical-representation principle are what the rest of the ruleset reads, and they stay where they are.
- **`assets/IMAGES.md` is repaired here**, not deferred — the maintainer asked for it rather than let the index go stale. `CORE-002`'s row moves to `INF-001` and is renamed, its firing-arc clause dropped with the arcs. `CORE-001`'s and `CMP-018`'s rows are rewritten: **both were already describing rules that had moved on**, specifying a derivation and a *projection* that `core-states-only-what-it-owns` had removed. `scripts/lint_ruleset.py` sees none of it — it checks that a named rule ID exists in the document its section names, and every one of them did. The file records each move and rewrite in its own sections rather than leaving a silent edit.
- **`CMP-018`'s citation of `CORE-002`** for "at least as wide as the model's front edge". After this change `CORE-002` says a front exists and the domain decides which edge it is, so the 4-stud width is one hop further away through `INF-001`. Nothing dangles and the rule still resolves; re-aiming it is a tidy, not a repair.
- **`CORE-016` and `01-foundations.md` overlapping** on physical representation. Recorded before, still true, still separate.
