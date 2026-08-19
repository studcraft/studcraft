# Tasks — A chapter groups more than one rule

## How to apply this change

Every anchor below was checked with exact-substring matching against the
pre-change files and occurs **exactly once in the file its task names**.
Replace the whole anchor.

If an anchor returns anything other than 1, **stop and report it** rather than
guessing which occurrence was meant. Never edit a document to make a
verification command pass — report the mismatch instead.

### How to read the replacement blocks

The triple-backtick fence marks where the text starts and stops. **The fence is
not part of the text** — do not write the backticks into the document.

A `#` heading or a `---` horizontal rule inside a fence is real markdown that
must land in the file as markdown, not as quoted text. Several anchors carry a
line of prose or a `---` above the heading they change; that line is a
**landmark** — it must stay in the file, and it is in the anchor only to make
the anchor unique.

**Count the `#` characters.** Almost every edit here changes nothing but the
number of them on one line. An anchor reading `# DMG-004` and a replacement
reading `## DMG-004` differ by a single character, and getting it backwards
produces a file that still looks plausible. Copy both blocks exactly.

### The three things this change must not do

**No rule ID changes.** Nothing is renumbered, retired or reused. Every
`XXX-NNN` in every anchor appears unchanged in its replacement —
`system/documentation-standards.md` (Naming Conventions).

**No gameplay value changes.** The only prose this change touches is three
chapter blurbs that are deleted and one sentence that moves into `INF-011`. If
a replacement block would alter a distance, a cost, a die roll or a
measurement, it is wrong — stop and report it.

**No rule goes to `###`.** `repo.RULE_HEADER_RE` is `^#{1,2} ([A-Z]{2,6})-(\d{3}) — `,
so a rule written three deep becomes invisible to five scripts at once, and
silently. The eight worked examples in section 4 are the only headings that
reach `###`, and none of them is a rule.

- [x] 0.1 The branch is `a-chapter-groups-more-than-one-rule`, named for this
  change directory, and it is branched from an up-to-date `main`.

### Scope and coverage

Five ruleset documents, one `system/` document, one script and its test:
**forty-six anchor pairs across the five ruleset documents, plus five more
across the three files outside `docs/` — fifty-one in all.** Every one of them
is an anchor-and-replacement pair that `scripts/apply_tasks.py` places; nothing
here is typed. No spec delta — `design.md`, Decision 7.

| `proposal.md` item | Task | Path |
|---|---|---|
| Seven one-rule chapters deleted | 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7 | `docs/02-core-rules.md` |
| Terrain Movement keeps its three rules | 2.1, 2.2, 2.3 | `docs/07-movement.md` |
| `# Falling` deleted | 2.4 | `docs/07-movement.md` |
| `# Damaged Weapons` deleted | 3.1 | `docs/11-combat.md` |
| Nineteen rules move to `##` | 4.1, 4.19 | `docs/16-damage-system.md` |
| Eight worked examples move to `###` | 4.20, 4.27 | `docs/16-damage-system.md` |
| Terrain keeps its five rules | 5.1, 5.5 | `docs/17-infantry.md` |
| `# Falling` deleted, its pointer folded into `INF-011` | 5.6 | `docs/17-infantry.md` |
| `# Damage Effects` deleted | 5.7 | `docs/17-infantry.md` |
| The rule itself | 6.1 | `system/documentation-standards.md` |
| The docstring bullet that announces the check | 6.2 | `scripts/lint_ruleset.py` |
| The check | 6.3 | `scripts/lint_ruleset.py` |
| The check wired into `main` | 6.4 | `scripts/lint_ruleset.py` |
| The test that pins it | 6.5 | `tests/test_lint_ruleset.py` |

**Untouched, deliberately:** `# Unit Types` and `# Line of Sight` in
`docs/02-core-rules.md` — both already group two or more rules at `##`, and
they are the pattern the rest of `docs/` adopts here. Every `#` section holding
no rules: `# The Battlefield`, `# Universal Rule`, `# Physical Priority`,
`# Combat Flow`, `# Turn Sequence`, `# Examples`, `# Weapon Archetypes`,
`# Design Notes`, `# Combat Examples`, `# Combat Philosophy`, and every
`# Purpose`, `# Design Philosophy` and `# Summary`. `docs/01-foundations.md`,
`docs/03-game-flow.md`, `docs/05-construction-components.md`,
`docs/06-deployment.md`, `docs/08-vehicles.md`, `docs/09-transport.md`,
`docs/10-weapons.md`, `docs/12-melee.md`, `docs/14-glossary.md`,
`docs/15-geometry-layers.md`. `openspec/specs/`. `CHANGELOG.md` and every
version header.

---

## 1. `docs/02-core-rules.md` — seven chapters that group one rule

Each of the seven groups one rule, which is what makes it a chapter over
nothing. The chapter heading goes; the rule takes its place at `#`. **The `---`
above each chapter is not in any anchor and stays where it is**, becoming the
separator before the rule.

- [x] 1.1 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Unit Base

## CORE-001 — Unit Base (UB)
```

with:

```
# CORE-001 — Unit Base (UB)
```

- [x] 1.2 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Unit Orientation

## CORE-002 — Facing
```

with:

```
# CORE-002 — Facing
```

- [x] 1.3 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Activation

## CORE-006 — Action Points
```

with:

```
# CORE-006 — Action Points
```

- [x] 1.4 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Interactive Elements

## CORE-007 — Physical Interaction
```

with:

```
# CORE-007 — Physical Interaction
```

- [x] 1.5 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Cover

## CORE-010 — Physical Cover
```

with:

```
# CORE-010 — Physical Cover
```

- [x] 1.6 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Equipment

## CORE-014 — Visible Equipment
```

