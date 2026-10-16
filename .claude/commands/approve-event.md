---
description: "Human-only: approve the event plan of a run and record the deterministic approval (writes approval.json)."
argument-hint: <run-id>
disable-model-invocation: true
---

# /approve-event — record human approval

This command is **human-only**: a human operator runs it after reviewing the event plan.
The model must never invoke it on its own.

Arguments: `$ARGUMENTS` (must contain exactly one run id, e.g. `run-001-birthday`).

Do exactly this, nothing else:

1. Run the deterministic approval script (it refuses if any quality gate is still failing):

   ```
   python3 scripts/approve_event.py <run-id>
   ```

   On Windows without a `python3` on PATH use `python scripts/approve_event.py <run-id>`.

2. Report the script's output to the user: the run id, the recorded `plan_sha256`, and the
   `approved_at` timestamp.

Do not modify any artifact, do not write `approval.json` yourself, and do not proceed to
generate HTML — the coordinator continues the workflow after seeing
`approval.status = "approved"` in the run state.
