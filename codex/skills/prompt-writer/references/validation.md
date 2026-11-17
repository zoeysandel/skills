# Prompt Validation

Validate observable outcomes in proportion to failure cost. A draft, a static
review, and a successful runtime test are different levels of evidence.

For substantial refactors or high-impact/product prompts, choose representative
cases or a compact eval checklist based on risk, not a fixed case count.
Define observable acceptance criteria before comparing results: exact values
survive, absent facts are not invented, advice stays read-only, and authorized
execution reaches its completion bar. Include relevant negative cases.
Cover the important failure modes, not a generic test catalog:
unsupported claims, wrong format, missing prerequisites, unsafe side effects,
contradictory evidence, or an unfinished authorized objective.

Use concise rationale, evidence, assumptions, and checks; never request hidden
chain-of-thought. Preserve required human review before use or sharing.

## Refactors and migration comparisons

1. Preserve the current prompt, model, effective reasoning, and observed behavior.
2. For a prompt refactor, compare old and new on the same cases with the same
   model and effective settings. For a model migration, compare targets before
   attributing differences to prompt edits.
3. Evaluate representative assembled contexts, including relevant higher-level
   rules, conditional references, tools, and handoffs; isolated files can look
   correct while their combination conflicts. Check that required guidance is
   present when its route activates, not merely that the reference exists.
4. Review outputs against the predeclared criteria, blind to the variant when
   practical. Separate intended behavior changes from accidental regressions.
   Repeat variable or consequential cases when needed; do not infer a reliable
   gain from one favorable sample.
5. Make attributable corrections and re-run affected cases. Keep prompt, model,
   tool, and runtime effects distinguishable. These checks are for material
   changes, not a mandatory ceremony for every small rewrite or handoff.

Do not adopt optional runtime features automatically. If baseline or target runs
are unavailable, provide a comparison plan and explicitly say behavioral
equivalence or improvement remains unverified.
State what was tested: prompt construction, downstream execution, or both.

## Domain-specific checks

For coding prompts, request targeted tests and affected type/lint/build checks,
plus a meaningful smoke test where possible. Name checks that could not run.

For visual prompts, preserve the existing design system and required states;
prevent unsolicited features. Follow the applicable design workflow, then render
and inspect for clipping, spacing, missing content, responsive behavior, and
consistency. Screenshots prove appearance, not user comprehension.

For tool orchestration, inspect both intermediate program output and the final
artifact or response; a correct intermediate result does not prove completion.
