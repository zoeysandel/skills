---
name: loop-creator
description: "Use when Zoey has a broad idea, refactor goal, product flow, architecture concern, or quality ambition that is too large for direct execution and must be turned into a closed engineering loop: current state, ideal state, gap map, reviewed werkbonnen, atomic slices, Linear issues, verification gates, sub-agent reviews, execution-thread handoff, PR/CI/bot-finding loop, merge, Linear update, and return-to-werkbon continuation. Do not use for tiny fixes, already-reviewed workbonnen, or direct implementation."
---

# Loop Creator

## Purpose

Use this skill to turn a broad goal into a controlled delivery loop for verified state transitions.

Core rule:

```text
Human-owned goal.
AI-proposed route.
Reviewed gates.
Atomic execution.
Evidence-based done.
```

The skill creates the loop. It does not run implementation.

## When To Use

Use when Zoey asks to:

- turn a broad idea into an executable plan;
- improve a whole flow or domain without losing control;
- design a closed loop, roadmap, migration loop, or autonomous goal;
- split a refactor into Linear issues and werkbonnen;
- define verification gates before execution;
- decide how to use sub-agents and execution threads.

Do not use when:

- the task is a small bugfix or answer-only question;
- a reviewed workbon already exists;
- Zoey explicitly asks to implement a known slice now;
- the next step is a PR review, CI fix, or merge.

## Mental Model

A loop is not "let agents improve the codebase".

A loop is:

```text
goal + boundary
  -> evidence-backed current map
  -> ideal-state invariants
  -> gap map
  -> werkbonnen with verification
  -> werkbon sub-review
  -> atomic slices per werkbon
  -> slice sub-review
  -> Linear issue per slice
  -> one execution thread per approved issue
  -> PR/tests/CI/bot findings
  -> fix within scope or pause
  -> merge to develop when clean
  -> Linear update
  -> return to the current or next werkbon
```

Every loop artifact must do at least one of:

1. cite reality;
2. constrain execution;
3. verify an outcome.

If it does none of those, delete it.

Every loop must also have checkpoints by default. A checkpoint is a small,
explainable stop point where the user can see:

- what happened;
- which artifact, command, diff, report, or screenshot proves it;
- what is proven;
- what is not proven;
- how to reproduce the step;
- what the next checkpoint is.

Do not let a loop advance on vibes. If a checkpoint cannot be explained or
reproduced, mark the evidence as weak and tighten the next step before expanding
scope.

## Control Split

| Owner | Owns | Does Not Own |
| --- | --- | --- |
| Cockpit/main thread | goal, scope, target state, risk, slice order, approvals, halt/merge decisions | broad implementation |
| Sub-agents | bounded analysis, critique, specialist review, missing evidence checks | final decisions, execution ownership |
| Nested sub-agents | narrow deeper exploration with a specific question and budget | generic sparring, confidence-building, swarms |
| Execution threads via `create_thread` | one approved implementation slice in a separate worktree/thread | architecture discovery, scope expansion, product decisions |

Any sub-agent that runs, monitors, reviews, or repairs part of the loop needs its own loop goal. The goal must say what correct loop execution means for that lane: scope, checkpoints, allowed actions, required evidence, terminal state, and escalation triggers.

Tool names may vary by harness, but in Codex Desktop the usual split is:

- execution lane: `codex_app.create_thread`, then `codex_app.send_message_to_thread` for follow-up;
- sub-agent lane: `multi_agent_v1.spawn_agent`, then `multi_agent_v1.wait_agent`, `multi_agent_v1.send_input`, and `multi_agent_v1.close_agent` when available.

If these exact tools are unavailable, use the closest equivalent with the same ownership model.

## Thread Versus Sub-agent

Use a separate thread tool such as `codex_app.create_thread` only for execution lanes or durable separate work that should not pollute the cockpit context.

Use a separate execution thread when all are true:

- a reviewed workbon exists;
- the slice is selected for execution;
- branch/worktree ownership matters;
- the lane may create commits, PRs, or run a full implementation loop;
- the cockpit must stay clean for coordination.

Use sub-agents when the task is read-only or bounded analysis:

- current-state exploration;
- frontend/backend boundary review;
- verification review;
- auth/security/work-context critique;
- product/UX loading-state critique;
- checking whether a werkbon is atomic and testable.

Use nested sub-agents only when a sub-agent has a narrow question such as:

- "find all backend entry points that write conversation messages";
- "compare query key usage across this feature";
- "trace where Work Context is derived and passed into provider calls".

Nested sub-agent rule:

```text
one question + one expected artifact + loop goal when applicable + budget/reasoning limit + stop condition
```

No nested sub-agent swarms.

## Default Workflow

### 1. Goal And Boundary

Clarify:

- desired outcome;
- domain/flow;
- included and excluded surfaces;
- non-goals;
- risk class;
- human decision gates;
- stop conditions.

If the goal is not sharp enough, ask at most one concise question or state a reasonable assumption.

### 2. Evidence-backed Current Map