with:

```
# CORE-014 — Visible Equipment
```

- [x] 1.7 In `docs/02-core-rules.md`, replace this anchor — the chapter heading and the rule heading under it:

```
# Physical State

## CORE-016 — Battlefield Representation
```

with:

```
# CORE-016 — Battlefield Representation
```


---

## 2. `docs/07-movement.md`

`# Terrain Movement` groups three rules and stays. Tasks 2.1 to 2.3 put those
three at `##` under it. **2.1 also removes the `---` between the chapter's
intro line and its first rule** — a chapter is not separated from its own first
rule, which is how `# Unit Types` and `# Line of Sight` are already written.
The `---` between siblings stays.

- [x] 2.1 In `docs/07-movement.md`, replace this anchor — the chapter's closing line, the rule below it, and the `---` between them:

```
Terrain physically affects movement.

---

# MOVE-012 — Slopes
```

with:

```
Terrain physically affects movement.

## MOVE-012 — Slopes
```

- [x] 2.2 In `docs/07-movement.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# MOVE-013 — Stairs
```

with:

```
---

## MOVE-013 — Stairs
```

- [x] 2.3 In `docs/07-movement.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# MOVE-014 — Vertical Access
```

with:

```
---

## MOVE-014 — Vertical Access
```


- [x] 2.4 In `docs/07-movement.md`, replace this anchor — the whole `# Falling` chapter heading, its one sentence, and the `---` below it. `# MOVE-015 — Falling` is a landmark and keeps its level:

```
# Falling

When a unit falls and where it lands are stated here. What the fall costs is its own domain's rule.

---

# MOVE-015 — Falling
```

with:

```
# MOVE-015 — Falling
```

  **The blurb is deleted, not moved.** `MOVE-015` already says a unit may step off a ledge "at the risk its own domain's rule describes" and cites both domains. The chapter said the same thing one line above it — `design.md`, Decision 3.


---

## 3. `docs/11-combat.md`

`# Damaged Weapons` groups only `CBT-015`, and `CBT-015` is already written at
`#`, so the chapter and its one rule are peers. The chapter goes and the rule
stays exactly as it is.

- [x] 3.1 In `docs/11-combat.md`, replace this anchor — the chapter heading, its one sentence, and the rule heading below it. `# CBT-015 — Attacking While Wounded` is a landmark and keeps its level:

```
# Damaged Weapons

What a weapon's own damage does to the attack it makes.

# CBT-015 — Attacking While Wounded
```

with:

```
# CBT-015 — Attacking While Wounded
```

  **Note there is no `---` between the blurb and `CBT-015`** — the anchor is four lines, not six. The blurb is deleted rather than moved: `CBT-015` already says "This rule reads the state of the component that provides the attack."


---

## 4. `docs/16-damage-system.md` — two chapters, nineteen rules

`# Component Damage` groups eight rules and `# Damage Resolution` eleven. Both
chapters stay, both keep their intro paragraphs, and all nineteen rules move to
`##`.

**4.1 and 4.9 are the two that also drop a `---`** — the one between a
chapter's intro and its first rule. Every other task in this section changes
one line and nothing else.

- [x] 4.1 In `docs/16-damage-system.md`, replace this anchor — the chapter's closing line, the rule below it, and the `---` between them:

```
This section defines the structural model: components, geometry-derived Resistance, and the universal state machine every component uses.

---

# DMG-001 — Component Targeting
```

with:

```
This section defines the structural model: components, geometry-derived Resistance, and the universal state machine every component uses.

## DMG-001 — Component Targeting
```

- [x] 4.2 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-002 — Components Have No Hit Points
```

with:

```
---

## DMG-002 — Components Have No Hit Points
```

- [x] 4.3 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-003 — Geometry Defines Resistance
```

with:

```
---

## DMG-003 — Geometry Defines Resistance
```

- [x] 4.4 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-004 — Reading Component Resistance
```

with:

```
---

## DMG-004 — Reading Component Resistance
```

- [x] 4.5 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-005 — Component State Progression
```

with:

```
---

## DMG-005 — Component State Progression
```

- [x] 4.6 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-006 — Universal Destruction
```

with:

```
---

## DMG-006 — Universal Destruction
```

- [x] 4.7 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-007 — Internal Components
```

with:

```
---

## DMG-007 — Internal Components
```

- [x] 4.8 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-008 — No Material-Specific Mechanics
```

with:

```
---

## DMG-008 — No Material-Specific Mechanics
```

- [x] 4.9 In `docs/16-damage-system.md`, replace this anchor — the chapter's closing line, the rule below it, and the `---` between them:

```
The LEGO model defines capability. The dice introduce uncertainty.

---

# DMG-009 — Combat Resolution Overview
```

with:

```
The LEGO model defines capability. The dice introduce uncertainty.

## DMG-009 — Combat Resolution Overview
```

- [x] 4.10 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-010 — Generate Impacts
```

with:

```
---

## DMG-010 — Generate Impacts
```

- [x] 4.11 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-011 — Attack Roll
```

with:

```
---

## DMG-011 — Attack Roll
```

- [x] 4.12 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-012 — Select Target Component
```

with:

```
---

## DMG-012 — Select Target Component
```

- [x] 4.13 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-013 — Composite Vehicle Targeting
```

with:

```
---

## DMG-013 — Composite Vehicle Targeting
```

- [x] 4.14 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-014 — Geometry Check
```

with:

```
---

## DMG-014 — Geometry Check
```

- [x] 4.15 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-015 — Damage Roll
```

with:

```
---

## DMG-015 — Damage Roll
```

- [x] 4.16 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-016 — Multiple Impacts
```

with:

