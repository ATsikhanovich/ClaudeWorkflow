"""Structural checks for the workflow configuration files.

Validates YAML frontmatter of agents, skills and commands, and the JSON config
files, so a malformed file fails fast instead of silently breaking the workflow.
Python 3 standard library only - run with:

    python3 -m unittest discover -s tests -t . -p "test_*.py"
"""
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = REPO_ROOT / ".claude" / "agents"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
COMMANDS_DIR = REPO_ROOT / ".claude" / "commands"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "%s has no frontmatter block" % path
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


class TestAgentFrontmatter(unittest.TestCase):
    def test_all_agents_have_required_fields(self):
        agents = sorted(AGENTS_DIR.glob("*.md"))
        self.assertGreaterEqual(len(agents), 6)
        for path in agents:
            data = frontmatter(path)
            self.assertEqual(data.get("name"), path.stem, path.name)
            self.assertTrue(data.get("description"), path.name)
            self.assertTrue(data.get("tools"), path.name)

    def test_expected_agents_exist(self):
        names = {p.stem for p in AGENTS_DIR.glob("*.md")}
        expected = {
            "requirements-formalizer", "venue-planner", "weather", "catering-planner",
            "entertainment-planner", "logistics-planner", "timeline-planner",
            "budget-aggregator", "validator", "event-plan-builder", "html-builder",
        }
        self.assertTrue(expected.issubset(names), expected - names)


class TestSkillFrontmatter(unittest.TestCase):
    def test_skills_have_required_fields(self):
        skills = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        self.assertGreaterEqual(len(skills), 2)
        for path in skills:
            data = frontmatter(path)
            self.assertEqual(data.get("name"), path.parent.name, str(path))
            self.assertTrue(data.get("description"), str(path))

    def test_expected_skills_exist(self):
        names = {p.parent.name for p in SKILLS_DIR.glob("*/SKILL.md")}
        self.assertIn("artifact-validator", names)
        self.assertIn("event-html-theme-builder", names)


class TestCommandFrontmatter(unittest.TestCase):
    def test_commands_have_descriptions(self):
        commands = sorted(COMMANDS_DIR.glob("*.md"))
        self.assertGreaterEqual(len(commands), 3)
        for path in commands:
            data = frontmatter(path)
            self.assertTrue(data.get("description"), path.name)

    def test_approval_commands_are_human_only(self):
        for name in ("approve-event.md", "reject-event.md"):
            data = frontmatter(COMMANDS_DIR / name)
            self.assertEqual(data.get("disable-model-invocation"), "true", name)


class TestJsonConfigs(unittest.TestCase):
    def test_settings_json_registers_pre_and_post_hooks(self):
        with open(REPO_ROOT / ".claude" / "settings.json", encoding="utf-8") as handle:
            settings = json.load(handle)
        hooks = settings["hooks"]
        pre = json.dumps(hooks["PreToolUse"])
        post = json.dumps(hooks["PostToolUse"])
        self.assertIn("approval_gate_guard.py", pre)
        self.assertIn("no_leak_guard.py", pre)
        self.assertIn("post_write_state.py", post)

    def test_workflow_state_template_is_valid_json(self):
        with open(REPO_ROOT / "templates" / "workflow-state.template.json",
                  encoding="utf-8") as handle:
            template = json.load(handle)
        for key in ("run_id", "execution_plan", "artifacts", "gate_results",
                    "retry_counters", "approval"):
            self.assertIn(key, template)

    def test_mcp_json_registers_open_meteo(self):
        with open(REPO_ROOT / ".mcp.json", encoding="utf-8") as handle:
            mcp = json.load(handle)
        server = mcp["mcpServers"]["open-meteo"]
        self.assertEqual(server["command"], "npx")
        self.assertIn("open-meteo-mcp-server", " ".join(server["args"]))

    def test_approval_scripts_exist(self):
        for name in ("approve_event.py", "reject_event.py", "mcp_weather_probe.mjs"):
            self.assertTrue((REPO_ROOT / "scripts" / name).is_file(), name)

    def test_hook_scripts_exist(self):
        for name in ("approval_gate_guard.py", "no_leak_guard.py", "post_write_state.py",
                     "hooklib.py"):
            self.assertTrue((REPO_ROOT / ".claude" / "hooks" / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
