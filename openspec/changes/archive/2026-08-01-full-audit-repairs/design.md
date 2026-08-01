## Context

`delete-me-audit.md` is the deepest audit run against this ruleset so far — 35 findings across contradiction, omission, and duplication categories, several of them genuinely game-blocking (no AP cost for the two most common actions in the game) rather than editorial. Six findings required an actual design decision; the user was asked directly rather than defaulted, and every answer selected was the recommended (simplest, no-new-mechanic) option.

## Goals / Non-Goals

**Goals:** Close every blocking gap the audit found; resolve every direct contradiction; reduce every duplication to a single owning statement — using the same "cross-reference the owner, don't restate" pattern this repo has applied consistently since `ruleset-consistency-fixes`.

**Non-Goals:** Inventing full systems for the two large omissions that are legitimately future work (vehicle-terrain interaction, structure damage/collapse) — these get an honest scope acknowledgment, not an improvised ruleset.

## Decisions

### A-01: Dead is always a removal, no exception

**Alternative considered**: let a Dead minifig remain on the table (lying down), either blocking movement/Line of Sight/Cover like a standing model, or purely as inert scenery. Rejected — `DMG-006` ("no dead component remains on the battlefield") is the universal rule every other component already follows without exception (a destroyed wheel, door, or weapon is removed, full stop); carving out an infantry-specific exception would reintroduce exactly the "infantry has its own rules" problem `ruleset-consistency-fixes` Finding 1 already eliminated. Simpler, and consistent with the rest of the Component State machine.

### A-02: Resistance measured in plate layers, not bricks — DMG-004's examples recalculated, not just relabeled

The original bug wasn't just inconsistent units — it was that "1 brick = Resistance 1" and "4 plates = Resistance 4" implied a *thinner* stack of separate plates was four times more resistant than a *thicker* single-brick wall, which is backwards. Recounting in plate layers (1 brick = 3 plates) fixes the ordering, not just the label: a brick-built shield is now Resistance 3, correctly sitting between a 2-plate wall (Resistance 2) and a 4-plate stack (Resistance 4). This is a real value change for Example 3 (1 → 3), not a cosmetic unit swap — confirmed as the user's intent when they picked "plate layers" specifically over "bricks" as the finer-granularity option. Example 1 (Minifig) and the Combat Examples that depend on it are unaffected because a minifig is illustratively built 1 plate thick either way.

### A-03: No decision needed — the "ceiling" was a documentation bug, not a missing mechanic

`WPN-002`'s 1×1 through 4×4 muzzle-size list read as an exhaustive range, but nothing in its own logic actually bounds it — muzzle size is limited only by the Weapon Front Footprint (`WPN-019`), which scales with Weapon Width, which scales with Weapon Length (`WPN-018`, `Length ≥ 2 × Width`), which scales with Platform Length (`WPN-004`) — none of which have a maximum. The user pointed this out directly. Once `WPN-002`/`WPN-021` are reworded to say the size list is illustrative and Impact Strength has no maximum, the "any Resistance ≥ 5 is unconditionally invulnerable" problem dissolves on its own: a big enough weapon can always be built to threaten it, at the cost of needing a big enough platform to carry that weapon. This is a physical arms-race tension (bigger guns need bigger platforms), not a broken mechanic requiring a new rule — no Resistance cap, no dice-overflow exception, and no separate "widen the scale" hack were needed, just accurate wording.

### A-04/CORE-009: reworded to target-symmetry, not reaction fire

**Alternative considered**: implement real reaction fire (an activated unit spends reserved AP, or a limited reaction, to fire outside its own turn). Rejected as the user's choice — it's real new complexity for a rule that was only ever an unfulfilled promise; `CBT-014` already correctly flags Reaction Fire as a possible *future* extension, meaning the gap was already known and deliberately deferred. Rewording `CORE-009`/Principle 9 as symmetry ("if it can see you, you can be its target during its own activation") preserves the intended narrative beat (mutual visibility matters) without promising a mechanic that doesn't exist.

### A-05: melee's simultaneous-resolution rule no longer implies a free counter-attack

