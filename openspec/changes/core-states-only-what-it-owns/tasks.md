# Tasks — CORE states only what it owns

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change files and occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which occurrence was meant. Never edit a document to make a verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the text** — do not write the backticks into the document.

A `#` heading, a `|` table row or a `---` horizontal rule inside a fence is real markdown that must land in the file as markdown, not as quoted text. Task 6.1's anchor contains three `## ` rule headings and three `---` rules, all real, and its replacement is a single real `# Equipment` heading. Task 10.1's anchor and replacement both contain a real `# ` heading and a numbered list.

**This change is mostly deletion.** Several replacement blocks are shorter than their anchor and several repeat a line of the anchor unchanged — the repeated line is a landmark that must stay in the file, not an edit. Copy each block exactly.

**No rule ID changes and nothing is renumbered.** Three rule IDs are deleted outright — `CORE-011`, `CORE-012` and `CORE-013`. Do not renumber `CORE-014`, `CORE-015` or `CORE-016` into the gap, and do not leave a stub behind saying a rule used to be there.

**Section 11 is not a deletion.** It moves one sentence into `docs/16-damage-system.md`, and it is what keeps the infantry pose in the ruleset after section 6 removes the rules that used to state it. Applying section 6 without section 11 deletes a rule.

- [x] 0.1 The branch is `core-states-only-what-it-owns`, named for this change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Four ruleset documents, no spec delta: **twenty edits and thirty non-edit tasks** (0.1, 13.1 – 13.19 and 14.6 – 14.15). Sections 1–13 are the change as proposed — fifteen edits across three documents, listed below. Section 14 adds five repairs from the audit of the applied text, and brings in `docs/12-melee.md` as the fourth document; its own coverage note is in that section.

| `proposal.md` item | Task | Path |
|---|---|---|
| `CORE-001` — the height derivation | 1.1 | `docs/02-core-rules.md` |
| `CORE-001` — the "What must fit" paragraph | 1.2 | `docs/02-core-rules.md` |
| `CORE-001` — the Line of Sight / Cover sentence | 1.3 | `docs/02-core-rules.md` |
| `CORE-001` — the footprint paragraph | 1.4 | `docs/02-core-rules.md` |
| `CORE-004` — the Pilot paragraph | 2.1 | `docs/02-core-rules.md` |
| `CORE-006` — the size argument | 3.1 | `docs/02-core-rules.md` |
| `CORE-007` — the example list | 4.1 | `docs/02-core-rules.md` |
| `CORE-009` — the symmetry paragraph | 5.1 | `docs/02-core-rules.md` |
| `CORE-011`/`012`/`013` and `# Infantry States` | 6.1 | `docs/02-core-rules.md` |
| `CORE-014` — the example list | 7.1 | `docs/02-core-rules.md` |
| `CORE-015` — the two example lists | 8.1 | `docs/02-core-rules.md` |
| `CORE-016` — the example list | 9.1 | `docs/02-core-rules.md` |
| `Universal Rule` reworded, `Design Notes` removed | 10.1 | `docs/02-core-rules.md` |
| `DMG-005` — the infantry pose | 11.1 | `docs/16-damage-system.md` |
| Glossary ***Projection*** entry | 12.1 | `docs/14-glossary.md` |

**Untouched, deliberately:** `CORE-002` — the `Shield direction` bullet stays, because nothing else in `docs/` owns shield direction and the glossary's *Facing* entry cites `CORE-002` for it (`design.md`, Decision 2). `CORE-003`, `CORE-008` and `CORE-010`, which restate nothing. `CORE-005`, whose "not yet defined" sentence is quoted verbatim by `TODO.md` and checked character for character by `scripts/check_todo_quotes.py` (`design.md`, Decision 3). `CORE-006`'s bulleted action list, including `- Reload (future rule)`, which `TODO.md` also quotes verbatim — task 3.1 edits only the paragraph below that list. The `# Purpose` and `# The Battlefield` sections. `DMG-006` and every other rule in `docs/16-damage-system.md`, and that document's `# Summary`, which already names Structural States (`DMG-005`) and gains no new definition from task 11.1. Every other `docs/*.md` file. `openspec/specs/` — this change ships no delta (`design.md`, Decision 7). `CHANGELOG.md` and every `**Version:**` header.

---

## 1. `docs/02-core-rules.md` — `CORE-001`