```
---

## DMG-016 — Multiple Impacts
```

- [x] 4.17 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-017 — Penetration
```

with:

```
---

## DMG-017 — Penetration
```

- [x] 4.18 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-018 — Weapon Distribution
```

with:

```
---

## DMG-018 — Weapon Distribution
```

- [x] 4.19 In `docs/16-damage-system.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# DMG-019 — Repairs
```

with:

```
---

## DMG-019 — Repairs
```


### The worked examples inside `DMG-004` and `DMG-017`

`DMG-004` carries seven worked examples and `DMG-017` one, all written at `##`.
Tasks 4.1 to 4.19 put the rules that own them at `##` too, which would make each
example the rule's sibling rather than its subsection. They move to `###`.

**These eight are the only headings in this change that reach `###`, and none of
them is a rule** — `design.md`, Decision 4.

- [x] 4.20 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 1 — Minifig
```

with:

```
### Example 1 — Minifig
```

- [x] 4.21 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 2 — Mounted Cannon
```

with:

```
### Example 2 — Mounted Cannon
```

- [x] 4.22 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 3 — Shield built with Bricks
```

with:

```
### Example 3 — Shield built with Bricks
```

- [x] 4.23 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 4 — Shield built with Plates
```

with:

```
### Example 4 — Shield built with Plates
```

- [x] 4.24 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 5 — Bunker
```

with:

```
### Example 5 — Bunker
```

- [x] 4.25 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 6 — Moulded Windscreen
```

with:

```
### Example 6 — Moulded Windscreen
```

- [x] 4.26 In `docs/16-damage-system.md`, replace this anchor — one heading line:

```
## Example 7 — Vehicle Hull
```

with:

```
### Example 7 — Vehicle Hull
```

- [x] 4.27 In `docs/16-damage-system.md`, replace this anchor — the heading inside `DMG-017`, and the line under it. That line is a landmark and does not change; it is in the anchor because `## Example` on its own is a substring of `## Example 1 — Minifig`:

```
## Example

Heavy Cannon (`Strength 6`) vs. Shield (`Resistance 3`)
```

with:

```
### Example

Heavy Cannon (`Strength 6`) vs. Shield (`Resistance 3`)
```


---

## 5. `docs/17-infantry.md`

`# Terrain` groups five rules and stays; they move to `##`. `# Falling` and
`# Damage Effects` group one each and go.

- [x] 5.1 In `docs/17-infantry.md`, replace this anchor — the chapter's closing line, the rule below it, and the `---` between them:

```
what infantry can do with them is below.

---

# INF-006 — One Brick Obstacles
```

with:

```
what infantry can do with them is below.

## INF-006 — One Brick Obstacles
```

- [x] 5.2 In `docs/17-infantry.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# INF-007 — Two Brick Obstacles
```

with:

```
---

## INF-007 — Two Brick Obstacles
```

- [x] 5.3 In `docs/17-infantry.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# INF-008 — Three Brick Obstacles
```

with:

```
---

## INF-008 — Three Brick Obstacles
```

- [x] 5.4 In `docs/17-infantry.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# INF-009 — Slopes and Stairs
```

with:

```
---

## INF-009 — Slopes and Stairs
```

- [x] 5.5 In `docs/17-infantry.md`, replace this anchor — the rule heading and the `---` above it:

```
---

# INF-010 — Vertical Access
```

with:

```
---

## INF-010 — Vertical Access
```


- [x] 5.6 In `docs/17-infantry.md`, replace this anchor — the `# Falling` chapter, the `---` below it, and `INF-011`'s heading and first paragraph:

```
# Falling

When a unit falls at all, and where it lands, is `07-movement.md` (MOVE-015). What the fall costs an infantry model is below.

---

# INF-011 — Falling Damage

Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (INF-006).
```

with:

```
# INF-011 — Falling Damage

Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (INF-006). When a unit falls at all, and where it lands, is `07-movement.md` (MOVE-015).
```

  **This is the one blurb in the change that is not redundant, and it is moved rather than deleted.** It carries the ruleset's only pointer from Infantry's falling damage to `07-movement.md` (MOVE-015), which states when a unit falls at all and where it lands. `INF-011` never cited it, so deleting the heading without folding the sentence in would drop a cross-reference — `design.md`, Decision 3. **The replacement does two things — read it against the anchor rather than against this note.** The navigational half-sentence, "What the fall costs an infantry model is below", goes with the heading, because after this nothing is above anything. The `MOVE-015` pointer moves word for word, appended to `INF-011`'s first paragraph. Task 7.7 is the check that it survived.


- [x] 5.7 In `docs/17-infantry.md`, replace this anchor — the chapter heading, its one sentence, and the `---` below it. `# INF-012 — Wounded Movement` is a landmark and keeps its level:

```
# Damage Effects

What a damaged infantry model can still do. The Component States themselves are `16-damage-system.md` (DMG-005).

---

# INF-012 — Wounded Movement
```

with:

```
# INF-012 — Wounded Movement
```

  Deleted, not moved: `INF-012`'s own first line already cites `16-damage-system.md` (DMG-005) for the Component States.

---

## 6. The rule, and the check that keeps it

**These three files sit outside `docs/`, and shipping them on this branch is a
deliberate choice** — `design.md`, Decision 8. Splitting them lands a ruleset
whose convention is written nowhere and enforced by nothing.

**Apply this section after sections 1 to 5.** Task 6.4 makes the linter fail on
a one-rule chapter, and until sections 1 to 5 have landed `docs/` holds eleven —
seven of which the check can see.

- [x] 6.1 In `system/documentation-standards.md`, the `# Documentation Guidelines` section, replace this anchor — the last two lines of the first paragraph:

```
rules; `02-core-rules.md` predates the standard and is a recorded exemption in
the linter, not a precedent.
```

with:

```
rules; `02-core-rules.md` predates the standard and is a recorded exemption in
the linter, not a precedent.

A `#` chapter heading exists only to group two or more rules, and the rules
inside one are written at `##`; a rule belonging to no chapter is written at
`#`. A chapter over a single rule says nothing that rule's own heading does not,
and is deleted rather than kept. A `#` section holding no rules is prose, not a
chapter, and this does not reach it.

A rule's own sub-headings — worked examples, tables of cases — sit one level
below the rule wherever the rule sits: `##` under a standalone rule, `###`
under one inside a chapter. **No rule is itself written at `###`.**
`repo.RULE_HEADER_RE` matches one `#` or two, so a rule three levels deep is
invisible to every script that reads the ruleset, and invisible silently.
```

  The rule lands beside the document skeleton it belongs with. It states the
  `###` ceiling because that is the part with a consequence a reader cannot see
  (`design.md`, Decision 4), and it states where a rule's own sub-headings go
  because this change moves eight of them and `docs/06-deployment.md` keeps four
  more at a different level for the same reason — without the clause the two
  look like a contradiction.

- [x] 6.2 In `scripts/lint_ruleset.py`, the module docstring, replace this anchor — one bullet:

```
- The document skeleton required by system/documentation-standards.md:
  Purpose, Design Philosophy and Summary sections, and a closing motto.
```

with:

```
- The document skeleton required by system/documentation-standards.md:
  Purpose, Design Philosophy and Summary sections, and a closing motto.
- A `#` chapter heading that groups exactly one rule. A chapter groups two
  or more; a `#` heading with no rules under it is prose, not a chapter,
  and is not reported.
```

- [x] 6.3 In `scripts/lint_ruleset.py`, replace this anchor — the end of `check_structure` and the line that opens `check_versions`. **Both lines are landmarks**: the new constant and function go between them, and neither existing line changes:

```
    return errors


def check_versions(texts: dict[str, str]) -> list[str]:
```

with:

```
    return errors


# A heading at `#` or `##`, split into its hashes and its title. A rule heading
# is one whose title starts with a rule ID; any other `#` heading is either a
# chapter over rules or a section of prose, and only the number of rules under
# it tells those two apart.
HEADING_DEPTH_RE = re.compile(r"^(#{1,2}) (\S.*?)\s*$")


def check_chapter_depth(texts: dict[str, str]) -> list[str]:
    """A `#` chapter heading exists only to group two or more rules.

    system/documentation-standards.md (Documentation Guidelines) states the
    convention: the rules inside a chapter are written at `##`, a rule
    belonging to no chapter at `#`, and a chapter holding a single rule says
    nothing that rule does not already say in its own heading.

    Zero is not one. A `#` heading with no rules under it is prose — Purpose,
    Summary, Combat Flow, Weapon Archetypes — and is not a chapter over rules
    at all. Checking for *exactly* one is what lets this run over the whole of
    docs/ without carrying a list of exceptions.

    **Only half the convention is mechanical.** A chapter whose rules were left
    at `#` is indistinguishable from a run of standalone rules: same text, same
    level, and what separates them is what the author meant. That half needs a
    reader, and this function does not pretend to cover it.
    """
    errors: list[str] = []

    for name, text in sorted(texts.items()):
        # (line number, title, rules counted, whether the heading is itself a
        # rule). A rule at `#` closes the chapter above it exactly as a new
        # chapter heading does, so it is recorded here too and counts nothing.
        headings: list[list] = []

        for lineno, line in enumerate(text.splitlines(), start=1):
            heading = HEADING_DEPTH_RE.match(line)
            if not heading:
                continue
            hashes, title = heading.groups()
            is_rule = RULE_ID_RE.match(title) is not None

            if hashes == "#":
                headings.append([lineno, title, 0, is_rule])
            elif is_rule and headings and not headings[-1][3]:
                headings[-1][2] += 1

        for lineno, title, rules, is_rule in headings:
            if not is_rule and rules == 1:
                errors.append(
                    f"{name}:{lineno}: '# {title}' groups one rule. A chapter "
                    f"groups two or more — delete it and write the rule at '#', "
                    f"per system/documentation-standards.md"
                )

    return errors


def check_versions(texts: dict[str, str]) -> list[str]:
```

- [x] 6.4 In `scripts/lint_ruleset.py`, `main`, replace this anchor — two lines:

```
    errors.extend(check_structure(texts, ids_by_file))
    errors.extend(check_image_index(ids_by_file))
```

with:

```
    errors.extend(check_structure(texts, ids_by_file))
    errors.extend(check_chapter_depth(texts))
    errors.extend(check_image_index(ids_by_file))
```

- [x] 6.5 In `tests/test_lint_ruleset.py`, replace this anchor — the last test in the file. **It is a landmark and does not change**; the new class goes after it:

```
    def test_a_row_naming_no_file_is_still_returned(self):
        text = "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n| WPN-020 | to be drawn |\n"
        (entry,) = lint_ruleset.parse_image_entries(text)
        assert entry[3] == ""
```

with:

```
    def test_a_row_naming_no_file_is_still_returned(self):
        text = "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n| WPN-020 | to be drawn |\n"
        (entry,) = lint_ruleset.parse_image_entries(text)
        assert entry[3] == ""


CHAPTERED = """# 16-damage-system.md

# Purpose

Why this document exists.

# Design Philosophy

What it is built on.

# Component Damage

The structural model.

## DMG-001 — Component Targeting

Every impact is assigned to one component.

---

## DMG-002 — Components Have No Hit Points

A component has a state, not a total.

# DMG-003 — Geometry Defines Resistance

Resistance is read from the model.

# Summary

What the rules above say.

> **Every Brick Matters.**
"""

