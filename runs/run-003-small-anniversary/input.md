# Input

- **Run:** run-003-small-anniversary
- **Received:** 2026-10-10
- **Invocation:** `/plan-event Plan a small wedding-anniversary dinner for 12 family members in Warsaw on 2026-12-05, restaurant-style with a private room, budget 5000 PLN, two vegetarian guests, no entertainment.`

## Raw request

> Plan a small wedding-anniversary dinner for 12 family members in Warsaw on
> 2026-12-05, restaurant-style with a private room, budget 5000 PLN, two vegetarian
> guests, no entertainment.

## Clarifying Q&A (coordinator → user, recorded 2026-10-10)

| Question | Answer |
|----------|--------|
| Which anniversary and tone? | 25th wedding anniversary — warm, classic, family dinner |
| Dinner hours? | Evening: guests arrive ~19:00, dinner 19:30, end by 23:00 |
| Restaurant style? | Traditional/classic cuisine preferred; private room on the Old Town is ideal |
| Meal format? | Three-course plated dinner from the restaurant menu |
| Drinks? | Welcome toast + wine with dinner |
| Entertainment? | **None** — conversation and family toasts only (explicitly excluded) |
| Cake? | Not needed — desserts from the menu instead |
| Dietary needs? | Two vegetarian guests |
| Accessibility requirements? | None declared at this point |

**Final requirements (confirmed by the user on 2026-10-10):** 25th wedding anniversary ·
12 guests · Warsaw Old Town preferred · 2026-12-05 (Saturday) evening · budget limit
5 000 PLN · restaurant with private room · three-course plated dinner · 2 vegetarian
guests · welcome toast + wine · **no entertainment** · no cake (menu desserts) ·
no photographer.

## Human review round 1 (recorded later in this run)

`/reject-event run-003-small-anniversary` feedback (see `workflow-state.json`):
*“Please add accessibility information — one guest uses a walking aid (step-free access,
seating with a wide aisle) — and move guest arrival 30 minutes earlier so dinner can
start on time.”*
