---
name: create-subagents
description: Create and coordinate bounded subagents with appropriate roles and context. Use for sub/subs requests, delegated contributions or independent review, subject to the active delegation permissions.
---

# Create Subagents

The current parent owns scope, decisions, synthesis, and external effects.
Delegation is a tool, not a mandatory phase.

Use `$team-up` at `../team-up/SKILL.md` when several interdependent contributions
must become one continuously integrated result with a designated independent
final critic. Ordinary bounded help stays here; do not impose team-up's whole-result
policy or final-review contract on every subtask.

Treat "sub" as one subagent and "subs" as multiple when those terms are used. Both invoke this
single skill; do not create a separate plural alias. Interpret them in the
current task context, not as requests to design a team from scratch.

## Choose a perspective and context

Choose the concrete question and evidence needed before selecting a role.
Resolve useful questions and methods before delegating uncertain work. Use the global rules for broad tradeoff judgment and focused domain depth;
these are perspectives, not separate skills or runtime agent types. When a
concrete domain skill is needed, provide its verified path and ask the child
to read it; a name alone does not prove the runtime loaded it.

The parent leads as a generalist and weighs specialist findings rather than
automatically turning every recommendation into work. Choose the perspective
that helps; do not create both lanes as a standard sequence.

Choose fresh or inherited context deliberately using the host's supported tools.
Prefer fresh context for independent reviews or self-contained assignments.
Supply current intent, settled choices, sources and authority. Inherit history
when needed, respecting the user's choice, and identify superseded decisions.
Do not assume Codex-specific tool arguments work in Claude Code or vice versa.

## Adapt help to the outcome

The parent remains a maker and decision owner, not only a monitor. Organize
authorized help without making the user choose roles, models, or review moments.
Choose a concrete contribution first: independent parallel work, a missing
capability or perspective, or a consequential claim that needs independent
checking. Agent count and reasoning are means, not quality targets.

Preserve the quality ambition in the task and the user's known preferences. Do not
silently lower it to save usage. Select model and reasoning for the contribution
using available capabilities and evidence, without a fixed model hierarchy.
An expert persona is not expertise; require relevant sources or observable work.

Use only the context the contribution needs. A fresh review gets the result,
goal, constraints and evidence, not the maker's preferred verdict. A first-use
perspective gets a concrete user task without the design rationale that would
explain away confusion. Simulated users identify hypotheses, not user validation.
Fresh context alone does not guarantee independence or correctness.

For substantial interface design delivery, use an independent visual review with rendered evidence; not for every trivial visual edit. Add a
first-use perspective when comprehension or navigation is materially uncertain.
The design skill owns screenshot preparation and bounded review rounds; the
critic role owns assessment, so do not make it recursively invoke that skill.

Adapt after observing results: clarify an assignment, change context or means,
request a targeted recheck, or take over locally. Do not add opinions by default.
Stop at sufficient verified quality or a real boundary, not endless refinement.

## Decide whether a lane helps

At the start of substantial work, actively look for a useful independent
contribution and start it when the scope is clear and authorized. Do not wait
until stuck or nearly finished, or require the user to request the team. Do not
create a lane merely to increase agent use or exercise a prompting skill.

Use an agent for named independent work that can run alongside useful parent
work, or for a genuine independent make/verify split. A vague request to
"double-check everything" is not a bounded lane. Work directly when coordination
would cost more than it adds.

Use the runtime's supported roles and models. A configured role is a default,
not evidence that its model ran. Prefer the selected model or a suitable exposed
specialist; do not invent model IDs or silently substitute an unavailable model.

Use roles only when supported by the current host; these are responsibilities, not mandatory configured agent names:
- scout: read-only source mapping and extraction;
- implementor: bounded implementation;
- worker: routine, well-specified execution;
- reviewer: independent correctness and risk review.

Do not hardcode a new generation into this skill or change every specialist
when the parent model changes. Report runtime model evidence only when available.

## Give a bounded assignment

For assignments involving judgment, prepare a concrete handoff connecting the
question, source material, scope and evidence needed. Apply any available prompt
writing guidance directly; do not spawn another agent just to write the prompt
or add an unnecessary user approval stage. Simple lookups need only a short brief.

Preserve the relevant original user request, settled choices and source
references. A polished rewrite must not turn an assumption into a requirement
or replace missing evidence. Retrieve necessary facts and ask only for
material user decisions; the original intent remains authoritative.

Provide the outcome, exact files or responsibility, relevant context, constraints,
verification expected, and a return/stop condition. Say whether the result is
required for completion or optional. Use ordinary language; no packet or prompt
template is compulsory.

Size the assignment by remaining judgment, not length. Distinguish settled
decisions from choices the executor may make; provide concrete references and
observable acceptance checks. Clarify dependencies and shared interfaces before
parallel implementation. A small subjective decision can require more judgment
than a larger mechanical change. If the assignment cannot be made sufficiently
clear, retain the judgment with the parent rather than pretending it is routine.

Tell writing agents they are not alone: preserve others' edits and adapt to
concurrent work. Assign disjoint files or explicit integration ownership.
Give the minimum sufficient context and no unrelated secrets or private data.

Agents must not create child lanes or take Git, production, communication,
configuration, or other external effects unless the parent explicitly delegates
that exact authorized scope. Read-only assignments stay read-only. Higher-priority
runtime restrictions still apply.

## Coordinate and join

Keep parallelism bounded by independent work, budget, and runtime capacity.
Do useful local work while agents run. Avoid duplicate investigations unless
independence itself is the verification goal.

A lane returns its result, exact evidence, changed paths if any, verification,
uncertainty, and any blocking decision. The parent resolves conflicting results
against source evidence, integrates changes, and joins every required lane
before declaring completion.

A summary is not proof by itself. Verify consequential claims against the
reported source or test output. If a lane fails, use a new bounded hypothesis,
take over locally, or report the blocker; never retry indefinitely.

Do not create user-visible threads or native Goals as a substitute for internal
delegation. Those need explicit user requests and their own tool contracts.
