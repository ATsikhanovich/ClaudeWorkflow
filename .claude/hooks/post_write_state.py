#!/usr/bin/env python3
"""PostToolUse hook: post-write-state.

On every artifact write inside runs/<run-id>/, updates that run's
workflow-state.json: artifact status, SHA-256 hash, timestamp, owner agent and
current step. Writing artifacts/01-requirements.md also refreshes the
requirements_hash.

Fails closed: a write inside runs/ without a resolvable workflow-state.json, or
any error while updating state, exits 2 with a clear message so the mistake is
never silent. Exit 0 = state updated (or nothing to do).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hooklib as h  # noqa: E402

HOOK = "post-write-state"

OWNER_BY_FILENAME = {
    "01-requirements.md": "requirements-formalizer",
    "02-venue.md": "venue-planner",
    "02-weather.md": "weather",
    "03-catering.md": "catering-planner",
    "03-entertainment.md": "entertainment-planner",
    "03-logistics.md": "logistics-planner",
    "04-timeline.md": "timeline-planner",
    "04-budget.md": "budget-aggregator",
    "05-validation.md": "validator",
    "06-event-plan.md": "event-plan-builder",
    "event-plan.html": "html-builder",
}

STEP_BY_FILENAME = {
    "01-requirements.md": "requirements",
    "02-venue.md": "recon",
    "02-weather.md": "recon",
    "03-catering.md": "services",
    "03-entertainment.md": "services",
    "03-logistics.md": "services",
    "04-timeline.md": "schedule-and-cost",
    "04-budget.md": "schedule-and-cost",
    "05-validation.md": "validation",
    "06-event-plan.md": "synthesis",
    "event-plan.html": "html",
}


def update_state(run_root, written_path):
    rel = os.path.relpath(written_path, run_root).replace(os.sep, "/")
    filename = os.path.basename(rel)
    owner = OWNER_BY_FILENAME.get(filename)
    if owner is None:
        return False
    if not (rel.startswith("artifacts/") or rel.startswith("output/")):
        return False

    state_path = os.path.join(run_root, "workflow-state.json")
    with open(state_path, encoding="utf-8") as handle:
        state = json.load(handle)
    if not isinstance(state, dict):
        raise ValueError("workflow-state.json is not a JSON object")

    digest = h.sha256_file(written_path)
    stamp = h.now_iso()
    artifacts = state.setdefault("artifacts", {})
    entry = artifacts.get(rel) if isinstance(artifacts.get(rel), dict) else {}
    entry.update({
        "owner": entry.get("owner", owner),
        "status": "done",
        "sha256": digest,
        "updated_at": stamp,
    })
    artifacts[rel] = entry
    state["current_step"] = STEP_BY_FILENAME.get(filename, state.get("current_step"))
    if rel == "artifacts/01-requirements.md":
        state["requirements_hash"] = digest
    state["updated_at"] = stamp

    tmp_path = state_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(state, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(tmp_path, state_path)
    return True


def main():
    try:
        event = h.read_event()
        tool_name = event.get("tool_name", "")
        if tool_name not in h.RECOGNIZED_TOOLS:
            h.block(HOOK, "unrecognized tool %r; refusing (fail closed)" % tool_name)
        tool_input = event.get("tool_input") or {}
        written = tool_input.get("file_path") or tool_input.get("path")
        if not written:
            sys.exit(0)
        if not h.is_under_runs(written):
            sys.exit(0)
        run_root = h.find_run_root(os.path.dirname(written) or ".")
        if run_root is None:
            h.block(HOOK, "write %r is inside runs/ but no workflow-state.json was found; "
                          "state cannot be updated (fail closed)" % written)
        update_state(run_root, os.path.abspath(written))
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as exc:
        h.block(HOOK, "failed to update workflow-state.json (%r); refusing to continue silently"
                      % exc)


if __name__ == "__main__":
    main()
