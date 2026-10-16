# Budget — corporate offsite, 2027-04-23

- **Owner agent:** budget-aggregator
- **Run:** run-002-corporate-offsite
- **Revision:** 2 (regenerated after the catering revision of gate retry G1)
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` (hard ceiling 20 000 PLN all-in)
- `artifacts/02-venue.md` (4 500 PLN allocation)
- `artifacts/03-catering.md` (revision 2: 8 240 PLN)
- `artifacts/03-entertainment.md` (3 290 PLN allocation)
- `artifacts/03-logistics.md` (AV 1 015 PLN + transport 1 820 PLN)
- `artifacts/04-timeline.md` (revision 2: no dinner/grill slots)

## Summary

**Revision 2 total: 19 808.25 PLN ≤ 20 000 PLN hard ceiling (headroom 191.75 PLN).**
Revision 1 totaled **25 016.25 PLN** and failed gate G1; the targeted retry cut only the
catering line (13 200 → 8 240 PLN) and regenerated this artifact and the timeline.

## Details

### Attempt comparison

| Category | Revision 1 (attempt 1) | Revision 2 (attempt 2, final) | Change |
|----------|------------------------|-------------------------------|--------|
| Venue (room + day service) | 4 500.00 | 4 500.00 | — |
| Catering | 13 200.00 (2 coffee breaks + lunch + garden grill + dinner, 165 PLN/guest) | **8 240.00** (1 coffee break + hot working lunch, 90 PLN/guest + coffee) | −4 960.00 (targeted retry) |
| Team-building city game | 3 290.00 | 3 290.00 | — |
| AV equipment | 1 015.00 | 1 015.00 | — |
| Transport (2 coaches) | 1 820.00 | 1 820.00 | — |
| Subtotal | 23 825.00 | 18 865.00 | |
| Contingency 5 % | 1 191.25 | 943.25 | |
| **Total** | **25 016.25** | **19 808.25** | **−5 208.00** |
| Ceiling | 20 000.00 | 20 000.00 | |
| Result | **OVER by 5 016.25 → G1 FAIL** | **headroom +191.75 → G1 PASS** | |

Arithmetic (revision 2): 4 500.00 + 8 240.00 + 3 290.00 + 1 015.00 + 1 820.00 =
18 865.00; contingency 5 % = 943.25; **total 19 808.25 PLN** (247.60 PLN/guest all-in).

### Costs not carrying a number

| Item | Status | Basis / note |
|------|--------|--------------|
| Venue room + day service | budget allocation | venue publishes no prices (preliminary quote on request); allocation is the leanest day-format figure the plan allows |
| City game | budget allocation | organiser publishes per-attraction catalogue price points; allocation = lowest one (3 290 PLN); quote pending |
| Coffee break | budget allocation | 13 PLN/guest planning allocation |
| AV delivery to the venue | price on request | avoided by host-collected pickup (default) |

### Reduction plan if the venue quote exceeds the allocation

1. Move the city game to a self-organised garden game (saves up to 3 290 PLN).
2. Drop the projection screen and use the venue's TV (saves 199 PLN).
Contingency (943.25 PLN) is the first buffer before any of these.

## Costs

| Item | Unit | Qty | Unit cost | Total | Source / basis |
|------|------|-----|-----------|-------|----------------|
| Venue room + day service | day | 1 | 4 500.00 PLN | 4 500.00 PLN | allocation (quote pending) |
| Working lunch + coffee break | guest | 80 | — | 8 240.00 PLN | published package level + coffee allocation |
| Team-building city game | attraction | 1 | 3 290.00 PLN | 3 290.00 PLN | allocation at published catalogue price point |
| AV rental | day | 1 | — | 1 015.00 PLN | published rental prices |
| Coach transport | coach-hour | 7 | 260.00 PLN | 1 820.00 PLN | published Warsaw hourly rate |
| Contingency 5 % | — | — | — | 943.25 PLN | |
| **Total** | | | | **19 808.25 PLN** | |

## Sources

No external sources used (aggregated from the cost artifacts listed under Inputs used;
their sources are cited in those artifacts).

## Open issues

- Venue and city-game quotes pending (both flagged as allocations); the reduction plan
  above covers the worst-case variance within the ceiling.
