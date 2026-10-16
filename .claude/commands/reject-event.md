---
description: "Human-only: reject the event plan of a run with feedback; the coordinator then revises and re-validates before asking again."
argument-hint: <run-id> <feedback>
disable-model-invocation: true
---

# /reject-event — record human rejection

This command is **human-only**: a human operator runs it after reviewing the event plan.
The model must never invoke it on its own.

Arguments: `$ARGUMENTS` (`<run-id>` followed by the free-text feedback).

Do exactly this, nothing else:

1. Run the deterministic rejection script:

   ```
   python3 scripts/reject_event.py <run-id> "<feedback>"
   ```

   On Windows without a `python3` on PATH use `python scripts/reject_event.py <run-id> "<feedback>"`.

2. Report the script's output: the run id and the stored feedback.

Do not edit any artifact yourself and do not attempt to fix the plan — the coordinator
reads the stored feedback from the run state, re-runs only the affected agents plus the
synthesis, re-validates, and presents the revised plan for approval again.
