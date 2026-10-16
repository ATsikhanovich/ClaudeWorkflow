# Logistics — not applicable

- **Owner agent:** logistics-planner
- **Run:** run-004-harry-potter-party
- **Revision:** 1
- **Status:** final

## Inputs used

- `runs/run-004-harry-potter-party/artifacts/01-requirements.md` (rev. 2, final) — required services are exactly "1) Venue; 2) Catering"; "Anything explicitly NOT required" lists "theming/props/decorations as a booked service; entertainment (music, DJ, costumed host, activities); photography; transport; staffing"
- `runs/run-004-harry-potter-party/artifacts/02-venue.md` — recommended venue The Alchemist Grill & Cocktail, ul. Grzybowska 5a, Warsaw: a restaurant with its own kitchen, own cocktail bar and a private room (Sala VIP) offered for occasion parties; no outside-catering policy published
- `runs/run-004-harry-potter-party/artifacts/02-weather.md` — event is fully indoor; evening window ~9.5–10.9 °C, sunset 17:24 on 2026-10-23
- Confirmed exclusions recorded by the coordinator: the user selected **only Venue and Catering** as services and listed theming/props/decorations, entertainment, photography, transport and staffing as not required

## Summary

**Not applicable — no decorations, equipment, transport or staffing required (confirmed in requirements).** The coordinator skipped this agent's planning work as part of plan adaptation; this artifact exists only to keep the artifact structure stable and to make gate G5 (service coverage) decidable. The user booked only two service lines — venue and catering — and explicitly excluded theming/props/decorations, entertainment, photography, transport and staffing, which leaves nothing inside this agent's remit (decorations, equipment, transport, staffing, permits) to procure. The event is a seated themed dinner for 10 in a private room of a restaurant that supplies its own furniture, tableware, service staff and kitchen, so no furniture hire, no equipment hire, no transport and no external staffing are being booked. Accordingly, no logistics suppliers, regulations or cost lines were researched and none are recommended here.

## Details

Everything below is recorded as an explicit not-applicable decision rather than dropped silently,
so the exclusion is visible to the validator and to the reader.

### Scope decision

The requirements artifact (`01-requirements.md`, rev. 2) fixes the required services as
**venue and catering only**, and its "Anything explicitly NOT required" row names
theming/props/decorations, entertainment, photography, transport and staffing. Every line
of this agent's remit therefore falls inside an explicit exclusion, and the coordinator
skipped this agent's planning work under plan adaptation. This artifact is the structural
placeholder that keeps that skip decidable.

### Decorations

**Not applicable — theming/props/decorations excluded as a booked service (confirmed in requirements).**

No decorations, props, theming kit, florals or table-scaping were researched, costed or booked.
Per the binding theme-delivery note in `01-requirements.md`, the Harry Potter theme is carried by
two non-logistics channels only: the **venue's own alchemical interior character** (The Alchemist
Grill & Cocktail, ul. Grzybowska 5a, Warsaw — chosen precisely because its own published character
is alchemical/wizard-like, with signature drinks such as "Philosopher's Stone" and "Elixir of Life")
and the **themed catering concept** (themed menu plus a themed welcome drink). Both are owned by
other agents (venue-planner, catering-planner); nothing decoration-related is procured here.

### Equipment (sound, lighting, furniture)

**Not applicable — no equipment hire of any kind (confirmed in requirements).**

- **Sound / AV:** no sound system, microphone, DJ booth or PA is hired. No entertainment is booked
  (music, DJ, costumed host and activities are all explicitly excluded), so no act has technical needs
  to serve — the third input named in this agent's definition (`03-entertainment.md`) is itself a
  "not applicable" artifact for this run.
- **Lighting:** no lighting hire. The room's own ambience is part of the venue character, which is the
  point of the venue choice.
- **Furniture:** no tables, chairs, linens or tableware are hired. The private room is offered by the
  restaurant as a furnished, seated dining space (Sala VIP, 40 seated — comfortably above the 10 guests),
  and the restaurant supplies its own tableware and service setup as part of its normal dining operation.

### Transport & parking

