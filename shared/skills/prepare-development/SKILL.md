---
name: prepare-development
description: "Prepare a meaningful software change for implementation: business rules, UX and visual design, architecture, data contracts, and acceptance evidence. Reconcile existing projects before filling gaps."
---

# Prepare Development

Make the next agreed change implementable by another developer without having
to invent product rules. Scale the preparation to the change; a small fix may
only need a clarified scenario and existing references. Preparation itself
does not authorize implementation or external actions.

## Start from the actual project

- Recover the intended outcome, scope, latest decisions and current authority.
  Resolve discoverable facts before asking questions.
- For an existing product, inspect its relevant code, accepted designs, docs,
  tests and schema. Distinguish intended, implemented and runtime-verified
  behavior. A design or migration file alone does not establish live behavior.
- Reuse the project's stack and conventions. For a new project, choose and explain the stack from the requirements, team knowledge, deployment constraints and maintenance needs; do not assume a preferred framework.
- Preserve accepted visual character. Identify the gap between design and
  implementation before proposing a redesign.
- For a new or materially changed visual direction, use
  a design exploration workflow. Align taste and visual references
  before screen elaboration; an already accepted direction needs no new intake.

## Work through professional responsibilities

Use these responsibilities to find missing decisions and handoffs. One person
or agent may cover several roles; this table does not require extra agents or
a separate document for each role.

| Responsibility | Information needed for the next person |
| --- | --- |
| Business modeller / analyst | Purpose, actors, terminology, scenarios, business rules, agreed scope and observable acceptance criteria. |
| UX designer | User journey, relevant screens, interactions and states within scope. |
| UI / visual designer | Accepted visual direction, layout, typography, components and responsive examples needed to implement it. |
| Solution architect | Component responsibilities, integrations, data flow and material technical decisions. |
| Data modeller / backend engineer | Entities, cardinalities, schemas, runtime validation and interface contracts. |
| Developer | Implementation steps, affected files, function responsibilities, documentation and proportionate checks. |
| Independent reviewer / QA | Task and design references, current diff, acceptance criteria and actual verification evidence. |

For AI features, identify the responsible AI engineer and the behavior that
needs evaluation. Choose representative cases and useful telemetry only when
they answer a concrete question. State the expected outcome, evaluation method
and data handling; keep the initial approach as small as the feature allows.

## Prepare the relevant evidence

Trace each significant requirement through:
**business purpose → scenario → design / diagram → contract → implementation → acceptance check**.

- **System overview:** show the components involved, their responsibilities,
  system boundaries and integrations. Use an existing accurate diagram where
  possible; do not redraw unaffected architecture for every change.
- **Flowchart:** show the principal path and decisions that affect the agreed
  outcome. Describe who does what and what result moves the flow forward.
- **ERD:** for relevant stored data, show entities and minimum/maximum
  cardinalities at both ends, including optionality. Explain lifecycle rules
  that change those relationships. Verify against actual constraints when
  documenting an implemented system.
- **Contracts:** define inputs, outputs, relevant validation, business rules
  and errors. Distinguish TypeScript/Python types from runtime validation at
  external boundaries. Reuse the project's existing contract source.
- **Visual specification:** connect the flow to accepted screen designs and
  the states the frontend must render. Record material design decisions that
  cannot be inferred reliably from a screenshot alone.
- **Acceptance and tests:** identify observable success before implementation.
  Select existing checks, useful new tests and visual/manual verification.
  Assess whether planned tests prove meaningful behavior rather than mirror implementation.
  Use test-driven development when a failing test meaningfully demonstrates the
  behavior or regression; existing evidence can suffice for a small refactor.

Network recovery, concurrent edits, transactions, performance work and broad
observability are scope decisions. Include them when required by the agreed
scenario or a concrete change to an existing guarantee. Do not silently turn
them into product requirements. Ask a focused question when an unresolved
choice materially changes implementation; continue independent work meanwhile.

## Handoff and storage

- Expose unresolved questions and their effect. Routine technical choices can
  be made with a brief reason; unknown product policy must not become a fact.
- The affected part is ready when its behavior, visual expectations where
  relevant, data relationships, contracts and verification are clear enough
  to implement. Unresolved blocking choices prevent only dependent work.
- Apply the project's code conventions while implementing and reviewing touched code. Keep responsibilities clear, preserve contracts and keep relevant docs and diagrams in step with the implementation.
- Code-coupled diagrams, contracts and technical docs belong in the repository.
  Reusable business/process decisions belong in the user's agreed knowledge store. Link between sources instead of keeping two
  authoritative copies. Ordinary inline advice needs no saved document.
- Before reporting a saved artifact complete, read it back at its intended
  destination. Report any missing placement or access precisely.

Report what is ready, the evidence, and only the remaining decisions that
affect the next step. Continue implementation when already authorized; use
the project's review and verification process before opening or updating its PR.
