# Output Patterns

Use only a pattern that helps the actual deliverable. The core skill already
covers ordinary prompts and internal handoffs; no template is compulsory.

## Useful prompt shapes

- Chat: goal, relevant context, output, real boundaries.
- Multi-source work: goal, sources, deliverable, review/approval, verification.
- Tool-using agent: objective, context, tool rules, autonomy, evidence,
  useful updates, verification, stop condition.
- Extraction/classification: goal, definitions, decision rules, examples,
  output schema, ambiguity handling.
- Coding agent: goal, relevant code or reproduction, preservation constraints,
  allowed changes, validation, final response.

Keep personality and collaboration style separate when both materially affect
a customer-facing or collaborative product. Preserve facts, claims, artifact
type, requested length, structure, and genre before polishing a rewrite.

## Draft or critique

Return the ready-to-use prompt in a fenced block, then only useful additions:

- Highest-impact issues and meaningful changes for a critique.
- Relevant, verified configuration suggestions separately from prompt changes.
- Representative tests where failure cost warrants them.
- Consequential unconfirmed assumptions and the missing evidence.

Do not fill an empty config checklist. Surface, model, reasoning effort or mode,
verbosity, structured outputs, tool calling, or state belong here only when
relevant and supported by the exact runtime.

## Migration

Report the baseline, smallest proposed prompt change, separate config changes,
comparison evidence or eval plan, and missing runtime evidence. Use
[validation](validation.md) for the comparison rather than claiming improvement
from a rewrite alone.

## Variants

Offer alternatives only for a real choice:

- Lean: smallest candidate likely to meet the acceptance criteria.
- Strict: extra validation or edge-case handling for a demonstrated risk.
- Agentic: necessary tools, authority, evidence, progress, and stop rules.

Avoid generating all three by default.
