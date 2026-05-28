---
name: intent-check
description: "Explicit intent clarification for Zoey. Use only when Zoey invokes `$intent-check`, asks for an intent check, says 'bedoel je dit', 'interpreteer mijn vraag', or wants Codex to restate what it thinks she means before doing work. Converts the request into one short Dutch 'Ik interpreteer dit als...' paragraph and waits for Zoey's akkoord before execution."
---

# Intent Check

## Overview

Use this skill as a pause-before-action layer. Restate Zoey's likely user intent in plain Dutch so she can confirm, correct, or narrow the request before Codex starts planning, coding, searching, or mutating anything.

## Workflow

1. Do not execute the underlying task yet.
2. Extract the likely intent:
   - desired outcome;
   - action requested;
   - scope or object;
   - important constraints;
   - approval boundary when relevant.
3. Return one short paragraph, usually starting with:
   - `Ik interpreteer dit als: ...`
   - or `Bedoel je dit: ...?`
4. If the request is ambiguous, ask one concise clarification question after the paragraph.
5. Stop and wait for Zoey's akkoord, correction, or next instruction.

## Output Rules

- Keep it short: one compact paragraph by default.
- Use Dutch unless Zoey's request is clearly in another language.
- Do not add a full plan, checklist, implementation steps, or tool trace.
- Do not say "ik ga..." as if execution has already started.
- Mention risk or approval gates only when they change the interpretation.
- If the request includes an irreversible, external, production, privacy, CRM, email, billing, or destructive action, explicitly state that execution still needs akkoord.

## Examples

User:

```text
$intent-check pak TAB-2559 op
```

Response:

```text
Ik interpreteer dit als: je wilt dat ik eerst kort bevestig wat TAB-2559 inhoudt en daarna pas na jouw akkoord de kleine backend-fix oppak voor de stale `linkedin_accounts.account_name` select, zonder database migration, enrichment changes of brede cleanup.
```

User:

```text
$intent-check kan je dit mergen?
```

Response:

```text
Bedoel je dit: je wilt dat ik de actuele PR-status en checks controleer en, als er geen blockers zijn, expliciet jouw merge-akkoord vraag voordat ik de PR merge?
```

User:

```text
$intent-check onderzoek die Railway logs
```

Response:

```text
Ik interpreteer dit als: je wilt een read-only productie-debug rond de Railway logs, met als doel begrijpen waar de signalen vandaan komen en daarna pas een aparte fix-scope bepalen; geen deploy, database writes, queue reset of codewijzigingen zonder nieuw akkoord.
```
