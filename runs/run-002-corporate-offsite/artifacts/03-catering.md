# Catering — working lunch and coffee break for 80

- **Owner agent:** catering-planner
- **Run:** run-002-corporate-offsite
- **Revision:** 2 (revised after budget gate G1 failed on revision 1)
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` (80 guests, vegetarian + gluten-free, hard ceiling
  20 000 PLN, lean service level)
- `artifacts/02-venue.md` (Villa Foksal in-house kitchen; diets arranged with the same team)
- Validator findings on revision 1 (G1 FAIL: catering at 13 200 PLN drove the overrun)

## Summary

**Revised package (revision 2):** one welcome coffee break plus a hot working-lunch
buffet served by the venue's in-house kitchen — **8 240 PLN** (≈103 PLN/guest), down from
13 200 PLN. Revision 1 included a garden grill block and a dinner service priced at the
published Warsaw maximum (165 PLN/guest) and pushed the total over the hard ceiling; both
were cut in this targeted retry while vegetarian and gluten-free coverage is unchanged.

## Details

### Revision 2 menu (final)

| Block | Content | Dietary coverage |
|-------|---------|------------------|
| Welcome coffee break (08:45) | coffee, tea, water, pastries | vegetarian pastries; gluten-free option labelled |
| Working lunch (12:30) | hot buffet: two hot dishes (one vegetarian), grains, salads, bread, fruit, drinks | **vegetarian dish as a main (not a side)**; **gluten-free option labelled**; both confirmed with the venue kitchen |

Catering runs through the venue's in-house kitchen (no external caterer) — menus, service
times and diets are arranged with the same team that runs the event, which is also where
the vegetarian/gluten-free coverage is guaranteed (gate G3).

### Why revision 1 failed and what changed

| | Revision 1 | Revision 2 |
|---|-----------|-----------|
| Service | 2 coffee breaks + lunch buffet + garden grill + dinner | 1 coffee break + hot working-lunch buffet |
| Basis | Warsaw maximum of the published vegetarian grill package (165 PLN/guest) | published standard grill package level (90 PLN/guest) + coffee allocation |
| Catering total | 13 200 PLN | **8 240 PLN** |
| Effect on run total | 25 016.25 PLN → **G1 FAIL** | 19 808.25 PLN → **G1 PASS** |

Market references checked for both revisions: professional grill catering in Warsaw runs
90–165 PLN/guest (average 136 PLN), wedding-grade buffet catering 380–480 PLN/guest —
the revision-2 package sits deliberately at the bottom of the realistic event range.

## Costs

| Item | Unit | Qty | Unit cost | Total | Source / basis |
|------|------|-----|-----------|-------|----------------|
| Hot working-lunch buffet (incl. vegetarian + gluten-free options) | guest | 80 | 90.00 PLN | 7 200.00 PLN | published standard grill/buffet package level ("od 90 zł/os") |
| Welcome coffee break (coffee, tea, water, pastries) | guest | 80 | 13.00 PLN | 1 040.00 PLN | budget allocation (coffee-break allocation; not a quoted price) |
| **Catering total** | | | | **8 240.00 PLN** | ≈ 103 PLN/guest |

## Sources

- Vegetarian grill catering price level 2026 (min 90, avg 136, max 165 PLN/guest) —
  https://cenauslug.pl/gastronomia-catering-i-eventy/catering-grillowy-pakiet-wegetarianski-sery-i-warzywa
  (fetched 2026-10-10; supports: both revision baselines)
- Warsaw catering price level 2026 (380–480 PLN/guest standard) —
  https://weselewstolicy.pl/catering-weselny-w-warszawie-jak-wybrac-firme-co-podac-i-ile-to-kosztuje-w-2026/
  (fetched 2026-10-10; supports: upper market reference; in-house vs external catering trade-off)
- Villa Foksal — in-house kitchen, diet arrangements with the event team —
  https://www.villafoksal.pl/eventy-villa-foksal/ (fetched 2026-10-10; supports: service
  model and dietary coverage route)

## Open issues

- The final lunch menu and gluten-free handling (separate prep surfaces) should be
  confirmed with the venue kitchen at booking.
