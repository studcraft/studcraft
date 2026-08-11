# Tasks — Wounded degrades capability

## How to apply this change

Every anchor below was checked with exact-substring matching against the pre-change files and
occurs **exactly once in the file its task names**. Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than guessing which
occurrence was meant. Never edit a document to make a verification command pass — report the
mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is not part of the
text** — do not write the backticks into the document.

A `#` heading, a `|` table row or a `---` horizontal rule inside a fence is real markdown that must
land in the file as markdown, not as quoted text. Three blocks add a whole new rule and therefore
carry a real `#` heading, a real `---`, and the heading of the section that follows the new rule,
which the anchor removed and the replacement puts back: tasks 3.1 (`# Physical Priority`), 4.1
(`# Summary`) and 5.1 (`# Combat Flow`). Task 4.1's block also contains a real markdown table;
task 8.1's block contains the glossary's closing `> **Every Brick Matters.**` line; and task 9.1's
block contains a real `### ` heading and a real `> ` blockquote, which is `TODO.md`'s own format.

Several blocks repeat the anchor's own text with a paragraph added before or after it. That is
intentional — the anchor is a landmark, not only a target. Copy the block exactly.

**No existing rule is renumbered and no rule ID changes.** Three rule IDs are added — `MOVE-021`,
`VEH-031` and `CBT-015` — each at the end of its document's rule list, because
`scripts/lint_ruleset.py` requires rule IDs to increase within a document (`design.md`,
Decision 9).

**Task 9.1 edits `TODO.md`, whose quotes are checked verbatim** by
`scripts/check_todo_quotes.py`. Its blockquote reproduces two sentences that task 4.1 writes into
`VEH-031`. If those two blocks ever disagree, the check fails — copy both exactly.

- [x] 0.1 The branch is `wounded-degrades-capability`, named for this change directory, and it is
  branched from an up-to-date `main`.

### Scope and coverage

Eight ruleset documents, `TODO.md` and two spec deltas: **twenty-two edits and twenty-four non-edit
tasks** (0.1 and 10.1 – 10.23).

| `proposal.md` item | Task | Path |
|---|---|---|
| `DMG-005` — the Wounded paragraph | 1.1 | `docs/16-damage-system.md` |
| `DMG-008` — "identically to every component" | 1.2 | `docs/16-damage-system.md` |
| `DMG-011` — "the attacker rolls one die" | 1.3 | `docs/16-damage-system.md` |
| `16-damage-system.md` Summary | 1.4 | `docs/16-damage-system.md` |
| `CORE-012` rewritten | 2.1 | `docs/02-core-rules.md` |
| The paragraph above `CORE-011` | 2.2 | `docs/02-core-rules.md` |
| New `MOVE-021` | 3.1 | `docs/07-movement.md` |
| `MOVE-004` pointer | 3.2 | `docs/07-movement.md` |
| `MOVE-005` pointer | 3.3 | `docs/07-movement.md` |
| `MOVE-010` — the 12-stud figure | 3.4 | `docs/07-movement.md` |
| `07-movement.md` Summary — the count | 3.5 | `docs/07-movement.md` |
| `07-movement.md` Summary — a seventh principle | 3.6 | `docs/07-movement.md` |
| New `VEH-031` | 4.1 | `docs/08-vehicles.md` |
| `VEH-004` pointer | 4.2 | `docs/08-vehicles.md` |
| `08-vehicles.md` Summary | 4.3 | `docs/08-vehicles.md` |
| New `CBT-015` | 5.1 | `docs/11-combat.md` |
| `11-combat.md` Summary | 5.2 | `docs/11-combat.md` |
| `WPN-006` pointer | 6.1 | `docs/10-weapons.md` |
| `MEL-003` pointer | 7.1 | `docs/12-melee.md` |
| `MEL-008` pointer | 7.2 | `docs/12-melee.md` |
| Glossary ***Wounded*** entry | 8.1 | `docs/14-glossary.md` |
| `TODO.md` — "locomotion damage" | 9.1 | `TODO.md` |
| `component-damage` delta | already written | `openspec/changes/wounded-degrades-capability/specs/component-damage/spec.md` |
| `damage-resolution` delta | already written | `openspec/changes/wounded-degrades-capability/specs/damage-resolution/spec.md` |

