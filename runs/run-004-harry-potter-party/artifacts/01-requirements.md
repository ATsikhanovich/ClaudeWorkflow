# Confirmed event requirements — Harry Potter themed friends' reunion

- **Owner agent:** requirements-formalizer
- **Run:** run-004-harry-potter-party
- **Revision:** 2
- **Status:** final

## Inputs used

- Raw user request (verbatim): "plan event in Harry Potter style for 10 person on 23 October" (`runs/run-004-harry-potter-party/input.md`)
- Clarifying Q&A answers collected by the coordinator on 2026-10-15 (9 topics, all answered — including the new row 9 on accessibility)
- Intake note: "Harry Potter style" is a theme requirement, not a booked service line
- Workflow state: theming/props, entertainment, photography, transport and staffing are explicitly not required
- User confirmation of the requirements set on 2026-10-15 at the requirements-confirmation step
- Today's date: 2026-10-15

## Summary

This artifact fixes the requirements for a Harry Potter themed friends' reunion in
Warsaw on Friday 23 October 2026 (evening) for 10 guests, with an all-in budget of
4,000 PLN (about 400 PLN per person). Only two service lines are required: venue and
catering. The theme is not a purchased service — it must be delivered entirely through
the character of the venue plus the catering concept (themed menu and themed welcome
drink). Drinks are partly covered: the themed welcome drink and soft drinks sit inside
the budget, while any further drinks are paid by guests individually. There are no
dietary requirements and no accessibility requirements — the user confirmed "no access
needs" (no step-free access, accessible WC or mobility-aid seating is required) — and
there are no constraints beyond the budget and the date. The requirements set below was
confirmed by the user on 2026-10-15 before planning began. Downstream agents
(venue-planner, catering-planner, and the weather / logistics / timeline / budget /
synthesis chain) must plan against exactly this scope.

## Details

| Field | Confirmed value |
|-------|-----------------|
| Occasion | Friends' reunion / gathering — Harry Potter themed ("Harry Potter style" is a **theme**, not a booked service line) |
| Date(s) | Friday 2026-10-23, evening (single-day event; year confirmed as 2026) |
| City/area | Warsaw, Poland |
| Guest count | 10 (fixed as given) |
| Budget (amount + currency) | 4,000 PLN total, all-in (≈400 PLN per person) |
| Venue type (indoor/outdoor/either) | Indoor |
| Dietary requirements | None — no restrictions |
| Accessibility requirements | None — no access needs (confirmed by the user on 2026-10-15) |
| Required services (explicit list) | 1) Venue; 2) Catering. That is the complete list. |
| Entertainment wishes | None |
| Constraints (max daily hours, transport limits, noise curfew, etc.) | None stated beyond the budget (4,000 PLN all-in) and the date (Friday 2026-10-23, evening) |
| Priorities | Not stated by the user |
| Anything explicitly NOT required | Theming/props/decorations as a booked service; entertainment (music, DJ, costumed host, activities); photography; transport; staffing |

### Requirements confirmation

The user confirmed this requirements set on **2026-10-15** at the requirements-confirmation
step (including the accessibility answer "no access needs"), before planning began.

### Theme delivery mechanism (binding scope note)

The Harry Potter theme is a requirement on *content*, not a third service line. Because
theming/props/decorations and entertainment are explicitly not required, the theme must
be delivered through exactly two channels:

1. **Venue character** — the venue chosen under the "Venue" service line should itself
   carry atmosphere suitable to the theme (historic, dark-academia, candlelit,
   stone/cellar, library-like character, or similar), since no decorations are booked.
2. **Catering concept** — the "Catering" service line includes a themed menu and a
   themed welcome drink (e.g. a "butterbeer"-style welcome drink served as part of the
   catering, subject to the caterer's real offering).

This framing keeps gate G5 satisfiable: services 1 and 2 fully cover the stated
requirements, and no unbooked third service is implied.

### Drinks scope

| Drink category | Who pays | Note |
|----------------|----------|------|
| Themed welcome drink | Inside the 4,000 PLN budget | Delivered as part of the catering concept |
| Soft drinks | Inside the 4,000 PLN budget | Included for 10 guests |
| Any further drinks | Guests individually | Outside the budget; guests settle their own tabs |

### Excluded services (used by the coordinator to skip or N/A agents)

| Not required | Effect on the plan |
|--------------|--------------------|
| Theming / props / decorations (as a booked service line) | No decoration or prop line items, no theming vendor; theme via venue character + catering only |
| Entertainment (music, DJ, costumed host, activities) | entertainment-planner service work is not required |
| Photography | No photographer line item |
| Transport | No transport line item; guests arrange their own travel |
| Staffing (hired staff as a service) | No staffing line item beyond whatever is intrinsic to the venue and caterer offerings |

### Accessibility

- No access needs: no guest requires step-free access, an accessible WC, or
  mobility-aid seating.
- Confirmed by the user on 2026-10-15; this is a confirmed requirement, not an
  unresolved open question.

### Budget interpretation

- Currency: PLN (Polish zloty), as stated by the user.
- Total: 4,000 PLN **all-in** — venue + catering + themed welcome drink + soft drinks
  must fit inside this single ceiling.
- Drinks beyond the welcome drink and soft drinks are not part of this ceiling.

**Final requirements (for confirmation)**

- Occasion: friends' reunion / gathering, Harry Potter themed — "Harry Potter style" is a theme, not a booked service line.
- Theme is delivered through venue character plus the catering concept (themed menu + themed welcome drink); no theming, props or decorations are booked.
- Date: Friday 23 October 2026, evening.
- City/area: Warsaw, Poland.
- Guests: 10 people.
- Budget: 4,000 PLN total, all-in (about 400 PLN per person).
- Venue type: indoor.
- Required services: venue and catering — that is the complete list.
- Catering must include a themed menu and a themed welcome drink.
- Drinks: themed welcome drink + soft drinks are inside the budget; any further drinks are on the guests' own tabs.
- Dietary requirements: none — no restrictions.
- Accessibility requirements: none — no access needs (confirmed by the user on 2026-10-15).
- Entertainment wishes: none.
- Constraints: none stated beyond the budget and the date.
- Priorities: not stated by the user.
- Explicitly NOT required: theming/props/decorations as a service, entertainment (music, DJ, costumed host, activities), photography, transport, staffing.

## Costs

No costs in this artifact. This artifact states the 4,000 PLN all-in budget ceiling as a
requirement only; no prices, quotes or estimates are produced here.

## Sources

No external sources used (user-provided requirements).

## Open issues

- No priority ordering was stated by the user; if the venue and catering concepts
  conflict inside the 4,000 PLN ceiling, the coordinator must resolve the trade-off
  against the budget limit (gate G1) and the guest count (gate G2) rather than an
  assumed priority.
- The theme depends on finding a venue whose own character carries the atmosphere, and
  on a caterer able to deliver a themed menu and welcome drink within budget; if either
  cannot be satisfied within 4,000 PLN, this must be surfaced to the user rather than
  silently dropped.
