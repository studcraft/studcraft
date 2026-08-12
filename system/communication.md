# Communication Style

Agents should:

- Reply in the language the user writes in, in a neutral standard variety.
- Explain **why** a proposal improves the design, not only what it changes. A
  proposal that states its reasoning can be argued with; one that states only
  its result can only be accepted or refused.
- Avoid unnecessary rewrites. Rewriting correct text hides the real change in a
  large diff, and here it also causes artificial merge conflicts with every
  concurrent branch (`system/repository-strategy.md`).

Large architectural changes are proposed before implementation — see
`system/workflow.md`.

---

# Never state repository state you have not just checked

**Do not say how many pull requests are open, which are merged, or what is left
to land, without running `gh pr list` in that same turn.** Same for issues and
branch state.

The maintainer merges between turns, so any count carried forward is stale by
construction. A closing summary of "what is pending" needs its own fresh check,
because that is exactly where a remembered count gets restated.
