# Design — No Action Point cost scales with size

## The defect, stated once

`CORE-006` sets a fixed supply: 3 Action Points per activation, for every unit, with no
profile able to raise it. `TRN-005` and `TRN-006` set a variable price: 1 AP per Unit
Base occupied. A fixed supply and a size-scaled price meet at a wall:

| Unit | Unit Bases occupied | Embark | Disembark | Budget |
|---|---|---|---|---|
| Infantry | 1 | 1 AP | 1 AP | 3 ✔ |
| Motorcycle | 2 | 2 AP | 2 AP | 3 ✔, but never both in one activation |
| Walker | 3 | 3 AP | 3 AP | 3 — the whole activation, nothing else |
| Walker | 4 | 4 AP | 4 AP | 3 ✘ **impossible** |

`TRN-001` lists a Heavy Walker "defined by its footprint" among the objects a transport
carries and `TRN-003`'s worked load counts a light walker of 2 UB beside four infantry,
so the fourth row is the ruleset's own case rather than a hypothetical. And the failure
is silent: no rule refuses the model, the arithmetic does.

---

## Decision 1 — The rule lives in `CORE-006`, not in `09-transport.md`

Principle 8 (One Universal Economy) already answers this: `CORE-006` is "the authority on
the amount **and on what may be spent**". A rule about what actions cost belongs beside
the rule about what a unit has to spend, and `CBT-001` already cites `CORE-006` when it
states a cost.

Putting it in `09-transport.md` would have made it look like a transport rule, and the
defect is not about transports — embarking is simply the only place the ruleset
currently charges by size. Stating it once in `CORE-006` also gives the next rule tempted
to charge by size something to be checked against.

Rejected: repeating the principle in `TRN-005` and `TRN-006`. That is the restatement #80
spent a whole change removing from the Unit Base's height. Both rules state their own
cost — 1 AP — and cite `CORE-006` for why it does not vary. For the same reason
`CORE-006` does **not** restate `TRN-005`'s figure: it says an infantry model and a
walker "pay the same to embark" and cites the rule that owns the number.

---

## Decision 2 — The rule bars scaling by size, in both directions

The owner's case was a door: "es tan ilógico como si la puerta es muy grande necesita más
AP. eso no." So the rule has to bar two things, not one — a cost that grows with the
**unit paying it**, and a cost that grows with the **thing it acts on**. An earlier draft
barred only the first, and would have left `CORE-007`'s "unless another rule specifies
otherwise" open to exactly the large-gate rule the owner rejected.

A repo-wide `grep` for AP charges in `docs/` finds them in `02-core-rules.md`,
`04-construction-standard.md`, `07-movement.md`, `08-vehicles.md`, `09-transport.md`,
`11-combat.md`, `12-melee.md`, `16-damage-system.md` and `17-components.md`. The rules
that set a price are these, and every one of them is flat once `TRN-005` and `TRN-006`
are fixed. `VEH-004` is the clearest statement of the principle already in the ruleset:
every vehicle covers three of its own lengths per action, "whatever its size".

| Rule | Charges | Varies with size? |
|---|---|---|
| `CORE-007` | 1 AP to open or close any interactive element | No — hatch and gate alike |
| `SCS-007`, `SCS-008`, `TRN-008` | doors, ramps, access points, 1 AP, citing `CORE-007` | No |
| `CBT-001` | 1 AP per weapon system attacking | No — "regardless of how many Attack Dice" |
| `12-melee.md` | 2 AP for two weapon systems | No — two attacks |
| `MOVE-008` | 1 AP, infantry rotates to any facing | No |
| `VEH-008`, `VEH-011` | 1 AP per 90° turn, "matching MOVE-008's infantry rotation cost" | No |
| `VEH-009`, `VEH-010` | 1 AP to rotate 90°, 180° or 270° | No — a tracked hull turns further for the same Action Point than a wheeled one, which is locomotion, not size |
| `MOVE-009`, `MOVE-010` | crossing an obstacle: free below 4 plate layers, 1 additional AP from 4 to 6 | Within a rule, no — 4 and 6 cost the same. Between them, the obstacle's height selects the rule, and that is the distinction `CORE-006` draws |
| `DMG-019` | 1 AP to repair a Wounded component or stand up | No |
| `TRN-005`, `TRN-006` | 1 AP **per Unit Base occupied** | **Yes — this change** |

`MOVE-010` is the case that decided the wording. Read against `MOVE-011` above it, it
looks safe: the band is 4 to 6 plate layers, the price is flat across it, and above 6 no
climb is permitted at any price. Read against `MOVE-009` below it, it is not: the same
infantry crosses 3 plate layers for 1 AP and 4 for 2. An earlier draft of `CORE-006`
claimed no cost varies with "the size of what the action acts on" and cited the
within-band comparison for it, which is the true half of a false claim.

