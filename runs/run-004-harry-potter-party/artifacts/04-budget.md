# Budget aggregation — Harry Potter themed friends' reunion, Warsaw, Fri 2026-10-23

- **Owner agent:** budget-aggregator
- **Run:** run-004-harry-potter-party
- **Revision:** 1
- **Status:** draft

## Inputs used

- `runs/run-004-harry-potter-party/artifacts/01-requirements.md` (rev 2, final) — budget limit **4,000 PLN all-in**, 10 guests (≈400 PLN/person), currency PLN; required services = venue + catering only; entertainment, photography, transport, theming and staffing explicitly NOT required; themed welcome drink + soft drinks inside the budget, further drinks on guests' own tabs.
- `runs/run-004-harry-potter-party/artifacts/02-venue.md` (rev 1, final) — recommended venue The Alchemist Grill & Cocktail, ul. Grzybowska 5a, Sala VIP private room; **no prices published** (hire fee assumed 0 PLN, minimum spend estimated 1,200–1,500 PLN); explicit instruction not to add hire fee and minimum spend as two additive costs over the same restaurant bill.
- `runs/run-004-harry-potter-party/artifacts/02-weather.md` (rev 2, final) — indoor event; gate G6 PASS-N/A; **no costs**.
- `runs/run-004-harry-potter-party/artifacts/03-catering.md` (rev 1, final) — the venue's own kitchen/bar delivers catering; **catering line = the single restaurant bill = 1,850–2,200 PLN (planning figure 2,000 PLN)**; explicit double-counting rule that the minimum spend is a floor on this line, not an additive venue cost.
- `runs/run-004-harry-potter-party/artifacts/03-entertainment.md` (rev 1, final) — not applicable; **no costs**.
- `runs/run-004-harry-potter-party/artifacts/03-logistics.md` (rev 1, final) — not applicable (decorations, equipment, transport, permits, hired staffing all excluded); **no costs**.
- `runs/run-004-harry-potter-party/input.md` — raw request + clarifying Q&A (budget 4,000 PLN; only Venue + Catering selected).
- Today's date: 2026-10-15.
- Not read: `artifacts/04-timeline.md` — it does not exist yet (the timeline-planner runs in parallel with this agent) and no timing/overtime cost appears in any of the artifacts above. See Open issues.

## Summary

Aggregating the cost tables of the two in-scope service artifacts and the two excluded-service artifacts, the event's numeric total is **1,850–2,200 PLN** (planning figure 2,000 PLN), against the confirmed 4,000 PLN all-in limit. **Gate G1 is PASS**: the total is within the limit with headroom of 1,800–2,150 PLN even before contingency, and 1,580–2,057 PLN once the contingency proposed below is included. The single largest cost is the **catering line**, which is the one restaurant bill: because the venue's own kitchen does the catering, its possible hire fee (assumed 0 PLN) is the venue line and the estimated 1,200–1,500 PLN minimum spend is a **floor on the catering line, not an additive venue cost** — entering both would double count the same invoice. Entertainment and logistics including hired staffing are genuinely **0 PLN / not applicable** (confirmed excluded), so they are shown explicitly rather than dropped. The decisive caveat: the recommended venue **publishes no prices at all** and issues an individual written offer per enquiry, so essentially every figure here is a `price on request` estimate built on comparable published Warsaw prices; the whole budget must be replaced by the venue's written offer before anything is booked.

## Details

### 1. Category breakdown

