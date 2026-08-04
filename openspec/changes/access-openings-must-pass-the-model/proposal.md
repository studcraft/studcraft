## Why

### A hinged 1×2 tile is a legal door today

Everything the ruleset asks of an access point is that it **moves**:

| Rule | The entire requirement |
|---|---|
| `CMP-009` — Doors | "Must physically open and close. Decorative doors have no gameplay effect." |
| `CMP-010` — Ramps | "Must physically move. Decorative ramps have no effect." |
| `TRN-007` — Access Points | "Only functional access points may be used. Decorative access points have no gameplay effect." |

Nowhere does any rule say the opening has to be big enough for anything to go through it.

"Functional" is defined in `CMP-001` as "a physical part of a model that affects gameplay", which closes the loop without adding anything: the door affects gameplay because it is an access point, and it is an access point because it affects gameplay.

So a 1×2 tile on a hinge qualifies. It physically opens and closes, therefore it is functional, therefore it is an access point, therefore a minifigure embarks through it.

`TRN-005` and `TRN-006` do not close the hole either. Both require the unit to be **adjacent** to an open access point; neither requires it to pass through one. A model embarks through a keyhole.

### This is the defect class the ruleset exists to prevent

The premise is **The Model Is The Rules**. A model that declares a capability its plastic does not have breaks that premise more directly than any balance question does.

It is the same fault that `CORE-004` closed for vehicles one change ago: a 1 Unit Base vehicle was entirely filled by its own Pilot, so the footprint was declaring room that was not there. Here a component is declaring passage that is not there. Both are answered the same way — by checking the model instead of taking the label at its word.

Nothing else in the ruleset has this shape, which is why it is worth closing while the reasoning is still in one piece.

## What Changes

- **`CMP-018` — Access Openings** (new). An access point's opening must physically pass the models that use it. Verified by passing the model through, with the component in its open position.
- **`CMP-009`, `CMP-010`, `TRN-007`** — each gains the requirement, citing `CMP-018`. These are the three places that today say "must move" and stop.
- **`MOVE-018`, `MOVE-019`** — a doorway is a valid movement path only if it passes the moving model.
- **`TRN-011`** — firing ports are explicitly **not** subject to the check. Line of sight passes through a slit; a body does not.
- **`GEO-004`** — the aperture check joins Line of Sight and Cover as a third physical check against the model as it sits on the table.
- A glossary entry for **Access Opening**.

### Width comes from the Unit Base; height comes from the model

The two dimensions are answered by different means, because the ruleset defines one of them and not the other.

**Width is already defined.** Every infantry model is *mounted on* a Unit Base — `CORE-001` calls the 4 × 3 plate "the standard base for infantry", `SCS` requires it, and `TRN-002` states that carrying gear or changing posture never changes the 1 UB it occupies. What crosses a doorway is therefore never a bare minifigure; it is a minifigure on a 4-stud-wide plate. And `CORE-002` makes the 4-stud edge the model's **front**, so that edge is exactly what enters an opening first.

So the requirement derives with no new number: **the opening must be at least as wide as the front edge of what passes through it.** Infantry, invariably 4 studs. A vehicle W Unit Bases wide, `W × 4`.

**Height is not defined**, because a Unit Base is a floor footprint and carries none. That half stays a physical check: take the model and pass it through.

This is Principle 13 respected rather than bypassed. 4 is not a magic constant — it is the Unit Base, the measuring unit the whole ruleset already uses. Every distance, deployment area and vehicle footprint in the game is expressed in it; an aperture is no different.

A minifigure appears in the text only to make the failure concrete: about 4 bricks tall on its base, so a hinged 1 × 2 tile covering an opening under one brick high moves and is still not a door.

### The check is on the opening, not the approach

A rear ramp is a surface a model climbs. What it must fit through is the hatch at the top of it. A ramp that is perfectly drivable leading to a portal too low for the vehicle is not an access point.

Stating it this way answers "must a ramp pass the whole vehicle?" without needing a second rule: the ramp is not what is measured.

### What must pass depends on what the component is declared to do

`TRN-011` lists **roof hatches** among firing ports, and `TRN-007` lists **roof hatches** among access points. The same component can be both.

The requirement therefore attaches to the claimed function, not to the component's name. A roof hatch used to embark must pass the models that embark through it. The same hatch used to shoot from is under no such requirement in that role, and an observation slit that is only ever a firing port needs to pass nothing but a line of sight.

Without this, the change would invalidate every gun port in the game.

## Impact

**No mechanic changes and no value changes.** No distance, cost, threshold or roll is touched. Embarking still costs 1 AP per Unit Base; opening a door still costs 1 AP.

**One new rule ID**, `CMP-018`. No existing ID is renumbered.

**Some existing models may lose an access point.** That is the intent. A door too small to pass anything never worked; the ruleset simply had no way to say so. The consequence is one the ruleset already defines — the component is **decorative**, per `CMP-009`, `CMP-010` and `TRN-007` as they already read. No new penalty is invented.

**A vehicle can end up with no usable access point at all.** `TRN-015` already handles this: passengers who have no functional access point remaining are trapped. The new rule reaches that state through construction rather than through damage, and needs no new text to do it.

**Decoration can now cost you a door.** `GEO-004` already establishes that Visual Geometry participates in physical checks — decorative plastic blocks a sight line because it is really there. Greebling that narrows a hatch closes it for the same reason. This is a consequence of the existing rule, not a new one, and it is worth a builder knowing.

### Deliberately not included

- **A minimum dimension in studs or bricks.** See above.
- **Any rule about interior clearance** once a model is through the opening. `TRN-003` and `TRN-004` govern capacity; passage and capacity are separate questions.
- **Windows** (`CMP-011`) and **firing ports** (`TRN-011`), unless declared as access points.
- **A check during play.** Openings are verified when the model is built, like every other construction requirement.

Not applied — proposal only.
