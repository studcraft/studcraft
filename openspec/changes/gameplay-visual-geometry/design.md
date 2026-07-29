## Context

The shipped ruleset already behaves as if this split exists — `WPN-003`/`WPN-015` say decorative elements are ignored when measuring Weapon Length, `VEH-003` says the same for vehicles — but no document defines the split itself, names its two sides, or says what happens where the split gets ambiguous (Line of Sight, Cover — both defined in `02-core-rules.md` as direct physical checks against the whole model, not as measured values). This proposal was drafted, then reviewed for internal contradictions before being turned into this OpenSpec change; the review's biggest finding is captured in the Decisions section below.

## Goals / Non-Goals

**Goals:**
- Name and define the two geometry layers (Gameplay Geometry, Visual Geometry) so future rules have one place to check what "measurable" means.
- Resolve, explicitly, how Visual Geometry interacts with Line of Sight and Cover — rules that are physical checks, not measured values, and therefore cannot simply "ignore" Visual Geometry the way Range/Attack Dice/Impact Strength do.
- Define Functional Equivalence precisely enough that it doesn't overclaim (see Decisions).

**Non-Goals:**
- Changing any existing measured rule value or formula (Range, Attack Dice, Impact Strength, Weapon Capacity, Transport Capacity, Movement distance) — this proposal is purely classificatory.
- Defining new physical-check rules — Line of Sight and Cover already exist (`CORE-008`–`CORE-010`); this proposal only clarifies that Visual Geometry participates in them, it doesn't change how they work.
- Picking a final home/document number for this content — see Open Questions.

## Decisions

**Visual Geometry has zero effect on measured rule values, but full effect on physical checks (Line of Sight, Cover).**
Alternative considered: Visual Geometry has zero effect on gameplay, full stop — this was the initial draft's position ("Visual Geometry is always ignored"). Rejected on review: it directly contradicts `CORE-008` ("a target is visible if any part of it can be physically seen... no visibility templates are used") and `CORE-010` ("cover is determined by the physical amount of the model that is hidden") — both defined over the whole physical model, with no carve-out for decoration. A rule that says "ignore visual geometry, always" cannot coexist with a rule that says "whatever is physically there blocks sight," so one of them had to give. Measured values keep the strict Gameplay-Geometry-only rule (that's the part that needs to be portable/comparable across differently-built models); physical checks keep operating on the real model, decoration included, because that's what "true line of sight, no templates" already means.

**Functional Equivalence claims measured-value equivalence, not total behavioral equivalence.**
Alternative considered: keep the original unqualified claim ("functionally identical models produce identical gameplay, period"). Rejected because, once the above decision is made, it's simply false — two models with identical Gameplay Geometry but very different visual bulk can produce different Line of Sight/Cover outcomes. The proposal now scopes the claim to what it can actually guarantee (identical Range/Attack Dice/Impact Strength/etc.), and calls out the one place it doesn't extend to (physical checks), rather than silently overpromising.

**"Platform" (footprint/dimensions) is used instead of separate "Unit"/"Vehicle" terminology.**
Alternative considered: keep the original draft's three overlapping terms ("Unit footprint," "Unit dimensions," "Vehicle dimensions"). Rejected because `WPN-004` (already shipped) already defines "Platform Length" as covering both a Unit Base and a vehicle — introducing competing terminology for the same concept in a new proposal creates exactly the kind of drift this review process exists to catch.

**Muzzle position is not listed as Gameplay Geometry; muzzle count is.**
The original draft listed "Muzzle positions" as Gameplay Geometry, but no shipped rule (`WPN-006`, `WPN-020`, `WPN-021`) reads muzzle position — only count (Attack Dice) and size (Impact Strength) feed any measured value. Position only matters for build validity (fits inside the footprint, doesn't overlap), which is already covered by Weapon Width / Weapon Front Footprint. Listing it as if it independently mattered was misleading.

**`weapon-construction`'s decorative-exclusion scenario is reworded to reference `geometry-layers` instead of standing alone.**
By the time this proposal is applied, `openspec/specs/weapon-construction/spec.md` (shipped via the `weapon-construction-system` change) already has its own "Weapon Length Determines Range" requirement asserting that decorative elements are excluded from the measurement — worded independently, with no reference to a formal Visual Geometry concept (since that concept didn't exist yet when it shipped). Alternative considered: leave it as-is and let the two capabilities separately assert the same rule in different words. Rejected — that's exactly the kind of terminology drift this change exists to prevent (see the "Platform" terminology decision above, and the original review's terminology findings). Fix: a small `MODIFIED` delta on `weapon-construction` that only reworks the wording of the existing scenario to say "excluding Visual Geometry (per the `geometry-layers` capability)" instead of "excluding decorative elements" — no measured behavior changes, purely a terminology alignment once the general concept exists.

**Added a "Detailed Representation" requirement, since it was referenced but never formally specified.**
The reviewed source material (and this change's own `tasks.md`) described a "Detailed Representation" concept — a model stays valid when built with extra detail on top of a Minimum Representation, as long as Gameplay Geometry is unchanged — but no ADDED Requirement for it existed in `specs/geometry-layers/spec.md`. It's the natural converse of Minimum Representation and Functional Equivalence (both already-specified), so it belongs in the same capability rather than being left as prose-only intent.

## Risks / Trade-offs

- [Risk] The Line of Sight/Cover carve-out means two "functionally identical" weapons can still have different tactical outcomes if one is visually bulkier (e.g. one grants more cover). → Mitigation: this is explicitly documented as expected behavior (see Functional Equivalence), not a bug — it's an accepted consequence of "true line of sight, no templates" (`CORE-008`), which every true-LOS tabletop game shares.
- [Risk] Without a hard cap, a player could build deliberately oversized Visual Geometry specifically to farm extra cover. → Mitigation: out of scope for this proposal (it's a game-balance/etiquette question, not a geometry-classification one); flagged as an Open Question below for a future proposal if it proves to be a real problem in practice.
- [Risk] This content doesn't cleanly fit any existing numbered doc (`01-foundations.md` is the closest thematically, but inserting content there mid-document would not match "rule identifiers remain stable"). → Mitigation: see Open Questions; likely lands as a new appended doc rather than an insertion.

## Open Questions

- Which `docs/*.md` file should own this content — a new `docs/15-geometry-layers.md`, or a new section appended to `docs/01-foundations.md`? Leaning toward a new file (matches "large systems receive their own document" per `system/documentation-standards.md`, and avoids renumbering anything), but not decided here — left for the tasks phase to resolve against actual doc structure.
- Should there be a hard rule limiting how far Visual Geometry may protrude beyond a model's Gameplay Geometry bounding box, to bound the cover-farming risk above? Deferred — no evidence yet that it's needed.