| Category | Low (PLN) | High (PLN) | Planning figure (PLN) | Type | Basis |
|---|---:|---:|---:|---|---|
| Venue (hire fee only) | 0 | 0 | 0 | **Estimate / assumption** | No hire fee published by the venue (`02-venue.md`); planning assumption 0 PLN, to be confirmed. `price on request` |
| Catering (single restaurant bill: themed menu + welcome drink + soft drinks) | 1,850 | 2,200 | 2,000 | **Estimate** | `03-catering.md` Option A; all components `price on request`, built on published Warsaw comparators |
| Entertainment | 0 | 0 | 0 | **Not applicable** | Confirmed excluded (`01-requirements.md`, `03-entertainment.md`); not researched, not booked |
| Logistics (decor, equipment, transport, permits) | 0 | 0 | 0 | **Not applicable** | Confirmed excluded (`01-requirements.md`, `03-logistics.md`); nothing procured |
| Staffing (hired staff as a service) | 0 | 0 | 0 | **Not applicable** | Confirmed excluded (`01-requirements.md`, `03-logistics.md`); service is intrinsic to the venue/caterer |
| **Subtotal (all numeric items)** | **1,850** | **2,200** | **2,000** | — | Sum of the rows above |
| Contingency — 5–10% (**my own proposal, not a sourced cost**) | 93 | 220 | — | **Proposal** | See §7; not present in any upstream artifact |
| **Total including contingency** | **1,943** | **2,420** | — | — | Subtotal + contingency |
| **Limit (confirmed user budget)** | — | — | **4,000** | **Confirmed** | `01-requirements.md` rev 2 |
| **Headroom (excluding contingency)** | **2,150** | **1,800** | — | — | 4,000 − 2,200 = 1,800 (high); 4,000 − 1,850 = 2,150 (low) |
| **Headroom (including contingency)** | **2,057** | **1,580** | — | — | 4,000 − 2,420 = 1,580 (high); 4,000 − 1,943 = 2,057 (low) |

**G1 verdict: PASS.** The numeric total (1,850–2,200 PLN, up to 2,420 PLN with contingency) is **≤ 4,000 PLN** in every case. No overage, no reductions required.

### 2. Arithmetic (per-category subtotals, then total)

Per-person view: the limit is 4,000 PLN ÷ 10 = 400 PLN/person.

- **Venue line.** Hire fee only: 0 PLN (assumption; `price on request`).
  `0 PLN`
- **Catering line.** `03-catering.md` Option A = themed set menu 1,300–1,500 + welcome "potion" drink 350–450 + soft drinks 200–250:
  `1,300 + 350 + 200 = 1,850` (low)
  `1,500 + 450 + 250 = 2,200` (high)
  `1,850–2,200 PLN` → per person `185–220 PLN`.
- **Entertainment.** `0 PLN` (not applicable).
- **Logistics.** `0 PLN` (not applicable).
- **Staffing.** `0 PLN` (not applicable).
- **Subtotal.**
  `0 (venue) + 1,850…2,200 (catering) + 0 + 0 + 0 = 1,850–2,200 PLN`
- **Contingency (my proposal, §7).**
  `5% × 1,850 = 92.50 ≈ 93 PLN`; `10% × 2,200 = 220 PLN`
- **Total including contingency.**
  `1,850 + 93 = 1,943 PLN` (low); `2,200 + 220 = 2,420 PLN` (high)
- **Comparison with the limit.**
  `4,000 − 2,200 = 1,800 PLN` headroom (high case, no contingency)
  `4,000 − 2,420 = 1,580 PLN` headroom (high case, with 10% contingency)
  → `PASS` (≤ limit). Even the top of the range sits 1,580 PLN below the ceiling.

### 3. The non-double-count rule (why the venue line is 0 PLN, not 1,200–1,500 PLN)

The user chose on 2026-10-15 to let the **venue's own kitchen and bar** deliver the catering (no shortlisted themed Warsaw venue publishes permission for an outside caterer). There is therefore **one restaurant bill**, not a hire fee plus a separate external caterer:

- The **venue line carries only the hire fee** — none published, so assumed **0 PLN** (`price on request`).
- The **catering line carries the actual food-and-drink bill** (1,850–2,200 PLN), which must itself be **at or above any compulsory minimum spend**.
- The estimated **1,200–1,500 PLN minimum spend** in `02-venue.md` is therefore a **FLOOR on the catering line, not an additive venue cost.** The recommended catering line (1,850–2,200 PLN) already exceeds that floor, so **nothing is added to the venue line for it.**
- Adding the minimum spend and the catering bill as two separate lines would **double count the same invoice** and is explicitly forbidden by `03-catering.md` §2.
- If the venue's confirmed minimum spend later turns out **higher** than the food and drink ordered, the shortfall is charged by the venue and belongs to the **catering line** (the bill is lifted to the minimum). The venue line still carries only the hire fee. This case is quantified under §8 (risk).

