#!/usr/bin/env python3
"""Record human approval for a run (invoked only via /approve-event).

Writes runs/<run-id>/approval.json {run_id, plan_sha256, approved_at} where
plan_sha256 is the SHA-256 of artifacts/06-event-plan.md at approval time, and
marks the run state approval.status = "approved". Refuses to approve while any
quality gate is still failing. Never called by the coordinator or any agent.

Usage: python3 scripts/approve_event.py <run-id>
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

ALLOWED_GATE_STATUSES = {"PASS", "PASS-N/A"}


def fail(message):
    sys.stderr.write("approve_event: %s\n" % message)
    sys.exit(1)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        fail("usage: approve_event.py <run-id>")
    run_id = sys.argv[1].strip()
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    run_dir = os.path.join(repo_root, "runs", run_id)
    if not os.path.isdir(run_dir):
        fail("run folder not found: %s" % run_dir)

    plan_path = os.path.join(run_dir, "artifacts", "06-event-plan.md")
    state_path = os.path.join(run_dir, "workflow-state.json")
    if not os.path.isfile(plan_path):
        fail("artifacts/06-event-plan.md not found; nothing to approve")
    if not os.path.isfile(state_path):
        fail("workflow-state.json not found; run state is required")

    with open(state_path, encoding="utf-8") as handle:
        state = json.load(handle)

    failing = sorted(
        gate for gate, result in state.get("gate_results", {}).items()
        if result.get("status") not in ALLOWED_GATE_STATUSES
    )
    if failing:
        fail("refusing to approve: gate(s) not passing: %s" % ", ".join(failing))

    plan_sha256 = sha256_file(plan_path)
    approved_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    approval = {"run_id": run_id, "plan_sha256": plan_sha256, "approved_at": approved_at}

    with open(os.path.join(run_dir, "approval.json"), "w", encoding="utf-8", newline="\n") as handle:
        json.dump(approval, handle, indent=2)
        handle.write("\n")

    approval_state = state.setdefault("approval", {})
    approval_state.update({
        "status": "approved",
        "approved_at": approved_at,
        "plan_sha256": plan_sha256,
    })
    state["updated_at"] = approved_at
    tmp_path = state_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(state, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(tmp_path, state_path)

    print("approve_event: run %s approved" % run_id)
    print("  plan_sha256: %s" % plan_sha256)
    print("  approved_at: %s" % approved_at)
    print("  wrote %s" % os.path.join("runs", run_id, "approval.json"))


if __name__ == "__main__":
    main()
