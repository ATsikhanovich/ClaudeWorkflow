#!/usr/bin/env python3
"""PreToolUse hook: approval-gate-guard.

Blocks any Write/Edit/Bash that creates runs/<run-id>/output/event-plan.html
unless runs/<run-id>/approval.json exists AND its stored plan_sha256 equals the
current SHA-256 of artifacts/06-event-plan.md. Any revision of the plan
therefore invalidates the approval.

Fails closed: an unresolvable run folder, a missing plan, an unreadable
approval.json, a run_id mismatch or any unexpected error BLOCKS the call.
Exit 0 = allow, exit 2 = block (message on stderr).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hooklib as h  # noqa: E402

HOOK = "approval-gate-guard"


def check_target(target):
    if os.path.basename(target).lower() != h.HTML_BASENAME:
        return
    run_root = h.find_run_root(os.path.dirname(target) or ".")
    if run_root is None:
        h.block(HOOK, "cannot resolve the run folder for %r (no workflow-state.json found); "
                      "refusing to write the final HTML (fail closed)" % target)

    plan_path = os.path.join(run_root, "artifacts", "06-event-plan.md")
    approval_path = os.path.join(run_root, "approval.json")

    if not os.path.isfile(approval_path):
        h.block(HOOK, "human approval is missing for run %r: ask the user to run "
                      "/approve-event %s before creating output/event-plan.html"
                      % (os.path.basename(run_root), os.path.basename(run_root)))
    if not os.path.isfile(plan_path):
        h.block(HOOK, "artifacts/06-event-plan.md is missing for run %r; approval cannot "
                      "be verified (fail closed)" % os.path.basename(run_root))

    try:
        with open(approval_path, encoding="utf-8") as handle:
            approval = json.load(handle)
    except Exception as exc:
        h.block(HOOK, "approval.json is unreadable (%s); refusing (fail closed)" % exc)

    run_id = approval.get("run_id") if isinstance(approval, dict) else None
    stored = approval.get("plan_sha256") if isinstance(approval, dict) else None
    if run_id != os.path.basename(run_root):
        h.block(HOOK, "approval.json run_id %r does not match run folder %r; refusing (fail closed)"
                      % (run_id, os.path.basename(run_root)))
    if not isinstance(stored, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", stored):
        h.block(HOOK, "approval.json has no valid plan_sha256; refusing (fail closed)")

    current = h.sha256_file(plan_path)
    if stored.lower() != current.lower():
        h.block(HOOK, "approval invalidated: artifacts/06-event-plan.md changed after approval "
                      "(approved %.12s..., current %.12s...); re-run /approve-event %s"
                      % (stored, current, os.path.basename(run_root)))


def main():
    try:
        event = h.read_event()
        tool_name = event.get("tool_name", "")
        if tool_name not in h.RECOGNIZED_TOOLS:
            h.block(HOOK, "unrecognized tool %r; refusing (fail closed)" % tool_name)
        for target in h.target_paths(tool_name, event.get("tool_input") or {}):
            check_target(target)
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as exc:
        h.block(HOOK, "unexpected error %r; refusing (fail closed)" % exc)


if __name__ == "__main__":
    main()
