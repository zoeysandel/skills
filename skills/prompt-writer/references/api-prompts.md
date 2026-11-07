# API Prompts, Tools, and State

Keep runtime configuration separate from prompt text. Verify exact-target support
before suggesting reasoning effort, Pro mode, verbosity, persisted reasoning,
caching, Programmatic Tool Calling, or multi-agent settings. These are optional
runtime features, not default prompt requirements.

## Product contract

- Use structured outputs for enforced schemas when supported; reserve prose
  for definitions, decision rules, ambiguity, and representative examples.
- Let runtime verbosity control default detail where available. Prompt for
  required content, useful structure, and what may be omitted.
- Keep personality separate from collaboration behavior such as questions,
  initiative, approvals, checks, and uncertainty.
- Preserve current model and effort as the migration baseline; use a supported
  equivalent when the requested target rejects the old effort.
- Do not change application code, credentials, or runtime settings during a
  prompt-only assignment.

## Tools and grounding

Expose only relevant tools. Describe when each applies, prerequisites, return
fields, and errors. Parallelize independent retrieval; keep dependent decisions
sequential. Define meaningful fallbacks for empty or suspiciously narrow results.

For grounded answers, require support for consequential claims, citations to
retrieved sources, labeled inference, and disclosure of conflicting evidence.
For longer work, define the active objective, useful progress updates,
verification, and the terminal condition without imposing unnecessary phases.

Programmatic Tool Calling can help with bounded deterministic filtering, joins,
ranking, deduplication, aggregation, batching, or repeated validation. Prefer
direct calls for small results, semantic judgment, approval, citations, or native
artifacts. When mixing them, define the bounded stage, eligible tools, evidence,
output schema, retry/stop limits, and handoff. Check both the program result and
the final answer.

## State and caching

Preserve assistant phase values when replaying history if the host uses them.
Use persisted reasoning only while objectives and assumptions remain stable.
Keep stable reusable prefixes before dynamic context when caching matters;
recommend explicit cache breakpoints only for a supported, measured benefit.

Fetch exact feature schemas when implementing. Never infer a Codex setting from
an API request field or enable a capability merely because it is supported.