**Untouched, deliberately:** `DMG-015` (the Damage Roll stays one D6 for every component state —
`design.md`, Decision 2), `DMG-010` (one impact per muzzle, which `CBT-015` explicitly preserves),
`DMG-016`, `MOVE-016` and all five of `16-damage-system.md`'s combat examples, every one of which
counts the two-failure path from Operational to Dead and stays literally true; `DMG-008`'s **second**
paragraph, whose "exactly two failed Damage Rolls" is unaffected — only its first paragraph is
edited, by task 1.2; `DMG-019` Repairs; `CBT-004`, which sits in the same document as `CBT-015` and
gets no pointer (`design.md`, Decision 10); `CBT-013`; `MOVE-012` and `MOVE-013`, which cite "the
normal movement limit (MOVE-004)" without naming a number and stay true; `VEH-019` and `VEH-026`,
which govern a *destroyed* locomotion and are outside this change; `MEL-005`, which routes melee
through `DMG-011` and therefore inherits task 1.3's edit; the glossary's *Component State*, *Attack
Dice*, *Damage Roll* and *Armour*
entries; `CHANGELOG.md` and every `**Version:**` header; `openspec/specs/` (both deltas live in this
change directory and are applied only by the Archive cut).

---

## 1. `docs/16-damage-system.md` — `DMG-005`, `DMG-008`, `DMG-011` and the Summary

- [x] 1.1 In `DMG-005`, replace this anchor — one line, the `Wounded` bullet of the three-state
  list. The `Operational` and `Dead` lines around it are **not** part of the anchor and are not
  touched:

```
**Wounded** — the component has suffered structural damage. It continues to function normally. A second successful damaging impact will kill it.
```

with:

```
**Wounded** — the component has suffered structural damage. It still functions, but the capability it provides is degraded. Exactly three degradations exist, each owned by the document that owns the capability: a Wounded infantry model's movement (`07-movement.md`, MOVE-021), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded (`11-combat.md`, CBT-015). That list is closed. Nothing else about a Wounded component changes: its Resistance (DMG-003), the Impact Strength of a weapon (`10-weapons.md`, WPN-021), the Damage Roll rolled against it (DMG-015), its Unit Base occupancy, its footprint, its transport capacity and every Action Point cost are all read exactly as they are for an Operational component. A second successful damaging impact will kill it, and a repair (DMG-019) returns it to Operational.
```

  The closed list is load-bearing and must land as written: it is what stops `Wounded` from being
  read as a general licence to halve things (`design.md`, Decision 1). Two phrasings inside it are
  equally deliberate. "How each Attack Die is **read**" — the *number* of Attack Dice does not
  change, and `CBT-015` spends a paragraph on that. And "the component **providing the attack**",
  not "the weapon" — in an unarmed attack (`12-melee.md`, MEL-008) that component is the
  minifigure, and a closed list must not close over a case `CBT-015` answers (`design.md`,
  Decision 8).

- [x] 1.2 In `DMG-008`, replace this anchor — one line, the rule's first paragraph. The second
  paragraph, which counts "exactly two failed Damage Rolls", is **not** part of the anchor and is
  not touched:

```
Every component follows exactly the same mechanical rules regardless of what it represents — glass, metal, wood, infantry, or anything else. Resistance (DMG-003/004), the Geometry Check (DMG-014), the Damage Roll (DMG-015), and the Component State machine (DMG-005) apply identically to every component. StudCraft does not define material-specific hit thresholds, Resistance modifiers, or damage tables of any kind.
```

with:

