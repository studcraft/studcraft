## 1. Merge the two real mechanics out of 13-materials.md before deleting it

- [x] 1.1 `docs/16-damage-system.md` DMG-012 (Select Target Component): state the visibility requirement directly ("hidden components cannot be selected") instead of citing `13-materials.md` MAT-018.
- [x] 1.2 `docs/16-damage-system.md` DMG-013 (Composite Vehicle Targeting): add the explicit "a single attack's impacts may be split across different components of the same target" statement, plus the multi-component example, absorbing MAT-019's content instead of citing it.
- [x] 1.3 `docs/16-damage-system.md` DMG-018 (Weapon Distribution): update citation from MAT-019 to DMG-013.

## 2. Repurpose DMG-008 in place

- [x] 2.1 `docs/16-damage-system.md` DMG-008: rename from "Relationship to Materials" to "No Material-Specific Mechanics"; rewrite body to state directly that every component follows the same Resistance/Geometry Check/Damage Roll regardless of material, and that physical/cosmetic representation is left to the player rather than defined by a dedicated document.
- [x] 2.2 `docs/16-damage-system.md` Summary: update the sentence referencing "how this system relates to Materials (DMG-008)" to match DMG-008's new framing.

## 3. Remove remaining 13-materials.md / MAT- citations elsewhere in 16-damage-system.md

- [x] 3.1 DMG-005 (Component State Progression): drop the `13-materials.md` (MAT-017) citation from the Dead bullet, keep the CORE-016 one.
- [x] 3.2 DMG-006 (Universal Destruction): drop the `13-materials.md` (MAT-017) citation, keep the CBT-009 one.

## 4. Fix cross-references in docs/11-combat.md

- [x] 4.1 CBT-008 (Defender Resolution): remove the `13-materials.md` physical/cosmetic-response sentence and the redundant Examples subsection; fold "reaches Dead → physically removed, no material-specific distinction" into the main paragraph, citing DMG-006/DMG-008.
- [x] 4.2 CBT-009 (Physical State Changes): drop the `13-materials.md` (MAT-017) citation, keep the DMG-006 one.
- [x] 4.3 CBT-012 (Cover): point directly at `02-core-rules.md` CORE-010 instead of `13-materials.md`.
- [x] 4.4 CBT-013 (Armour): drop the `13-materials.md` MAT-011 citation (already redundant with DMG-008/DMG-014/DMG-015).

## 5. Fix cross-references in other docs

- [x] 5.1 `docs/04-construction-standard.md` SCS-023 (Transparency): replace "Material rules determine whether they stop projectiles" with a direct Resistance/Geometry Check reference.
- [x] 5.2 `docs/05-construction-components.md` CMP-011 (Windows): replace "Follow the Material Rules for transparent elements" with a direct `16-damage-system.md` reference.
- [x] 5.3 `docs/09-transport.md` TRN-012 (Transparent Elements): replace "follows the Material Rules" with a direct Line of Sight (`CORE-008`) reference.
- [x] 5.4 `docs/10-weapons.md` WPN-012 (Line of Fire): replace "transparent elements follow the Material Rules" with a reference to `04-construction-standard.md` SCS-023.
- [x] 5.5 `docs/08-vehicles.md` VEH-017 (Components): replace "See: materials.md" with a `16-damage-system.md` reference.
- [x] 5.6 `docs/12-melee.md`: update the Purpose section, MEL-010, and MEL-012's document list to drop Material Rules references in favor of the Component Damage System.

## 6. Delete the document and update navigation/meta docs

- [x] 6.1 Delete `docs/13-materials.md`.
- [x] 6.2 `README.md`: remove `13-materials.md` from the directory tree, the numbered rulebook reading order (renumbered subsequent entries), the Current Status implemented-systems list, and the Core Concepts "materials" mention.
- [x] 6.3 `system/documentation-standards.md`: remove `13-materials.md` from its directory tree listing.
- [x] 6.4 `system/proposal-review.md`: remove `docs/13-materials.md` from its illustrative example list.
- [x] 6.5 `scripts/generate_site_docs.py`: remove `13-materials.md` from the `TITLES` dict (its own sync-check would otherwise fail the site build).

## 7. Verify

- [x] 7.1 Grep the full repo for any remaining `13-materials.md` or "Material Rules" reference.
- [x] 7.2 Run `python3 scripts/lint_ruleset.py` and confirm no structural issues.
- [x] 7.3 Run `openspec validate "remove-materials-document" --strict` and confirm valid.
- [x] 7.4 Run `python3 scripts/generate_site_docs.py` and confirm it completes without a TITLES-sync error.
