# Prompt validation

Validate in proportion to failure cost. A written draft, a static review and an
observed model run are different levels of evidence; say which one you have.

## Static check for any rewrite

Before handing over a rewritten prompt, compare it with the source and confirm:

- Every fact survives exactly. Numbers, names, dates, paths, IDs, quoted text.
- Scope is unchanged. Nothing added that the user did not ask for, nothing
  dropped that they did.
- Permissions are unchanged. Read-only stays read-only; no new push, send,
  delete, install or spend; no new approval step the user did not ask for.
- The deliverable, its location, format and audience are the same.
- Writing preferences (language, register, banned words or punctuation) are kept.
- The completion bar and the evidence to return are stated.
- No request to write out internal reasoning in the reply.
- No runtime setting written as prompt text, and no unsupported setting
  suggested (sampling parameters, prefill or forced `tool_choice` on either 5.5
  model, see [API](api.md)).

A quick way is a must-contain and must-not-contain list per prompt, checked by
reading or with a small script.

## Behavioral comparison for material changes

For a product prompt, a large refactor or a model migration:

1. Keep the current prompt, model and effective effort as the baseline.
2. Pick representative cases and write observable pass criteria first, including
   negative cases (absent facts not invented, advice stays read-only, an
   authorized task reaches its completion bar).
3. Run old and new on the same model and settings. For a migration, compare
   models with the same prompt before attributing a difference to prompt edits.
4. Judge against the criteria, blind to the variant when practical. One good
   sample is not a reliable gain; repeat variable cases.
5. Fix what is attributable and re-run the affected cases.

Effort changes behavior on both 5.5 models (thinking depth, check-ins,
verification, scope), so record the effort level with every result.

If runs are not possible, give the comparison plan and state that behavioral
equivalence or improvement is unverified.

## Domain checks

- Coding prompts. Ask for the project's real tests, type checks or build for the
  changed code, and for a named list of checks that could not run.
- Research prompts. Ask for sources per consequential claim, labeled inference,
  and disclosed conflicts between sources.
- Tool-using agents. Check intermediate tool results and the final answer; a
  correct intermediate step does not prove completion.