```
Every component follows exactly the same mechanical rules regardless of what it represents — glass, metal, wood, infantry, or anything else. Resistance (DMG-003/004), the Geometry Check (DMG-014), the Damage Roll (DMG-015), and the Component State machine (DMG-005) apply identically to every component; where DMG-005's Wounded state costs a component something, the cost is set by the capability that component provides — moving, or attacking — and never by the material it represents. StudCraft does not define material-specific hit thresholds, Resistance modifiers, or damage tables of any kind.
```

- [x] 1.3 In `DMG-011`, replace this anchor — one line, the rule's first paragraph. The `Example`
  line below it is **not** part of the anchor and is not touched:

```
The attacker rolls one die for every generated impact. A result of 4, 5, or 6 succeeds and creates one valid impact (per `11-combat.md` CBT-005's existing threshold). A result of 1, 2, or 3 fails; the impact simply disappears.
```

with:

```
The attacker rolls one die for every generated impact. A result of 4, 5, or 6 succeeds and creates one valid impact (per `11-combat.md` CBT-005's existing threshold). A result of 1, 2, or 3 fails; the impact simply disappears.

Where the component providing the attack is Wounded — the weapon, or the attacker itself in an unarmed attack (`12-melee.md`, MEL-008) — the roll for each impact is two dice read as one (`11-combat.md`, CBT-015). The number of impacts rolled for does not change.
```

  This rule states a count that `CBT-015` contradicts, which is why it is edited at all — it is not
  a signpost (`design.md`, Decision 10).

- [x] 1.4 In the `Summary`, replace this anchor — one line:

```
It defines: Components, Resistance, Structural States, Destruction, Internal Protection, and the absence of any material-specific mechanic (DMG-008); and the combat resolution sequence — Generate Impacts, Attack Roll, Select Target Component, Composite Vehicle Targeting, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Weapon Distribution, and Repairs.
```

with:

```
It defines: Components, Resistance, Structural States and what being Wounded costs (DMG-005), Destruction, Internal Protection, and the absence of any material-specific mechanic (DMG-008); and the combat resolution sequence — Generate Impacts, Attack Roll, Select Target Component, Composite Vehicle Targeting, Geometry Check, Damage Roll, Multiple Impacts, Penetration, Weapon Distribution, and Repairs.
```

---

## 2. `docs/02-core-rules.md` — `CORE-012` and the Infantry States preamble

- [x] 2.1 In `CORE-012`, replace this anchor — one line, the whole third paragraph of the rule. The
  two paragraphs above it (the seated position and the game marker) are **not** part of the anchor
  and are not touched:

```
A Wounded unit has no penalty of any kind — it moves, attacks, rotates, and climbs exactly as if Operational (`16-damage-system.md`, DMG-005: Wounded "continues to function normally"). The seated pose is purely a visual marker. The only consequence of Wounded is that the next successful Impact advances the minifigure to Dead (`11-combat.md`, CBT-008), the same as any other component.
```

with:

```
A Wounded minifigure's movement is reduced — `07-movement.md` (MOVE-021) states by how much. Its own movement is the only thing reduced: it rotates and falls exactly as if Operational, and a climb still costs the additional Action Point MOVE-010 charges, on top of a move that is now shorter. The weapons it carries are components in their own right and are degraded only when they are themselves Wounded (`11-combat.md`, CBT-015) — but an unarmed attack is the one attack whose weapon system is the minifigure itself (`12-melee.md`, MEL-008), so a Wounded minifigure punches worse, and CBT-015 says by how much. The seated pose is the marker for all of it — a seated model moves less, and the next successful Impact advances it to Dead (`16-damage-system.md`, DMG-005), the same as any other component.
```

  Three things about this replacement are deliberate. It does **not** repeat `MOVE-021`'s numbers
  (`design.md`, Decision 10). It does **not** say the model "climbs exactly as if Operational",
  because the climb sits inside a move that is now shorter. And the `CBT-008` citation is dropped:
  the replacement cites `DMG-005`, which is where the state progression it describes actually
  lives.

- [x] 2.2 In the `Infantry States` section, replace this anchor — one line, the paragraph above
  `CORE-011`:

