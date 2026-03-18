---
name: continue
description: "Determine and execute the next best step after a local completion point. Use when Zoey says continue, keep going, what's next, what is the next step, what now, what do you recommend, what options are there, or when Codex reaches a natural handoff and needs to decide whether to keep going autonomously. Default behavior: continue automatically for in-scope follow-through, and ask only when the next action is out of scope, approval-bound, or requires a real product or policy decision."
visibility: public
---

# Continue

Goal: prevent unnecessary handoffs.  
If the next step is logical, within scope, and low risk, execute that step instead of handing control back to Zoey.

## When this skill takes the lead

Use this skill in two situations:

1. Explicit trigger from Zoey
- `continue`
- `keep going`
- `what's next`
- `what is the next step`
- `what now`
- `what do you recommend`
- `what options are there`

2. Implicit trigger from the agent itself
- a subtask is complete and there is a clear follow-through step;
- you notice you are about to ask a question where the recommended answer is already obvious;
- you have just opened a PR, started checks, completed a slice, finished a plan, done a review, or cleared a blocker;
- you are about to say "I am now waiting for X" while in reality ownership or a watch-loop still belongs to you.

## Default stance

- Default to momentum.
- Take ownership of follow-through within the same scope.
- Do not ask Zoey for confirmation if the best next step is already clear.
- Present options only when there are genuinely multiple plausible directions with meaningful trade-offs.
- If there is one clearly best option, choose it and briefly explain why.

## Decision routine

Run through this routine as soon as the skill is triggered.

### 1) Determine the local finish line

Summarize in 1 to 2 lines:
- what was just completed;
- what is still open;
- what the original scope or workflow chain was.

### 2) Find the next concrete action

Look first for mandatory follow-through in this order:

1. DoD or workflow next step
2. open review, CI, or bot feedback
3. next slice or next queue step
4. required docs, log, or registry update
5. only after that, optional improvements or new ideas

### 3) Classify the action

#### A. In scope and required or clearly recommended

Execute the step immediately.

Examples:
- after implementation, open the PR;
- after opening the PR, immediately babysit it;
- fix actionable bot findings;
- after merge, automatically pick up the next slice if the parent flow implies it;
- complete required validators, docs, or workflow updates;
- carry out a clear next step in the same debug or review flow.

#### B. In scope but not necessary for completion

Execute immediately only if the step is small, safe, and clearly valuable.  
Otherwise, report it briefly as an optional next step, without blocking the current flow.

Examples:
- minor polish;
- extra observability that is not needed for acceptance;
- a follow-up idea that falls outside the agreed deliverable.

#### C. Out of scope or approval-bound

Stop and ask at most 1 focused question.  
State:
- why you are stopping;
- the recommended option;
- the next action if Zoey approves.

Examples:
- new feature work outside the agreed issue;
- breaking schema or API change;
- privacy, security, or policy decision;
- extra work that requires a new issue or an explicit priority choice.

## Anti-patterns

Do not do this:

- "I created a PR. Let me know if you want me to babysit it."
- "I am waiting for checks now."
- "Slice 2 is merged. Tell me if I should continue to slice 3."
- "There are bot findings. Do you want me to handle them?"
- "There are three options." when in practice one option is already dominant.

Replace this with:

- start babysitting;
- keep the watch-loop active;
- pick up the next slice if it belongs to the same execution chain;
- process bot findings;
- only ask back when the boundary genuinely belongs to Zoey.

## Scope boundary

Explicitly ask Zoey only in cases of:

- product direction or policy choice with a real trade-off;
- expansion beyond the agreed scope;
- irreversible or high-impact action;
- missing priority between two equally plausible options;
- any existing global stop or escalate rule.

Use this compact format:

`Current state -> recommended next step -> why this is a Zoey decision`

## Output contract

When continuing autonomously:
- briefly say what was just completed;
- state the next step;
- execute that step.

When asking back:
- provide 1 recommended option;
- mention at most 1 to 3 alternatives if they are truly relevant;
- keep the question narrow and easy to decide.

Every status, planning, or review update must include:
- `Skill Trace: continue | Sub-agents: <roles> | Why: determine follow-up action after local completion`

## Heuristics

- "Within scope" means: necessary to properly complete the current task, issue, slice, PR, or watch-loop.
- "Recommended" means: highest expected value with low risk, without forcing a new product decision.
- "Waiting" is rarely a terminal state. Ownership stays with the agent as long as an active loop still makes sense.
- If you notice that you want to ask Zoey for permission for something that is already the default according to the workflow, just do it.