Map current behavior with evidence:

- user actions / triggers;
- frontend routes, components, hooks, services, query keys;
- backend routes, services, repositories, domain entities;
- tests and missing tests;
- runtime or UI observations when available.

No source reference, no strong claim.

### 3. Ideal-state Invariants

Define what "good" means as enforceable invariants, not taste:

- boundaries;
- contracts;
- read/write/provider separation;
- frontend data-flow;
- loading/error/empty behavior;
- performance expectations;
- tests and observability.

### 4. Gap Map

Convert differences into gaps:

- current evidence;
- target invariant;
- risk;
- dependency;
- possible slice.

### 5. Atomic Slice Plan

First group the gap map into werkbonnen. Then split each reviewed werkbon into
atomic slices.

Definitions:

```text
Werkbon = problem area + intent + scope + mental map + verification shape.
Slice = one reviewable PR/Linear issue from that werkbon.
Linear issue = one slice.
Execution thread = one Linear issue.
```

A werkbon may contain multiple slices. Do not skip back from a completed slice
straight to a random next issue; return to the werkbon first and decide whether
the next step is another slice in the same werkbon, a revised werkbon, or the
next werkbon.

Each slice must have:

- one primary intent;
- one review surface;
- explicit anti-scope;
- expected files/layers;
- dependency relation;
- verification strategy.

Split when a slice mixes:

- refactor and behavior change;
- frontend and backend unless the contract requires both;
- reads and writes;
- provider side effects and local state;
- auth/security and cleanup;
- performance and unrelated architecture.

### 6. Werkbon

For every meaningful problem area, produce a compact werkbon before Linear issue
creation. The workbon is the parent understanding; slices are extracted from it.

```md
## Purpose
One sentence describing the state transition.

## Current Behavior
Evidence-backed summary with file/runtime references.

## Target Behavior
What should be true after this slice.

## Scope
Included files, layers, flows, and behavior.

## Anti-scope
What must not change.

## Architectural Invariant
The target rule this slice advances.

## Expected Implementation Shape
Likely files, seam, constraints, and migration approach.

## Verification Points
- Static:
- Unit:
- Integration:
- E2E:
- Smoke:
- Human review:

## Required Evidence
Command output, CI link, screenshots, logs, PR review, or notes.

## Pause Conditions
When execution must return to cockpit.

## Done Criteria
Checklist for verification contract passed.
```

### 7. Review Gate

Run at least one sub-agent review on every non-trivial werkbon before splitting
it into execution slices.

Run a second, narrower sub-agent review on each non-trivial slice before making
or updating the Linear issue.

Reviewer output must be structured:

- `PASS` / `FAIL` / `PASS_WITH_CHANGES`;
- blocking issues;
- non-blocking concerns;
- missing evidence;
- suggested split;
- verification changes.

Do not treat "looks good" as a review.

### 8. Linear And Execution Loop

For each reviewed slice:

1. create or update exactly one Linear issue;
2. start exactly one execution thread from the agreed base branch;
3. require a PR with tests/checks appropriate to the slice;
4. monitor CI, bot findings, and review blockers;
5. fix findings inside scope without asking Zoey again;
6. pause only for scope/product/schema/security/privacy/provider/production decisions;
7. merge to `develop` when verification is clean and merge approval is already in scope;
8. update Linear with PR and final state;
9. return to the werkbon.

The return step is mandatory:

```text
slice done -> Linear updated -> current werkbon status -> next slice or next werkbon
```

### 9. Closed-loop Goal Packet

If the work requires a durable goal, produce a `goal-runner` compatible packet:

- objective;
- scope;
- anti-goals;
- read first;
- validation;
- checkpoints;
- pause conditions;
- stop condition.

If any sub-agent owns part of the loop, include a separate sub-agent loop goal for that lane. Do not rely on the parent closed-loop goal to imply correct sub-agent behavior.

Do not activate the goal from inside this skill unless Zoey explicitly asks.

### 10. Execution Handoff

End with:

- selected first werkbon and first slice;
- Linear issue or issue-ready text;
- branch name proposal;
- whether to use `create_thread`;
- exact execution prompt outline;
- checks to run;
- what remains cockpit-owned.

## Done Bar

`loop-creator` is done when:

- current state is evidence-backed;
- ideal state has testable invariants;
- gaps are mapped;
- werkbonnen have verification points;
- werkbonnen are sub-reviewed;
- slices are atomic;
- slices are sub-reviewed before Linear issue creation;
- first execution slice is named;
- return-to-werkbon continuation is explicit;
- a closed-loop goal prompt is ready when needed.

An implementation slice is done only when its verification contract passes.

## Anti-patterns

Avoid:

- creating more Linear issues than can realistically be executed;
- maps that do not cite code or runtime evidence;
- ideal states that cannot be tested or reviewed;
- work orders longer than the likely diff;
- nested sub-agent swarms;
- asking sub-agents for vague reassurance;
- execution threads that "figure out the architecture";
- accepting agent summaries as proof;
- turning every observation into immediate work.