### 4. Low and high case (where the total sits)

| Case | Catering line | Contingency | Total | Per person | vs 4,000 PLN |
|---|---:|---:|---:|---:|---|
| **Low case** (catering at the bottom of its estimate, contingency 5%) | 1,850 | 93 | **1,943** | ≈194 | PASS (−2,057) |
| **Planning figure** (catering at 2,000, no contingency) | 2,000 | — | **2,000** | 200 | PASS (−2,000) |
| **High case** (catering at the top of its estimate, contingency 10%) | 2,200 | 220 | **2,420** | ≈242 | PASS (−1,580) |

Whole plausible range of the total: **≈1,850 PLN (no contingency) to ≈2,420 PLN (with contingency)** — 46–61% of the 4,000 PLN ceiling. The gap between low and high is driven almost entirely by the catering line, which is itself an estimate (see §6).

### 5. Excluded services, shown honestly (not silently dropped)

| Service | Status | Reason |
|---|---|---|
| Entertainment (music, DJ, costumed host, activities, photography) | **0 PLN — not applicable** | Confirmed excluded in `01-requirements.md`; `03-entertainment.md` records "not applicable — no entertainment required". Nothing researched or booked. |
| Logistics (decorations/props/theming, equipment, transport, permits) | **0 PLN — not applicable** | Confirmed excluded in `01-requirements.md`; `03-logistics.md` records "not applicable". The venue supplies its own furnished room, tableware and setup. |
| Staffing (hired staff as a service) | **0 PLN — not applicable** | Confirmed excluded; `03-logistics.md` records no hired staff — food, drink and table service are intrinsic to the venue's normal dinner operation. |

These three are kept as visible 0 PLN lines so a reader (and gate G5) can see they were considered and consciously excluded, not forgotten.

### 6. Estimate quality — what is estimated vs published/confirmed

**Nothing in this budget is a published or confirmed price from the recommended venue.** The venue publishes no prices at all — no hire fee, no minimum spend, no menu prices — and answers each enquiry with an individually prepared offer (`02-venue.md`, `03-catering.md`).

| Figure | Quality | Where it comes from |
|---|---|---|
| Budget limit 4,000 PLN | **Confirmed (user)** | `01-requirements.md` rev 2 |
| Venue hire fee 0 PLN | **Assumption** (`price on request`) | No hire fee published; planning assumption only |
| Catering 1,850–2,200 PLN | **Estimate** (`price on request`) | Three sub-estimates built on published Warsaw comparators (see below) |
| Entertainment / logistics / staffing 0 PLN | **Not applicable (confirmed scope)** | `01-requirements.md` exclusions |
| Contingency 93–220 PLN | **My own proposal** | Not sourced; see §7 |

The catering estimate's comparator basis (carried from `03-catering.md`): a comparable Warsaw Old Town restaurant's published à la carte prices (starters 43–92, mains 53–210, desserts 39–59 PLN), a published Warsaw group-catering rate "od 136 zł netto / os.", and published Warsaw café-bar cocktail (30–35 PLN), alcohol-free cocktail (27–30 PLN) and soft-drink (10–22 PLN) prices. These are **other venues' published prices, not the recommended venue's prices**.

**Consequence:** the whole budget must be replaced by the venue's **written offer** before anything is booked. Until that offer exists, no figure here is bankable.

### 7. Contingency (explicitly my own proposal — not a sourced cost)

No upstream artifact contains a contingency line. The 5–10% band is **my own proposal**, offered because every figure in this budget is a `price on request` estimate and the venue may add terms it has not published (deposit, minimum-spend sizing, service charges, bar-service surcharge). I am not attributing this percentage to any source.

