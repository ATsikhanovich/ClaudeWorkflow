"""Shared deterministic helpers for the workflow hooks.

Python 3 standard library only. No network access. Fail closed: every hook
using this module must treat exceptions and unresolved state as blocking
conditions, never as permission to continue.
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

RECOGNIZED_TOOLS = {"Write", "Edit", "Bash"}
HTML_BASENAME = "event-plan.html"

# Deterministic Bash patterns that indicate the final HTML file is written.
# A Bash command that merely mentions event-plan.html (e.g. `cat`) is a read.
WRITE_PATTERNS = [
    r">+\s*[\"']?[^\s\"']*event-plan\.html",
    r"\btee\b[^\n]*event-plan\.html",
    r"\bcp\s+[^\n]*event-plan\.html",
    r"\bmv\s+[^\n]*event-plan\.html",
    r"\binstall\s+[^\n]*event-plan\.html",
]


def read_event():
    raw = sys.stdin.read()
    if not raw.strip():
        raise ValueError("empty hook input on stdin")
    event = json.loads(raw)
    if not isinstance(event, dict):
        raise ValueError("hook input is not a JSON object")
    return event


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_bash_write(command):
    return any(re.search(pattern, command) for pattern in WRITE_PATTERNS)


def target_paths(tool_name, tool_input):
    """Paths this tool call writes ("" reads are not targets)."""
    if tool_name in ("Write", "Edit"):
        path = tool_input.get("file_path") or tool_input.get("path")
        return [path] if path else []
    if tool_name == "Bash":
        command = tool_input.get("command") or ""
        if not is_bash_write(command):
            return []
        return re.findall(r"[^\s\"']*event-plan\.html", command)
    return []


def find_run_root(start):
    """Walk up from `start` until a directory holding workflow-state.json."""
    cur = os.path.abspath(start or ".")
    if os.path.isfile(cur):
        cur = os.path.dirname(cur)
    while True:
        if os.path.isfile(os.path.join(cur, "workflow-state.json")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def is_under_runs(path):
    parts = re.split(r"[\\/]", os.path.abspath(path))
    return "runs" in parts


def block(hook_name, message):
    sys.stderr.write("BLOCKED [%s]: %s\n" % (hook_name, message))
    sys.exit(2)
