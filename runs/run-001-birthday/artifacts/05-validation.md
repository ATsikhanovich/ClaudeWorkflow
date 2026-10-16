# Validation — run-001-birthday

- **Owner agent:** validator
- **Run:** run-001-birthday
- **Revision:** 1
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` … `04-budget.md` (all artifacts of the run)
- artifact-validator skill (structural + citation checks, gate G8)
- WebFetch verification of every cited URL (gate G7), performed 2026-10-10

## Summary

**All gates PASS** (G6 is PASS-N/A for the indoor event). One structural note: the live
music price is a labelled reservation inside a published market range, not a quote —
tracked as an open issue, not a gate failure.

## Details

### G1 — Budget total ≤ user limit
**PASS.** 5 874.20 PLN ≤ 6 000 PLN (headroom 125.80 PLN). Arithmetic verified in
`04-budget.md` against the cost artifacts.

### G2 — Venue capacity ≥ guest count
**PASS.** Venue package is published for up to 50 guests; 40 ≤ 50.

### G3 — Dietary/accessibility requirements covered
**PASS.** Vegetarian requirement: ≥60 % of food volume vegetarian (Margherita, Vege
Mania, Grecka/Serowa pizzas, salads, stuffed mushrooms), labelled at service. No
accessibility requirements were declared; the venue's step-free access is flagged as an
informational open issue.

### G4 — No double-booked or overlapping items in the timeline
**PASS.** Every run-of-show row occupies a distinct interval (14:00–00:30 checked
end-to-end); program blocks have 10–20 min buffers.

### G5 — Every required service is covered by an artifact
**PASS.** Required services: venue → `02-venue`; catering → `03-catering`; live music →
`03-entertainment`; decorations → `03-logistics`; sound equipment → venue package
(recorded in `02-venue` and `03-logistics` "provided by venue" split).

### G6 — Date/weather consistency (outdoor plans have a backup)
**PASS-N/A.** Indoor event; weather outlook recorded in `02-weather` with the explicit
reason `Not applicable — indoor event`. The weather data (5–10 °C, drizzle risk) supports
the indoor choice.

### G7 — Every recommendation links to a real source page
**PASS.** All 10 distinct URLs were fetched on 2026-10-10 (HTTP 200):
1. https://www.lofthouseclub.pl/cennik — venue packages and policies ✓
2. https://jabeerwocky.com/en/event-space — fallback venue ✓
3. https://ceny-swiat.pl/polska/ceny/warszawa/pizza — food prices ✓
4. https://cenauslug.pl/gastronomia-catering-i-eventy/catering-grillowy-pakiet-wegetarianski-sery-i-warzywa — catering market level ✓
5. https://weselewstolicy.pl/catering-weselny-w-warszawie-jak-wybrac-firme-co-podac-i-ile-to-kosztuje-w-2026/ — catering market level ✓
6. https://zleca.pl/cennik/wystep-zespolu-muzycznego-na-zywo-cena — music price range ✓
7. https://band4event.pl/ — music provider ✓
8. https://lovedecor.pl/ — decoration rental prices ✓
9. https://wynajemsprzetu.waw.pl/cennik/wypozyczalnia-sprzetu-eventowego-cennik-2/ — equipment fallback prices ✓
10. https://open-meteo.com/en/docs + https://github.com/cmer81/open-meteo-mcp — weather ✓

### G8 — Artifact structure complete
**PASS.** artifact-validator checks C1–C12 run on all 8 domain artifacts: title, owner,
Inputs used, Summary, Details, Costs, Sources, Open issues present in order; every
recommendation traced to a source; no unsourced prices (the music line is explicitly a
reservation inside a published range).

## Costs

No costs in this artifact.

## Sources

No external sources used (validation report; the verified URLs are listed under G7).

## Open issues

- Live duo quote pending (tracked in `03-entertainment` / `04-budget`) — does not block
  any gate; headroom covers the published range.
