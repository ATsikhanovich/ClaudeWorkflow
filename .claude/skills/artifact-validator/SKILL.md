---
name: artifact-validator
description: Reusable structural + citation check for workflow artifacts. Use after each artifact group finishes and before the next group starts, and whenever quality gate G8 (artifact structure) is evaluated. Reports PASS/FAIL per check with findings and the responsible agent.
---

# artifact-validator

Validate one or more workflow artifacts (Markdown) against the fixed skeleton and
the citation rules. This skill is **read-only**: it never edits artifacts, it only
reports findings so the coordinator can map failures to agents.

## What to check

Run every check below against each artifact file. Report each check as
`PASS` or `FAIL` with concrete findings (quote the offending lines).

### Structure (backs gate G8)

1. The file starts with a single `# ` title line.
2. `- **Owner agent:** <agent>` is present and matches the artifact ownership table
   in `CLAUDE.md` (artifact filename ↔ agent name).
3. Sections exist, in this order, each as `## `:
   `Inputs used`, `Summary`, `Details`, `Costs`, `Sources`, `Open issues`.
4. `## Costs` is either a table (`| Item | Unit | Qty | Unit cost | Total | Source / basis |`)
   or the exact sentence `No costs in this artifact.`
5. `## Open issues` contains at least one bullet, or `None.`
6. `## Sources` contains at least one bullet **unless** the artifact is explicitly
   marked `Not applicable` (then it must state the reason).

### Citations (backs gates G7 and G3)

7. Every source bullet has the shape
   `- <Page title> — <URL> (fetched YYYY-MM-DD; supports: <claims>)`.
8. URLs are real pages: `https://` or `http://`, no placeholders
   (`example.com`, `localhost`, `TODO`, `...`), no invented patterns.
9. Every named venue, caterer, provider, price or weather figure in `Details`/`Costs`
   traces to a claim in a `Sources` bullet. A recommendation without a source is a FAIL.
10. Prices must come from a source or be marked `price on request` with the estimate
    basis stated. Unmarked, unsourced prices are a FAIL.

### Ownership and safety

11. The artifact does not claim work owned by another agent (e.g. a venue artifact
    containing a full timeline).
12. Nothing in the artifact asks anyone to write `output/event-plan.html` or
    `approval.json` — those are forbidden outside html-builder / /approve-event.

## How to report

Produce a compact report, one line per check:

```
<artifact> C1 PASS ... C12 PASS
<artifact> C9 FAIL — "Koneser Hall" has no source citation → responsible: venue-planner
```

End with `OVERALL: PASS` or `OVERALL: FAIL — <responsible agents>`.
On FAIL, the coordinator applies the retry policy (see CLAUDE.md §6): re-run only the
responsible agent with these findings, regenerate downstream dependents, re-validate.