```
Infantry uses the universal Component State machine (`16-damage-system.md`, DMG-005) exactly like any other component — CORE-011/012/013 describe the infantry-specific physical representation of each state, not a separate state system.
```

with:

```
Infantry uses the universal Component State machine (`16-damage-system.md`, DMG-005) exactly like any other component — CORE-011/012/013 describe the infantry-specific physical representation of each state, and what Wounded costs an infantry model, not a separate state system.
```

---

## 3. `docs/07-movement.md` — new `MOVE-021`, three pointers, and the Summary

- [x] 3.1 Replace this anchor — the section heading that follows the last rule in the document.
  The `---` already above it stays where it is and becomes the separator before the new rule:

```
# Physical Priority
```

with:

```
# MOVE-021 — Wounded Movement

A Wounded infantry model (`16-damage-system.md`, DMG-005) moves **at most two steps** in whichever direction it travels.

The step is the one that direction already uses (`02-core-rules.md`, CORE-001): the Unit Base's 3-stud depth forward and backward (MOVE-004, MOVE-006), and its 4-stud width sideways (MOVE-005). So a Wounded model may move **up to 6 studs forward or backward** and **up to 8 studs sideways** — distances those rules already allow, with the longer ones removed.

Nothing else about the move changes. It still costs **1 Action Point**, it still travels in a single direction (MOVE-007), and rotation (MOVE-008), slopes (MOVE-012), stairs (MOVE-013) and falling (MOVE-015, MOVE-016) are untouched. Climbing a two-brick obstacle still costs the 1 additional Action Point MOVE-010 charges — what changes there is the length of the move the climb belongs to, not the climb.

The limit is counted in steps rather than taken as half the normal distance because half of a side move is 6 studs, which MOVE-005 does not allow. A fraction of a legal distance is not always a legal distance; a count of steps always is.

---

# Physical Priority
```

- [x] 3.2 In `MOVE-004`, replace this anchor — the last line of the rule:

```
Future scenarios may allow sprinting or other special movement.
```

with:

```
A Wounded model's limit is lower — see MOVE-021.

Future scenarios may allow sprinting or other special movement.
```

  `TODO.md` quotes the sprinting line verbatim and `scripts/check_todo_quotes.py` checks it. The
  line is preserved exactly; the new paragraph goes **above** it.

- [x] 3.3 In `MOVE-005`, replace this anchor — the last line of the rule:

```
Side movement is a movement action and costs **1 Action Point**, the same as moving forward (MOVE-004).
```

with:

```
Side movement is a movement action and costs **1 Action Point**, the same as moving forward (MOVE-004).

A Wounded model's limit is lower — see MOVE-021.
```

  `MOVE-005` owns the 8-stud figure `MOVE-021` produces, so it gets its own pointer rather than
  inheriting `MOVE-004`'s.

- [x] 3.4 In `MOVE-010`, replace this anchor — one line:

```
The climb is part of that movement action and does not increase the distance the unit may travel: the 12-stud limit (MOVE-004) still applies to the move as a whole.
```

with:

```
The climb is part of that movement action and does not increase the distance the unit may travel: the limit on that move still applies as a whole — 12 studs (MOVE-004), or a Wounded model's shorter limit (MOVE-021).
```

  A concrete number that is wrong for a Wounded model. This is the only place in the ruleset where
  the 12-stud figure is restated as *the* limit. The replacement names no Wounded figure either:
  `MOVE-021` gives 6 forward or backward and 8 sideways, and 12 was correct on both axes before, so
  a single Wounded number here would be wrong on one of them.

- [x] 3.5 In the `Summary`, replace this anchor — one line:

```
Movement in StudCraft is based on six simple principles:
```

with:

```
Movement in StudCraft is based on seven simple principles:
```

- [x] 3.6 In the same `Summary`, replace this anchor — the last numbered point:

```
6. Physical construction always defines legal movement.
```

with:

