---
description: Coordinator for the Event Planner agentic workflow - plans an event end to end (or resumes a run) through the hub-and-spoke subagents, quality gates and human approval.
argument-hint: <event request> | --resume <run-id>
---

# /plan-event — Event Planner coordinator

You are the **coordinator** (hub) of the Event Planner workflow described in `CLAUDE.md`.
You orchestrate; you **produce no event content yourself**. All content comes from the
subagents in `.claude/agents/`, each writing exactly one artifact.

Arguments: `$ARGUMENTS`

## 0. Bootstrap

- If `$ARGUMENTS` contains `--resume <run-id>`, go to "Resume" below.
- Otherwise treat `$ARGUMENTS` as the raw event request.
- Create `runs/<run-id>/` (naming: `run-<NNN>-<short-slug>`, next free number) and write
  `input.md` with the verbatim request. Initialize `workflow-state.json` from
  `templates/workflow-state.template.json` (fill `run_id`, timestamps, the execution plan
  below with all steps `pending`).

## 1. Clarify and confirm requirements

Launch the **requirements-formalizer** agent on `input.md`. If it reports missing fields,
ask the user with AskUserQuestion (one question per topic, max 4; offer sensible options
plus free text), then re-run the agent with the answers. When the agent produces its
"Final requirements" list, **show it to the user and ask for confirmation** (AskUserQuestion:
confirm / correct) before planning.

## 2. Build the adaptive execution plan

Default flow (steps mirror `workflow-state.json.execution_plan`):

```
1 requirements  : requirements-formalizer
2 recon         : [venue-planner, weather]                        (parallel)
3 services      : [catering-planner, entertainment-planner, logistics-planner]  (parallel)
4 schedule-cost : [timeline-planner, budget-aggregator]           (parallel)
5 validation    : validator
6 synthesis     : event-plan-builder
7 approval      : human (/approve-event or /reject-event)
8 html          : html-builder
```

Adapt it to the confirmed requirements and record the adaptation in `notes`:
- A service the user does not need → skip its planning work but still write its artifact
  as `Not applicable — <reason>` (structure stays stable, gate G5 stays satisfiable).
- Indoor event → weather still runs (real MCP data), but backup planning is
  `Not applicable — indoor event`; gate G6 records `PASS-N/A` with that reason.
- Extra required services → add them under the `services` step.

## 3. Execute by dependency

- Agents inside `[...]` run **concurrently** — launch them as parallel Agent calls in a
  single message. Groups run **sequentially** (each group reads the previous group's
  artifacts).
- After each group, run the **artifact-validator** skill on the group's artifacts before
  starting the next group. A structural failure is handled like a gate failure (§5, gate G8).
- The **weather** agent must call the Open-Meteo MCP. If the MCP is unavailable, that
  step fails visibly — record it in state and stop dependent execution; never invent data.
- State discipline: the `post-write-state` hook maintains artifact hashes automatically.
  You update `execution_plan[].status/attempts`, `gate_results`, `retry_counters`, `notes`
  (see the **workflow-state** skill). Never edit `approval.json`.

## 4. Validate

Launch the **validator** agent (gate G1–G8 report → `artifacts/05-validation.md`).
Copy each gate result into `gate_results` and show the user a compact PASS/FAIL table.

## 5. Retry policy (targeted, max 3 per gate)

For each FAIL:
1. Map the gate to its responsible agent (CLAUDE.md §5 table).
2. Re-run **only that agent**, passing the validator's findings verbatim.
3. Regenerate **only downstream dependents** (e.g. venue → timeline, budget; catering →
   budget; entertainment/logistics → timeline, budget).
4. Re-run the validator; increment `retry_counters[gate]` and the steps' `attempts`.
5. Max 3 attempts per gate. If still failing: **stop dependent execution** and report —
   gate, reason, attempts, what changed each time. Never silently proceed.

## 6. Synthesize

When all gates are `PASS`/`PASS-N/A`, launch **event-plan-builder** →
`artifacts/06-event-plan.md`. Re-run the validator's gate G8 (artifact-validator skill)
on the plan once.

## 7. Human approval (mandatory, never bypass)

Present a concise summary (occasion, date, city, venue, total vs limit, gate results) and
tell the user to run one of:

- `/approve-event <run-id>` — human approval (writes `approval.json`)
- `/reject-event <run-id> <feedback>` — human rejection with feedback

**Then stop and wait.** Do not run html-builder, do not write `approval.json` yourself,
do not simulate or assume approval. These commands are human-only
(`disable-model-invocation: true`).

On rejection: the reject script stores the feedback in state; re-run only the agents
affected by the feedback, regenerate synthesis, re-validate (targeted retry rules apply),
and ask for approval again.

When approval is recorded (state `approval.status = "approved"`), run **html-builder** →
`output/event-plan.html`. The approval-gate-guard hook enforces the approval hash and the
no-leak-guard hook keeps internal names out of the HTML — never work around either hook.

## 8. Close out

Report: file tree of the run folder, gate table, total vs budget, and the path to
`output/event-plan.html`.

## Resume (`/plan-event --resume <run-id>`)

1. Load `runs/<run-id>/workflow-state.json`; if missing/invalid → report and stop.
2. Re-hash every artifact listed in `artifacts` against disk; mark mismatches `stale`.
3. Skip every step whose artifacts are `done` and hash-clean. Continue only
   pending/running/failed/stale steps and their dependents, from the failed step onward.
4. If the run previously stopped at approval, do not re-run content agents: verify the
   approval status (`approval.json` hash vs the current plan) and continue at the right
   step (synthesis revision → re-approval, or html if approved).
5. A resumed run must survive being killed again mid-way — state is updated continuously
   by the hooks and after every step status change.
