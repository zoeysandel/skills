# Continuation Notes

This file preserves useful continuation heuristics from the old `continue` skill. The `go` contract is now canonical behavior, but old `continue` wording remains a trigger phrase. `Yes`, `ja`, and `doe maar` are confirmation triggers only when there is a concrete proposed/default next step in the immediate context.

## Local Finish Line

Before handing back, identify:

- what just finished;
- what remains open;
- what the original task, PR, issue, slice, or workflow loop promised.

If promised in-scope work remains, the loop is still active.

Zoey often uses `go` to keep the chat moving. Assume momentum is requested, but still protect her from unclear, risky, or scope-changing next steps.

## Follow-Through Priority

Look for required follow-through in this order:

1. Definition-of-done or workflow next step.
2. Review, CI, bot, or watcher feedback.
3. Next slice or queue step.
4. Required docs, ledger, registry, or memory update.
5. Optional improvements or new ideas.

## Continue-Now Examples

- Open a PR after implementation when PR lifecycle was requested.
- Start or keep PR babysitting after PR creation.
- Fix actionable CI, bot, or review feedback.
- Merge when the active PR lifecycle reaches policy-complete readiness.
- Move to the next slice when the same execution chain requires it.
- Run targeted validation required by the current change.
- Update mandatory workflow docs or ledgers before closing.

## Ask-First Examples

- New feature work outside the current issue.
- Breaking schema, auth, public API, or policy changes.
- Destructive recovery steps.
- Bulk vendor retries or meaningful credit usage.
- A real priority choice between equally plausible paths.

## Common Failure Modes

- Treating a ready-to-merge state as terminal instead of merging.
- Saying "waiting" while the agent still owns the watcher loop.
- Ending with a recommendation when the recommended action is executable now.
- Asking Zoey to type `go` again while the current loop can proceed.
- Treating `go` as blind approval when the next step is ambiguous or risky.
- Carrying a dirty lane into a new task instead of setting up the correct clean branch/worktree.