```
6. Physical construction always defines legal movement.
7. A Wounded model moves at most two steps in any direction — 6 studs forward or backward, 8 sideways.
```

  Tasks 3.5 and 3.6 are one edit split in two because the list sits between them. Applying only one
  of the pair leaves the Summary claiming a count it does not have — the exact drift
  `system/proposal-review.md` records under *Verify the Number, Not Just the Direction*.

---

## 4. `docs/08-vehicles.md` — new `VEH-031`, a pointer, and the Summary

- [x] 4.1 Replace this anchor — the `Summary` heading and the sentence below it, together. The
  `---` already above the heading stays where it is and becomes the separator before the new rule:

```
# Summary

Vehicle behaviour is defined by six physical characteristics.
```

with:

```
# VEH-031 — Wounded Pilot

A vehicle whose Pilot (VEH-013) is Wounded (`16-damage-system.md`, DMG-005) moves **twice its own length** per movement action, instead of three times (VEH-004).

Facing, measurement and Action Point cost are unchanged. One whole length is removed rather than a fraction taken, so the distance stays a whole number of studs at every vehicle size, exactly as VEH-004's own multiplier does.

| Vehicle | Movement | With a Wounded Pilot |
|---|---:|---:|
| Bike | 18 studs | 12 studs |
| Buggy | 24 studs | 16 studs |
| Jeep | 27 studs | 18 studs |
| Tank | 45 studs | 30 studs |
| Heavy Transport | 72 studs | 48 studs |

The middle column is VEH-004's, repeated so the pair can be read together; only the right-hand column belongs to this rule.

The Pilot is the only component this rule reads, because VEH-013 already makes the Pilot the only component a powered vehicle needs in order to move at all — a Dead Pilot stops the vehicle, and a Wounded one slows it.

A Wounded wheel, track or hover assembly therefore reduces nothing on its own, and Terrain Thresholds (VEH-021 through VEH-024) are read from the locomotion's geometry whether it is Operational or Wounded. What VEH-019 calls "locomotion damage" is named there and defined by no rule; this rule does not define it either.

A destroyed locomotion is a different matter and is not this rule's: VEH-019 already governs a vehicle that cannot move at all.

---

# Summary

Vehicle behaviour is defined by six physical characteristics.
```

  The count **six** in that last line is correct and is not changed: `VEH-031` adds no physical
  characteristic — a Wounded Pilot is already covered by *Crew*.

  The two sentences beginning "A Wounded wheel, track or hover assembly" are quoted verbatim by
  task 9.1 in `TODO.md`, and `scripts/check_todo_quotes.py` compares them character for character.

- [x] 4.2 In `VEH-004`, replace this anchor — the last line of the rule:

```
This rule scales naturally for all vehicle sizes.
```

with:

```
A vehicle whose Pilot is Wounded moves twice its length instead of three times — see VEH-031.

This rule scales naturally for all vehicle sizes.
```

- [x] 4.3 In the `Summary`, replace this anchor — one line:

```
A player should understand how a vehicle behaves simply by examining its construction.
```

with:

```
A Wounded Pilot costs the vehicle one of its three lengths of movement (VEH-031); no other component's Wounded state changes how far it travels.

A player should understand how a vehicle behaves simply by examining its construction.
```

  The word **Wounded** in the second clause is what keeps this true: a *destroyed* wheel or track
  still immobilises the vehicle under VEH-019.

---

## 5. `docs/11-combat.md` — new `CBT-015` and the Summary

- [x] 5.1 Replace this anchor — the section heading that follows the last rule in the document.
  The `---` already above it stays where it is and becomes the separator before the new rule, and
  the ```` ``` ```` fence below it is not touched:

```
# Combat Flow
```

with:

```
# CBT-015 — Wounded Weapon System

A Wounded weapon (`16-damage-system.md`, DMG-005) still fires, less reliably.

For **each** Attack Die it generates (CBT-004; `10-weapons.md`, WPN-006; `12-melee.md`, MEL-003), roll **two dice instead of one, and read only the lower of the two**. That pair resolves as a single die against CBT-005's unchanged threshold: a 4, 5 or 6 generates one Impact, anything lower generates none. A hit therefore needs both dice at 4 or better — one chance in four, where an Operational weapon has one in two.