- [x] 1.1 In `CORE-001`, replace this anchor — two whole paragraphs, the plate-layer paragraph and the derivation paragraph below it. The line above them, ending "The 4-stud edge is the front (CORE-002).", is **not** part of the anchor and is not touched:

```
Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Thirteen plate layers is therefore 4 bricks and a plate. Height is measured from the underside of the base an infantry model stands on: that base is part of the volume, not the floor beneath it.

The height is read from the model rather than chosen. Infantry occupies exactly one Unit Base whether standing or seated (`09-transport.md`, TRN-002), so a Unit Base must contain a standing minifigure on the base it is built on (`04-construction-standard.md`, SCS-002): 4 bricks from its feet to the top of its head, and one plate beneath them. Thirteen plate layers is that model, base included, and a Unit Base is the minimum operational space an object needs (`09-transport.md`, TRN-001), so it takes that and no more. **The stud on top of the minifigure's head is not counted here.** The counts in the paragraph above are stacking heights: a stud sits inside the piece above it rather than adding to the stack, and this measurement is taken the same way. Nor do headgear, weapons or equipment change the figure — infantry occupies exactly one Unit Base whatever it carries (`09-transport.md`, TRN-002).
```

with:

```
Height is counted in plate layers because that is the ruleset's vertical unit — a plate counts as 1 and a standard brick as 3 (`16-damage-system.md`, DMG-003; `08-vehicles.md`, VEH-021). Thirteen plate layers is a standing minifigure on the base it is built on (`04-construction-standard.md`, SCS-002): 4 bricks from its feet to the top of its head, and one plate beneath them. **The stud on top of the head is not counted**, because a stud sits inside the piece above it rather than adding to the stack. Height is measured from the underside of that base, which is part of the volume rather than the floor beneath it.
```

  Two paragraphs become one. What is kept is what four other places cite `CORE-001` for — the plate/brick conversion and where the 13 comes from (`design.md`, Decision 5). What goes is stated elsewhere: infantry occupying one Unit Base standing or seated and whatever it carries (`09-transport.md`, TRN-002; `05-construction-components.md`, CMP-018), and the Unit Base as minimum operational space (`09-transport.md`, TRN-001).

- [x] 1.2 In `CORE-001`, replace this anchor — the whole **What must fit is the Unit Base** paragraph together with the `**Projections.**` line below it:

```
**What must fit is the Unit Base.** Wherever a rule asks whether something physically fits — a passenger, a crew member, cargo, a model passing an opening — the volume that must fit is the Unit Base: one for a minifigure, its own volume in Unit Bases for a vehicle (`04-construction-standard.md`, SCS-005). Never the loose model. A minifigure that would slip into a smaller gap than its Unit Base does not fit there.

**Projections.** A rule never reads more of the volume than it needs:
```

with:

```
**Projections.** A rule never reads more of the volume than it needs:
```

  The `**Projections.**` line is a landmark, not an edit: it is repeated so the deletion has a unique anchor. The table below it is not part of the anchor and is not touched. `04-construction-standard.md` (SCS-005) states the deleted paragraph already, in the document that owns what must physically fit.

- [x] 1.3 In `CORE-001`, replace this anchor — two paragraphs, below the vertical-projection sentence:

```
A projection supplies a measured value and nothing else — the boundary `15-geometry-layers.md` draws (GEO-003).

It never replaces a physical check. Line of Sight (CORE-008) and Cover (CORE-010) are resolved against the plastic actually on the table, never against a Unit Base's silhouette (`15-geometry-layers.md`, GEO-004).
```

with:

```
A projection supplies a measured value and nothing else, and never replaces a physical check — the boundary `15-geometry-layers.md` draws (GEO-003, GEO-004).
```

  The clause `CORE-001` keeps is the one about projections. What goes is the restatement of `GEO-004`, which spends five paragraphs on Line of Sight and Cover against the physical model, and of `CORE-008` and `CORE-010` themselves. The `GEO-004` citation is preserved in the surviving sentence so no reference is lost.

- [x] 1.4 In `CORE-001`, replace this anchor — the last paragraph of the rule:

```
All distances, Deployment Volumes and vehicle footprints are expressed using this unit. When a footprint is written as `W × D` UB (e.g. "Jeep: 2 × 3 UB"), the first number is a count of 4-stud widths and the second a count of 3-stud depths — a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`. A footprint is a horizontal reading, and says nothing about how tall a model actually is — though for a vehicle it does bound how tall the model may be (`08-vehicles.md`, VEH-028).
```

with:

```
All distances, Deployment Volumes and vehicle footprints are expressed using this unit. A footprint written `W × D` UB counts 4-stud widths by 3-stud depths, so a `2 × 3 UB` footprint measures `8 × 9` studs, not `6 × 12`.
```

  The `W × D` reading stays: `08-vehicles.md` (VEH-028) cites `CORE-001` for it by name. The Jeep example goes — `VEH-001` tabulates every footprint including that one — and so does the height clause, which `VEH-028` owns and states in full.

---

## 2. `docs/02-core-rules.md` — `CORE-004`

- [x] 2.1 In `CORE-004`, replace this anchor — three paragraphs. The rule's opening line, "A powered vehicle occupies two or more Unit Bases.", is **not** part of the anchor and is not touched:

```
One of those is taken by its Pilot, who occupies a Unit Base like any other crew member (`09-transport.md`, TRN-014) and is required for the vehicle to move at all (`08-vehicles.md`, VEH-013). A single-Unit-Base vehicle would be entirely filled by its own driver, with no vehicle left around them.

Its footprint is defined by the LEGO model itself.

Vehicle movement and transport capacity are described in the Vehicle Rules.
```

with:

```
Two and not one because the Pilot occupies a Unit Base of its own — `08-vehicles.md` (VEH-013) gives the reason in full.

Its footprint is defined by the LEGO model itself.
```

  `VEH-013` states the deleted paragraph almost word for word and `CMP-002` states it a third time. The one-clause reason stays, immediately below the sentence it explains, so "Two and not one" sits next to its referent. The closing signpost goes: it names a document without stating anything.

---

## 3. `docs/02-core-rules.md` — `CORE-006`

- [x] 3.1 In `CORE-006`, replace this anchor — the rule's last paragraph, one line. The bulleted action list above it and the "Every unit receives exactly **3 Action Points**" paragraph are **not** part of the anchor and are not touched:

```
**No Action Point cost scales with size.** Not with the size of the unit paying it — its footprint, its height, or the Unit Bases it occupies: an infantry model and a motorcycle pay the same to embark (`09-transport.md`, TRN-005). Not with the size of an interactive element it operates (CORE-007): a hatch and a cargo ramp cost the same to open. The allotment above is fixed, so a price that grew with the model would put a large enough model beyond acting at all — forbidden by arithmetic rather than by a rule, which is not how this ruleset forbids anything. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010). And where more than one Action Point is spent, the reason is stated in the rule that spends it and is never size — `11-combat.md`, CBT-001 charges per weapon system attacking, `08-vehicles.md`, VEH-008 per 90° turn, and MOVE-010 charges the climb itself: the second Action Point buys crossing the obstacle, not the obstacle's height.
```

with:

```
**No Action Point cost scales with size** — not with the size of the unit paying it, and not with the size of an interactive element it operates (CORE-007). An action's cost is set by the rule that governs that action, and where more than one Action Point is spent that rule states why; the reason is never size. A measurement may still decide **which** rule applies: an obstacle of 3 plate layers is crossed freely and one of 4 is climbed (`07-movement.md`, MOVE-009, MOVE-010).
```

  **The rule itself is kept, deliberately.** It is the one paragraph in this change that states something no other rule states — `openspec/specs/action-economy` carries it as a requirement with four scenarios (`design.md`, Decision 1). Every clause of that requirement survives: no scaling with the payer, no scaling with the operated element, the cost set by the governing rule, and a measurement selecting which rule applies. What goes is the two worked examples, the argument from arithmetic, and the enumeration of `CBT-001`, `VEH-008` and `MOVE-010`, each of which states its own cost.

---

## 4. `docs/02-core-rules.md` — `CORE-007`

- [x] 4.1 In `CORE-007`, replace this anchor — the `Examples:` line, the six-item list below it, and the cost line that follows:

```
Examples:

- Doors

- Gates

- Drawbridges

- Ramps

- Hatches

- Elevators

