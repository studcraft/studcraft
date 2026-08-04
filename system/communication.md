# Communication Style

Agents should:

- Reply in the same language the user writes their prompts in, using neutral/standard variety (e.g. neutral Spanish, not regional dialects like Argentinian or Chilean; standard English, not regional dialects).
- Explain **why** a proposal improves the design, not only what it changes. A proposal that states its reasoning can be argued with; one that states only its result can only be accepted or refused.
- Avoid unnecessary rewrites. Rewriting text that was already correct hides the real change inside a large diff, and on this repo it also causes artificial merge conflicts with every concurrent branch (`system/repository-strategy.md`).

*Prefer evolution over replacement* and *preserve backwards compatibility* used
to be on that list. They are Principle 15 (Future Compatibility) in
`CODE_OF_DESIGN.md`, which is where they are argued rather than asserted.

Large architectural changes should be proposed before implementation — see
`system/workflow.md` for what that means procedurally.

---

# Never state repository state you have not just checked

**Do not say how many pull requests are open, which are merged, or what is left
to land, without running `gh pr list` in that same turn.** The same goes for
issues and for branch state.

This was corrected three times in a single session. The reason it recurs is
structural, not careless: the maintainer merges pull requests between turns, so
any count carried forward from earlier in a conversation is stale by
construction — it was true when it was written and false by the time it is
repeated.

A closing summary of "what is pending" needs its own fresh check, because that
is exactly where a remembered count gets restated. And being wrong about
something a command answers in one second reads as a rotten context, which
costs trust in everything stated alongside it.
