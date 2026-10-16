# Validation — run-002-corporate-offsite

- **Owner agent:** validator
- **Run:** run-002-corporate-offsite
- **Revision:** 2 (re-validation after the targeted retry of gate G1)
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` … `04-budget.md` (all artifacts of the run)
- artifact-validator skill (structural + citation checks, gate G8)
- WebFetch verification of every cited URL (gate G7), performed 2026-10-10

## Summary

**Attempt 1: G1 FAIL** — the all-day catering package (13 200 PLN) drove the total to
25 016.25 PLN against the 20 000 PLN hard ceiling. The coordinator mapped the failure to
**catering-planner** (the cost owner driving the overrun), re-ran only that agent with
these findings, regenerated the downstream **timeline** and **budget** artifacts and
re-validated. **Attempt 2: all gates PASS** (G6 PASS with a concrete indoor backup).

## Details

### G1 — Budget total ≤ user limit
**Attempt 1: FAIL.** Total 25 016.25 PLN vs. ceiling 20 000 PLN (over by 5 016.25 PLN).
Finding: catering at 13 200 PLN (80 × 165 PLN, all-day package incl. grill and dinner)
consumed 66 % of the ceiling. Responsible agent: **catering-planner**. Minimal change:
cut the grill/dinner blocks to the confirmed lean service level.
**Attempt 2: PASS.** Catering revised to 8 240 PLN (working lunch + one coffee break);
regenerated totals: 18 865.00 + 943.25 = **19 808.25 PLN ≤ 20 000 PLN** (headroom
191.75 PLN). Verified arithmetic in `04-budget.md` revision 2. Retry counter G1: 1 of 3.

### G2 — Venue capacity ≥ guest count
**PASS.** Venue hosts up to 400; 80 ≤ 400.

### G3 — Dietary/accessibility requirements covered
**PASS.** Vegetarian main dish and labelled gluten-free options are confirmed through the
venue's in-house kitchen (diets arranged with the same event team); both are named in the
catering artifact and the lunch slot of the timeline. No accessibility requirements were
declared.

### G4 — No double-booked or overlapping items in the timeline
**PASS.** Revision 2 checked end-to-end (07:45–17:30): every row occupies a distinct
interval; 15-minute buffers between workshop/lunch/game blocks.

### G5 — Every required service is covered by an artifact
**PASS.** venue → `02-venue`; catering → `03-catering`; team-building →
`03-entertainment`; AV + transport → `03-logistics`.

### G6 — Date/weather consistency (outdoor plans have a backup)
**PASS.** The venue commits to a parallel under-roof variant for outdoor events
(indoor fallback = orangery/rooms) and the activity has a documented indoor variant with
a decision rule (rain or feels-like < +8 °C) that does not change the schedule.

### G7 — Every recommendation links to a real source page
**PASS.** All 8 distinct URLs were fetched on 2026-10-10 (HTTP 200):
1. https://www.villafoksal.pl/eventy-villa-foksal/ — venue, catering model, indoor backup ✓
2. https://www.archehotelkrakowska.pl/imprezy-okolicznosciowe/o-przyjeciach — fallback venue ✓
3. https://cenauslug.pl/gastronomia-catering-i-eventy/catering-grillowy-pakiet-wegetarianski-sery-i-warzywa — catering baselines ✓
4. https://weselewstolicy.pl/catering-weselny-w-warszawie-jak-wybrac-firme-co-podac-i-ile-to-kosztuje-w-2026/ — catering market level ✓
5. https://integracyjne.pl/warszawa — team-building organiser, price points, terms ✓
6. https://wynajemsprzetu.waw.pl/cennik/wypozyczalnia-sprzetu-eventowego-cennik-2/ — AV prices ✓
7. https://cenauslug.pl/transport-i-logistyka/wynajem-busa-z-kierowca-stawka-godzinowa — transport rates ✓
8. https://open-meteo.com/en/docs + https://github.com/cmer81/open-meteo-mcp — weather ✓

### G8 — Artifact structure complete
**PASS.** artifact-validator checks C1–C12 run on all artifacts (revision 2 set):
structure complete, every recommendation traced to a fetched source, allocations clearly
labelled as such (venue, city game, coffee break) with their basis stated.

## Costs

No costs in this artifact.

## Sources

No external sources used (validation report; the verified URLs are listed under G7).

## Open issues

- Venue and city-game quotes pending (allocations flagged in the budget artifact); if the
  venue quote exceeds the allocation, the documented reduction plan keeps the ceiling.
