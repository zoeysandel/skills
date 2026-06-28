# Continue Decision Table

| Signal | Classification | Action |
| --- | --- | --- |
| Zoey says `go`, `ga`, `start`, `pak op`, or `voer uit` with a clear current task | Start | Begin with the first safe context/action step |
| Zoey says `ga door`, `continue`, `what's next`, `wat nu`, or `volgende stap` inside an active loop | Continue | Execute the next required in-scope step |
| Zoey says `go` after prior assistant work or a handoff | Continue | Treat this as "continue this chat/owner-loop"; proceed unless ambiguity, risk, or approval boundaries require a narrow question |
| Zoey says `yes`, `ja`, or `doe maar` after a concrete recommended/default next step | Confirm | Execute that specific proposed step inside the existing boundaries |
| Zoey says `yes`, `ja`, or `doe maar` without a concrete recent proposal | Recover | Rebuild the intended next step before acting |
| Zoey asks what is open, context is stale, or the next action is uncertain | Recover | Reconstruct state from thread, ledger, repo, PR/checks, and active plans |
| Required next step is in scope and low risk | Continue | Do it now |
| Helpful next step is in scope but optional for completion | Optional | Mention briefly; do not block completion |
| Existing workflow already defines the default | Continue | Follow it; do not ask again |
| PR/check/watch state is ready, mergeable, or `merge_now` | Continue | Merge or perform the readiness action unless monitor-only was explicit |
| Planning is clear but execution was not approved | Decision | Advance the planning/review gate, not build execution |
| Next step changes scope, policy, auth, privacy, schema, public API, or vendor-credit usage | Escalate | Ask one narrow question with a recommended default |
| Destructive action or missing permission blocks progress | Escalate | Ask for the specific approval or credential needed |