**Not applicable — transport excluded as a service (confirmed in requirements).**

No transport is arranged: no coach, minibus, taxi package, shuttle, chauffeur or parking reservation
is booked, and no transport line item belongs in the budget. Per `01-requirements.md`, guests arrange
their own travel, and any further drinks beyond the themed welcome drink and soft drinks are settled on
guests' own tabs — the plan carries no travel logistics. The recommended venue is central Warsaw
(ul. Grzybowska 5a) and the venue states both of its locations are central and transit-accessible with
nearby metro stations (`02-venue.md`), which is context for guests making their own way there, not a
work package.

### Staffing (who does what, setup/teardown)

**Not applicable — no hired staffing (confirmed in requirements).**

No event staff, coordinator, host/hostess, decor crew, AV technician, setup or teardown labour is hired.
Hired staffing as a service is explicitly excluded, and the requirements note there is no staffing beyond
what is intrinsic to the venue and caterer offerings. All room setup, table setting, food and drink
service and clearing are performed by the restaurant's own front-of-house and kitchen team as part of
its standard dining service; no guest has a logistics duty. Access and timings for the room are a booking
detail to be settled with the venue (an open issue in `02-venue.md`, not a logistics work package here).

### Permits & compliance (noise curfew, alcohol, public-space rules)

**Not applicable — no permits are procured by this plan (confirmed in requirements).**

No public-space, street, noise-variance, temporary-event or outdoor-assembly permit is sought or needed:
the event is entirely indoor, in a private room of an operating licensed restaurant during its normal
evening trading hours, with no outdoor structures, no amplified sound, no public-space use and no
road closure. Alcohol service is the restaurant's own licensed activity as part of its normal operation,
not a permit this plan applies for; any further drinks are settled on guests' own tabs. Where the venue's
own operating hours, licensing or private-room terms might impose a limit on the evening, that is the
venue's compliance to state in its offer — it is a question for the venue booking, not work itemised here.

The one weather-derived constraint worth recording: the event is **fully indoor**, so no weather
contingency, rain cover, heating or tentage is required — `02-weather.md` records gate G6 as **PASS-N/A**
with the backup section reading exactly `Not applicable — indoor event`. On the night itself
(2026-10-23, about 10 °C, sunset 17:24, dark and damp), guests arriving on foot may simply want a warm
coat. That is a **guest-comfort note, not a logistics work package**.

### Provided by venue vs to arrange

| Remit area | Provided by venue | To arrange by this agent |
|---|---|---|
| Furniture, tableware, room setup | Restaurant supplies its furnished private dining space, tableware and service setup as normal operation | **None** |
| Food & drink service | Restaurant kitchen and front-of-house team | **None** |
| Sound / lighting / AV | Room's own ambience only; no AV hired | **None** |
| Decorations / props / theming | Theme carried by the venue's own alchemical interior character | **None** |
| Transport & parking | — | **None** — guests arrange their own travel |
| Additional staffing | Restaurant's own staff | **None** |
| Permits & compliance | Restaurant operates under its own licence and trading hours | **None** |

Nothing is double-booked: every practical function is intrinsic to the venue, and this artifact books
nothing, so no item appears both here and in the venue or catering artifacts.

## Costs

No costs in this artifact.

## Sources

No external sources used (service explicitly excluded — nothing researched).

## Open issues

- **Not applicable — nothing is procured here, so nothing is at risk in this artifact.** The
  coordination points that could touch logistics — whether the venue handles its own room setup and
  teardown, the exact access and evening hours for the private room, and whether the venue's own
  licensing or trading hours impose any limit — were **not confirmed** and are carried as open issues in
  `02-venue.md` (availability for 2026-10-23 is unconfirmed and the venue publishes no terms). I did not
  contact the venue or research any regulation for this artifact because the service is excluded; if the
  venue's written offer later reveals a private-room condition with a logistics implication (for example
  a hard room-vacate time), that would be surfaced by the venue booking, not planned here.
- No permit is expected to be needed for a private room inside an operating restaurant, but I could not
  and did not confirm this with any authority, since no permit line is being procured. Flagged plainly
  rather than assumed away.
