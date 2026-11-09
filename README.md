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
| [Shadow Run](skills/shadow-run/) | **Deprecated** | Retired on 2026-11-09: no longer used; the reset/usage exploration idea needs reconsideration. Retained for historical reference; no replacement yet. |
| [Continue](skills/continue/) | **Deprecated** | No longer installed locally. Continuation/completion behavior is covered by global instructions; the separate local `follow-through` skill was removed on 2026-11-07. |
| [Intent Check](skills/intent-check/) | **Deprecated** | No longer installed locally. Use `understand-intent` for alignment; ask for confirmation explicitly when wanted. |
| [Loop Creator](skills/loop-creator/) | **Deprecated** | No longer installed locally. Functional alternatives: `prepare-development` for preparation and `graph-engineering` for coordination; not a drop-in replacement. |
| [Example Skill](skills/example-skill/) | Template only | Not installed locally; retained as a starter template, not a maintained operational skill. |

Deprecated folders remain available for historical reference and existing links.
They are not recommended for new installations. Their original workflow text is
retained below a deprecation notice.

### Active skills

- [Prompt Writer for Claude](skills/prompt-writer-claude/) — separate Claude Code
  edition for Sonnet 5.5 and Opus 5.5, with model, API and host references.

- [Manage Chat Status](skills/manage-chat-status/) — Codex sidebar status,
  parent-child handoffs and cleanup under the owner's global policy.
  Install together with [the Codex sidebar rules](rules/codex-sidebar.md).

- [Clean Code Standard](skills/clean-code-standard/) — Codex edition of the
  owner’s code and review standard, with review checklist and examples.

- [Prompt Writer](skills/prompt-writer/) — write and improve prompts and agent
  assignments. Includes all four conditional references and Codex UI metadata.

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

### Install the Codex sidebar setup on another laptop

This is a narrowly scoped Codex setup, not the complete cross-client marketplace
or a full copy of the owner's global instructions. It contains no credentials,
personal chat contents, fixed section IDs or machine-specific paths. Claude Code
does not gain Codex sidebar capabilities by installing this package.

1. Clone or update this repository. Copy the complete
   `skills/manage-chat-status/` folder to the active Codex user skills directory
   (usually `~/.codex/skills/manage-chat-status/`, or under your custom
   `CODEX_HOME`). Keep any existing customized version backed up before replacing.
2. Merge `rules/codex-sidebar.md` into that Codex user's global `AGENTS.md`
   (usually `~/.codex/AGENTS.md`). Replace an older sidebar/archiving policy;
   preserve unrelated rules and resolve local conflicts instead of appending
   competing copies. Review its five-/fifteen-weekday cleanup authorization before
   adopting it on a separate work account. Installing a skill alone does not
   install global rules or grant account permissions.
3. Reload skill discovery if necessary. In Codex desktop, ask:
   “Use $manage-chat-status. Set up the five sidebar sections from my global
   rules, reuse existing sections, and verify this chat's placement.”
   Required names: Jouw actie nodig, Codex actie nodig, Bezig, Wacht op extern,
   Afgerond. Resolve IDs on that installation. The Codex app tools for listing,
   reading, moving, waiting and messaging chats must actually be available.
4. Verify one normal chat and one already-authorized parent-child handoff. No
   recurring cleanup is installed. Missing tools are reported, not bypassed.

To update, pull the repository, replace the installed skill and reconcile only
the sidebar policy in global `AGENTS.md`. Keep local changes visible; there is
no automatic synchronization, plugin refresh or background watcher here.

## Repo structure

- `skills/<skill-id>/SKILL.md`: one folder per skill, following the `SKILL.md` convention
- `rules/codex-sidebar.md`: the portable Codex sidebar policy to merge into global instructions
