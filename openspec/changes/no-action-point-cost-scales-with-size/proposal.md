# No Action Point cost scales with size

## Why

`CORE-006` fixes the budget: **every unit receives exactly 3 Action Points**, with no
exception and no way to earn more. Against that fixed budget, two rules in the whole
ruleset charge by size:

> Embarking costs **1 Action Point per Unit Base** the embarking unit occupies — an
> infantry model (1 UB) costs 1 AP; a motorcycle (2 UB) costs 2 AP (`TRN-005`)

`TRN-006` says the same for disembarking. Everywhere else the price is already flat, and
flat in both directions — it varies neither with the model paying it nor with the thing
it acts on:

- `CORE-007` — 1 AP to open or close any interactive element, a hatch and a gate alike.
  `SCS-007`, `SCS-008` and `TRN-008` charge doors, ramps and access points by citing it.
- `CBT-001` — 1 AP per weapon system attacking, "regardless of how many Attack Dice that
  weapon system rolls". A bigger gun costs no more.
- `MOVE-008`, `VEH-008` – `VEH-011` — 1 AP to rotate, for a minifigure and for a tank.
- `MOVE-010` — 1 additional AP to climb an obstacle of 4 to 6 plate layers: the same
  price at 4 as at 6, and the same for any model that can climb it. Below 4 the crossing
  is free (`MOVE-009`), so the obstacle's height selects the rule rather than pricing the
  action.
- `DMG-019` — 1 AP to repair a Wounded component or stand up, whatever is standing.

**A fixed budget and a price that grows with the model do not survive each other.** A
unit occupying four Unit Bases needs 4 AP to embark and has 3. It cannot embark. If it
starts the game inside a transport it can never leave, because disembarking charges the
same way. Nothing in the ruleset says so: the model is not forbidden, it is priced out,
and the builder finds out at the table rather than in the text. `TRN-001` lists a Heavy
Walker "defined by its footprint" among the things a transport carries, and `TRN-003`'s
worked load counts a light walker of 2 UB beside its infantry, so the case is the
ruleset's own.

Nor does the physical model justify it. StudCraft charges Unit Bases for **space** —
`DEP-003` for the battlefield a model stands on, `TRN-003` for the compartment it fills.
Time is not space. A big model climbing into a truck does not perform the act of
climbing twice. Principle 1 asks the model to supply the values, and the model supplies
no such value; Principle 8 makes `CORE-006` the authority on the amount and on what may
be spent.

## What Changes

- **`CORE-006`** gains the rule in its own voice: no Action Point cost scales with size
  — neither the size of the unit paying it nor the size of what it acts on. It also says
  what to make of a rule that charges two: the reason is stated in that rule, and it is
  never size.
- **`TRN-005`** — embarking costs **1 Action Point**, whatever the unit occupies. Its
  motorcycle example goes with the multiplier; the requirements below it (adjacency, an
  open access point, a free Unit Base inside) are untouched.
- **`TRN-006`** — disembarking costs **1 Action Point**. Its restatement of the infantry
  case ("An infantry model (1 UB) therefore costs: **1 AP**") existed only to work the
  multiplier through an example, and goes with it.
- **`TRN-002`** — "The space was paid for on embarking (TRN-005)" now says the space is
  *claimed* on embarking. After this change `TRN-005` charges an action, not a volume,
  and a citation pointing at a payment it no longer contains is a citation aimed wrong.
- **`09-transport.md`'s Summary**, points 5 and 6, which repeat the per-Unit-Base
  figure.
- **One spec delta** — `action-economy` gains a requirement stating that an action's cost
  does not scale with size. The capability holds only the 3 AP allotment today, which is
  the supply half of the same economy.

## What Does Not Change

- **The allotment.** `CORE-006` and `FLOW-005` keep 3 AP for every unit, and nothing
  earns more.
- **`FLOW-006`.** "Each action's AP cost is defined in its corresponding rule document"
  stays true — this change makes those costs independent of size, not identical to each
  other.
- **Climbing.** `MOVE-010` keeps its additional Action Point, and `MOVE-009` keeps its
  free crossing below 4 plate layers. An obstacle's height selects which of the two
  applies; within each, the price is flat and a larger model pays no more. `CORE-006`
  says exactly that, and says it about terrain rather than about elements a unit
  operates. The movement rules are out of scope by the owner's instruction, and nothing
  here disturbs them.
- **Rotation.** Infantry turns to any facing for 1 AP (`MOVE-008`); a wheeled vehicle
  pays 1 AP per 90° turn (`VEH-008`), so a half-turn costs it two. That difference is
  locomotion, read off how the model is built, not size — Principle 1 working as
  intended.
- **Melee.** `12-melee.md`'s 2 AP for two weapon systems is two attacks, not a multiplier
  on one.
- **Who may embark, and where.** `TRN-005`'s requirements, `TRN-019`'s clearance and
  `DEP-005` are untouched. This change moves a price, not a permission.

## Out of Scope

- **The cargo-charging change** — "what is charged is charged whole", the rule that
  space is counted in whole Unit Bases rounded up. It is designed but not yet written
  into `openspec/changes/`, and one proposal per branch keeps it out of this one. This
  change removes the question that would otherwise have forced it to talk about
  embarking at all.
- **`CHANGELOG.md` and every `**Version:**` header.** Release-cut-only. No `**Bump:**`
  line is written either: `system/documentation-standards.md` (Versioning) makes minor
  the default and reserves the marker for a major, which this is not — a cost falls for
  large units and no previously legal model becomes illegal.