So the rule states the two things that are true of the whole ruleset. An **element that
is operated** — door, ramp, hatch, access point — costs the same whatever its size;
`CORE-007` already charges it that way and it is the owner's own case. Terrain is not
operated: its height selects which movement rule applies, and each of those rules is flat
within itself. Neither statement needs an exception, and the movement rules are left
exactly as the owner asked.

---

## Decision 3 — Not "every action costs exactly 1 AP"

That absolute is false in the ruleset as it stands, twice over:

- `MOVE-010` charges **2 AP** to cross an obstacle and says in the same breath that the
  climb "is part of that movement action". One action, two Action Points.
- Rotation is one action with two prices: infantry turns to any facing for 1 AP
  (`MOVE-008`), a wheeled vehicle pays 1 AP per 90° (`VEH-008`), so the same half-turn
  costs one model 1 AP and another 2.

Writing the absolute into `CORE-006` would contradict both on the day it is applied, and
repairing them means rewriting the movement and vehicle rules — which the owner
explicitly excluded. The anti-scaling claim is narrower, it is the one the owner actually
stated, and it is true. The vehicle's extra Action Point is bought by its locomotion,
which is read off the physical model (Principle 1); size buys nothing.

`CORE-006`'s new paragraph therefore closes with what a reader should make of a rule that
charges two: the reason is stated in that rule, and it is never size. `CBT-001`,
`VEH-008` and `MOVE-010` are named there so the rules are read together rather than
against each other.

---

## Decision 4 — The motorcycle example is deleted, not corrected

`TRN-005`'s example exists to teach the multiplier: "an infantry model (1 UB) costs 1 AP;
a motorcycle (2 UB) costs 2 AP". With the multiplier gone the example teaches nothing —
both cost 1 AP, which the sentence already says.

The replacement keeps a two-model comparison, because the point worth teaching is now the
opposite one: the sizes differ and the price does not. `TRN-006`'s "An infantry model (1
UB) therefore costs: **1 AP**" is deleted outright — it worked the multiplier through a
single case and has no equivalent to say.

---

## Decision 5 — `TRN-002`'s citation is repaired in the same change

`TRN-002` closes with "The space was paid for on embarking (TRN-005)". The ID stays
valid and the linter stays silent, but after this change `TRN-005` charges an action and
says nothing about paying for space — the citation would point at a payment the rule no
longer contains.

The repair is one word: the space is **claimed** on embarking. The alternative was to
leave it and record the drift, which is how citations rot; `system/proposal-review.md`
calls the touching proposal the low-risk moment to fix exactly this.

---

## Decision 6 — One spec delta, on `action-economy`, `ADDED`

`openspec/specs/action-economy/spec.md` holds exactly one requirement, *Universal Action
Points*, which is the supply half: 3 AP, no profile grants more. This change adds the
price half to the same capability rather than opening a new one — they are two halves of
one economy, and a reader checking whether a cost is legal needs both in one place.

The delta is `ADDED`, not `MODIFIED`: *Universal Action Points* is untouched and keeps
both of its scenarios, so `check_delta_coverage.py` has nothing to check.

There is no `transport` capability in `openspec/specs/`, so `TRN-005` and `TRN-006` have
no spec surface of their own. That is pre-existing and not opened here.

---

## Decision 7 — Minor, and no `**Bump:**` line

`system/documentation-standards.md` (Versioning) makes minor the default and reserves the
`**Bump:** major` marker for changes that make previously legal models illegal. This one
makes a previously impossible action possible: no model becomes illegal, no construction
is invalidated, and one cost falls. Minor, by default, with nothing written in the commit
message.

---

## What this change deliberately leaves open

- **`MOVE-010`'s second Action Point for one movement action.** Consistent with the new
  rule, because it does not scale — but it is still one action priced at two. If it is
  ever revisited, the direction is to make the climb its own action, not to make one
  action cost two. Out of scope by instruction.
- **`CORE-007`'s "unless another rule specifies otherwise".** The escape hatch survives.
  What it may vary by is now bounded — not by size, in either direction — which is what
  the owner's door case demanded; the hatch itself is left for a rule that needs it.
- **`docs/14-glossary.md`'s `## AP` entry** cites no rule ID, unlike every entry added
  since. Pre-existing, and a glossary sweep is its own change.
- **Whether a multi-Unit-Base vehicle embarks or is loaded.** `TRN-001` lists a Light
  Walker and a Heavy Walker among the objects a transport carries and `TRN-005` prices a
  unit embarking, while `TRN-013`'s table classes a motorbike and a walker as *cargo*,
  which no rule prices in Action Points at all. This change does not settle it: it fixes
  what embarking costs for whatever embarks, and `CORE-006`'s example is the motorcycle
  `TRN-005` already uses rather than a walker, so the core document asserts nothing about
  the open question.
