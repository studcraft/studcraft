# Every glossary entry names the rule that owns it

## Why

`docs/14-glossary.md` holds 47 entries. **Twelve of them cite no rule at all.**

An entry a reader cannot trace to a rule is a definition with no owner. It can drift from
the rule it describes without anything noticing, and a reader who wants the full statement
has nowhere to go. The other 35 entries already carry a citation, so this is a gap in a
convention the document otherwise keeps, not a new obligation being invented for it.

The gap was surfaced mechanically by `python3 scripts/rule.py glossary`, which reports
entries citing no rule. It reports rather than fails precisely because of these twelve —
a gate that is red on arrival gets switched off.

## What Changes

**Eleven entries gain a citation.** Ten gain nothing but a `See …` sentence appended to
their last paragraph, in the form the document already uses. `Impact` is the exception:
its `See …` sentence goes on its first paragraph, and the parenthetical citation already
in its last paragraph gains a rule ID.

**Each entry cites the rule that *owns* the term, not one that restates it.** That
distinction did real work: four of these eleven were pointed at the wrong rule in an
earlier draft, in each case at a rule that cites the owner rather than at the owner.

| Entry | Cites | Why that rule |
|---|---|---|
| `AP` | `02-core-rules.md`, CORE-006; `03-game-flow.md`, FLOW-011 | CORE-006 defines Action Points and sets the allotment; FLOW-011 is *Action Economy*, whose opening line is the entry's own wording |
| `Impact` | `11-combat.md`, CBT-005; `16-damage-system.md`, DMG-009 | CBT-005 is where an Attack Die becomes an Impact; DMG-009 is the resolution overview the entry already gestures at |
| `Priority` | `03-game-flow.md`, FLOW-003 | FLOW-003 *is* Priority |
| `Activation` | `03-game-flow.md`, FLOW-004; `02-core-rules.md`, CORE-006 | FLOW-004 is Unit Activation; CORE-006 is where the 3 AP is defined, which FLOW-004 and FLOW-005 both say in as many words |
| `Open Transport` | `09-transport.md`, TRN-009 | TRN-009 *is* Open Transport |
| `Facing` | `02-core-rules.md`, CORE-002; `04-construction-standard.md`, SCS-004 | CORE-002 defines facing; SCS-004 makes an ambiguous front illegal |
| `Turn` | `03-game-flow.md`, FLOW-002 | FLOW-002 is Turn Structure |
| `Weapon Body` | `04-construction-standard.md`, SCS-017; `10-weapons.md`, WPN-003, WPN-018 | SCS-017 requires the body; the entry's second sentence is about Weapon Length and Weapon Width, which SCS-017 never mentions — WPN-003 defines the first and WPN-018 the second |
| `Weapon Front` | `10-weapons.md`, WPN-019 | WPN-019 states the definition this entry paraphrases, word for word. SCS-018 restates it and cites WPN-019 for it, as do WPN-003 and WPN-021 |
| `Weapon Front Footprint` | `10-weapons.md`, WPN-019 | WPN-019 defines the Front and its Footprint in one rule |
| `Weapon Capacity` | `10-weapons.md`, WPN-004 | WPN-004 *is* Weapon Capacity |

**The twelfth entry could not be fixed by citing anything, and that is the real finding.**

`Functional Component` has **two** owners. `SCS-006` and `CMP-001` carry the same title —
`Functional Components` — in different documents, define different things, and neither
cites the other:

- `SCS-006` — *"Interactive elements must physically exist."* Examples: doors, hatches,
  ramps, drawbridges, elevators, gates.
- `CMP-001` — *"A functional component is a physical part of a model that affects
  gameplay."* Examples: pilot, wheels, tracks, hover systems, weapons.

Two concepts wearing one name is Principle 12 (Consistency) and the "one idea, stated
once" standard, both broken. The glossary entry cannot name an owner because there are
two, with incompatible scopes.

**So `SCS-006` is retitled `Interactive Elements`**, and the glossary entry then cites
`CMP-001` alone.

That is not a compromise between two candidate names. `SCS-006`'s own first line reads
*"Interactive elements must physically exist"* — the title contradicts the body directly
beneath it, and every one of its examples is an interactive element. The ruleset already
uses the term throughout: `02-core-rules.md` has a section headed `Interactive Elements`,
`CORE-007` governs operating one, and `MOVE-018`, `MOVE-019` and `MOVE-020` each call the
thing they act on an interactive element. The retitle makes `SCS-006` say what it has
always meant.

**The retitle exposes a second duplication, and this change closes it too.** `SCS-006` and
`CORE-007` list the same six examples — doors, hatches, ramps, drawbridges, elevators,
gates — and assert the same thing about physical existence, and neither cites the other.
After the retitle, `SCS-006`'s title is character-identical to the section heading that
houses `CORE-007`. Moving a title next to an unacknowledged duplication is worse than
leaving it where it was, so `SCS-006` gains a one-sentence pointer to `CORE-007`, which is
what its immediate neighbours `SCS-007` and `SCS-008` already do.

## Impact

- **Affected documents:** `docs/14-glossary.md`, `docs/04-construction-standard.md`, and
  `.claude/agents/ruleset-auditor.md`, which carries two counts this change makes stale.
- **No rule ID changes.** `SCS-006` keeps its number; only its title text changes, which
  is precedented — `MEL-010` was retitled the same way.
- **No behaviour changes.** Every edit is editorial: eleven entries gain a citation, one
  gains a citation after a collision is resolved, one rule heading is corrected and gains a
  pointer, and one agent definition loses two counts that go stale.
- **Nothing cites `SCS-006`.** Verified with `python3 scripts/rule.py refs SCS-006` and
  with a grep across `docs/`, `assets/`, `README.md` and `CODE_OF_DESIGN.md`: the string
  appears only in its own header and in the gitignored `site/docs/` build output. The
  retitle breaks no reference.
- **No spec delta.** No capability under `openspec/specs/` covers the glossary or
  interactive elements, and `system/proposal-review.md` ("Delta vs. Direct Edit") is
  explicit that inventing a delta against a capability that does not exist is the wrong
  move.
- **Mechanically verifiable end state:** `python3 scripts/rule.py glossary` reports
  **0** entries citing no rule, down from 12.
