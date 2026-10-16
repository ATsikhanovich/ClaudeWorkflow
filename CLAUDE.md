# Event Planner — Reliable Agentic Workflow

This repository implements a **model-driven hub-and-spoke agentic workflow** for the
Event Planner domain. A coordinator slash command plans an event (occasion, budget,
location, guests, date, services) from a user request and produces a human-readable
`output/event-plan.html` **only after explicit, deterministically verified human approval**.

> The coordinator orchestrates. It **produces no event content itself** — every piece of
> content is owned by exactly one subagent and written to exactly one artifact file.

---

## 1. Repository layout

```
.claude/
  settings.json                 # hook registration (PreToolUse + PostToolUse)
  commands/
    plan-event.md               # coordinator (hub) — /plan-event [request | --resume <run-id>]
    approve-event.md            # human-only — /approve-event <run-id>
    reject-event.md             # human-only — /reject-event <run-id> <feedback>
  agents/                       # 11 single-responsibility subagents (spokes)
  skills/
    artifact-validator/         # structural + citation check for every artifact
    event-html-theme-builder/   # HTML rendering rules + standalone template
    workflow-state/             # conventions for workflow-state.json
  hooks/
    approval_gate_guard.py      # PreToolUse: blocks output/event-plan.html until approved
    no_leak_guard.py            # PreToolUse: keeps internal names out of the HTML
    post_write_state.py         # PostToolUse: updates workflow-state.json on artifact writes
scripts/
  approve_event.py              # writes approval.json (run only via /approve-event)
  reject_event.py               # records rejection feedback in workflow-state.json
  mcp_weather_probe.mjs         # smoke-tests the Open-Meteo MCP server (no secrets)
templates/
  artifact-template.md          # skeleton every domain artifact must follow
  event-plan-template.md        # skeleton for the synthesis artifact
  workflow-state.template.json  # documented state schema
tests/hooks/                    # unit tests + fixture JSON inputs for the hooks
runs/<run-id>/                  # one folder per workflow run (input, artifacts, state, output)
.mcp.json                       # Open-Meteo MCP server registration
```

## 2. Roles

### Coordinator — `.claude/commands/plan-event.md`
Builds the execution plan from the confirmed requirements, runs the quality gates,
enforces human approval, maps gate failures to the responsible agent, and
persists/resumes `workflow-state.json`. **Produces no event content.**

### Subagents — `.claude/agents/*.md`

| Agent | Single responsibility | Owns artifact |
|-------|----------------------|---------------|
| requirements-formalizer | Turns the request + clarifying Q&A into structured requirements | `artifacts/01-requirements.md` |
| venue-planner | Finds real venues matching capacity/budget/accessibility | `artifacts/02-venue.md` |
| weather | Date/location weather outlook **via the Open-Meteo MCP** | `artifacts/02-weather.md` |
| catering-planner | Caterers/menus matching dietary needs and budget | `artifacts/03-catering.md` |
| entertainment-planner | Music/DJ/activities/photographer for the occasion | `artifacts/03-entertainment.md` |
| logistics-planner | Decorations, equipment, transport, staffing, permits | `artifacts/03-logistics.md` |
| timeline-planner | Run-of-show schedule (setup → teardown) | `artifacts/04-timeline.md` |
| budget-aggregator | Aggregates all costs into total + category breakdown | `artifacts/04-budget.md` |
| validator | Checks all artifacts against gates G1–G8 | `artifacts/05-validation.md` |
| event-plan-builder | Merges validated artifacts into one coherent plan | `artifacts/06-event-plan.md` |
| html-builder | Renders the approved plan as standalone HTML | `output/event-plan.html` |

## 3. Execution flow

```
requirements-formalizer
  → [venue-planner, weather]                        (parallel)
  → [catering-planner, entertainment-planner, logistics-planner]   (parallel)
  → [timeline-planner, budget-aggregator]           (parallel)
  → validator  (gates G1–G8; targeted retry, max 3)
  → event-plan-builder
  → HUMAN APPROVAL  (revision loop on reject)
  → html-builder
```

- Items in `[...]` run **concurrently** via parallel Agent calls; groups run **sequentially**
  because they depend on the previous group's artifacts.
- **Plan adaptation is mandatory.** The coordinator adapts the plan to the confirmed
  requirements and records the chosen plan in `workflow-state.json`:
  - skip an agent's service work when the user does not need it (e.g. no entertainment),
    but still write its artifact as `Not applicable — <reason>` so the structure stays stable;
  - skip weather-driven backup logic for indoor events, but record
    "Not applicable — indoor event" with the reason (gate G6 records PASS-N/A);
  - add agents/services when the requirements demand it.
- The coordinator asks the user (AskUserQuestion) for anything missing and **confirms the
  final requirements before planning**.

## 4. Artifact rules

Per run:

```
runs/<run-id>/
  input.md                      # the raw user request + clarifying Q&A
  workflow-state.json           # persisted execution state (see §7)
  artifacts/01-requirements.md
  artifacts/02-venue.md
  artifacts/02-weather.md
  artifacts/03-catering.md
  artifacts/03-entertainment.md
  artifacts/03-logistics.md
  artifacts/04-timeline.md
  artifacts/04-budget.md
  artifacts/05-validation.md
  artifacts/06-event-plan.md
  approval.json                 # written ONLY by /approve-event
  output/event-plan.html        # written ONLY by html-builder after approval
```

Every artifact follows `templates/artifact-template.md` exactly:

**Title → Owner agent → Inputs used → Summary → Details → Costs (if any) → Sources (real URLs) → Open issues.**

