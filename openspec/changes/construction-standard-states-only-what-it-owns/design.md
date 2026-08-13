# Design — Construction Standard states only what it owns

## The test each rule was put to

A rule stays in `docs/04-construction-standard.md` only if it answers:

> **What must physically be built for this to be legal?**

and no other `docs/*.md` rule already answers it. A rule that answers "what does the built thing do during the game" belongs to the document that owns that behaviour. A rule whose whole body is a pointer at another rule answers nothing.

Both halves matter. Applying only the first would have retired `SCS-015` and `SCS-018` for being weapon-shaped while keeping them for being physical; applying only the second would have retired `SCS-016` and `SCS-017`, which are physical **and** unowned.

---

## Decision 1 — `SCS-004`'s legality sentence moves to `CORE-002` rather than staying in the Construction Standard

`CORE-002` says every unit *has* a facing and that a vehicle's front comes from its construction. It never says a model whose front cannot be read is illegal. That sentence is real and had one owner.

The requirement moved; the second sentence did not. `CORE-002` gains "Every model must have an obvious front." and not "Models with ambiguous fronts are not legal.", because the second is the first negated rather than a reason for it — `system/documentation-standards.md` ("How a Rule Is Written") allows one imperative sentence and one clause of reason. The "must" carries the same force, so nothing is left undecided.

**Rejected: keeping `SCS-004` as one trimmed sentence.** It would have left the ruleset answering "which edge is the front" in `CORE-002` and "must there be a readable front at all" in a different document, which is the split this change exists to remove. A reader who needs one needs the other.

**Consequence:** `docs/14-glossary.md`'s *Facing* entry cited `CORE-002` **and** `SCS-004`; it now cites `CORE-002` alone, which states both halves.

## Decision 2 — `SCS-023`'s visibility clause moves to `CORE-008`; its mechanical clause is deleted, not moved

`SCS-023` said three things. Two already had owners:

- *"Resistance and the Geometry Check determine whether they stop an Impact — the same as any other component."* `DMG-008` states this as its whole subject, and names glass first: "Every component follows exactly the same mechanical rules regardless of what it represents — glass, metal, wood, infantry, or anything else."
- *"Transparent LEGO pieces represent transparent materials"*, with glass and cockpit canopies as examples. `SCS-009` states the same thing for the case that carries a rule — transparent elements represent windows — and `CMP-011` and `TRN-012` both cite `SCS-009` for it. The example list also carried "Energy shields (future)", which `system/documentation-standards.md` ("How a Rule Is Written") excludes: no section for a case that does not exist yet.

One did not: **visibility passes through transparent pieces.** It moves to `CORE-008`, the universal Physical Visibility rule, which every visibility question in the ruleset already routes through — `CBT-002`, `WPN-012`, `TRN-009` and `TRN-012` all cite it.

**Rejected: moving it to `CBT-002`.** Line of Sight in combat is one consumer of visibility, not its owner; `TRN-012` asks the same question about passengers and would then cite a combat rule.

## Decision 3 — `SCS-005` folds into `TRN-019` rather than becoming a new `GEO` rule

`TRN-019` opens by stating the fit rule and citing `SCS-005` for it: "What must fit inside a vehicle is the Unit Base itself rather than the loose model." The only clause `SCS-005` carried that `TRN-019` did not is the gap case — a model that would slip into a gap smaller than its Unit Base does not fit there — and it is added to `TRN-019` here.

**Rejected: a new rule in `15-geometry-layers.md`.** It would mint a rule ID to hold a sentence one existing rule already opens with, and `GEO`'s subject is which geometry a value is read from, not what must fit where.

**Accepted narrowing, and it is a real one.** `SCS-005` stated the fit rule for everything — passengers, cargo, vehicles, buildings, terrain — and `TRN-019` is transport-scoped. Nothing in `docs/` will state it in general afterwards.

That is deliberate, and it needs saying plainly because the general statement used to live in `CORE-001` and was deleted one change ago (`core-states-only-what-it-owns`) **on the ground that `SCS-005` owned it**. Retiring `SCS-005` now is the second half of a hand-off, so the residue has to be checked rather than assumed. It was:

- **Inside a transport** — `TRN-019`, which states it and gains the gap clause here, and `DEP-005`: "If a Unit Base fits inside the vehicle, a minifigure may be transported in it. If it does not fit, it cannot. The LEGO model is the source of truth."
- **In a crew position** — `VEH-015`: "Crew must physically fit inside the vehicle. A crew member occupies a Unit Base like any other passenger, so what must fit is that Unit Base."
- **Through an opening** — `CMP-018`: what must pass is the model's Unit Base, not the loose plastic, resolved against the plastic as built (`GEO-004`).
- **On the battlefield** — `DEP-001`, which bounds an army by the agreed Deployment Volume in Unit Bases.