Opening or closing an interactive element costs:
```

with:

```
Opening or closing an interactive element costs:
```

  The cost line is a landmark, not an edit — it is repeated so the deletion has a unique anchor, and the `**1 Action Point**` line below it is not touched. `04-construction-standard.md` (SCS-006) lists the same six elements and already points at `CORE-007` for what operating one costs.

---

## 5. `docs/02-core-rules.md` — `CORE-009`

- [x] 5.1 In `CORE-009`, replace this anchor — the paragraph below the blockquote. The blockquote itself, "> If you can see it, you can shoot it.", is **not** part of the anchor and is not touched:

```
This is symmetric: if it can see you, you can be its target during its own activation (`03-game-flow.md`, FLOW-002). It does not grant a shot outside of a unit's own activation — StudCraft has no reaction fire (`11-combat.md`, CBT-014 lists it as a possible future extension, not a current rule).
```

with:

```
This does not by itself grant a shot outside a unit's own activation: StudCraft has no reaction fire, which `11-combat.md` (CBT-014) lists as a possible future extension rather than a current rule.
```

  **The disclaiming form is deliberate and must land as written.** "This does not by itself grant X" is not "X never happens", and the difference is load-bearing: `CBT-010` contemplates "something else already declares" two attacks resolving together, and `FLOW-013` lets a scenario extend the ruleset. An absolute prohibition here would outrank both under the precedence task 10.1 makes explicit (`design.md`, Decision 10). The `CBT-014` citation is kept because `CORE-009` is its only citer. The symmetry sentence goes: `CODE_OF_DESIGN.md` Principle 9 owns it (`design.md`, Decision 11).

---

## 6. `docs/02-core-rules.md` — `CORE-011`, `CORE-012`, `CORE-013` and their section

- [x] 6.1 Replace this anchor — the whole `# Infantry States` section, from its heading through the `# Equipment` heading that follows it. The `---` above `# Infantry States` stays where it is and becomes the separator before `# Equipment`:

```
# Infantry States

Infantry uses the universal Component State machine (`16-damage-system.md`, DMG-005) exactly like any other component — CORE-011/012/013 describe the infantry-specific physical representation of each state, and what Wounded costs an infantry model, not a separate state system.

## CORE-011 — Operational

The minifigure stands upright.

The unit functions normally.

---

## CORE-012 — Wounded

The minifigure is placed in a seated position, representing an injured soldier.

The seated position is the game marker. No additional token is required.

A Wounded minifigure changes in exactly two ways. Its movement is reduced — `07-movement.md` (MOVE-021) states by how much. And it punches worse: an unarmed attack is the one attack whose weapon system is the minifigure itself (`12-melee.md`, MEL-008), so there its own Component State is read (`11-combat.md`, CBT-015). Nothing else changes. It rotates and falls exactly as if Operational, a climb still costs the additional Action Point MOVE-010 charges on top of a move that is now shorter, and the weapons it carries are components in their own right, degraded only when they are themselves Wounded (`11-combat.md`, CBT-015). The seated pose is the marker for all of it — a seated model moves less, punches worse, and dies to the next successful Impact (`16-damage-system.md`, DMG-005), the same as any other component.

---

## CORE-013 — Dead

The minifigure is physically removed from the battlefield — the same removal every component undergoes on reaching Dead (`16-damage-system.md`, DMG-006). No casualty marker is used; removal is the marker.

Dead units no longer participate in the game and no longer block movement, Line of Sight, or provide Cover.

---

# Equipment
```

with:

```
# Equipment
```

  Three rule IDs are deleted outright — do not renumber `CORE-014`, `CORE-015` or `CORE-016` into the gap, and do not write replacement rules or a stub recording that the rules were removed. Nothing in `docs/` cites `CORE-011`, `CORE-012` or `CORE-013`; `python3 scripts/rule.py refs CORE-011 CORE-012 CORE-013` reports all three uncited. Every sentence deleted here is a rule elsewhere — `MOVE-021` and `CBT-015` for what Wounded costs an infantry model, which `CORE-012` cited rather than defined, and `DMG-006` for removal — **except the pose, which section 11 moves into `DMG-005` in the same change.** `design.md`, Decision 4 tabulates the mapping.

---

## 7. `docs/02-core-rules.md` — `CORE-014`

- [x] 7.1 In `CORE-014`, replace this anchor — the rule's second line and the example list below it:

```
A unit cannot use equipment that is not present on the model.

Examples:

Weapons

Shields

Backpacks

Tools

Medical packs

Special devices
```

with:

```
A unit cannot use equipment that is not present on the model.
```

  The first line is a landmark, not an edit. The rule keeps both of its statements — equipment must be physically represented, and a unit cannot use what is not on the model.

---

## 8. `docs/02-core-rules.md` — `CORE-015`

- [x] 8.1 In `CORE-015`, replace this anchor — everything from the guideline line to the end of the rule. The rule's opening line, "A minifigure may only use equipment it can physically carry.", is **not** part of the anchor and is not touched:

```
As a general guideline:

One hand carries one one-handed item.

Examples:

- Pistol
- Sword
- Knife
- Shield

Two-handed equipment occupies both hands.

Examples:

- Rifle
- Heavy Machine Gun
- Rocket Launcher

The physical model determines what the unit carries.
```

with:

```
As a general guideline, one hand carries one one-handed item — a shield among them — and two-handed equipment occupies both hands. `10-weapons.md` (WPN-010) states which weapons are which.

The physical model determines what the unit carries.
```

  **"As a general guideline" is kept deliberately**: the rule is a guideline today, and this change alters no gameplay value. The shield is named because the deleted list classified it as one-handed and `WPN-010` covers it only in passing — it states which *weapons* are one- or two-handed, and a shield is not a weapon. `WPN-010` reproduces both weapon lists verbatim and already cites `CORE-015` for the universal rule. The last line is a landmark and stays as it is.

---

## 9. `docs/02-core-rules.md` — `CORE-016`

- [x] 9.1 In `CORE-016`, replace this anchor — the rule's opening line, the example list, and the closing line:

```
Whenever possible, changes in game state should be represented by modifying the model itself.

Examples:

A wounded soldier sits.

A dead soldier is removed.

A destroyed weapon is removed.

A broken window loses its transparent brick.

An opened door is physically opened.

StudCraft always prefers physical representation over markers.
```

with:

```
Whenever possible, changes in game state should be represented by modifying the model itself.

StudCraft always prefers physical representation over markers.
```

  Both statements are landmarks and stay. `CORE-016` remains the owner of the principle — `DMG-005`, `DMG-006`, `MEL-011` and `VEH-025` all cite it — and only its examples go: `01-foundations.md` (*Physical Representation*) and `MEL-011` list the same ones.

---

## 10. `docs/02-core-rules.md` — `Universal Rule` and `Design Notes`

- [x] 10.1 Replace this anchor — the whole `Universal Rule` section and the whole `Design Notes` section below it, including the `---` that separates them. The `---` above `# Universal Rule` and the `---` and closing motto below `Design Notes` are **not** part of the anchor and are not touched:

```
# Universal Rule

Whenever a conflict exists between:

- written rules
- physical construction

the following priority applies:

1. Foundations
2. Core Rules
3. Construction Standards
4. Scenario Rules

---

# Design Notes

These rules intentionally avoid introducing statistics.

The goal of StudCraft is for players to understand the battlefield simply by observing the LEGO models.

The physical model is always the primary source of truth.
```

with:

```
# Universal Rule

When rules from different levels conflict, the higher level takes precedence:

1. Foundations
2. Core Rules
3. Construction Standards
4. Scenario Rules

The physical model is the source of every physical fact these rules read; this order settles which rule reads it and what it means.
```

  Two changes in one anchor because the sections are adjacent. The reworded opening stops the four levels reading as though physical construction were ranked among them and could override a written rule; all four are written rules, and `03-game-flow.md` (FLOW-013) already states the direction this makes explicit (`design.md`, Decision 8). `Design Notes` goes because each rule-bearing document states the no-statistics stance in its own Design Philosophy and `CODE_OF_DESIGN.md` states it as a principle — except its last sentence, which survives as the closing clause above.

  **The file must still end with `---` and then `> **Every Brick Matters.**`** — `scripts/lint_ruleset.py` checks the last non-empty line.

---

## 11. `docs/16-damage-system.md` — `DMG-005`

This is the one addition in the change. Section 6 deletes the rules that stated how an infantry model shows its Component State; this puts that sentence where the Component State machine lives. **Apply it in the same pass as section 6.**

- [x] 11.1 In `docs/16-damage-system.md`, `DMG-005`, replace this anchor — the `Dead` bullet, which is the last paragraph of the rule:

```
**Dead** — the component immediately ceases to exist. It is physically removed from the model. No dead component remains on the battlefield. This is the same physical-representation principle as `02-core-rules.md` (CORE-016) — see DMG-006.
```

with:

```
**Dead** — the component immediately ceases to exist. It is physically removed from the model. No dead component remains on the battlefield. This is the same physical-representation principle as `02-core-rules.md` (CORE-016) — see DMG-006.

For an infantry model the state is read from its pose: an Operational minifigure stands upright, a Wounded one is seated. The pose is the marker; no token is used.
```

  The `Dead` bullet is repeated unchanged as a landmark; the new paragraph goes below it, after all three states rather than inside one, because it names two of them. This is a relocation and not a new rule: `CORE-011` and `CORE-012` state it today, `12-melee.md` (MEL-011) lists it as an example, and `01-foundations.md` states it as philosophy in a section that defines no rules. No `component-damage` delta is owed — no behaviour changes (`design.md`, Decision 7).

  **The new sentence cites nothing, deliberately.** `CORE-016` is already cited two paragraphs above it for the physical-representation principle, and citing `MEL-011` here as well would point one rule at two places for the same principle (`design.md`, Decision 4).

---

## 12. `docs/14-glossary.md` — the ***Projection*** entry

- [x] 12.1 In `docs/14-glossary.md`, replace this anchor — the body of the `## Projection` entry. The heading is **not** part of the anchor:

```
The reading of the Unit Base volume a rule takes: horizontal for distance, deployment floors and footprints; the whole volume for transport capacity and for the Deployment Volume a model must fit inside; vertical for passing an opening. A projection is a measured value and never replaces a physical check. See `02-core-rules.md` (CORE-001).
```

with:

```
The reading of the Unit Base volume a rule takes: horizontal for distance, deployment floors and footprints; the whole volume for transport capacity and for the Deployment Volume a model must fit inside; vertical for passing an opening. A projection is a measured value and never replaces a physical check. See `02-core-rules.md` (CORE-001) and `15-geometry-layers.md` (GEO-004).
```

  Only the closing citation changes. The entry asserts "never replaces a physical check" and cited only `CORE-001`, which after task 1.3 states that clause without elaborating it; `GEO-004` is where the elaboration lives.

  The glossary's *UB*, *Facing*, *Component State* and *Wounded* entries are **not** touched. *UB* points at `CORE-001` for where the height comes from and the projections, both of which survive; *Facing* points at `CORE-002`, which this change does not edit; *Component State* and *Wounded* point at `DMG-005`, whose three states are unchanged by task 11.1.

---

## 13. Verification

Run each command and write down what it actually returned. If a figure differs from the one stated here, **stop and report it** — do not edit a document to make it match. Every "before" figure below was produced by running the command against the pre-change files.

- [x] 13.1 `grep -c -F "What must fit is the Unit Base" docs/02-core-rules.md` — before: **1**, after: **0**. Task 1.2.

- [x] 13.2 `grep -c -F "never against a Unit Base's silhouette" docs/02-core-rules.md` — before: **1**, after: **0**. Task 1.3.

- [x] 13.3 `grep -c -F "forbidden by arithmetic" docs/02-core-rules.md` — before: **1**, after: **0**. Task 3.1.

- [x] 13.4 `grep -c -F "No Action Point cost scales with size" docs/02-core-rules.md` — before: **1**, after: **1**. The rule survives task 3.1; only its argument goes. A **0** here means the paragraph was deleted instead of compressed — stop and report it.

- [x] 13.5 `grep -c "^## CORE-01[123]" docs/02-core-rules.md` — before: **3**, after: **0**. Task 6.1.

- [x] 13.6 `grep -c "^# Infantry States" docs/02-core-rules.md` — before: **1**, after: **0**. Task 6.1.

- [x] 13.7 `grep -c "^# Design Notes" docs/02-core-rules.md` — before: **1**, after: **0**. Task 10.1.

- [x] 13.8 `grep -c "^# " docs/02-core-rules.md` — before: **15**, after: **13**. The two section headings removed are `# Infantry States` (6.1) and `# Design Notes` (10.1); every other section heading survives, including `# Equipment`, which task 6.1's replacement puts back.

- [x] 13.9 `grep -c -F "Heavy Machine Gun" docs/02-core-rules.md` — before: **1**, after: **0**. Task 8.1.

- [x] 13.10 `grep -c -F "Shield direction" docs/02-core-rules.md` — before: **1**, after: **1**. `CORE-002` is untouched (`design.md`, Decision 2). A **0** here means an edit ran past its anchor — stop and report it.

- [x] 13.11 `grep -c -F "only structure-wide consequences" docs/02-core-rules.md` — before: **1**, after: **1**. `CORE-005` is untouched, and `scripts/check_todo_quotes.py` compares that sentence against `TODO.md` character for character (`design.md`, Decision 3).

- [x] 13.12 `grep -c -F "As a general guideline" docs/02-core-rules.md` — before: **1**, after: **1**. Task 8.1 keeps `CORE-015` a guideline rather than promoting it to a rule.