Hard content rules for every agent:
- **Cite only sources you actually fetched** (WebSearch/WebFetch, or the MCP for weather).
  Never invent URLs, prices, venues or providers. If a price is not published, say
  "price on request" and state what an estimate is based on.
- One responsibility, one output file. Never write another agent's artifact.
- Use the `artifact-validator` skill after each artifact group, before the next group starts.

## 5. Quality gates (validator, named and reported individually)

| Gate | Check | Failure maps to |
|------|-------|-----------------|
| G1 | Budget total ≤ user limit | the cost owner driving the overrun (e.g. catering-planner) + budget-aggregator |
| G2 | Venue capacity ≥ guest count | venue-planner |
| G3 | Dietary/accessibility requirements covered | catering-planner / logistics-planner |
| G4 | No double-booked or overlapping items in the timeline | timeline-planner |
| G5 | Every required service is covered by an artifact | requirements-formalizer + the missing service's agent |
| G6 | Date/weather consistency (outdoor plans have a backup) | weather + logistics-planner |
| G7 | Every recommendation links to a real source page (URLs verified with WebFetch, not just format) | the agent owning the artifact with the bad link |
| G8 | Artifact structure complete (via the artifact-validator skill) | the agent owning the malformed artifact |

## 6. Retry policy

On gate failure the coordinator:
1. maps each failed gate to the responsible agent (table above),
2. re-runs **only that agent**, passing the validator's findings,
3. regenerates **only downstream dependents** (e.g. venue change → timeline, budget),
4. re-validates.

**Max 3 attempts per gate.** If a gate is still failing after 3 attempts: stop dependent
execution and report clearly — which gate, why, how many attempts, what changed each time.
**Never silently proceed** past a failed gate.

## 7. Human approval rules

- After `event-plan-builder` finishes, the coordinator presents a concise summary and tells
  the user to run `/approve-event <run-id>` or `/reject-event <run-id> <feedback>`.
- Both commands are **human-only**: `disable-model-invocation: true` in their frontmatter.
  The model can never invoke them on its own.
- `/approve-event` runs `scripts/approve_event.py`, which writes `approval.json`
  `{run_id, plan_sha256, approved_at}`. **Only this script writes approval.json** — never
  the coordinator, never an agent.
- The PreToolUse hook `approval-gate-guard` blocks any write of `output/event-plan.html`
  unless `approval.json` exists **and** its `plan_sha256` equals the current SHA-256 of
  `artifacts/06-event-plan.md`. Any revision to the plan therefore invalidates the approval.
- `/reject-event` runs `scripts/reject_event.py`, which stores the feedback in
  `workflow-state.json`; the coordinator then re-runs only the affected agents plus the
  synthesis, re-validates, and asks for approval again.
- The coordinator never creates the HTML before the hook allows it.

## 8. Hooks (registered in `.claude/settings.json`)

| Hook | Event | Behavior | Fail-closed rule |
|------|-------|----------|------------------|
| `approval-gate-guard` | PreToolUse | Blocks Write/Edit/Bash that creates `output/event-plan.html` without a matching `approval.json` | Any ambiguity (missing state, unreadable approval, missing plan) → block |
| `no-leak-guard` | PreToolUse | Blocks writes of the user-facing HTML that contain internal artifact names/paths/state keys | Content of the HTML cannot be determined → block |
| `post-write-state` | PostToolUse | On every artifact write updates `workflow-state.json` (status, hash, timestamp, owner, current step) | Run folder without state file → error (exit 2), never silent |

Hooks are **deterministic scripts (Python 3 stdlib only, no network)** and are unit-tested
with fixture JSON inputs in `tests/hooks/` (`python3 -m unittest discover -s tests/hooks`).

## 9. State and resume

`workflow-state.json` (schema: `templates/workflow-state.template.json`) holds: `run_id`,
`requirements_hash`, `execution_plan` (per-step status pending/running/done/failed),
`artifacts` (status + sha256 + timestamp + owner), `gate_results`, `retry_counters`,
`approval` status, and free-form `notes`.

`/plan-event --resume <run-id>`:
1. reads `runs/<run-id>/workflow-state.json`,
2. re-hashes every recorded artifact on disk and compares to the stored hash,
3. skips steps whose artifacts are `done` and hashes match,
4. continues only remaining or failed steps (re-running a step whose artifact changed),
5. never repeats completed work.

This survives a killed session or restart at any point. See README "How to test resume".

## 10. Skills

- **artifact-validator** — reusable structural + citation check, run after each artifact
  group before the next group starts (also backs gate G8).
- **event-html-theme-builder** — HTML rendering rules and the predefined standalone
  template (inline CSS, no external dependencies, responsive, printable) so output
  structure is identical across runs.
- **workflow-state** — conventions for reading/updating `workflow-state.json`.

## 11. MCP and external data

- `.mcp.json` registers the **Open-Meteo MCP server** (`open-meteo-mcp-server` via `npx`,
  pinned). No API key is needed. Prerequisites: Node.js 22+.
- The **weather agent must call the MCP for real**. If the MCP is unavailable, the step
  **fails visibly** (recorded in state and in `05-validation.md`) — it never invents data.
- All other agents use WebSearch/WebFetch and cite real URLs they actually fetched.

## 12. Hard rules (all roles)

1. Never commit secrets. Never write credentials into any file in this repo.
2. Never output internal file names/paths (`workflow-state.json`, `approval.json`,
   `artifacts/*`, `runs/*`, gate internals) in the user-facing HTML — `no-leak-guard`
   enforces this.
3. Never invent URLs, prices, venues or providers.
4. Never write `output/event-plan.html` before human approval has been verified.
5. Never write `approval.json` except through `/approve-event`.