Those are the four places a `docs/` rule asks whether something fits. Each states the rule for its own case, and `TRN-019` is the only one that cited `SCS-005`.

**One thing this check found and this change does not fix.** `VEH-015` and `DEP-005` both cite `CORE-001` for the "what must fit is the Unit Base" formulation, and `CORE-001` stopped containing that sentence one change ago. Both still read correctly — `CORE-001` defines the Unit Base, which is what they measure against — but the citation aims at a sentence that is no longer there. It is a `08-vehicles.md`/`06-deployment.md` repair rather than a Construction Standard one, and `proposal.md` records it in Out of Scope so the next reader inherits it.

**Rejected: restoring a general clause to `CORE-001`.** It would reverse a decision taken one change ago and put back the restatement that change removed. The universal form of the principle is `CODE_OF_DESIGN.md` Principle 1 — the model is the rules — and it is stated there rather than in a rule, which is the right altitude for a sentence with no consuming rule of its own.

## Decision 4 — `SCS-015` is retired and `WPN-009` is left alone

They state the same two sentences. One of them had to go, and the choice is not symmetric: `WPN-009` also carries the list of valid mounts (hands, turrets, hull, pintle, side), and `VEH-030` and `WPN-003` cite `WPN-009`, while nothing cites `SCS-015`.

**Rejected: trimming `WPN-009` to the mount list and keeping `SCS-015` as the requirement.** It splits one rule across two documents, retargets two live citations, and leaves `10-weapons.md` unable to state its own mounting rule without a cross-reference.

## Decision 5 — `SCS-016` and `SCS-017` stay, though both are about weapons

The test is ownership, not subject matter.

- `WPN-002` defines what a functional muzzle *is*. **No `10-weapons.md` rule says a weapon must have one.** `SCS-016` does.
- No rule in `10-weapons.md` requires a muzzle to be connected to a weapon body. `WPN-018` constrains the body's proportions and `WPN-003` measures it, both assuming the connection `SCS-017` requires. `docs/14-glossary.md`'s *Weapon Body* entry cites `SCS-017` first.

Both are exactly the kind of rule the document should hold: a physical requirement the model must satisfy, with no gameplay value attached.

## Decision 6 — `SCS-018` is retired even though the brief for this change asked to keep it as a construction rule

`WPN-019` already states the requirement in full: "Every weapon has exactly one Weapon Front — the only face from which the weapon may fire. Muzzles may not be placed on the rear, side, top, or bottom faces." `SCS-018`'s first paragraph restates that sentence; its second is a pointer at `WPN-007` and `WPN-020` for adjacency.

A construction-only `SCS-018` is empty. Retiring it is the same judgement that retires `SCS-019` and `SCS-020`, and applying it inconsistently is what would need defending.

## Decision 7 — `DMG-008`'s citation drops to `CORE-016` alone

`DMG-008` currently says cosmetic representation is "left entirely to the player and the table, per `02-core-rules.md` (CORE-016) and `04-construction-standard.md` (SCS-024) — this document does not prescribe it."

The Damage System explicitly declines to own it, so the source brief's assignment of `SCS-024` to the Damage System is not available. `CORE-016` owns it: "Whenever possible, changes in game state should be represented by modifying the model itself. StudCraft always prefers physical representation over markers." `SCS-024` restated that for the damage case and added four examples, which `01-foundations.md` and `MEL-011` also carry.

## Decision 8 — the AP cost leaves `SCS-007` and `SCS-008` but stays in `CMP-009` and `CMP-010`

`CORE-007` owns the cost. Four rules restate it. `SCS-006` already delegates correctly ("What operating one costs is defined in `02-core-rules.md`, CORE-007"), so `SCS-007` and `SCS-008` restating a number two rules down is the defect this change is scoped to.

`CMP-009` and `CMP-010` had the same defect and were left standing, recorded in `proposal.md` (Out of Scope) so the next reader would inherit the finding rather than rediscover it.

**The review of #104 asked for them, and they are now in — tasks 18.4 and 18.5.** The reviewer's reasoning is the one this decision deferred to a later change: `CORE-007` owns the generic interaction cost, and a component rule establishes that the component physically exists and can operate. `MOVE-018` and `MOVE-019` were already the model — they name the cost's owner without repeating its value. Nothing else in `05-construction-components.md` is touched; `CMP-018`, which the same review calls out as overlong, stays Out of Scope.

## Decision 13 — `SCS-010`, `SCS-011` and `SCS-012` lose their delegation sentence

