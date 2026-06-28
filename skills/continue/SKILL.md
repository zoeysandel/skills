---
name: continue
description: "Momentum and state-recovery controller for Codex work. Use when Zoey says continue, go, ga, ga door, start, pak op, voer uit, yes, ja, doe maar, wat nu, what's next, wat is de volgende stap, wat staat er nog open, welke opties zijn er, or when Codex reaches a handoff while in-scope work may still remain. Treat go-style requests primarily as: continue this chat or owner-loop from the current intent. Start the next safe step, keep active owner-loops moving, reconstruct current state when the next step is unclear, and stop only when no in-scope work remains, Zoey explicitly pauses/stops, or a real ambiguity, approval, risk, or missing-input boundary blocks safe progress."
visibility: public
---

# Continue

## Purpose

Use this skill to keep momentum without losing boundaries. `Continue` now uses the `go` contract: continue this chat or owner-loop by taking the next safe action inside Zoey's current intent.

Zoey usually says `go`, `ga door`, or `continue` when she wants Codex to keep the conversation/work moving. If she had a new question, she would usually ask it directly. Stay sharp anyway: these phrases are not blind approval to guess through ambiguity or risk.

This is broader than the old `continue` contract:

- start work when the first safe action is clear;
- continue active loops until they are truly terminal;
- reconstruct state when it is unclear what is open;
- choose the dominant next step when Zoey asks "what now?";
- treat `yes`, `ja`, or `doe maar` as approval only for a concrete proposed/default next step.

## Core Rule

Do the next safe, in-scope thing. Do not hand control back to Zoey just because a local step finished.

If the next step is unclear, reconstruct state first. If the next step is outside scope or needs a real decision, ask one narrow question with a recommended default.

Default posture: continue by default, guardrails still active.

## Operating Modes

Classify the situation before acting.

| Mode | Use when | Action |
| --- | --- | --- |
| Start | Zoey gives a clear task but not a step-by-step plan | Begin with the first low-risk action, usually context discovery or repo/status inspection |
| Continue | A PR, CI, merge, slice, debug, implementation, automation, or review loop is active | Execute the next required follow-through step until terminal |
| Recover | Zoey asks what is open, context is stale, or you are unsure what remains | Rebuild state from the thread, ledger, worktree, PR/checks, plans, queues, and recent tool output |
| Decide | Several next actions seem possible | Pick the dominant safe next step; ask only if the tradeoff is real |
| Confirm | Zoey says `yes`, `ja`, `doe maar`, or equivalent after a concrete recommendation | Execute that specific recommended/default next step, preserving all normal risk and scope boundaries |

## State-Recovery Checklist

When the next step is not obvious, inspect the smallest useful set:

- current user request and most recent assistant commitment;
- `CONTINUITY.md` or other active session ledger if present;
- current working directory, git branch, and `git status --porcelain` for repo work;
- active PR, CI, review threads, watcher output, or merge state for PR work;
- active spec, plan, slice-map, task queue, or workflow log for planned execution;
- last blocker, approval boundary, or stop condition.

Stop the scan as soon as the next safe action is clear.

## Action Rules

- Treat open in-scope work as an active owner-loop, not as completed work.
- Execute required follow-through directly when the workflow already defines the default.
- Keep PR ownership active until `merged`, `closed`, or explicit `user_help_required`.
- Treat `ready_to_merge`, `mergeable`, `merge_now`, and equivalent readiness states as action triggers, not terminal states, unless Zoey asked for monitor-only behavior.
- If a watcher is running, keep consuming it or restart it after patches until a strict stop condition appears.
- If the next step crosses into a new issue, slice, branch, or worktree lane, first establish the clean lane required by local workflow rules.
- If a repo-owned controller is active, preserve its status contract instead of replacing it with vague prose.
- If the current task is only planning, discovery, or review, do not infer execution approval from `go`; move to the next planning/review gate unless Zoey explicitly approved build/merge/execute.
- If Zoey says `yes`, `ja`, or `doe maar` without a concrete proposal in the immediate context, treat it like `go`: recover the intended next step first instead of inventing approval.
- Do not call a run done until it has a lane-appropriate terminal state. If the run is not terminal, name the continuation target, blocker, or next owner.

## Escalation Rules

Ask Zoey one narrow question when the next step would:

- change product direction, policy, auth, privacy, security, schema, or public API behavior;
- widen scope beyond the current task, issue, PR, or workflow loop;
- take a destructive action or consume meaningful vendor credits;
- require missing credentials, permissions, or live-system access;
- choose between two similarly plausible options with real tradeoffs.

Use this shape:

`Current state -> recommended next step -> why this needs Zoey's decision`

## Anti-Patterns

Do not say:

- "Let me know if I should continue."
- "The PR is mergeable; say if I should merge."
- "I am waiting on checks" when ownership of the watch-loop is still yours.
- "There are some options" when one safe next step dominates.
- "Done" while in-scope required work remains.

Instead, keep moving, monitor, merge, patch, validate, or reconstruct state as the current loop requires.

## Output Contract

When acting:

- state what is done;
- name the next action;
- perform it in the same turn when it is safe and in scope.

When the parent loop remains active, include:

- `run_state`
- `phase`
- `owner_loop`
- `continuation_target`
- `terminal_reason`

For non-trivial owner loops, also include:

- `lane`
- `terminal_state`
- `evidence`
- `not_verified`
- `skipped_checks`
- `blockers_or_pending`
- `next_owner`

When escalating:

- ask one narrow question;
- include the recommended default;
- avoid broad menus unless the choice is genuinely strategic.

## Resources

- `references/decision-table.md` - compact routing table for action classification.
- `references/continuation-notes.md` - preserved continuation heuristics from the old `continue` skill.
