# Event Planner — Reliable Agentic Workflow (Claude Code)

A model-driven **hub-and-spoke agentic workflow** for the Event Planner domain, built for
Claude Code. A coordinator slash command (`/plan-event`) drives 11 single-responsibility
subagents, enforces named quality gates with targeted retries, persists state for
interruption-safe resume, and renders the final `event-plan.html` **only after explicit,
deterministically verified human approval**.

- Workflow rules and architecture: [`CLAUDE.md`](./CLAUDE.md)
- Example runs with full artifacts: [`runs/`](./runs/)

## Prerequisites

| Tool | Version | Why |
|------|---------|-----|
| Claude Code | recent | runs the coordinator, agents, hooks, skills, MCP |
| Node.js | **22 or newer** | launches the Open-Meteo MCP server via `npx` |
| Python | **3.8+** (`python3` on PATH) | deterministic hooks + approval scripts |
| Network access | — | WebSearch/WebFetch and Open-Meteo API calls |

## Environment setup

```bash
git clone <this-repo> && cd <this-repo>
```

No secrets are required. `.env.example` documents this; copy it to `.env` only if you
extend the workflow with a keyed service. Never commit `.env`.

**Windows note:** the hooks and approval scripts are registered as `python3 ...` in
`.claude/settings.json` and the commands reference `python3 scripts/...`. If `python3` is
not on your PATH (python.org installers provide `python`), change the three `command`
strings in `.claude/settings.json` to `python .claude/hooks/...` — nothing else changes.

### Verify the setup

```bash
# 1. unit tests for the hooks and config frontmatter (Python stdlib only)
python3 -m unittest discover -s tests -t . -p "test_*.py"

# 2. smoke-test the Open-Meteo MCP server exactly as Claude Code launches it
node scripts/mcp_weather_probe.mjs --list
echo {"name": "Warsaw"} > args.json
node scripts/mcp_weather_probe.mjs geocoding @args.json
```

`mcp_weather_probe.mjs` reads the command from `.mcp.json`, performs the MCP handshake
over stdio and lists/calls tools. The weather agent uses the same server through the MCP
integration.

## How to run

In Claude Code, from the repo root:

```
/plan-event Plan a 40-person 30th birthday party in Warsaw on 2026-11-14, budget 6000 PLN, indoor venue, vegetarian options, live music.
```

The coordinator then:
1. creates `runs/<run-id>/` and writes `input.md` + `workflow-state.json`,
2. asks you (AskUserQuestion) to confirm anything missing from the request,
3. runs the subagents in dependency order (parallel groups where independent),
4. validates artifacts against gates **G1–G8** and retries only failing agents (max 3),
5. synthesizes `artifacts/06-event-plan.md` and **stops for your approval**.

## Human approval (deterministic)

After the plan is synthesized, review `runs/<run-id>/artifacts/06-event-plan.md`, then run
**one** of these human-only commands (`disable-model-invocation: true` — the model can
never run them itself):

```
/approve-event <run-id>              # writes runs/<run-id>/approval.json {run_id, plan_sha256, approved_at}
/reject-event <run-id> <feedback>    # stores feedback in state; the coordinator revises and asks again
```

`/approve-event` runs `scripts/approve_event.py`, which refuses while any gate is failing
and records the SHA-256 of the plan. The `approval-gate-guard` hook blocks any write of
`output/event-plan.html` unless `approval.json` exists **and** its hash matches the
current plan — so **any revision after approval invalidates it** and requires re-approval.

## How to resume

```
/plan-event --resume <run-id>
```

Resume reads `runs/<run-id>/workflow-state.json`, re-hashes every artifact on disk, skips
completed hash-clean steps and continues only pending/failed/stale ones.

### Testing resume after a kill (the "kill mid-run" drill)

1. Start a run and interrupt Claude Code (close the window / Ctrl-C) right after a
   subagent writes its artifact — e.g. during the services group.
2. Inspect `runs/<run-id>/workflow-state.json`: the finished artifacts have `status:
   "done"` with hashes, later steps are `pending`.
3. Restart Claude Code and run `/plan-event --resume <run-id>`.
4. Observe: completed agents are **not** re-run; execution continues from the first
   unfinished step. Repeat the kill at any later point to confirm it keeps working.

## Quality gates and retries

`G1` budget · `G2` venue capacity · `G3` dietary/accessibility · `G4` timeline overlaps ·
`G5` service coverage · `G6` weather consistency · `G7` real source URLs · `G8` artifact
structure. Failures map to the responsible agent; only that agent and its downstream
dependents are re-run, max 3 attempts per gate, then dependent execution stops with a
clear report. See `CLAUDE.md` §5–6.

## Hooks

Registered in `.claude/settings.json` (Python 3, stdlib only, no network, fail closed):

| Hook | Event | Does |
|------|-------|------|
| `approval-gate-guard` | PreToolUse | blocks the final HTML until human approval matches the plan hash |
| `no-leak-guard` | PreToolUse | blocks internal artifact/state names from leaking into the HTML |
| `post-write-state` | PostToolUse | updates `workflow-state.json` on every artifact write |

Run their unit tests with the command in "Verify the setup" above.

## MCP

`.mcp.json` registers **open-meteo-mcp-server@2.5.2** (community MCP server,
[github.com/cmer81/open-meteo-mcp](https://github.com/cmer81/open-meteo-mcp)) via
`npx -y -p open-meteo-mcp-server@2.5.2 open-meteo-mcp-server`. No API key is needed
(Open-Meteo is free for non-commercial use). The weather agent **must** call it; if it is
unavailable the step fails visibly instead of inventing data.

## Sample runs

| Run | Scenario | Demonstrates |
|-----|----------|--------------|
| `runs/run-001-birthday` | 40 guests, indoor birthday, 6 000 PLN, vegetarian, live music | happy path |
| `runs/run-002-corporate-offsite` | 80 guests, outdoor-capable offsite, 20 000 PLN | gate G1 failure → targeted retry → downstream regeneration |
| `runs/run-003-small-anniversary` | 12 guests, restaurant anniversary, no entertainment | plan adaptation (agent skipped) + one `/reject-event` revision loop |

Each folder contains `input.md`, `artifacts/`, `workflow-state.json`, `approval.json` and
`output/event-plan.html`.

## Secrets

None required, none committed. `.gitignore` excludes `.env*`, key files and local
Claude settings; `.env.example` is the only env file in the repo.

## Troubleshooting

- **Hook blocked your HTML write** — read the `BLOCKED [...]` message: either approval is
  missing/stale (run `/approve-event`) or the HTML contains internal names (rewrite from
  the public plan only).
- **Weather step fails** — check `node scripts/mcp_weather_probe.mjs --list`; the server
  needs Node 22+ and network access on first `npx` run.
- **`python3: command not found`** — see the Windows note above.