**The second die is never an Impact.** The number of Attack Dice is still the number of functional muzzles (`10-weapons.md`, WPN-006) or independently wielded melee weapons (`12-melee.md`, MEL-003), and each muzzle still generates exactly one impact (`16-damage-system.md`, DMG-010). A Wounded weapon rolls more dice and produces no more Impacts than it did before. `16-damage-system.md` (DMG-011) states the same thing from the damage side.

This rule reads the state of the component that provides the attack. Usually that is the weapon, which is a component in its own right (`16-damage-system.md`, DMG-001; `02-core-rules.md`, CORE-014): a Wounded soldier carrying an Operational rifle attacks exactly as if unhurt, and an unhurt soldier carrying a Wounded rifle rolls the pair of dice above.

An unarmed attack (`12-melee.md`, MEL-008) is the one case where the attacker *is* the weapon system, so there the rule reads the attacker: a Wounded minifigure punches with the pair of dice above.

Everything else the weapon has is unchanged: its Range (CBT-003), the Impact Strength of every die it rolls (`10-weapons.md`, WPN-021), the 1 Action Point the attack costs (CBT-001), and whether its dice may be split across targets (CBT-007).
```

- [x] 5.2 In the `Summary`, replace this anchor — the last line of the document above its closing
  motto:

```
This keeps StudCraft modular and entirely construction-driven.
```

with:

```
A Wounded weapon — or a Wounded minifigure attacking unarmed — generates the same number of Attack Dice and reads each of them worse (CBT-015).

This keeps StudCraft modular and entirely construction-driven.
```

---

## 6. `docs/10-weapons.md` — a pointer at `WPN-006`

The edit states no mechanic; it names the rule that owns one (`design.md`, Decision 10).

- [x] 6.1 In `WPN-006`, replace this anchor — the last line of the rule:

```
Rate of fire is entirely determined by construction.
```

with:

```
A Wounded weapon still grants one die per muzzle; what changes is how each of those dice is read (`11-combat.md`, CBT-015).

Rate of fire is entirely determined by construction.
```

---

## 7. `docs/12-melee.md` — a pointer at `MEL-003`

- [x] 7.1 In `MEL-003`, replace this anchor — one line, the paragraph about weapon systems and
  Action Points. The `Examples:` line and the fenced block below it are **not** part of the anchor
  and are not touched:

```
Each independently wielded weapon is its own weapon system (`10-weapons.md`, WPN-008) and costs its own **1 Action Point** to attack with (`11-combat.md`, CBT-001) — wielding two weapons and attacking with both is two attacks, not one attack producing two dice.
```

with:

```
Each independently wielded weapon is its own weapon system (`10-weapons.md`, WPN-008) and costs its own **1 Action Point** to attack with (`11-combat.md`, CBT-001) — wielding two weapons and attacking with both is two attacks, not one attack producing two dice.

If the weapon is Wounded, that die is rolled as `11-combat.md` (CBT-015) directs.
```

- [x] 7.2 In `MEL-008`, replace this anchor — one line, the rule's second paragraph. The first
  paragraph, which makes bare hands a weapon system for AP purposes, is **not** part of the anchor
  and is not touched:

```
An unarmed attack generates **1 Attack Die**, counting as a size-1 striking end (`10-weapons.md`, WPN-021) for Impact Strength purposes, representing punches, kicks, or physical force.
```

with:

```
An unarmed attack generates **1 Attack Die**, counting as a size-1 striking end (`10-weapons.md`, WPN-021) for Impact Strength purposes, representing punches, kicks, or physical force.

