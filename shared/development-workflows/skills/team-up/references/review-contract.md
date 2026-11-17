# Whole-result review contract

Prepare a task-specific brief before the final review. Detail is useful when it
removes ambiguity; verbosity, hidden reasoning requests, and generic exhaustive
checklists do not make a review stronger. Request conclusions with observable
evidence and concise rationale, not private chain-of-thought.

Include the following information in natural language, without requiring a form:

- **Judgment:** The one integrated outcome to assess and the user's intended use.
- **Authority:** Original feedback, settled decisions, tentative ideas, and
  constraints. Do not pass the makers' proposed verdict or self-assessment.
- **Target:** Exact version and entry point; current renders, code, or runnable
  artifact as relevant. Specify permitted read-only inspection and safe checks.
  Do not review a moving target; have the parent preserve a stable snapshot or
  coordinate a bounded review window for the affected surfaces.
- **Coverage:** Important end-to-end scenarios, transitions, and failure states.
  State exclusions and which specialist checks supply additional evidence.
- **Criteria:** Concrete questions about correctness, coherence, user intent,
  and tradeoffs. Prioritize consequential properties rather than asking to
  review all quality dimensions at once.
- **Return:** Ready within the agreed scope, changes required, or inconclusive.
  Explain feedback coverage and important tradeoffs. Each actionable finding
  identifies the location or scenario, observed evidence, user consequence,
  severity, and needed correction or missing proof. Separate preference from
  requirement violations. Do not invent findings to satisfy a quota.

The critic does not edit, expand scope, launch other agents, or approve external
effects. It reports missing access or stale evidence instead of filling gaps
with confidence. A judgment is limited to the inspected version and coverage.
If coverage is too complex for one pass, the parent obtains bounded specialist
checks or adjusts effort; one final critic still assesses the relevant seams.
