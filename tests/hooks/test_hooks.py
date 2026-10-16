"""Unit tests for the workflow hooks (tests/hooks/).

Each hook is exercised as a subprocess fed a fixture JSON document on stdin
(same shape as Claude Code hook input), against a temporary run folder.
Python 3 standard library only — run with:

    python3 -m unittest discover -s tests/hooks
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOKS_DIR = REPO_ROOT / ".claude" / "hooks"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

RUN_ID = "run-test-001"
RUN_REL = os.path.join("runs", RUN_ID)
PLAN_TEXT = "# Event plan\n\nDraft plan used by the hook tests.\n"
VENUE_TEXT = "# Venue\n\n- **Owner agent:** venue-planner\n"
REQUIREMENTS_TEXT = "# Requirements\n\n- **Owner agent:** requirements-formalizer\n"

APPROVAL_GUARD = "approval_gate_guard.py"
NO_LEAK_GUARD = "no_leak_guard.py"
POST_WRITE_STATE = "post_write_state.py"


def load_fixture(name):
    with open(FIXTURES_DIR / name, encoding="utf-8") as handle:
        return json.load(handle)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run_hook(script, payload, cwd):
    return subprocess.run(
        [sys.executable, str(HOOKS_DIR / script)],
        input=json.dumps(payload).encode("utf-8"),
        capture_output=True,
        cwd=str(cwd),
    )


def base_state():
    return {
        "schema_version": 1,
        "run_id": RUN_ID,
        "created_at": "2026-10-10T10:00:00Z",
        "updated_at": "2026-10-10T10:00:00Z",
        "current_step": "validation",
        "requirements_hash": None,
        "execution_plan": [{"step": 5, "name": "validation", "agents": ["validator"],
                            "depends_on": [4], "status": "running", "attempts": 1}],
        "artifacts": {
            "artifacts/06-event-plan.md": {
                "owner": "event-plan-builder",
                "status": "done",
                "sha256": sha256_text(PLAN_TEXT),
                "updated_at": "2026-10-10T10:00:00Z",
            }
        },
        "gate_results": {
            "G1": {"status": "PASS", "attempts": 1, "findings": [], "responsible_agent": None}
        },
        "retry_counters": {"G1": 0},
        "approval": {"status": "pending", "approved_at": None, "plan_sha256": None,
                     "rejected_count": 0, "feedback": []},
        "notes": ["seeded by tests"],
    }


class HookTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def build_run(self, approval="valid", state=True, plan_text=PLAN_TEXT):
        run_dir = self.root / "runs" / RUN_ID
        (run_dir / "artifacts").mkdir(parents=True)
        (run_dir / "output").mkdir(parents=True)
        (run_dir / "artifacts" / "06-event-plan.md").write_bytes(plan_text.encode("utf-8"))
        if state:
            (run_dir / "workflow-state.json").write_text(
                json.dumps(base_state(), indent=2), encoding="utf-8")
        if approval == "valid":
            self.write_approval(sha256_text(plan_text))
        elif approval == "wrong":
            self.write_approval(sha256_text("some other plan revision\n"))
        return run_dir

    def write_approval(self, plan_sha256, run_id=RUN_ID):
        payload = {"run_id": run_id, "plan_sha256": plan_sha256,
                   "approved_at": "2026-10-10T12:00:00Z"}
        (self.root / "runs" / RUN_ID / "approval.json").write_text(
            json.dumps(payload, indent=2), encoding="utf-8")

    def read_state(self):
        path = self.root / "runs" / RUN_ID / "workflow-state.json"
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)

    def materialize_write(self, payload):
        """Simulate the tool's write so PostToolUse sees the file on disk."""
        tool_input = payload["tool_input"]
        target = self.root / tool_input["file_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(tool_input.get("content", "").encode("utf-8"))


class TestApprovalGateGuard(HookTestCase):
    def test_allows_html_after_human_approval(self):
        self.build_run(approval="valid")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blocks_html_without_approval(self):
        self.build_run(approval="missing")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"/approve-event", result.stderr)

    def test_blocks_html_with_wrong_plan_hash(self):
        self.build_run(approval="wrong")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"approval invalidated", result.stderr)

    def test_revision_after_approval_invalidates_approval(self):
        self.build_run(approval="valid")
        plan = self.root / "runs" / RUN_ID / "artifacts" / "06-event-plan.md"
        plan.write_text(PLAN_TEXT + "\nA revision after approval.\n", encoding="utf-8")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"approval invalidated", result.stderr)

    def test_blocks_bash_write_without_approval(self):
        self.build_run(approval="missing")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_bash_write_html.json"), self.root)
        self.assertEqual(result.returncode, 2)

    def test_allows_bash_read_of_html(self):
        self.build_run(approval="missing")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_bash_read_html.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blocks_when_run_folder_cannot_be_resolved(self):
        result = run_hook(APPROVAL_GUARD,
                          load_fixture("pre_write_html_unknown_run.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"fail closed", result.stderr)

    def test_allows_artifact_writes(self):
        self.build_run(approval="missing")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_artifact.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blocks_on_run_id_mismatch(self):
        self.build_run(approval="valid")
        self.write_approval(sha256_text(PLAN_TEXT), run_id="run-other")
        result = run_hook(APPROVAL_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"does not match", result.stderr)

    def test_blocks_unrecognized_tool(self):
        self.build_run(approval="valid")
        payload = {"hook_event_name": "PreToolUse", "tool_name": "MysteryTool",
                   "tool_input": {"file_path": "runs/run-test-001/output/event-plan.html"}}
        result = run_hook(APPROVAL_GUARD, payload, self.root)
        self.assertEqual(result.returncode, 2)


class TestNoLeakGuard(HookTestCase):
    def test_blocks_internal_names_in_html(self):
        result = run_hook(NO_LEAK_GUARD, load_fixture("pre_write_html_leak.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"internal names", result.stderr)
        self.assertIn(b"workflow-state", result.stderr)

    def test_allows_clean_html(self):
        result = run_hook(NO_LEAK_GUARD, load_fixture("pre_write_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_allows_clean_edit_of_html(self):
        result = run_hook(NO_LEAK_GUARD, load_fixture("pre_edit_html_clean.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blocks_bash_write_of_html(self):
        result = run_hook(NO_LEAK_GUARD, load_fixture("pre_bash_write_html.json"), self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"Write tool", result.stderr)

    def test_allows_artifact_writes(self):
        result = run_hook(NO_LEAK_GUARD, load_fixture("pre_write_artifact.json"), self.root)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_blocks_when_content_missing(self):
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Write",
                   "tool_input": {"file_path": "runs/run-test-001/output/event-plan.html"}}
        result = run_hook(NO_LEAK_GUARD, payload, self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"fail closed", result.stderr)


class TestPostWriteState(HookTestCase):
    def test_updates_state_on_artifact_write(self):
        self.build_run()
        payload = load_fixture("post_write_venue.json")
        self.materialize_write(payload)
        result = run_hook(POST_WRITE_STATE, payload, self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        state = self.read_state()
        entry = state["artifacts"]["artifacts/02-venue.md"]
        self.assertEqual(entry["owner"], "venue-planner")
        self.assertEqual(entry["status"], "done")
        self.assertEqual(entry["sha256"], sha256_text(VENUE_TEXT))
        self.assertEqual(state["current_step"], "recon")
        self.assertEqual(state["gate_results"]["G1"]["status"], "PASS")
        self.assertEqual(state["notes"], ["seeded by tests"])

    def test_updates_requirements_hash(self):
        self.build_run()
        payload = load_fixture("post_write_requirements.json")
        self.materialize_write(payload)
        result = run_hook(POST_WRITE_STATE, payload, self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        state = self.read_state()
        self.assertEqual(state["requirements_hash"], sha256_text(REQUIREMENTS_TEXT))
        self.assertEqual(state["current_step"], "requirements")

    def test_records_html_output(self):
        self.build_run()
        payload = load_fixture("post_write_html.json")
        self.materialize_write(payload)
        result = run_hook(POST_WRITE_STATE, payload, self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        entry = self.read_state()["artifacts"]["output/event-plan.html"]
        self.assertEqual(entry["owner"], "html-builder")
        self.assertEqual(entry["status"], "done")

    def test_ignores_writes_outside_runs(self):
        self.build_run()
        payload = load_fixture("post_write_nonrun.json")
        self.materialize_write(payload)
        before = self.read_state()
        result = run_hook(POST_WRITE_STATE, payload, self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.read_state(), before)

    def test_fails_closed_without_state_file(self):
        self.build_run(state=False)
        payload = load_fixture("post_write_venue.json")
        self.materialize_write(payload)
        result = run_hook(POST_WRITE_STATE, payload, self.root)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b"fail closed", result.stderr)


class TestHookHygiene(unittest.TestCase):
    def test_hooks_use_no_network_modules(self):
        banned = ("urllib", "socket", "http", "requests", "httpx")
        for script in (APPROVAL_GUARD, NO_LEAK_GUARD, POST_WRITE_STATE, "hooklib.py"):
            source = (HOOKS_DIR / script).read_text(encoding="utf-8")
            for name in banned:
                self.assertNotIn("import %s" % name, source, script)
                self.assertNotIn("from %s" % name, source, script)

    def test_fixtures_are_valid_json(self):
        fixtures = sorted(FIXTURES_DIR.glob("*.json"))
        self.assertGreaterEqual(len(fixtures), 8)
        for path in fixtures:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
            self.assertIn("tool_name", data, path.name)
            self.assertIn("tool_input", data, path.name)


if __name__ == "__main__":
    unittest.main()