- What it covers: the risk that the venue's confirmed offer lands **above** the low end of the catering estimate; an unexpected **deposit or private-room condition**; a possible **dedicated bar-service surcharge**; and rounding on the estimate range.
- Arithmetic: `5% × 1,850 = 92.50 ≈ 93 PLN` (low); `10% × 2,200 = 220 PLN` (high). Added to the subtotal: `1,850 + 93 = 1,943 PLN` … `2,200 + 220 = 2,420 PLN`.
- Even at the top (2,420 PLN), the total stays 1,580 PLN inside the limit — the contingency is **affordable within the ceiling** and does not by itself create a G1 risk.
- Because the venue publishes nothing, a contingency sized at 5–10% is a **minimum**, not a maximum: it covers estimate slop, not a minimum spend sized for a 40-seat room (that risk is quantified separately in §8).

### 8. The single largest risk: minimum spend sized for a 40-seat room

The private **Sala VIP seats 40** for a party of **10**. The venue may therefore apply a compulsory minimum spend sized for the **larger room**, which is the most plausible way this budget breaks. It is a real risk but a **bounded** one here: because the limit is 4,000 PLN and the projected total is 1,850–2,420 PLN, the venue could impose a minimum spend of up to roughly **3,900 PLN of food and drink** and the plan would still pass G1 (the minimum spend is a floor on the catering line, §3).

Illustrative (arithmetic, not a quote):
- If the confirmed minimum spend is **≤ 2,200 PLN** → absorbed entirely inside the catering line; total unchanged; **PASS**.
- If the confirmed minimum spend is, say, **3,000 PLN** → the catering line is lifted to 3,000 PLN; total ≈ 3,000 + contingency ≈ **3,000–3,300 PLN**; still **PASS**, but the food order must be increased to reach the floor (more/different dishes, or a second potion round).
- If the venue demands a minimum spend **above ≈4,000 PLN** → **G1 fails** and the coordinator must surface the choice to the user (raise the budget, change room, or change venue) — it must not be absorbed silently.

**G1 verdict for the current estimate: PASS.** The failure in this scenario is conditional on the venue's unpublished minimum spend, which cannot be known until its written offer arrives.

### 9. Reductions (not required — G1 is PASS)

Because the total is within the limit, **no reductions are required**. The ranked, already-costed fallbacks exist in the inputs should the venue's offer ever push the plan over; they are recorded here so the reserve is visible, not applied:

1. Switch to **catering Option B (lean two-stage plated)** — `03-catering.md` costs it at **1,550–1,650 PLN**, i.e. ≈**200–550 PLN** below Option A; new total ≈**1,550–1,650 PLN** (still PASS).
2. Switch to **catering Option D (standing cocktail reception)** — **1,300–1,600 PLN**; new total ≈**1,300–1,600 PLN** — but this under-delivers the themed *menu* the requirements ask for, so it is a last resort.
3. Drop the **optional fourth course (żurek)** if it were ever added — saves **400–450 PLN**. It is already excluded from the recommended plan.
None of these is needed today.

### 10. Price-on-request items (listed separately from the numeric total, with their basis)

These carry no number and are **not** in the total above.

| Item | Status | Estimate basis |
|---|---|---|
| Venue hire fee — The Alchemist, Sala VIP | `price on request` | No fee published (`02-venue.md`); planning assumption 0 PLN |
| Compulsory minimum spend | `price on request` (estimated 1,200–1,500 PLN) | No cennik published; comparable Warsaw Old Town à la carte implies ≈120–160 PLN/pp. **A floor on the catering line — NOT additive** (§3) |
| Deposit / cancellation terms | `price on request` | Not published (`02-venue.md`, `03-catering.md`) |
| Dedicated bar service ("obsługa barmańska") in the private room | `price on request` | Quoted individually by Warsaw venues; not required by the confirmed scope; not in Option A |
| Optional 4th course — żurek z borowikami | `price on request` (est. 400–450 PLN) | Published soups 43–49 PLN at a comparable Warsaw venue; **excluded** from the recommended plan |

## Costs