Because the attacker is the weapon system here, it is the attacker's own Component State that is read: a Wounded minifigure rolls that die as `11-combat.md` (CBT-015) directs.
```

  `MEL-008` is the rule the unarmed case belongs to, so it gets its own pointer rather than
  inheriting `MEL-003`'s fifty-nine lines above it (`design.md`, Decision 10).

---

## 8. `docs/14-glossary.md` — a new ***Wounded*** entry

This glossary is in **append order**, not alphabetical and not thematic, so the new entry goes at
the end of the file, after *Activation Order*. The *Component State* entry is not touched: it still
describes the three-state progression correctly.

- [x] 8.1 At the end of the file, replace this anchor — the document's closing motto, which is the
  last non-empty line:

```
> **Every Brick Matters.**
```

with:

```
## Wounded

The middle Component State: the component still functions, with the capability it provides degraded — a Wounded infantry model's movement (`07-movement.md`, MOVE-021), the movement of a vehicle whose Pilot is Wounded (`08-vehicles.md`, VEH-031), and how each Attack Die is read when the component providing the attack is Wounded, whether that is the weapon or an unarmed attacker (`11-combat.md`, CBT-015). Nothing else about the component changes, and the next successful damaging Impact advances it to Dead. See `16-damage-system.md`, DMG-005.

---

> **Every Brick Matters.**
```

  The `---` already above the anchor stays where it is and becomes the separator before *Wounded*.
  The motto must remain the last non-empty line of the file: `scripts/lint_ruleset.py` checks
  exactly that.

---

## 9. `TODO.md` — the gap `VEH-031` declares

`TODO.md` records gaps the ruleset declares in its own text, each with a verbatim quote. `VEH-031`
declares one, so it gets an entry. The new entry goes in the existing `## Vehicles` section, before
*Freeing a stranded vehicle*.

- [x] 9.1 In `./TODO.md`, replace this anchor — one line, an existing entry heading. The path is
  written with its leading `./` because `scripts/check_task_anchors.py` resolves a task's target
  only from a path containing a directory separator; without it the anchor is checked against the
  previous section's document and reported as missing:

```
### Freeing a stranded vehicle
```

with:

```
### What "locomotion damage" means

`VEH-031` (`docs/08-vehicles.md`):

> A Wounded wheel, track or hover assembly therefore reduces nothing on its own, and Terrain Thresholds (VEH-021 through VEH-024) are read from the locomotion's geometry whether it is Operational or Wounded. What VEH-019 calls "locomotion damage" is named there and defined by no rule; this rule does not define it either.

What would have to be decided: which components count as a vehicle's locomotion, what state they must reach before the vehicle is Immobilized (`VEH-019`), and whether losing some of them short of all of them does anything at all.

### Freeing a stranded vehicle
```

  The quote must match task 4.1's `VEH-031` text character for character —
  `scripts/check_todo_quotes.py` compares them and `scripts/preflight.py` runs it.

---

## 10. Verification

Run each command and write down what it actually returned. If a figure differs from the one stated
here, **stop and report it** — do not edit a document to make it match. Every "before" figure below
was produced by running the command against the pre-change files.

- [x] 10.1 `grep -c -F "continues to function normally" docs/16-damage-system.md` — before: **1**,
  after: **0**.

- [x] 10.2 `grep -c -F "no penalty of any kind" docs/02-core-rules.md` — before: **1**, after: **0**.

- [x] 10.3 `grep -c -F "MOVE-021" docs/07-movement.md` — before: **0**, after: **4** — the rule
  heading (3.1) and the pointers in `MOVE-004` (3.2), `MOVE-005` (3.3) and `MOVE-010` (3.4). The
  Summary's seventh point names no rule ID and is not counted here; task 10.11 covers it.

- [x] 10.4 `grep -c -F "VEH-031" docs/08-vehicles.md` — before: **0**, after: **3** — the rule
  heading (4.1), the `VEH-004` pointer (4.2) and the Summary (4.3).

- [x] 10.5 `grep -c -F "CBT-015" docs/11-combat.md` — before: **0**, after: **2** — the rule heading
  (5.1) and the Summary (5.2).

