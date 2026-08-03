## Context

The trigger was a small observation — `FLOW-001` should have a step for agreeing objectives. Checking it turned up two larger facts.

Nothing in the ruleset defines winning. `FLOW-010` defines the end of the game and stops there. And "scenario", the term that would naturally own victory conditions, is referenced by eight rules and defined by none.

Those are one problem. A step telling players to agree objectives would have pointed at nothing, because no rule consumes an objective and the artefact that should hold them does not exist.

## Decisions

### `FLOW-013` states what a scenario must contain, not what it may say

The ruleset's job is to define universal systems; the scenario's job is to define the game being played. So `FLOW-013` requires a scenario to state its victory conditions and does not constrain what they are.

This is the same shape `DEP-001` already uses for the Deployment Area and `FLOW-001` for the battlefield size: the rule requires the quantity to be agreed and refuses to pick it. Prescribing objective types here would be the ruleset reaching into the scenario's job, and would need an objective subsystem — markers, capture, scoring — that nothing has asked for.

It is Principle 13 one level up. The game defines no fixed units; it should define no fixed missions. What it can define is what a mission has to declare.

### The rule is placed at the end of `03-game-flow.md`, not near `FLOW-001`

Rule IDs in this repo are stable and never renumbered, so a new rule goes at the end regardless of where it reads best. `FLOW-013` sits after `FLOW-012`, and `FLOW-001` cites it.

That is slightly awkward — the definition arrives after the rules that use it. The alternative is renumbering everything from `FLOW-002` onward, which breaks every existing citation and is exactly what the ID-stability convention exists to prevent. Awkward ordering is the cheaper cost, and `FLOW-001`'s citation closes the gap for anyone reading in order.

### The new step goes second in `FLOW-001`

Objectives shape force composition. By step 4 a player is building, and by step 5 deploying; agreeing what the game is about after either is agreeing it too late to influence anything.

Placing it immediately after "Select a scenario" also reads correctly in both cases the ruleset currently allows: if a written scenario is being used, the step is confirming what it already states, and if the players are inventing one — which is all anyone can do today, since the repo contains no scenarios — the step is where they invent it.

### `FLOW-010` gains the winner, rather than a new rule taking it

Victory could have been its own rule. It is folded into `FLOW-010` because "when does the game end" and "who won when it did" are one question asked twice, and separating them would produce two rules that must always be read together — the coupling this repo has spent several changes removing elsewhere.

### A scenario library is out of scope, and does not belong in `docs/`

Worth having eventually. Not here, and not in the ruleset.

A scenario is a configuration built on the rules, not a rule. Giving one a `FLOW-` style identifier would place it in the ruleset's versioning, its priority order, and its linter — none of which should apply to a mission someone wrote for one evening. It belongs in its own directory, labelled as examples rather than canon, so that writing one stays the lowest-risk contribution available.

Not recorded in `TODO.md` either, though that was the first instinct. `TODO.md` states its own scope in its preamble: gaps *the documents declare in their own text*, every entry quoting the rule that declares it. No rule declares that the repository ships no scenarios — that is a fact about the repository, not about the ruleset. Adding it would have quietly widened a file whose value comes from being narrow. The record lives in this change instead.

## Risks / Trade-offs

- **`FLOW-013` is a rule that mostly says "the scenario decides".** That can read as empty. It is not: eight rules currently defer to an undefined artefact, and this gives all eight a definition to defer to. The value is in closing the reference, not in constraining play.
- **The ruleset still ships with no scenarios**, so `FLOW-001` step 1 remains "select" something that does not exist in the repo. This change makes the requirement explicit rather than resolving it, which is a genuine improvement in honesty and not a fix.
- **Definition-after-use ordering.** `FLOW-013` is cited by `FLOW-001` twelve rules earlier. Unavoidable without renumbering, and cheaper than breaking every existing citation.
- **Victory is now a stated obligation on scenario authors.** Anyone writing a scenario must decide how it is won, which is more work than the current silence demands — and is the point.

## Open Questions

None. Not applied — proposal only.
