#!/usr/bin/env python3
"""PreToolUse hook: no-leak-guard.

Prevents internal artifact filenames, run paths and workflow-state keys from
appearing in the user-facing HTML (runs/<run-id>/output/event-plan.html).
Only the content being written is scanned. Bash writes of the HTML are blocked
outright because their content cannot be scanned deterministically.

Fails closed: if the HTML content cannot be determined, the write is refused.
Exit 0 = allow, exit 2 = block (message on stderr).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hooklib as h  # noqa: E402

HOOK = "no-leak-guard"

# Internal names/state keys that must never appear in the user-facing HTML.
FORBIDDEN_TOKENS = [
    "workflow-state",
    "workflow_state",
    "approval.json",
    "artifacts/",
    "runs/",
    "01-requirements",
    "02-venue",
    "02-weather",
    "03-catering",
    "03-entertainment",
    "03-logistics",
    "04-timeline",
    "04-budget",
    "05-validation",
    "06-event-plan",
    "event-plan.md",
    ".claude/",
    "retry_counter",
    "gate_result",
    "requirements_hash",
    "plan_sha256",
    "sha256",
    "run-00",
]


def scanned_text(tool_name, tool_input):
    if tool_name == "Write":
        content = tool_input.get("content")
        return content if isinstance(content, str) else None
    if tool_name == "Edit":
        new = tool_input.get("new_string")
        old = tool_input.get("old_string", "")
        if not isinstance(new, str) or not isinstance(old, str):
            return None
        return new + "\n" + old
    return None


def check_target(target, tool_name, tool_input):
    if os.path.basename(target).lower() != h.HTML_BASENAME:
        return
    if tool_name == "Bash":
        h.block(HOOK, "writing the final HTML through Bash cannot be scanned for leaked "
                      "internal names; write it with the Write tool instead (fail closed)")
    text = scanned_text(tool_name, tool_input)
    if text is None:
        h.block(HOOK, "cannot determine the content being written to %r; refusing (fail closed)"
                      % target)
    lowered = text.lower()
    leaked = [token for token in FORBIDDEN_TOKENS if token.lower() in lowered]
    if leaked:
        h.block(HOOK, "user-facing HTML must not contain internal names/state keys: %s. "
                      "Remove them and rewrite the HTML from the public event plan only."
                      % ", ".join(sorted(set(leaked))))


def main():
    try:
        event = h.read_event()
        tool_name = event.get("tool_name", "")
        if tool_name not in h.RECOGNIZED_TOOLS:
            h.block(HOOK, "unrecognized tool %r; refusing (fail closed)" % tool_name)
        tool_input = event.get("tool_input") or {}
        for target in h.target_paths(tool_name, tool_input):
            check_target(target, tool_name, tool_input)
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as exc:
        h.block(HOOK, "unexpected error %r; refusing (fail closed)" % exc)


if __name__ == "__main__":
    main()