- [x] 10.6 `grep -c -F "CBT-015" docs/16-damage-system.md` — before: **0**, after: **2** — `DMG-005`
  (1.1) and `DMG-011` (1.3).

- [x] 10.7 `grep -c -F "CBT-015" docs/10-weapons.md` — before: **0**, after: **1**. This is the only
  edit in that document (6.1).

- [x] 10.8 `grep -c -F "CBT-015" docs/12-melee.md` — before: **0**, after: **2** — the `MEL-003`
  pointer (7.1) and the `MEL-008` pointer (7.2). These are the only two edits in that document.

- [x] 10.9 `grep -c -F "two dice read as one" docs/16-damage-system.md` — before: **0**, after:
  **1**. This is the `DMG-011` contradiction being closed (1.3).

- [x] 10.10 `grep -c -F "and never by the material it represents" docs/16-damage-system.md` —
  before: **0**, after: **1**. `DMG-008`'s first paragraph (1.2).

- [x] 10.11 `grep -c -F "at most two steps" docs/07-movement.md` — before: **0**, after: **2** —
  `MOVE-021`'s opening sentence (3.1) and the Summary's seventh point (3.6). `grep -c` counts
  matching lines, and these are two lines.

- [x] 10.12 `grep -c -F "12-stud limit" docs/07-movement.md` — before: **1**, after: **0**. The one
  place the ruleset restated 12 studs as *the* limit (3.4).

- [x] 10.13 `grep -c -F "twice its own length" docs/08-vehicles.md` — before: **0**, after: **1**.
  Task 4.2 deliberately writes "twice its length", without "own", so this stays at 1.

- [x] 10.14 `grep -c -F "read only the lower of the two" docs/11-combat.md` — before: **0**,
  after: **1**.

- [x] 10.15 `grep -c "^## Wounded$" docs/14-glossary.md` — before: **0**, after: **1**.

- [x] 10.16 `grep -c "six simple principles" docs/07-movement.md` — before: **1**, after: **0**.
  This is the pair-check for tasks 3.5 and 3.6: a non-zero result here means the count was left
  behind while the seventh point was added, or neither was done.

- [x] 10.17 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues
  found.` After: the same line. This is what confirms `MOVE-021`, `VEH-031` and `CBT-015` are
  strictly increasing within their documents and that every new cross-document citation points at a
  rule ID that exists.

- [x] 10.18 `python3 scripts/check_task_anchors.py wounded-degrades-capability` — must **exit 0**.
  Report the line it printed. Every anchor above is expected to report **zero** matches once the
  change has been applied and its boxes are ticked; on an unticked task a zero match is a defect.

- [x] 10.19 `python3 scripts/check_delta_coverage.py` — must **exit 0**. This change ships two
  deltas — `component-damage`'s *Component State Progression* and `damage-resolution`'s *Attack
  Roll* — and each carries every scenario the living spec has, unrenamed, plus new ones. Report the
  line.

- [x] 10.20 `python3 scripts/preflight.py` — must **exit 0**; report the summary line. This is the
  repository's required local gate and it is what covers this change, including `openspec validate`
  and the `TODO.md` quote check that task 9.1 depends on.

- [x] 10.21 `grep -c -F "what being Wounded costs" docs/16-damage-system.md` — before: **0**,
  after: **1**. The Summary edit (1.4), which no other check reaches.

- [x] 10.22 `grep -c -F "and what Wounded costs an infantry model" docs/02-core-rules.md` —
  before: **0**, after: **1**. The Infantry States preamble edit (2.2), which no other check
  reaches.

- [x] 10.23 `git status --short` — nine modified files — `TODO.md`, `docs/02-core-rules.md`,
  `docs/07-movement.md`, `docs/08-vehicles.md`, `docs/10-weapons.md`, `docs/11-combat.md`,
  `docs/12-melee.md`, `docs/14-glossary.md` and `docs/16-damage-system.md` — plus the untracked
  change directory `openspec/changes/wounded-degrades-capability/` reported as a single `??` entry.
  Anything else in the list is a mismatch: report it and stage nothing.
