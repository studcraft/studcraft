## 0. Setup

- [x] 0.1 Work on branch `editorial-reviews-followup` (`openspec/config.yaml` requires one branch per proposal).

**Every task below is a move or a deletion.** No sentence is reworded, no rule ID changes, no numeric value changes. If applying a task requires typing prose, something has been misread — cut and paste instead.

`editorial-reviews-cleanup` (#31) is merged. Do not re-apply, revert, or amend anything it did beyond the three items named here.

## 1. `docs/16-damage-system.md` — reattach DMG-004's closing paragraph

#31 inserted Example 7 ahead of DMG-004's closing paragraph, which discusses Examples 3 and 4. That paragraph now sits three examples away from its subject and reads as though it belonged to Example 7.

The paragraph to move is currently the last thing in DMG-004, immediately before the `---` that closes the rule:

```
A brick-built shield (Resistance 3) and a four-plate shield (Resistance 4) can occupy similar external bulk, yet resolve to different resistance values because the count of physical layers — not the external silhouette — is what matters. StudCraft rewards engineering, not appearance.
```

**Expect it to land mid-list, and leave it there.** After the move, DMG-004 reads Example 1–4, this paragraph, then Examples 5–7. That is deliberate: the paragraph was authored as the closing commentary on Examples 3 and 4, back when those were the last two. Examples 5 and 6 (`resistance-clarification-review`) and Example 7 (#31) were each inserted *before* it, which is what pushed it away from its subject. Moving it back restores its original position rather than inventing a new one.

All three anchors below were confirmed unique in the file at the time of writing.

- [x] 1.1 Cut that paragraph from the end of DMG-004, along with the blank line that separated it from Example 7's last paragraph.
- [x] 1.2 Re-insert it immediately after Example 4's body — the line ending "Therefore `Resistance = 4`." — and immediately before the `## Example 5 — Bunker` heading, with one blank line on each side.
- [x] 1.3 Confirm DMG-004 now ends with Example 7's second paragraph ("The empty interior contributes nothing..."), followed by the `---` that closes the rule.
- [x] 1.4 Confirm the moved paragraph is byte-identical to what was cut. This is a move, not an edit.
- [x] 1.5 Confirm Examples 5, 6 and 7 remain in that order with their text untouched — only their position relative to the moved paragraph changes.

## 2. `docs/10-weapons.md` — WITHDRAWN

**This task was applied, then reverted. Do not re-apply it.** The Summary's prose block stays in the order #31 shipped:

1. `Weapons define only how an Impact is generated. Every consequence of that Impact is determined by Combat Resolution (`11-combat.md`) and the Component Damage System (`16-damage-system.md`).`
2. `No hidden statistics are required.`
3. `A player should understand every weapon simply by looking at the LEGO model.`

The original finding claimed the document "no longer ends on its strongest line" and asked for the order **2, 3, 1**. That was wrong, and checking the other documents shows why. Every one of them closes its prose on a synthesis line, never on a cross-reference:

- `01-foundations.md` — "...building and playing become one continuous experience."
- `03-game-flow.md` — "StudCraft replaces traditional game phases with **alternating unit activations**..."
- `11-combat.md` — "This keeps StudCraft modular and entirely construction-driven."
- `16-damage-system.md` — "Every combat interaction emerges from two sources only: the physical LEGO construction, and the uncertainty introduced by the dice."

Reordering made `10-weapons.md` close on two file paths and then jump straight to `> **Every Brick Matters.**` — a tonal break no other document has. The finding mistook "strongest" for "most architectural"; by house convention the philosophical line is the strongest closer, and "A player should understand every weapon simply by looking at the LEGO model" also echoes this document's own Design Philosophy opening.

- [x] 2.1 ~~Reorder to **2, 3, 1**~~ — applied in `00e8f83`, reverted immediately after. Net effect on `main`: none.
- [x] 2.2 Confirm `docs/10-weapons.md` matches its state at `main` exactly — the revert restores it, it is not a further edit.
- [x] 2.3 Do not reword any of the three lines, and do not touch the `## Length`, `## Muzzle Count` or `## Muzzle Size` subsections above them.

## 3. `openspec/changes/editorial-reviews-cleanup/specs/weapon-construction/spec.md` — delete the vacuous scenario

Given `WPN-018` (Width is the smallest dimension of the Weapon Body) and `WPN-019` (the Weapon Front Footprint is Width × Width), a Weapon Body's longest dimension and its firing axis always coincide by construction. The scenario below therefore describes a build the rules already make impossible, and no legal model can violate it.

- [x] 3.1 Delete these three lines in full, plus the blank line separating them from the preceding scenario:

```
#### Scenario: Length is measured along the firing axis
- **WHEN** a Weapon Body's dimensions are measured
- **THEN** Weapon Length is the dimension running perpendicular to the Weapon Front, not merely the largest dimension in any arbitrary direction
```

- [x] 3.2 Leave the `### Requirement: Weapon Length Determines Range` prose above unchanged. Its firing-axis wording stays — that is where the content belongs, and `WPN-003` already carries it in `docs/`.
- [x] 3.3 Confirm the three remaining scenarios are untouched: "Range computed from length", "Decorative overhang excluded from length", "Mounting hardware excluded from length".
- [x] 3.4 Change nothing else anywhere under `openspec/changes/editorial-reviews-cleanup/`. Its `proposal.md`, `design.md` and `tasks.md` stay exactly as merged.

## 4. Verify

- [x] 4.1 Run `python3 scripts/lint_ruleset.py`; confirm no structural issues.
- [x] 4.2 Run `git diff --stat main...HEAD` and confirm exactly these files changed: `docs/16-damage-system.md`, `openspec/changes/editorial-reviews-cleanup/specs/weapon-construction/spec.md`, plus the four new files under `openspec/changes/editorial-reviews-followup/`. **`docs/10-weapons.md` must NOT appear** — section 2 was withdrawn and reverted, so the file is byte-identical to `main`.
- [x] 4.3 Run `grep -c "A brick-built shield" docs/16-damage-system.md` and confirm exactly **1** — moved, not copied.
- [x] 4.4 Run `grep -c "Weapons define only how an Impact is generated" docs/10-weapons.md` and confirm exactly **1** — the revert restored one copy, not zero and not two.
- [x] 4.5 Run `grep -c "Length is measured along the firing axis" openspec/changes/editorial-reviews-cleanup/specs/weapon-construction/spec.md` and confirm **0**.
- [x] 4.6 Run `git diff main...HEAD -- docs/ | grep -E "^[+-]# (CORE|FLOW|SCS|CMP|DEP|MOVE|VEH|TRN|WPN|CBT|MEL|GEO|DMG)-"` and confirm no output — no rule heading was touched.
- [x] 4.7 Run `git diff main...HEAD --numstat -- docs/16-damage-system.md docs/10-weapons.md` and confirm added and removed line counts match in each file. A move adds back exactly what it removed; a mismatch means text was duplicated, dropped, or retyped.
- [x] 4.8 Confirm this change contributes no spec delta of its own. It edits `editorial-reviews-cleanup`'s delta and touches no living capability under `openspec/specs/`, so `openspec/changes/editorial-reviews-followup/` contains only `.openspec.yaml`, `proposal.md`, `design.md` and `tasks.md`.