- [x] 13.13 `grep -c -F "stands upright" docs/02-core-rules.md` — before: **1**, after: **0**. The pose leaves this document (task 6.1).

- [x] 13.14 `grep -c -F "stands upright" docs/16-damage-system.md` — before: **0**, after: **1**. The pose arrives in this one (task 11.1). **13.13 and 13.14 are one pair**: if the first is 0 and the second is also 0, the rule was deleted rather than moved — stop and report it.

- [x] 13.15 `grep -c -F "GEO-004" docs/14-glossary.md` — before: **1**, after: **2**. Task 12.1 adds the second; the first is in the *Visual Geometry* entry and is not touched.

- [x] 13.16 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues found.` After: the same line. This is what confirms the deleted rule IDs break no cross-document citation and that every edited document still ends with its motto.

- [x] 13.17 `python3 scripts/check_task_anchors.py core-states-only-what-it-owns` — must **exit 0**. Report the line it printed. Every anchor above is expected to report **zero** matches once the change has been applied and its boxes are ticked; on an unticked task a zero match is a defect.

- [x] 13.18 `python3 scripts/preflight.py` — **read this before running it.** Exactly one check is **expected** to FAIL until the `rule-ids-may-be-retired` change has merged to `main` and `main` has been merged into this branch: **`Rule IDs are stable`**, naming `CORE-011`, `CORE-012` and `CORE-013` as gone. That is this change deleting three rule IDs against a checker that does not yet permit it (`design.md`, Decision 4, "Prerequisite"). This one is not a defect and is not cause to halt: **write down what it printed, tick this box, and carry on to 13.19.** Do not restore the rules, and do not edit the checker from this branch — a proposal branch may touch `docs/*.md` and its own change directory only. Every other check must PASS; if any *other* check fails, that is the halt-and-report case. Once the prerequisite has merged, all twelve pass.

- [x] 13.19 `git status --short` — three modified files — `docs/02-core-rules.md`, `docs/14-glossary.md` and `docs/16-damage-system.md` — plus the untracked change directory `openspec/changes/core-states-only-what-it-owns/` reported as a single `??` entry. Anything else in the list is a mismatch: report it and stage nothing.

---

## 14. Repairs after the audit of the applied text

The applied text was audited and returned six findings; five are repaired here and the sixth needs no edit. **Every anchor in this section was checked against the applied files, not the pre-change ones**, and occurs exactly once.

Two of the repairs are this change's own defects. One moved a rule and dropped its modal force on the way. One applied "check the glossary entry in the same pass" to the entry that moved and not to the entry of the rule that gained text. The other three are citations and wording that the deletions left aiming at the wrong place.

`docs/12-melee.md` joins the change here, so the coverage table above gains a sixteenth row: `MEL-011` — the pose citation | 14.3 | `docs/12-melee.md`.

Each task below names its own file path, because `scripts/check_task_anchors.py` resolves a target from the nearest preceding path and this section has no per-document sub-sections.

- [x] 14.1 In `docs/16-damage-system.md`, `DMG-005`, replace this anchor — the paragraph task 11.1 added, which is the last paragraph of the rule:

```
For an infantry model the state is read from its pose: an Operational minifigure stands upright, a Wounded one is seated. The pose is the marker; no token is used.
```

with:

```
An infantry model is placed in the pose of its state: upright while Operational, seated once Wounded. The pose is the marker; no token is used.
```

  Two defects in one sentence. `CORE-012` said the minifigure **is placed** seated; the sentence that replaced it only described a pose, so no rule instructed anyone to re-pose a Wounded model — `CORE-016` says representation "should" happen "whenever possible", which is a preference. And "the state is read from its pose" inverts the direction: `DMG-015` sets the state and the pose shows it, which is what the second sentence already said and the first contradicted. The replacement is normative and reads one way only.

- [x] 14.2 In `docs/14-glossary.md`, the `## Wounded` entry, replace this anchor — the entry's closing sentences. The heading and the rest of the entry are **not** part of the anchor:

```
Nothing else about any component changes, and the next successful damaging Impact advances it to Dead. See `16-damage-system.md`, DMG-005.
```

with:

```
Nothing else about any component changes, and the next successful damaging Impact advances it to Dead. A Wounded infantry model is placed seated, which is how the state is shown on the model. See `16-damage-system.md`, DMG-005.
```

  `system/proposal-review.md` ("The Summary Is Part of the Rule") requires the glossary entry to be checked in the same pass as the rule. This change did that for *Projection* and missed *Wounded*, which is the entry for the rule it actually added text to — leaving a reader who looks up *Wounded* told everything about the state except how it is shown, which is exactly what `CORE-012`'s deletion took away.

- [x] 14.3 In `docs/12-melee.md`, `MEL-011`, replace this anchor — the rule's opening line. The `Examples:` list below it is **not** part of the anchor and is not touched:

```
Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-006).
```

with:

```
Combat results should be represented on the LEGO model whenever possible, per the universal physical-representation principle (`02-core-rules.md`, CORE-016; `16-damage-system.md`, DMG-005, DMG-006).
```

  `MEL-011` lists "Wounded minifigure sits" as an example and cited only `CORE-016`, which lost its example list in task 9.1, and `DMG-006`, which is about removal. Neither states the pose any more. `DMG-005` does, after task 11.1, so it joins the citation — the example now points at the rule it illustrates.

- [x] 14.4 In `docs/02-core-rules.md`, the `Universal Rule` section, replace this anchor — the closing sentence task 10.1 wrote:

```
The physical model is the source of every physical fact these rules read; this order settles which rule reads it and what it means.
```

with:

```
The order ranks these four levels only. A system document — Movement, Vehicles, Damage and the rest — is not a level in it; it states the rules for its own subject.

The physical model is the source of every physical fact these rules read; this order settles which rule reads it and what it means.
```

  Task 10.1 made the ordering explicitly normative, and none of the system documents is one of the four levels — so a conflict between `DMG-005` and a `CORE-` rule was left undecided by the only rule that decides conflicts. That gap pre-dates this change, but this change is what put an infantry rule into `DMG-005` and made it load-bearing. **The new sentence scopes the order; it does not add a level or rank anything.**

- [x] 14.5 In `docs/02-core-rules.md`, `CORE-009`, replace this anchor — the line task 5.1 wrote:

```
This does not by itself grant a shot outside a unit's own activation: StudCraft has no reaction fire, which `11-combat.md` (CBT-014) lists as a possible future extension rather than a current rule.
```

with:

```
This does not grant a shot outside a unit's own activation: StudCraft has no reaction fire, which `11-combat.md` (CBT-014) lists as a possible future extension rather than a current rule.
```

  "By itself" qualified the symmetry clause, which task 5.1 deleted; with that gone the qualifier points at nothing. Removing it restores exactly the disclaiming force the pre-change text had ("It does not grant a shot outside of a unit's own activation"), which is what `design.md` Decision 10 asks for.

### Not repaired, deliberately

`06-deployment.md` (DEP-002) and `09-transport.md` (TRN-019) each cite `CORE-001` beside a second rule for a clause `CORE-001` no longer carries — `TRN-002` and `SCS-005` respectively. Both co-citations still carry the claim, so nothing dangles and no content is lost; `CORE-001` is merely decorative in those two pairs. Trimming them is a separate tidy, not a repair.

### Verification after section 14

- [x] 14.6 `grep -c -F "the state is read from its pose" docs/16-damage-system.md` — before: **1**, after: **0**. Task 14.1.

- [x] 14.7 `grep -c -F "is placed in the pose of its state" docs/16-damage-system.md` — before: **0**, after: **1**. Task 14.1.

- [x] 14.8 `grep -c -F "placed seated" docs/14-glossary.md` — before: **0**, after: **1**. Task 14.2.

- [x] 14.9 `grep -c -F "DMG-005, DMG-006" docs/12-melee.md` — before: **0**, after: **1**. Task 14.3.

- [x] 14.10 `grep -c -F "The order ranks these four levels only" docs/02-core-rules.md` — before: **0**, after: **1**. Task 14.4.

- [x] 14.11 `grep -c -F "by itself" docs/02-core-rules.md` — before: **1**, after: **0**. Task 14.5.

- [x] 14.12 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` This is what confirms task 14.3's new `DMG-005` citation resolves.

- [x] 14.13 `python3 scripts/check_task_anchors.py core-states-only-what-it-owns` — must **exit 0**.

- [x] 14.14 `python3 scripts/preflight.py` — as in 13.18, `Rule IDs are stable` is still expected to FAIL until the prerequisite merges, and every other check must PASS. Record it, tick this box, and carry on.

- [x] 14.15 `git status --short` — now **four** modified files: `docs/02-core-rules.md`, `docs/12-melee.md`, `docs/14-glossary.md` and `docs/16-damage-system.md`, plus the untracked change directory as a single `??` entry.
