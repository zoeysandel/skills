# skills

This is my public collection of **agent skills**: reusable instructions (and sometimes scripts/resources) that help an AI agent perform specialized tasks more reliably.

Skills are meant to be **portable**. You can use them with different agent runtimes and tools (for example Cursor, Codex, Claude Code, etc.) by pointing your agent at the relevant `skills/<skill-id>/` folder.

## What’s a skill?

A skill is a self-contained folder with a `SKILL.md` file that includes:

- **YAML frontmatter**: metadata like `name` and `description`
- **Instructions**: the behavior, constraints, and workflow the agent should follow when the skill is active

## Skill status

Compared with the owner's local skills on **2026-11-07**, at repository baseline
`754af6a`. This is a dated source comparison, not a runtime validation or an
ongoing synchronization guarantee. Local alternatives listed below are not yet
published here.

| Skill | Status | Finding / local alternative |
| --- | --- | --- |
| [Prompt Writer](skills/prompt-writer/) | Updated from local source | Synced on 2026-11-07: shorter core and separate API, output-pattern and validation references; optional-skill fallbacks added for portability. |
| [Shadow Run](skills/shadow-run/) | Locally present; source aligned | Local workflow and timebox script are aligned. The published edition adds portable setup, a bundled watchdog role and relative paths; delegation wording differs slightly. |
| [Continue](skills/continue/) | **Deprecated** | No longer installed locally. Continuation/completion behavior is covered by `follow-through` and active task instructions. |
| [Intent Check](skills/intent-check/) | **Deprecated** | No longer installed locally. Use `understand-intent` for alignment; ask for confirmation explicitly when wanted. |
| [Loop Creator](skills/loop-creator/) | **Deprecated** | No longer installed locally. Functional alternatives: `prepare-development` for preparation and `graph-engineering` for coordination; not a drop-in replacement. |
| [Example Skill](skills/example-skill/) | Template only | Not installed locally; retained as a starter template, not a maintained operational skill. |

Deprecated folders remain available for historical reference and existing links.
They are not recommended for new installations. Their original workflow text is
retained below a deprecation notice.

### Active skills

- [Clean Code Standard](skills/clean-code-standard/) — Codex edition of the
  owner’s code and review standard, with review checklist and examples.

- [Prompt Writer](skills/prompt-writer/) — write and improve prompts and agent
  assignments. Includes all four conditional references and Codex UI metadata.
- [Shadow Run](skills/shadow-run/) — unattended creative exploration and isolated
  prototypes within an explicit time and usage window.
  [Requirements and usage](skills/shadow-run/references/setup.md).

### Import Prompt Writer on another machine

Copy the complete [`skills/prompt-writer/`](skills/prompt-writer/) directory,
including `references/` and `agents/`, into your agent runtime's skills directory.
For Codex, the usual user location is `~/.codex/skills/prompt-writer/` (or the
`skills/prompt-writer/` directory under a custom `CODEX_HOME`). Reload the host
if needed, then invoke `$prompt-writer`.

No API key, scripts or machine-specific paths are required. `understand-intent`,
`investigate` and `openai-docs` are optional companion skills, not included in this
package. The skill has fallbacks when they are absent. Live documentation checks
need search/documentation access; without it, runtime claims remain unverified.
Dated model notes are retained as local source context, not freshly verified
provider guidance. Importability was checked statically; execution on another
machine has not been tested.

## Repo structure

- `skills/<skill-id>/SKILL.md`: one folder per skill, following the `SKILL.md` convention
