## Context

`docs/13-materials.md` was written before `component-damage-system` (`16-damage-system.md`) existed, back when material-specific flavor text was the only damage mechanism the ruleset had. `component-damage-system` deliberately kept materials.md alongside it (DMG-008 said so explicitly) rather than replacing it, reasoning that Resistance/Geometry Check/Damage Roll is the *mechanism* and materials.md was the *cosmetic layer* on top. The user has now decided that layer isn't worth a dedicated document — mechanism and (minimal) physical representation both belong in one place.

## Goals / Non-Goals

**Goals:**
- Remove `docs/13-materials.md` cleanly — no dangling cross-references anywhere in the repo afterward.
- Preserve the two genuine mechanics MAT-018/MAT-019 defined (visibility-gated targeting, cross-component impact splitting), since `16-damage-system.md`'s own DMG-012/013/018 already depend on them by citation rather than restating them.
- Keep DMG-008's rule ID stable by repurposing it, per this repo's established convention, rather than leaving a numbering gap.

**Non-Goals:**
- Preserving per-material flavor text (glass/wood/metal/doors/windows/wheels/tracks/weapon-systems/cover-as-material/armour-as-mapping). The user explicitly chose deletion over merging for this content.
- Introducing any new mechanic. This is a documentation/consolidation change only.

## Decisions

### Delete outright rather than merge, except for MAT-018/MAT-019

**Confirmed directly with the user in two passes**: first, whether to merge or delete the per-material physical-response content (glass/doors/wheels/etc.) — user chose delete without merging. Second, once MAT-018 (Target Components) and MAT-019 (Independent Resolution) were identified as real mechanics — not flavor — that `16-damage-system.md` depends on via citation only, the user chose to merge just those two rather than lose them. This mirrors the same judgment calls already made throughout `ruleset-consistency-fixes` (e.g. Finding 5's Engine removal — delete the concept, but explicitly replace its structural role with Pilot rather than leaving a silent gap): a deliberate content decision, confirmed rather than assumed, distinguishing "flavor we're choosing to drop" from "mechanic we'd accidentally lose."

### DMG-012 and DMG-013 absorb MAT-018/MAT-019 by strengthening/expanding existing rules, not by adding new DMG- IDs

**Alternative considered**: add fresh `DMG-020`/`DMG-021` for Target Visibility and Independent Resolution. Rejected — DMG-012 (Select Target Component) already asserts "assigned to a visible component" as its own first-class rule text, and DMG-013 (Composite Vehicle Targeting) already asserts component independence; both already covered nearly all of MAT-018/019's content, citing the `13-materials.md` rules mostly as historical attribution rather than as the sole source of the mechanic. Expanding these two existing rules in place — matching the same "expand rather than fragment" reasoning used for `SCS-018` in `ruleset-consistency-fixes` Finding 4 — keeps the rule count and cross-reference graph simpler than introducing two new IDs for content that was already 90% present.

### DMG-008 repurposed from "Relationship to Materials" to "No Material-Specific Mechanics"

**Alternative considered**: delete DMG-008 outright and leave a numbering gap, since its entire original purpose (reconciling with materials.md) no longer applies. Rejected for the same reason `WPN-007`/`SCS-018`/`CMP-002`/`VEH-013`/`MAT-010` were repurposed rather than deleted earlier in this repo's history — a stable ID carrying a directly-related restatement is more informative to a future reader than a silent gap, and there's a genuinely useful thing for DMG-008 to say now: that this system deliberately has *no* material-specific mechanical variation (no per-material Resistance modifiers, no per-material hit thresholds) — which is exactly the design consequence of removing materials.md's mechanism-adjacent content (MAT-003's per-material breaking behavior, MAT-011's Armour-as-modifier framing) and is worth stating explicitly rather than leaving implicit.

### Cover, Armour, Transparency: point straight at their real owning rule instead of a deleted intermediary

**CBT-012 (Cover)** pointed at `13-materials.md` wholesale (which itself, after `ruleset-consistency-fixes` Finding 11, pointed at `CORE-010`). With the intermediary gone, CBT-012 points directly at `CORE-010` — one hop instead of two.
**CBT-013 (Armour)** cited `13-materials.md` MAT-011 alongside DMG-014/015; MAT-011's entire content was already stated as "fulfilled by this document" in DMG-008 before this change, so the citation was already redundant — removing it loses nothing.
**SCS-023 (Transparency)**, **CMP-011 (Windows)**, **TRN-012 (Transparent Elements)**, **WPN-012 (Line of Fire)** all deferred "whether transparent pieces stop projectiles" / "follow the Material Rules" to materials.md, but that behavior was always just Resistance + the Geometry Check (any component, transparent or not, stops or doesn't stop an Impact the same way) — there was never material-specific transparency logic to lose. Each now cites the real mechanism directly.

## Risks / Trade-offs

- [Risk] Deliberate loss of flavor text (how a broken window vs. a destroyed wheel should look) that some future scenario/expansion might want back. → Mitigation: accepted by the user; DMG-008's new text explicitly leaves room for "future supplements" to reintroduce cosmetic guidance without needing a dedicated document or changing any mechanic.
- [Risk] Wide diff — nine `docs/*.md` files plus `README.md`, `system/documentation-standards.md`, and `system/proposal-review.md` all touched for a single document's removal. → Mitigation: every touched file had exactly one or two sentences referencing `13-materials.md`; each edit is small and mechanical (swap a citation), not a rewrite.

## Open Questions

None outstanding.
