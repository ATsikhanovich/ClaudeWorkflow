#!/usr/bin/env python3
"""Record human rejection feedback for a run (invoked only via /reject-event).

Stores the feedback in runs/<run-id>/workflow-state.json (approval.status =
"rejected", approval.feedback appended, approval.rejected_count incremented) and
removes a stale approval.json if one exists, so the approval gate can never let a
rejected plan through to HTML.

Usage: python3 scripts/reject_event.py <run-id> "<feedback>"
"""
import json
import os
import sys
from datetime import datetime, timezone


def fail(message):
    sys.stderr.write("reject_event: %s\n" % message)
    sys.exit(1)


def main():
    if len(sys.argv) < 3 or not sys.argv[1].strip() or not " ".join(sys.argv[2:]).strip():
        fail('usage: reject_event.py <run-id> "<feedback>"')
    run_id = sys.argv[1].strip()
    feedback = " ".join(sys.argv[2:]).strip()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    run_dir = os.path.join(repo_root, "runs", run_id)
    if not os.path.isdir(run_dir):
        fail("run folder not found: %s" % run_dir)

    state_path = os.path.join(run_dir, "workflow-state.json")
    if not os.path.isfile(state_path):
        fail("workflow-state.json not found; run state is required")
    with open(state_path, encoding="utf-8") as handle:
        state = json.load(handle)

    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    approval_state = state.setdefault("approval", {})
    feedback_list = approval_state.setdefault("feedback", [])
    feedback_list.append({"at": stamp, "feedback": feedback})
    approval_state["status"] = "rejected"
    approval_state["rejected_count"] = int(approval_state.get("rejected_count") or 0) + 1
    state.setdefault("notes", []).append("rejected at %s: %s" % (stamp, feedback))
    state["updated_at"] = stamp

    tmp_path = state_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(state, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(tmp_path, state_path)

    approval_path = os.path.join(run_dir, "approval.json")
    if os.path.isfile(approval_path):
        os.remove(approval_path)
        print("reject_event: removed stale approval.json")

    print("reject_event: run %s rejected" % run_id)
    print("  feedback: %s" % feedback)
    print("  rejection #%d recorded in workflow-state.json"
          % approval_state["rejected_count"])


if __name__ == "__main__":
    main()
