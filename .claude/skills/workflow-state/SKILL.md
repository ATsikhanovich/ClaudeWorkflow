---
name: workflow-state
description: Conventions for reading and updating runs/<run-id>/workflow-state.json. Use whenever the coordinator starts, resumes, retries or finishes workflow steps, and when the approval scripts record approval or rejection.
---

# workflow-state

`workflow-state.json` is the single source of truth for a run's execution. Schema:
`templates/workflow-state.template.json`. It is updated by the `post-write-state` hook on
every artifact write and by `scripts/approve_event.py` / `scripts/reject_event.py`.
Agents must not edit it by hand.

## Keys

| Key | Meaning |
|-----|---------|
| `run_id` | must equal the run folder name (`runs/<run-id>`) |
| `requirements_hash` | SHA-256 of `artifacts/01-requirements.md` (set when it is written) |
| `execution_plan` | ordered steps: `step`, `name`, `agents`, `depends_on`, `status` (pending/running/done/failed), `attempts` |
| `artifacts` | map of run-relative path → `{owner, status, sha256, updated_at}` |
| `gate_results` | map `G1..G8` → `{status: PASS/FAIL/PASS-N/A, attempts, findings, responsible_agent}` |
| `retry_counters` | map `G1..G8` → number of retry rounds already consumed |
| `approval` | `{status: pending/approved/rejected, approved_at, plan_sha256, rejected_count, feedback[]}` |
| `notes` | append-only free-form log (decisions, skipped agents + reasons) |

## Update rules

1. **Hashes are SHA-256 of file bytes** (hex, lowercase). When a step is skipped because
   its artifact is `done` and the on-disk hash matches, record nothing new.
2. **Status transitions**: `pending → running → done|failed`. A targeted retry re-runs
   only the responsible agent's step and its downstream dependents; bump that step's
   `attempts` and `retry_counters[gate]`.
3. **Skipped agents** are recorded in `notes` (e.g.
   `"entertainment-planner skipped: no entertainment required"`) and their artifact is
   still written as `Not applicable — <reason>`.
4. **Gate outcomes** are recorded per gate with findings and `responsible_agent`; a gate
   with `status: FAIL` and `attempts: 3` **stops dependent execution** — mark downstream
   steps `failed` and end the run with a clear report.
5. **Approval**: only `scripts/approve_event.py` may set `approval.status = "approved"`
   and `approval.plan_sha256`. `scripts/reject_event.py` appends to `approval.feedback`
   and increments `rejected_count`. A revision of `06-event-plan.md` invalidates
   `plan_sha256` for the guard even if the field is stale.
6. Writes are atomic (temp file + rename). Keep `updated_at` in UTC ISO-8601 (`...Z`).

## Resume contract (`/plan-event --resume <run-id>`)

1. Load state; if `workflow-state.json` is missing or invalid → stop with an error.
2. Re-hash every path in `artifacts` on disk; a mismatch marks that artifact `stale`.
3. Execute only steps with `status` in `pending/running/failed`, plus any step whose
   artifact is `stale` (and their downstream dependents).
4. Never repeat steps whose artifacts are `done` with matching hashes.
5. On completion of each artifact the hook updates state automatically — the coordinator
   only updates `execution_plan`, `gate_results`, `retry_counters` and `notes`.