| Item | Unit | Qty | Unit cost | Total | Source / basis |
|------|------|-----|-----------|-------|----------------|
| Venue hire fee — The Alchemist, Sala VIP | event | 1 | 0 PLN (assumption) | 0 PLN | `02-venue.md` — `price on request`; no fee published |
| Compulsory minimum spend (floor on catering, **not additive**) | event | 0 | — | 0 PLN | `02-venue.md` / `03-catering.md` §2 — absorbed inside the catering line; adding it again would double count |
| Catering — themed set menu (3 family-style stages) | person | 10 | 130–150 PLN | 1,300–1,500 PLN | `03-catering.md` — `price on request`; comparators |
| Catering — themed welcome "potion" drink | person | 10 | 35–45 PLN | 350–450 PLN | `03-catering.md` — `price on request`; comparators |
| Catering — soft drinks for the table | person | 10 | 20–25 PLN | 200–250 PLN | `03-catering.md` — `price on request`; comparators |
| **Catering line total (single restaurant bill)** | event | 1 | — | **1,850–2,200 PLN** | Sum of the three catering rows above |
| Entertainment | — | — | — | 0 PLN | `03-entertainment.md` — not applicable |
| Logistics | — | — | — | 0 PLN | `03-logistics.md` — not applicable |
| Staffing | — | — | — | 0 PLN | `03-logistics.md` — not applicable |
| **Subtotal** | — | — | — | **1,850–2,200 PLN** | Venue + catering + excluded services |
| Contingency (5–10%) — **my proposal, not sourced** | event | 1 | 93–220 PLN | 93–220 PLN | My own proposal; covers estimate slop and unpublished venue terms |
| **Total (including contingency)** | — | — | — | **1,943–2,420 PLN** | Subtotal + contingency |
| **vs limit 4,000 PLN** | — | — | — | **PASS (−1,580 to −2,150 PLN)** | `01-requirements.md` budget limit |

Figures are only those already present in the input artifacts; no new prices were researched and no amounts invented. Items with no published price remain `price on request` and are listed separately in §10.

## Sources

No external sources used (aggregated from the cost artifacts listed under Inputs used).

- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/01-requirements.md` (read 2026-10-15; supports: 4,000 PLN all-in limit, 10 guests, required services venue + catering, excluded services)
- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/02-venue.md` (read 2026-10-15; supports: venue hire fee assumed 0 PLN, minimum spend estimated 1,200–1,500 PLN, non-double-count instruction)
- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/03-catering.md` (read 2026-10-15; supports: catering line 1,850–2,200 PLN and its components; double-counting rule)
- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/03-entertainment.md` (read 2026-10-15; supports: entertainment not applicable, 0 PLN)
- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/03-logistics.md` (read 2026-10-15; supports: logistics and staffing not applicable, 0 PLN)
- Upstream artifact — `runs/run-004-harry-potter-party/artifacts/02-weather.md` (read 2026-10-15; supports: indoor event, no cost line)

No web pages were fetched by this agent, so no external URL is cited; every figure is quoted from the upstream artifacts above.

## Open issues

- **Every figure is a `price on request` estimate.** The recommended venue publishes no prices at all (no hire fee, no minimum spend, no menu prices), so the entire budget must be replaced by the venue's **written offer** before anything is booked. Gate G1 is conditional on that offer.
- **Minimum spend sized for a 40-seat private room (Sala VIP) for a party of 10** — the single largest budget risk. Bounded today (a floor up to ≈3,900 PLN of food and drink would still pass G1), but if the venue demands a spend above ≈4,000 PLN, G1 fails and the coordinator must surface the choice to the user (raise budget / change room / change venue). Must be resolved at first contact.
- **Availability for Friday 2026-10-23 is unconfirmed** at the recommended venue (8 days from today); the entire catering line is contingent on the room being confirmed.
- **No `04-timeline.md` was available** when this artifact was written (the timeline-planner runs in parallel, later in the same phase). If the timeline later introduces any overtime, extra-hour or staffing cost, this budget must be re-run and re-checked against G1 — none is expected, since staffing as a service is excluded and the venue's evening service covers the plan.
- **Contingency is my own proposal, not a sourced cost** (§7). It is 5–10% of the subtotal and is affordable inside the limit, but it is not a venue quotation.
- **Drinks beyond the welcome serve and soft drinks are outside this ceiling** by the confirmed requirements (guests' own tabs); if the venue will not run individual tabs in a private room, that is a booking constraint to confirm, not a budget line.
