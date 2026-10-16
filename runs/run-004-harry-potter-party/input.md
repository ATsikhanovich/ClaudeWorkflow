# Event request — run-004-harry-potter-party

## Raw request (verbatim)

> plan event in Harry Potter style for 10 person on 23 October

Received: 2026-10-15 (via `/plan-event`)

## Clarifying Q&A

Answers collected by the coordinator on 2026-10-15 via AskUserQuestion.

| # | Topic | Question | Answer |
|---|-------|----------|--------|
| 1 | Occasion | What is the occasion? | Friends' reunion / gathering (Harry Potter themed) |
| 2 | Location | Which city or area? | Warsaw, Poland |
| 3 | Budget | Total budget limit, everything included? | 4,000 PLN (~400 PLN/person) |
| 4 | Venue type | Indoor, outdoor, or either? | Indoor |
| 5 | Services | Which services should the plan cover? | Venue, Catering (only — no theming/props, no entertainment, no photography, no transport) |
| 6 | Dietary | What dietary requirements must the menu cover? | No restrictions |
| 7 | Date (year) | Which 23 October? | Friday 23 October 2026 |
| 8 | Drinks | How should drinks be handled? | Themed welcome drink + soft drinks included; further drinks on guests' own tabs |
| 9 | Accessibility | Do any of the 10 guests have accessibility or mobility needs? | None — no access needs. Confirmed by the user on 2026-10-15 at the requirements-confirmation step. |

The requirements set above was **confirmed by the user** on 2026-10-15 before planning began.

## Gaps identified at intake (now resolved)

The raw request did not state: occasion, city/area, budget + currency, venue type,
dietary requirements, required services, or the year. All were collected above.

## Open points for the requirements-formalizer

- "Harry Potter style" is a theme requirement, not a service line: with theming/props
  and entertainment explicitly **not** required, the theme must be delivered through
  (a) venue character and (b) the catering concept (themed menu + welcome drink).
  Record this explicitly so gate G5 stays satisfiable.
- Guest count 10 is fixed as given.