ONE_RULE_CHAPTER = CHAPTERED.replace(
    "---\n\n## DMG-002 — Components Have No Hit Points\n\n"
    "A component has a state, not a total.\n\n",
    "",
)


class TestChapterDepth:
    def test_a_chapter_of_two_and_a_rule_of_its_own_report_nothing(self):
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": CHAPTERED}) == []

    def test_a_chapter_holding_one_rule_is_reported(self):
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": ONE_RULE_CHAPTER})
        assert "Component Damage" in error

    def test_a_section_holding_no_rules_is_prose_and_not_a_chapter(self):
        text = CHAPTERED.replace("# Summary", "# Combat Flow\n\nA diagram.\n\n# Summary")
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": text}) == []

    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, this would look like a chapter
        # of two and the one-rule defect would go unreported.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "Component Damage" in error
```

  `.claude/rules/tooling.md` — a change to a script belongs in the same commit
  as the test that pins it. The fourth test is the one that matters: it pins
  that a rule written at `#` closes the chapter above it, which is what keeps a
  standalone rule from being counted as a chapter's second member and hiding
  the defect.

---

## 7. Verification

Run each command and write down what it actually returned. If a figure differs
from the one stated here, **stop and report it** — do not edit a file to make it
match. Every "before" figure was produced by running the command against the
pre-change files.

- [x] 7.1 `grep -c '^## CORE-' docs/02-core-rules.md` — before: **12**, after: **5**. Only `CORE-003`, `CORE-004`, `CORE-005`, `CORE-008` and `CORE-009` stay at `##`, because only they sit in a chapter that groups two or more.

- [x] 7.2 `grep -c '^# CORE-' docs/02-core-rules.md` — before: **0**, after: **7**. **7.1 and 7.2 are a pair.** 5 + 7 = 12: every rule is still there, and none was renumbered. If 7.1 is 5 and 7.2 is anything but 7, a rule was lost — stop and report it.

- [x] 7.3 `grep -c '^# DMG-' docs/16-damage-system.md` — before: **19**, after: **0**.

- [x] 7.4 `grep -c '^## DMG-' docs/16-damage-system.md` — before: **0**, after: **19**. **Pairs with 7.3** for the same reason.

- [x] 7.5 `grep -c '^### Example' docs/16-damage-system.md` — before: **0**, after: **8**: seven inside `DMG-004` and one inside `DMG-017`.

- [x] 7.6 `grep -rn '^# Falling' docs/` — before: **two hits**, `docs/07-movement.md` and `docs/17-infantry.md`. After: **no output at all**. Both were chapters over one rule.