**Alternative considered**: define a real counter-attack (automatic, 1 AP from the defender's own reserve even post-activation). Rejected as the user's choice — `MEL-004`/`CBT-010` already existed and were internally consistent about *how* to resolve two simultaneous attacks; the actual bug was that nothing ever granted the second attack in the first place. Scoping the rule to "governs resolution order for attacks that are *already* both declared" (rather than "melee is always mutual") removes the false promise without deleting the resolution-order rule itself, which remains useful for whatever future rule (a scenario, a charge mechanic) might legitimately produce two simultaneous attacks.

### A-06/A-07: shields and cover reduced to what the Component Damage System already provides

Both followed the same shape: a rule promised a defensive effect, and the actual damage-resolution system never implemented one. Rather than inventing a bonus for either (a defense-dice mechanic for shields, a cover-level bonus for partial/heavy visibility), both were reduced to cross-references to mechanisms that already exist and already do real work — `DMG-007` (Internal Components) for shields, `DMG-012` (visible-only targeting) for cover. This is the same resolution already used for `CBT-012`/`CORE-010` earlier in this repo's history (Finding 11) and for Armour here (A-08) — a phantom promise reduced to the real underlying mechanism, not a new one invented to match the promise.

### A-08: Armour redefined as Resistance's colloquial name, spelling unified

`CBT-013` named a system ("Armour... via the Geometry Check and Damage Roll") that doesn't exist anywhere in `16-damage-system.md` under that name — only `Resistance` does. Rather than either deleting the term or inventing a distinct Armour mechanic, `CBT-013` now says directly that Armour *is* Resistance, colloquially named — matching how the ruleset already uses "Armor Plate" as an example component whose Resistance happens to be high. Spelling unified to UK "Armour" since it was already the majority convention (four documents) versus US "Armor" (two documents, both more recently-written mechanical docs) — picked the spelling used by the player-facing rule documents.

### B-01/B-02/B-05: AP costs set to 1, matching the established pattern, not asked

Every other timed action in the shipped ruleset already costs exactly 1 AP: doors, ramps, infantry rotation (`MOVE-008`), embarking, interactive terrain. Move and Attack having no stated cost was an omission, not an unresolved design question — there's no plausible alternative value that wouldn't contradict `FLOW-007`'s own worked example ("Move, Move, Attack" spending a normal 3-AP activation implies 1 AP each). Set directly without asking, unlike the six items above which had no existing precedent to lean on.

### B-03/B-04: "Stand up" and Repair are the same action

No other "prone" or posture-change mechanic exists anywhere in the ruleset besides Wounded-is-seated. `CORE-006` listing "Stand up" as a distinct AP-consuming action, next to `DMG-019`'s separately-stated "Repairing consumes Action Points... Wounded → Operational," is almost certainly one mechanic described twice under different names in two different documents — the same duplication class this whole review effort has been finding all along, just crossing from a rules document into a summary list. Cross-referenced rather than treated as two separate gaps.

### B-06: embark/disembark AP source and per-unit activation, resolved via the existing activation model — not a new one

The audit's real concern was whether an embarked passenger still needs its own activation, which would make a Turn with transports impossible to complete under `FLOW-002`'s "every unit activated once" rule. Resolved without inventing anything: embarking *is* the embarking unit's activation (it spends its own AP, from its own 3-AP pool, and its turn is done) — the same is true of disembarking, which a still-embarked unit performs at the start of its own activation, spending remaining AP from the same pool to move or attack afterward. Every unit still gets exactly one activation; it just may spend that activation getting in or out of a vehicle instead of moving under its own power. Also fixed the flagged AP asymmetry (embark flat 1 AP vs. disembark 1 AP/UB) by making embark scale per UB too — no reason for the two mirror-image actions to cost differently.

### B-07: uneven-army alternation

Standard resolution used by most alternating-activation skirmish games: once a player runs out of unactivated units, the other continues activating consecutively. No plausible alternative preserves playability (forcing symmetric pass-turns would make the game literally unplayable with uneven forces, which `DEP-002` already explicitly allows) — set directly, not asked.

### B-08/B-10: acknowledged as scope gaps, not solved

Vehicle-terrain interaction and structure damage/collapse are large enough that inventing them here would be a real new ruleset addition disguised as a documentation fix. Both get an honest note pointing at the general principle that already covers the *individual-component* case (a building's door/window still resolves Impacts normally; a vehicle can still use Physical Priority for terrain questions the model can answer) while being explicit that the *system-wide* consequence (collapse, movement penalties from obstacles) isn't defined yet. This mirrors how `MAT-007`/`MAT-008` (wheels/tracks, before their removal) used to defer to "future vehicle rules" for movement penalties — an established, honest pattern for scoped gaps in this ruleset.

### B-11: penetration into closed-transport passengers, resolved via existing DMG-007

`TRN-010`'s "cannot be targeted directly" only ever governed initial target *selection* — it never addressed penetration, which is a separate mechanic (`DMG-017`) that already generalizes to any Internal-Components relationship (`DMG-007`'s own example is Armor → Pilot). Treating a transport's hull as protecting its passengers exactly the same way any component protects one behind it resolves the gap using the mechanism that already exists, rather than a transport-specific exception.

## Risks / Trade-offs

- [Risk] A-02's Resistance recalculation changes actual example values (Example 3: Resistance 1 → 3), which is a real mechanical change disguised inside a "unit consistency" fix. → Mitigation: confirmed as the intended effect of the user's own answer ("plate layers" specifically chosen over "bricks"), and the only downstream worked example that referenced it by exact value (Combat Example 4, Jeep Cannon) was checked and doesn't depend on Example 3's number.
- [Risk] Several fixes (B-01, B-02, B-05, B-07) set new default values without asking, unlike A-01–A-07. → Mitigation: each has a clear, singular precedent already established elsewhere in the shipped ruleset (every other timed action costs 1 AP; standard alternating-activation games resolve uneven forces the same way) — these aren't open design questions, they're omissions with only one plausible fill-in.

## Open Questions

D-08 (stray `delete-me-*.md` files) is left for the user — these files aren't tracked by git and aren't part of the ruleset, so removing them isn't a documentation change this proposal should make unilaterally.
