## Context

`delete-me-melee-org.md` proposed making melee a special case of the standard combat system rather than an independent subsystem — a good goal, already partially true in the shipped ruleset (`12-melee.md`'s own Purpose already said melee uses the same Impact-based philosophy). But the RFC's own artifact had a structural flaw that had to be fixed before any of its content could ship: it silently renumbered existing rule IDs.

## Goals / Non-Goals

**Goals:**
- Apply the RFC's actual mechanical intent (melee generates Impacts the same way ranged does, one Attack Die per independently-wielded weapon, resolution fully shared) without breaking rule-ID stability.
- Close the Impact Strength gap the RFC's own resolution-sharing goal exposes but doesn't solve.

**Non-Goals:**
- Reworking `10-weapons.md`'s ranged-specific construction rules (Weapon Front Footprint, muzzle placement, Weapon Proportion) to formally accommodate melee weapons beyond what's needed for Impact Strength. Melee weapons already had a construction identity (WPN-001/WPN-002's "functional striking end" reference); this proposal only formalizes it where the RFC's resolution-sharing goal requires it.

## Decisions

### Map RFC content to existing rule IDs by subject, not by the RFC's own sequential numbering

**The RFC's `MEL-001`–`MEL-009` do not correspond to this repo's existing `MEL-001`–`MEL-012`.** For example, the RFC's `MEL-006` ("Component Targeting") is, by subject, a rename of the *existing* `MEL-002` ("Eligible Targets") — but the existing `MEL-006` is "Multiple Combatants," an unrelated rule the RFC never mentions. Applying the RFC literally (writing new content at `MEL-001` through `MEL-009` per its own scheme) would have silently overwritten `MEL-002` through `MEL-009`'s current meaning and orphaned `MEL-010`, `MEL-011`, `MEL-012` — a direct violation of this repo's "rule identifiers should remain stable" convention (`system/documentation-standards.md`), and the kind of mistake `WPN-002`'s existing cross-reference to `MEL-003` would have made instantly stale and wrong (it currently cites `MEL-003` for a "functional striking end" concept that the RFC's own `MEL-003` doesn't define at all — it defines something else).

Verified via `grep -rn "MEL-[0-9]"` across the repo: `10-weapons.md` WPN-002 is the only external cross-reference to a specific `MEL-` ID (`MEL-003`), confirming the blast radius of getting this wrong was small but real. Every rule below was placed at the ID whose *existing content* it most closely replaces, and two genuinely new concepts (Functional Striking End, Weapon Reach) were appended as `MEL-013`/`MEL-014` rather than slotted into the RFC's numbering.

### MEL-002 absorbs MEL-010's duplicate target list instead of the reverse

The existing `MEL-002` ("Eligible Targets") and `MEL-010` ("Component Attacks") already overlapped before this RFC — both listed valid melee target types, `MEL-010` narrowed to vehicle components specifically. This is the same "same fact, two documents" pattern `ruleset-consistency-fixes` fixed repeatedly, just internal to one document this time. `MEL-002` (renamed "Component Targeting") becomes the single canonical target list; `MEL-010` is reduced to a one-line cross-reference, keeping its ID stable rather than deleting it.

### Melee needs a defined Impact Strength source — closed via a sized, non-round Functional Striking End

**This is the one place this proposal adds real content the RFC didn't specify at all.** The RFC's `MEL-005` (Standard Combat Resolution) routes every melee Impact through the Geometry Check (`16-damage-system.md` DMG-014), which compares Impact Strength against Resistance — but neither the RFC nor the previously-shipped melee doc ever defined what Impact Strength a melee attack carries. This was a silent blocking gap: applying the RFC as written would have made melee combat impossible to resolve at the Geometry Check step.

**Confirmed with the user**: a functional striking end is sized exactly like a muzzle (1×1 through 4×4, `10-weapons.md` WPN-021's existing table) — reusing the existing mechanism rather than inventing a new formula (alternatives considered: fixed Impact Strength 1 for all melee weapons; deriving strength from Weapon Width per WPN-018). The one deliberate difference from a muzzle: a striking end is **not** required to be built from round pieces. `WPN-002`'s round-only requirement was justified in `ruleset-consistency-fixes` Finding 9 specifically by ranged-barrel realism ("real weapon barrels are round") — that reasoning doesn't transfer to a blade or spear point, so extending the round-only constraint to melee would have been a new, unjustified restriction, not a simplification.

**Multiple striking ends on one weapon (e.g. a double-ended staff) don't multiply Impact Strength or Attack Dice.** Since `MEL-003` decouples Attack Dice count from striking-end count (one weapon = one die, regardless of ends), a weapon with two differently-sized ends needs a rule for which size applies. Resolved as: the attacker declares which end delivers the Impact for that attack. This preserves the RFC's simplification (still one die, one weapon) while giving multi-ended weapons a coherent reason to exist (tactical flexibility — choose the sharp end or the blunt end — rather than being strictly worse than two separate single-ended weapons).

**Unarmed attacks are explicitly Impact Strength 1** (`MEL-008`) — the weakest defined value, representing bare-handed force. Neither the old rule nor the RFC stated this; it falls out of the same gap as the striking-end case and needed the same explicit fix.

### WPN-021 generalizes to "muzzle or functional striking end" rather than melee getting its own Impact Strength rule

Alternative considered: define Impact Strength for melee entirely within `12-melee.md`, independent of `WPN-021`. Rejected — this is the exact "same rule, two documents" duplication this repo's review process exists to catch. `WPN-021`'s size→strength table is already piece-shape-agnostic in substance (it never actually required the piece be round; `WPN-002` owns the shape constraint separately) — generalizing its one sentence to "muzzle or functional striking end" and citing `MEL-013` costs less than restating the table a second time.

## Risks / Trade-offs

- [Risk] The Attack Dice mechanic change (per-weapon, not per-striking-end) is a real gameplay change, not a pure consolidation — a previously-legal double-ended staff build now generates 1 Attack Die instead of 2. → Mitigation: this is the RFC's explicit, deliberate intent ("Removed Rules: Weapon-end counting"), not an accidental side effect of consolidation; the multi-end "attacker chooses which end strikes" rule keeps such builds meaningful rather than making them strictly worse.
- [Risk] Two new rule IDs (`MEL-013`, `MEL-014`) and one generalized existing rule (`WPN-021`) add surface area beyond what the source RFC specified. → Mitigation: without them, `MEL-005`'s core claim ("melee fully shares ranged's resolution sequence") would be false at the first step that needs Impact Strength — the gap had to be closed for the RFC's own stated goal to hold.

## Open Questions

None outstanding.
