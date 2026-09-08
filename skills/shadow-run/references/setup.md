# Using Shadow Run

This is the Dutch-language public copy of my personal Codex skill. It explores
design alternatives or builds isolated first versions while the user is away.
It does not publish, deploy, or change the original project.

Copy the complete `shadow-run` directory into your runtime's skills directory.
Start in a task with a clear project scope and an explicit deadline, for example:

> Use $shadow-run for this project until 03:00 Europe/Amsterdam. Explore different
> design directions in separate copies and leave me results I can compare.

The agent must resolve the actual date and UTC deadline before starting. Read
the skill and adapt personal preferences to your environment. Existing user and
project instructions, including design-tool preferences, still apply.

## Requirements and limits

- A current clock and an account usage readback, such as Codex's
  `get_usage_limits`, are needed to track the available budget.
- Unattended checks need a verified wake-up mechanism. The skill uses a temporary
  thread heartbeat when the host provides one. Copying the skill does not install
  or activate a scheduler. A runtime without these capabilities must report the
  limitation instead of claiming unattended monitoring.
- The included `agents/shadow.toml` contains the optional read-only watchdog
  instructions and the author's Astra medium model configuration. The parent
  supplies `references/time-and-usage.md` with the run agreement. A file inside a
  skill does not automatically register a custom agent role. Use a supported
  runtime role setup or the general-subagent fallback described in the skill.
  Model availability must be checked; never silently substitute another model.
- The independent watchdog is optional when delegation is unavailable; the parent
  must still meet the time and usage control requirements.
- `scripts/timebox.py` requires Python 3 and a POSIX operating system. Run its
  commands from the skill directory or resolve its absolute installed path.
  `caffeinate` is macOS-specific and is only relevant when needed.

Usage checks are periodic. They cannot guarantee zero usage after a reset or
preempt an active model call. The local timebox only stops the process group it
starts, not Codex itself. The skill stops new work on a detected reset and keeps
an explicit hard deadline and closing buffer.

No additional personal skills are required. Independent design review is used
when available and authorized; it is not proof of real-user validation.