Each ended by naming `07-movement.md` as the owner of its gameplay consequence. The review of #104 asked for all three to go, and the reasoning holds: `SCS-010` says walls must be physically built, and that is the whole rule. A reader does not learn where the movement rule lives from a sentence saying it is elsewhere — they learn it from `07-movement.md`, which states it.

This is not the same as the pointers this change **kept**. `SCS-002` cites `CORE-001` because it uses the Unit Base to state its own requirement; `SCS-006` cites `CORE-007` because "what operating one costs" is a question the rule raises and does not answer. `SCS-010`'s deleted sentence raised no question — it disclaimed one.

**Nothing replaces the deleted lines.** `VEH-027` cites `SCS-011` and `SCS-008` for their physical requirements, which survive untouched.

## Decision 9 — no spec delta

`openspec/specs/` describes behaviour, not which document states it. Thirteen rules are retired and every sentence they carried is left standing at its owner, so no requirement and no scenario stops being true. The four sentences that move are equally true at their destinations: the front-must-be-obvious requirement at `CORE-002`, sight passing through transparent elements at `CORE-008`, shield orientation at `CMP-014`, and the gap clause at `TRN-019`.

## Decision 10 — nothing is renumbered

`system/documentation-standards.md` (Naming Conventions) makes rule identifiers permanent: never renumbered, never reused, and a deleted rule's number is retired with no stub left in its place. After this change `04-construction-standard.md` runs `SCS-002`, `006`–`013`, `016`, `017` with visible gaps, and that is the intended result. `scripts/check_id_stability.py` reports a moved or reused ID and deliberately does not report a deleted one.

The source brief asked for renumbering "if the repository's numbering convention requires it". It requires the opposite.

## Decision 11 — `TODO.md` moves with this change; `system/proposal-review.md` does not

Both cite text this change edits, and they are not the same case.

`scripts/check_todo_quotes.py`, which `scripts/preflight.py` runs, compares every `TODO.md` blockquote character for character against the document it cites. Two entries quote text edited here, so a `docs/`-only application of this change **fails its own verification**. The coupling is mechanical, and the archived `wounded-degrades-capability` change set the precedent: task 9.1 there edited `TODO.md` from a proposal branch for exactly this reason. No gate forbids it — `Branch name follows the convention` requires only that the branch is named for its change, and `Docs require OpenSpec proposal` only that the proposal exists.

`system/proposal-review.md:182` cites `SCS-003` in a worked example. Nothing checks `system/` against `docs/`, the line is prose rather than a quote, and repairing it is a `system/` edit that needs a branch and no proposal. It goes on its own.

**The *Energy shields* entry is deleted rather than re-sourced.** Its whole subject is `SCS-023`'s "Energy shields (future)" example, and after this change no document mentions an energy shield. `TODO.md`'s preamble scopes it to gaps "the ruleset acknowledges in its own text"; an entry whose declaring text is gone no longer meets that. The gap was announced by a speculative example that `system/documentation-standards.md` ("How a Rule Is Written") excludes from a rule anyway — removing the example removes the declaration, and `proposal.md` records that this change made the choice.

## Decision 12 — `SCS-022`'s orientation sentence moves to `CMP-014`

`CMP-014` covers everything else `SCS-022` said, and says it better: carried by infantry, physically attached, visible, one hand, targetable or interposing exactly like any other component, no bonus beyond being in the way. It does **not** say which way a shield has to face.

That matters beyond the shield rule. `CORE-002`'s `Facing determines:` list ends with `Shield direction`, and the previous change kept that bullet on the explicit ground that nothing else owns shield direction and the glossary's *Facing* entry cites `CORE-002` for it. `SCS-022` was the text that gave the bullet a meaning. Deleting it outright would leave `CORE-002` and the glossary pointing at a term the ruleset no longer explains.

The sentence lands in `CMP-014`, next to the interposition it qualifies.

**Rejected: keeping `SCS-022` as a trimmed rule.** What survives is not a construction requirement — it is which component the attacker's Impact meets first, which is geometry, and `CMP-014` already states the geometry half.

**Corrected after the applied text was audited (task 17.1).** The sentence first written into `CMP-014` ended "This is the `Shield direction` that `02-core-rules.md` (CORE-002) determines", which equated two tests that disagree: what a shield physically stands between, and the Facing a unit's base declares. A shield on a minifigure's left arm interposes against a westward attacker while the model faces north. `SCS-022` never claimed otherwise — it said orientation matters "for this reason, not for any separate defensive bonus" — and the corrected sentence says only that. Whether `CORE-002`'s `Shield direction` bullet is right is a `02-core-rules.md` question, recorded Out of Scope.