- [x] 7.7 `grep -c -F 'MOVE-015' docs/17-infantry.md` — before: **2** (the `# Falling` blurb, and `INF-012`'s list of what a Wounded model's move leaves untouched), after: **2** (`INF-011`'s folded-in sentence, and the same `INF-012` line). The pointer task 5.6 moves into `INF-011` is **moved, not dropped**. A **1** means the blurb was deleted like the other three instead of folded in — stop and report it, because that loses a cross-reference nothing else carries.

- [x] 7.8 `python3 scripts/check_id_stability.py` — must **exit 0**. This is what confirms no rule ID moved document or number while its heading level changed.

- [x] 7.9 `python3 scripts/lint_ruleset.py` — before: `Checked 15 docs, no structural issues found.` After: the same line. **This one only means something once section 6 has landed** — before task 6.4 the new check is not wired in. Run against the pre-change `docs/` it reports **seven**, all in `02-core-rules.md`: those are the one-rule chapters whose rule is at `##`. The other four are the half `design.md` Decision 6 says no script can see, and they are removed by sections 2, 3 and 5 rather than by the check.

- [x] 7.10 `python3 scripts/check_task_anchors.py a-chapter-groups-more-than-one-rule` — must **exit 0**.

- [x] 7.11 `python3 scripts/preflight.py` — **every check must PASS**, the test suite included. Nothing here is expected to fail: no new document, no `openspec/specs/` delta, and `TODO.md` quotes none of the text this change moves.

- [x] 7.12 `git status --short` — **eight modified files**: `docs/02-core-rules.md`, `docs/07-movement.md`, `docs/11-combat.md`, `docs/16-damage-system.md`, `docs/17-infantry.md`, `system/documentation-standards.md`, `scripts/lint_ruleset.py`, `tests/test_lint_ruleset.py` — plus the untracked change directory as a single `??` entry. Anything else is a mismatch: report it and stage nothing.

---

## 8. Repairs after the audit of the applied text

The applied text was audited and returned seven findings. Five are repaired
here. One is a single word in `design.md` and is corrected there directly. The
seventh needs a change of its own and is recorded at the end.

**Two documents outside `docs/` join the change in this section**:
`.claude/agents/proposal-applier.md`, whose standing instruction this change
falsified, and the linter, which gains two checks it should have had.

**Every anchor in this section was checked against the applied files**, and each
occurs exactly once.

- [x] 8.1 In `docs/17-infantry.md`, `INF-011`, replace this anchor — the rule's first paragraph:

```
Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (INF-006). When a unit falls at all, and where it lands, is `07-movement.md` (MOVE-015).
```

with:

```
When a fall happens and where the unit is placed is the general rule (`07-movement.md`, MOVE-015); this rule states what it costs an infantry model. Falling damage depends on the height fallen, measured in plate layers — the same unit obstacles use (INF-006).
```

  **Task 5.6 folded the pointer into the wrong sentence.** One clause was about the unit of measurement and the other about which document owns what, joined by nothing. `08-vehicles.md` (VEH-026) already states the identical relationship — "When a fall happens and where the vehicle is placed is the general rule (`07-movement.md`, MOVE-015); this rule states what it costs" — so this takes that shape rather than inventing a second one (`CODE_OF_DESIGN.md`, Principle 12). It also restores the half task 5.6 dropped: VEH-026 shows the "what it costs" clause never needed a heading above it.


- [x] 8.2 In `system/documentation-standards.md`, replace this anchor — both paragraphs added by task 6.1:

```
A `#` chapter heading exists only to group two or more rules, and the rules
inside one are written at `##`; a rule belonging to no chapter is written at
`#`. A chapter over a single rule says nothing that rule's own heading does not,
and is deleted rather than kept. A `#` section holding no rules is prose, not a
chapter, and this does not reach it.

A rule's own sub-headings — worked examples, tables of cases — sit one level
below the rule wherever the rule sits: `##` under a standalone rule, `###`
under one inside a chapter. **No rule is itself written at `###`.**
`repo.RULE_HEADER_RE` matches one `#` or two, so a rule three levels deep is
invisible to every script that reads the ruleset, and invisible silently.
```

with:

```
A `#` chapter heading exists only to group two or more rules, and the rules
inside one are written at `##`; a rule belonging to no chapter is written at
`#`, because a chapter over one rule says nothing that rule's own heading does
not. A `#` section holding no rules is prose, not a chapter, and this does not
reach it.

A rule's own sub-headings — worked examples, tables of cases — sit one level
below the rule wherever the rule sits: `##` under a standalone rule, `###`
under one inside a chapter. **No rule is itself written at `###`.**
`repo.RULE_HEADER_RE` matches one `#` or two, so a rule three levels deep is
invisible to every script that reads the ruleset, and invisible silently. The
two sub-heading levels are not equivalent to the tooling either:
`repo.HEADING_RE` ends a rule's body at the next `#` or `##`, so a standalone
rule's `##` sub-headings fall outside the body `scripts/rule.py` and the index
print, while a chaptered rule's `###` ones do not.
```

  Two repairs in one edit. The first paragraph stated its rule twice — the prohibition, then the remedy restating the prohibition — where "How a Rule Is Written" allows one sentence and one reason clause; the reason is kept and the restated remedy goes. The second gains the sentence the audit asked for: `##` and `###` sub-headings are **not** interchangeable to the tooling, and presenting them as a free choice hides that `scripts/rule.py show DEP-009` prints without its four scenario sub-sections.


- [x] 8.3 In `.claude/agents/proposal-applier.md`, replace this anchor — one paragraph under "The vocabulary tasks use":

```
**Never change, remove or renumber an existing heading.** Rule IDs are permanently stable — a superseded rule keeps its number with a note. If a task appears to ask for a renumbering, stop and report it.
```

with:

```
**Never change or renumber a rule's ID or its title.** Rule IDs are permanently stable — a superseded rule keeps its number with a note. If a task appears to ask for a renumbering, stop and report it.

**A heading's `#` level is a different matter, and a task may legitimately change it.** `system/documentation-standards.md` fixes which level a rule is written at, so moving a rule between `#` and `##`, or deleting a chapter heading that groups only one rule, is an ordinary edit. The ID and the title still do not change.
```

  **This change falsified a standing instruction, and every future one like it would too.** It changed the level of forty-six headings and deleted eleven, which the old sentence told the applier to stop and report. The intent was always rule-ID stability — the second sentence says so — but the literal scope was heading text *and* level (`system/proposal-review.md`, "Absolute claims falsified by a later fix"). An agent constraint that is routinely ignored stops constraining anything.


- [x] 8.4 In `scripts/lint_ruleset.py`, the module docstring, replace this anchor — the bullet added by task 6.2:

```
- A `#` chapter heading that groups exactly one rule. A chapter groups two
  or more; a `#` heading with no rules under it is prose, not a chapter,
  and is not reported.
```

with:

```
- The heading convention: a `#` chapter that groups exactly one rule, a
  rule written at `###` where no script can see it, and a `##` rule nested
  under another rule. A `#` heading with no rules under it is prose, not a
  chapter, and is not reported.
```


- [x] 8.5 In `scripts/lint_ruleset.py`, replace this anchor — the whole constant and function added by task 6.3:

```
# A heading at `#` or `##`, split into its hashes and its title. A rule heading
# is one whose title starts with a rule ID; any other `#` heading is either a
# chapter over rules or a section of prose, and only the number of rules under
# it tells those two apart.
HEADING_DEPTH_RE = re.compile(r"^(#{1,2}) (\S.*?)\s*$")


def check_chapter_depth(texts: dict[str, str]) -> list[str]:
    """A `#` chapter heading exists only to group two or more rules.

    system/documentation-standards.md (Documentation Guidelines) states the
    convention: the rules inside a chapter are written at `##`, a rule
    belonging to no chapter at `#`, and a chapter holding a single rule says
    nothing that rule does not already say in its own heading.

    Zero is not one. A `#` heading with no rules under it is prose — Purpose,
    Summary, Combat Flow, Weapon Archetypes — and is not a chapter over rules
    at all. Checking for *exactly* one is what lets this run over the whole of
    docs/ without carrying a list of exceptions.

    **Only half the convention is mechanical.** A chapter whose rules were left
    at `#` is indistinguishable from a run of standalone rules: same text, same
    level, and what separates them is what the author meant. That half needs a
    reader, and this function does not pretend to cover it.
    """
    errors: list[str] = []

    for name, text in sorted(texts.items()):
        # (line number, title, rules counted, whether the heading is itself a
        # rule). A rule at `#` closes the chapter above it exactly as a new
        # chapter heading does, so it is recorded here too and counts nothing.
        headings: list[list] = []

        for lineno, line in enumerate(text.splitlines(), start=1):
            heading = HEADING_DEPTH_RE.match(line)
            if not heading:
                continue
            hashes, title = heading.groups()
            is_rule = RULE_ID_RE.match(title) is not None

            if hashes == "#":
                headings.append([lineno, title, 0, is_rule])
            elif is_rule and headings and not headings[-1][3]:
                headings[-1][2] += 1

        for lineno, title, rules, is_rule in headings:
            if not is_rule and rules == 1:
                errors.append(
                    f"{name}:{lineno}: '# {title}' groups one rule. A chapter "
                    f"groups two or more — delete it and write the rule at '#', "
                    f"per system/documentation-standards.md"
                )

    return errors
```

with:

```
# A heading at `#`, `##` or `###`, split into its hashes and its title. A rule
# heading is one whose title starts with a rule ID; any other `#` heading is
# either a chapter over rules or a section of prose, and only the number of
# rules under it tells those two apart. `###` is matched so that a rule written
# there can be reported: repo.RULE_HEADER_RE stops at two, which is exactly what
# makes a three-deep rule vanish instead of fail.
HEADING_DEPTH_RE = re.compile(r"^(#{1,3}) (\S.*?)\s*$")

# A fenced block holds text about markdown, not markdown. This document set is
# the one most likely to contain a worked example of a heading, so a check that
# read one as real would fail a valid document on a required status check.
CODE_FENCE_RE = re.compile(r"^\s*```")


def check_chapter_depth(texts: dict[str, str]) -> list[str]:
    """The heading convention from system/documentation-standards.md.

    Three defects, and every one of them is silent otherwise:

    **A `#` chapter holding exactly one rule.** A chapter groups two or more;
    over one rule it says nothing that rule's own heading does not. Zero is not
    one — a `#` heading with no rules under it is prose (Purpose, Summary,
    Combat Flow, Weapon Archetypes) and is not a chapter over rules at all.
    Checking for *exactly* one is what lets this run over the whole of docs/
    without carrying a list of exceptions.

    **A rule written at `###`.** repo.RULE_HEADER_RE matches one `#` or two, so
    a rule three levels deep is read by no script in scripts/. It does not fail,
    it disappears, which is why it is worth a check rather than a comment.

    **A `##` rule directly under a `#` rule.** A rule is written at `##` only
    inside a chapter; under another rule it has a parent that cannot hold it.

    **What is not checked, because it cannot be:** a chapter whose rules were
    left at `#`. Those are indistinguishable from a run of standalone rules —
    same text, same level — and what separates them is what the author meant.
    That one needs a reader.
    """
    errors: list[str] = []

    for name, text in sorted(texts.items()):
        # (line number, title, rules counted, whether the heading is itself a
        # rule). A rule at `#` closes the chapter above it exactly as a new
        # chapter heading does, so it is recorded here too and counts nothing.
        headings: list[list] = []
        in_fence = False

        for lineno, line in enumerate(text.splitlines(), start=1):
            if CODE_FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            heading = HEADING_DEPTH_RE.match(line)
            if not heading:
                continue
            hashes, title = heading.groups()
            is_rule = RULE_ID_RE.match(title) is not None

            if hashes == "###":
                if is_rule:
                    errors.append(
                        f"{name}:{lineno}: '### {title}' is a rule written three "
                        f"levels deep. repo.RULE_HEADER_RE matches one '#' or two, "
                        f"so no script in scripts/ can see it — write it at '#' or "
                        f"'##', per system/documentation-standards.md"
                    )
                continue

            if hashes == "#":
                headings.append([lineno, title, 0, is_rule])
            elif is_rule:
                if headings and headings[-1][3]:
                    errors.append(
                        f"{name}:{lineno}: '## {title}' is a rule nested under "
                        f"'# {headings[-1][1]}', which is itself a rule. A rule is "
                        f"written at '##' only inside a chapter, per "
                        f"system/documentation-standards.md"
                    )
                elif headings:
                    headings[-1][2] += 1

        for lineno, title, rules, is_rule in headings:
            if not is_rule and rules == 1:
                errors.append(
                    f"{name}:{lineno}: '# {title}' groups one rule. A chapter "
                    f"groups two or more — delete it and write the rule at '#', "
                    f"per system/documentation-standards.md"
                )

    return errors

```

  **Three repairs, and two of them are defects the check was written to prevent.** *The fence.* The line loop read a fenced markdown example as real markdown, so a document showing a worked heading would fail the required `Docs ruleset linter` check with no way around it but rewriting the document. `docs/` has no such fence today, which made this latent rather than live. *The `###` rule.* `system/documentation-standards.md` calls a three-deep rule "invisible to every script that reads the ruleset, and invisible silently" — and then nothing checked for one. It is one branch. *The nested rule.* A `##` rule under a `#` rule is illegal under the same paragraph and equally mechanical. The docstring said "only half the convention is mechanical"; it was wrong by two cases, and now names what it does and does not cover.


- [x] 8.6 In `tests/test_lint_ruleset.py`, replace this anchor — the last test in `TestChapterDepth`. **It is a landmark and does not change**; three tests are added after it:

```
    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, this would look like a chapter
        # of two and the one-rule defect would go unreported.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "Component Damage" in error
```

with:

```
    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, this would look like a chapter
        # of two and the one-rule defect would go unreported.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "Component Damage" in error

    def test_a_rule_written_three_levels_deep_is_reported(self):
        text = CHAPTERED.replace(
            "# Summary", "### DMG-004 — Three Deep\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "three" in error
        # The point of the check: repo.RULE_HEADER_RE cannot see this heading,
        # so nothing else in scripts/ would have reported it.
        from repo import RULE_HEADER_RE

        assert "DMG-004" not in {f"{p}-{n}" for p, n in RULE_HEADER_RE.findall(text)}

    def test_a_rule_nested_under_another_rule_is_reported(self):
        text = CHAPTERED.replace(
            "# Summary", "## DMG-004 — Nested\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "nested under" in error

    def test_a_heading_inside_a_fenced_block_is_not_a_heading(self):
        # A document about document structure is the one most likely to show a
        # worked example of a heading. Read as real, the fenced `# Fake Chapter`
        # would close `# Component Damage` after one rule and fail a valid file.
        text = CHAPTERED.replace(
            "---\n\n## DMG-002",
            "```\n# Fake Chapter\n\n## DMG-999 — Fake\n```\n\n---\n\n## DMG-002",
        )
        assert lint_ruleset.check_chapter_depth({"16-damage-system.md": text}) == []
```

  `.claude/rules/tooling.md` — a change to a script belongs in the same commit as the test that pins it. The `###` test asserts the *reason* for the check as well as its output: `RULE_HEADER_RE` genuinely cannot see the heading, so nothing else would have reported it.


### Verification after section 8

- [x] 8.7 `grep -c -F 'this rule states what it costs' docs/17-infantry.md docs/08-vehicles.md` — **1** in each. The two falling-cost rules now state the same relationship the same way.

- [x] 8.8 `grep -c -F 'MOVE-015' docs/17-infantry.md` — **2**, unchanged by 8.1. The pointer moved within `INF-011`; it was not added or dropped.

- [x] 8.9 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.` The two new branches must report nothing against the applied `docs/`: no rule is at `###` and no rule is nested under another.

- [x] 8.10 `python3 scripts/preflight.py` — all 12 checks PASS, the test suite included. **Three new tests must pass**, and one of them is the fenced-block case that fails against the pre-8.5 function.

- [x] 8.11 `python3 scripts/check_task_anchors.py a-chapter-groups-more-than-one-rule` — must **exit 0**.

- [x] 8.12 `git status --short` — **ten** modified files: the eight from 7.12 plus `.claude/agents/proposal-applier.md`, and the change directory. `docs/08-vehicles.md` is **not** among them — 8.7 reads it, and nothing edits it.

### Not repaired here

**`repo.HEADING_RE` ends a rule's body at any `#` or `##` heading**, so
`scripts/rule.py show DEP-009` and the ruleset index both print that rule
without its four scenario sub-sections (`docs/06-deployment.md`, `## Patrol`
through `## Massive Battle`). Task 8.2 makes the consequence visible in the
written rule rather than leaving it implied.

**Fixing it is a tooling change, not a ruleset one**: narrowing the body
terminator touches `scripts/rule.py`, `scripts/build_index.py` and whatever the
index feeds, and it would land here with no proposal behind it and no test
budget. It is recorded in `proposal.md` under Out of Scope so the next reader
finds it stated rather than rediscovers it.

**Not a finding, and left alone:** whether `CORE-010` belongs inside
`# Line of Sight`, and `MOVE-019` and `MOVE-020` inside `# Terrain Movement`.
The convention this change writes governs a chapter's *depth*, not its
*membership*. Both are real questions and neither is this change's to settle.

### 8a. The landmark test was not a landmark

**Task 8.6 called this test unchanged, and it was wrong.** The section-8
preamble said every anchor was checked against the applied files; it did not say
the suite was run with 8.5 and 8.6 landed together, and it was not. The applier
found it, left task 8.10 unticked and reported it rather than editing anything
to pass — which is the standard.

**The check is right and the test is stale.** The fixture places
`## DMG-004` directly under `# DMG-003`, a rule at `#`, to exercise "a `#` rule
closes the chapter above it". That arrangement is *also* the nested-rule defect
task 8.5 added, so `check_chapter_depth` correctly returns two errors where the
`(error,) = ` unpacking expects one. Nothing about the function changes.

- [x] 8a.1 In `tests/test_lint_ruleset.py`, replace this anchor — the whole of `test_a_rule_at_the_top_level_closes_the_chapter_above_it`:

```
    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, this would look like a chapter
        # of two and the one-rule defect would go unreported.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        (error,) = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert "Component Damage" in error
```

with:

```
    def test_a_rule_at_the_top_level_closes_the_chapter_above_it(self):
        # DMG-003 sits at `#`, so the `##` rule below it counts toward nothing.
        # If a `#` rule did not close a chapter, `# Component Damage` would look
        # like a chapter of two and its one-rule defect would go unreported.
        #
        # That arrangement is *also* the nested-rule defect — a `##` rule under
        # a `#` rule — so two errors are correct here, and the two assertions
        # below are what keep this test about the first of them.
        text = ONE_RULE_CHAPTER.replace(
            "# Summary", "## DMG-004 — Reading Resistance\n\nHow.\n\n# Summary"
        )
        errors = lint_ruleset.check_chapter_depth({"16-damage-system.md": text})
        assert len(errors) == 2
        assert any("Component Damage" in error for error in errors)
        assert any("nested under" in error for error in errors)
```

  The two behaviours meet in one fixture because they describe one arrangement
  from two sides. Asserting both, and the count, is what stops a later change
  quietly dropping either.

- [x] 8a.2 `python3 scripts/preflight.py` — **all 12 checks PASS**, which is what task 8.10 asserted and could not reach. Tick 8.10 as well once this passes.

- [x] 8a.3 `python3 scripts/lint_ruleset.py` — `Checked 15 docs, no structural issues found.`, unchanged. This section touches a test and nothing else.
