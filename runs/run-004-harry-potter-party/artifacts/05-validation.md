# Quality-gate validation — Harry Potter themed friends' reunion, Warsaw, Fri 2026-10-23

- **Owner agent:** validator
- **Run:** run-004-harry-potter-party
- **Revision:** 1
- **Status:** final

## Inputs used

- `runs/run-004-harry-potter-party/input.md` — raw request + clarifying Q&A (Q1–Q9); requirements confirmed by the user on 2026-10-15
- `runs/run-004-harry-potter-party/artifacts/01-requirements.md` (rev 2, final) — confirmed requirements; required services = venue + catering only; 4,000 PLN all-in; 10 guests
- `runs/run-004-harry-potter-party/artifacts/02-venue.md` (rev 1, final)
- `runs/run-004-harry-potter-party/artifacts/02-weather.md` (rev 2, final)
- `runs/run-004-harry-potter-party/artifacts/03-catering.md` (rev 1, final)
- `runs/run-004-harry-potter-party/artifacts/03-entertainment.md` (rev 1, final)
- `runs/run-004-harry-potter-party/artifacts/03-logistics.md` (rev 1, final)
- `runs/run-004-harry-potter-party/artifacts/04-timeline.md` (rev 1, final)
- `runs/run-004-harry-potter-party/artifacts/04-budget.md` (rev 1, draft)
- `.claude/skills/artifact-validator/SKILL.md` (checks C1–C12, backing gate G8); `templates/artifact-template.md`
- Live web pages re-fetched by this validator on 2026-10-15 to verify gate G7 (35 URLs, all listed under Sources)

## Summary

All eight gates pass: **G1 PASS, G2 PASS, G3 PASS, G4 PASS, G5 PASS, G6 PASS-N/A, G7 PASS, G8 PASS** — no FAIL, no responsible agent to name. The two required services (venue, catering) are each owned by a substantive artifact; the budget total stays well inside the 4,000 PLN ceiling with no double-count of the restaurant bill; the timeline is contiguous and non-overlapping; and every web page cited by the venue, catering and weather artifacts was re-fetched and returned its claimed content. The plan's single material weakness is not a gate failure but a booking risk that the coordinator must carry: the recommended venue publishes no prices at all and issues only individual offers, so every figure is a `price on request` estimate and nothing can be booked until a written offer exists. A second, smaller risk is that the catering menu rests on comparator prices rather than the venue's own menu (which is published only as images). One accepted deviation is recorded under G7: `04-budget.md` cites upstream artifacts by path instead of web URLs, which is honest for an aggregator that fetches no pages — I agree it is not a fresh failure.

## Details

### G1 — Budget total ≤ user limit (4,000 PLN all-in)

**Verdict: PASS**

Evidence checked (`04-budget.md`): §1 category table, §2 arithmetic, §4 low/high case, and the `## Costs` table.

- Limit: `4,000 PLN all-in` (`01-requirements.md`: "Budget (amount + currency) | 4,000 PLN total, all-in (≈400 PLN per person)").
- Subtotal: `| **Subtotal (all numeric items)** | **1,850** | **2,200** | **2,000** |` — venue 0 + catering 1,850–2,200 + 0 + 0 + 0.
- With contingency: `| **Total including contingency** | **1,943** | **2,420** | — |`.
- Arithmetic re-checked: catering components `1,300 + 350 + 200 = 1,850` (low) and `1,500 + 450 + 250 = 2,200` (high); contingency `5% × 1,850 ≈ 93`, `10% × 2,200 = 220`; `4,000 − 2,420 = 1,580`. All consistent.
- Verdict line matches: `**G1 verdict: PASS.** The numeric total (1,850–2,200 PLN, up to 2,420 PLN with contingency) is **≤ 4,000 PLN** in every case.`

Double-count check (run context item 3): the artifacts do **not** double-count the restaurant bill. `04-budget.md` §3: "Adding the minimum spend and the catering bill as two separate lines would **double count the same invoice**"; the Costs table enters the minimum spend as `| Compulsory minimum spend (floor on catering, **not additive**) | event | 0 | — | 0 PLN |`. `03-catering.md` §2 agrees ("**Do not enter the venue minimum spend (1,200–1,500 PLN) and this food bill as two separate additive costs**"). No additive venue line of 1,200–1,500 PLN appears anywhere. So G1 is a genuine PASS, not a masked overrun.

No responsible agent (PASS).

### G2 — Venue capacity ≥ guest count (10)

**Verdict: PASS**

Evidence checked (`02-venue.md`): the shortlist table and the "Recommended venue" section.

- Guest count 10 (`01-requirements.md`: "Guest count | 10 (fixed as given)"), so the gate needs capacity ≥ 10.
- `**Sala VIP — 40 seated / 40–50 standing** (private room)` and "40 ≥ 10 ✔" (shortlist row for The Alchemist).
- Justification: "**Capacity ≥ guest count (gate G2).** The private Sala VIP seats 40 (40–50 standing against a party of 10); the main hall seats 80. 40 ≥ 10, so the requirement is met with a wide margin".
- Independent verification: I re-fetched `https://thealchemist.pl/imprezy.html` and it returns the venue's own numbers — "Main hall ('Sala główna'): seated — 80; standing — 100" and "VIP room ('Sala VIP'): seated — 40; standing — 40–50". The cited capacity is real.

No responsible agent (PASS).

### G3 — Dietary/accessibility requirements covered

**Verdict: PASS**

Evidence checked (`03-catering.md` §4 "Dietary coverage — every declared need, explicitly"; `03-logistics.md` "Staffing"/"Permits" sections; `01-requirements.md` accessibility section).

- The declared requirement set is empty: `01-requirements.md` — "| Dietary requirements | None — no restrictions |" and "| Accessibility requirements | None — no access needs (confirmed by the user on 2026-10-15) |".
- `03-catering.md` §4 covers the dietary line explicitly rather than silently: "**No dietary requirements** — the user confirmed 'no restrictions' for all 10 guests | Vacuous but verified: **no substitution, no alternative dish and no kitchen adaptation is required.**" It also records margins (vegetarian "wersje Vege", non-alcoholic potion serve) and flags the one real gap: "Allergens / intolerances | **Not published** by the venue anywhere (S1–S4) … the allergen list must be requested at booking".
- Accessibility is addressed and correctly allocated: `03-catering.md` §4 "Accessibility | Out of scope here (no access needs were declared; venue-side item owned by venue-planner)"; `02-venue.md` records "**Privacy**… not published … This is **not** a hard requirement here: the user confirmed 'no access needs'". `03-logistics.md` records no accessibility work package is needed because none was required.
- Because the requirement is a confirmed empty set and both artifacts explicitly record that fact (with allergen request as a safety margin), there is nothing unmet. Recorded as PASS (not PASS-N/A) because the artifacts contain positive evidence of coverage of the declared need, not an omission.

No responsible agent (PASS).

### G4 — No double-booked or overlapping items in the timeline

**Verdict: PASS**

Evidence checked (`04-timeline.md`): the run-of-show table and the "G4 — explicit no-overlap check" section.

- The nine blocks are contiguous: `17:00–18:15, 18:15–18:30, 18:30–19:00, 19:00–19:45, 19:45–21:15, 21:15–22:00, 22:00–22:30, 22:30–23:00, 23:00–23:30`.
- "Each block's end equals the next block's start; no interior or partial overlaps exist." Confirmed by inspection: 18:15=18:15, 18:30=18:30, 19:00=19:00, 19:45=19:45, 21:15=21:15, 22:00=22:00, 22:30=22:30, 23:00=23:00. No two rows share a clock time.
- Internal sums: "the three catering stages total 45 + 90 + 45 = **180 min** of dining". Confirmed (45+90+45=180).
- The one post-departure block is correctly non-overlapping with guests: "the **23:00–23:30 venue teardown** … is performed by the venue's own staff **after** the guests have left, so it does not double-book the guest group."
- No entertainment/decoration/transport blocks exist (those services are excluded), and the artifact states this explicitly ("Items deliberately NOT in the schedule").

No responsible agent (PASS).

### G5 — Every required service is covered by an artifact

**Verdict: PASS**

Evidence checked (`01-requirements.md` required-services list vs the artifact set).

- Required services: `01-requirements.md` — "| Required services (explicit list) | 1) Venue; 2) Catering. That is the complete list. |" and "Required services: venue and catering — that is the complete list."
- Venue → `02-venue.md` (venue-planner) is a real, substantive artifact: four researched candidates, one recommendation, sourced.
- Catering → `03-catering.md` (catering-planner) is a real, substantive artifact: menu concept, drinks plan, costs, sources.
- The two excluded services are covered by deliberate `Not applicable` artifacts with stated reasons, per plan adaptation: `03-entertainment.md` — "**Not applicable — no entertainment required (confirmed in requirements).**"; `03-logistics.md` — "**Not applicable — no decorations, equipment, transport or staffing required (confirmed in requirements).**" Both cite the requirements lines that justify the skip.
- Applying run context item 2, G5 is judged on whether every required service (venue, catering) is covered — it is — not on whether every conceivable service was planned.

No responsible agent (PASS).

### G6 — Date/weather consistency (outdoor plans have a backup)

**Verdict: PASS-N/A**

Reason for N/A: the event is fully indoor, so no weather-driven backup is required. `01-requirements.md` — "| Venue type (indoor/outdoor/either) | Indoor |".

Evidence checked (`02-weather.md`):

- Date/city consistency: the artifact resolves the correct location and date — "Open-Meteo MCP geocoding result for 'Warsaw' (Poland)"; forecast for "2026-10-23"; `01-requirements.md` fixes "Friday 2026-10-23, evening" and "Warsaw, Poland". No date mismatch.
- Backup plan section reads exactly as required: "### Backup plan / contingency / Not applicable — indoor event." with an explicit reason: "per `01-requirements.md` (rev. 2, final) the venue type is 'Indoor' and the event is held entirely inside; … so no weather-driven backup or contingency is required."
- The weather agent ran the real MCP (`.claude/skills/…`, CLAUDE.md §11): the artifact records two successful MCP calls and even reports a data quirk honestly ("precipitation_sum 6 mm and precipitation_hours 18 against precipitation_probability_max 11 %"). No invented figures.
- Cross-artifact consistency: `03-logistics.md` and `04-timeline.md` both propagate "G6 PASS-N/A" and "Not applicable — indoor event".

No responsible agent (PASS-N/A).

### G7 — Every recommendation links to a real source page (URLs verified with WebFetch)

**Verdict: PASS**

Method: I re-fetched the load-bearing pages myself via WebFetch on 2026-10-15 — **35 URLs across the venue, catering and weather artifacts, all of which loaded and returned the content they are attached to (HTTP success; no dead links, no 404s)**. The full list with the claim each supports is under Sources.

Load-bearing pages and outcomes (examples):

- Recommendation "The Alchemist Grill & Cocktail, ul. Grzybowska 5a" — `https://www.thealchemist.pl/` returned the address "ul. Grzybowska 5a, 00-132 Warszawa" and the alchemy copy (`"Jesteśmy mistrzami w ciemnych sztukach molekularnej miksolgii"`, `"prawdziwa magia dla Twoich zmysłów"`) — supports the theme-by-venue-character claim.
- Capacity claim — `https://thealchemist.pl/imprezy.html` returned `Sala VIP: 40 seated / 40–50 standing`, `Sala główna: 80 seated / 100 standing`, the individual-offer wording (`"Do każdego zapytania podchodzimy indywidualnie"`) and the `"wersji Vege"` line — matches the artifact's quotes verbatim.
- Catering comparator prices — `https://www.sale-konferencyjne-warszawa.pl/wycena/` returned `"od 136 zł netto / os."`, the room grid `2 775 / 3 700 / 5 550 / 6 500 zł`, and `"obsługa barmańska — wyceniamy indywidualnie"` — exactly the benchmark the catering estimate cites; `https://www.ufukiera.pl/menu/` returned the à-la-carte ranges used (starters 49–92, soups 43–49, mains 53–210, desserts 39–59, prosecco 40 PLN/15 cl); `https://poludnikzero.pl/menu-napoje` and `…/menu-alko/` returned the soft-drink and cocktail bands cited (water 10, cola 12, tonic 15, fresh juice 22; cocktails 30–35, alcohol-free 27–30).
- Weather — `https://open-meteo.com/en/docs` and `https://open-meteo.com/en/docs/geocoding-api` both load and document the variables/fields the artifact relies on.

Findings (none rise to a FAIL; two minor, non-load-bearing observations):

- Minor, does not affect the recommendation: `02-venue.md` S22 claims `https://www.cybermachina.pl/` supports a "gaming-bar chain including Warsaw", but the homepage copy reads `"Bary dla graczy. Jesteśmy w całej Polsce."` and does not name Warsaw; the Warsaw branch is in fact carried by S24 (`https://www.cybermachina.pl/cybermachina-warszawa`, returned "ul. Nowy Świat 54/56" and the Fri–Sat hours). Cybermachina is a rejected candidate, so nothing in the plan turns on it. Responsible if a fix were wanted: venue-planner (tighten S22's "supports" wording).
- Minor: `02-venue.md` S5 (`https://europetouristguide.com/…/the-alchemist`) returns the address "Plac Piłsudskiego 9" for the brand; the artifact correctly recommends Grzybowska 5a and lists this only as a source for the drink names, so the claim it is attached to (signature drinks "Philosopher's Stone"/"Elixir of Life"/"Alchemist's Secret") is supported.
- The `04-budget.md` URLs issue: the context (item 5) already accepts that the budget cites six **upstream-artifact path bullets instead of web URLs**. My independent view: I agree this is not a fresh G7 failure — `04-budget.md` fetched no web pages, contains the definition-mandated sentence (`No web pages were fetched by this agent, so no external URL is cited`), and its bullets do trace every figure to a real upstream artifact. It is a structural deviation from the template's `<Page title> — <URL>` shape, not a broken or invented citation.

No responsible agent (PASS).

### G8 — Artifact structure complete (artifact-validator skill, checks C1–C12)

**Verdict: PASS**

Method: I ran the `artifact-validator` checks C1–C12 against all eight artifacts. Compact result per artifact:

```
01-requirements.md      C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
02-venue.md             C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
02-weather.md           C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
03-catering.md          C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
03-entertainment.md     C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
03-logistics.md         C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
04-timeline.md          C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
04-budget.md            C1 PASS C2 PASS C3 PASS C4 PASS C5 PASS C6 PASS C7 PASS C8 PASS C9 PASS C10 PASS C11 PASS C12 PASS
OVERALL: PASS
```

Key evidence:

- C1 (single `# ` title): every file opens with one `# …` line.
- C2 (owner matches the CLAUDE.md ownership table): 01=requirements-formalizer, 02-venue=venue-planner, 02-weather=weather, 03-catering=catering-planner, 03-entertainment=entertainment-planner, 03-logistics=logistics-planner, 04-timeline=timeline-planner, 04-budget=budget-aggregator — all match.
- C3 (sections in order `Inputs used, Summary, Details, Costs, Sources, Open issues`): present and correctly ordered in all eight.
- C4 (`Costs` = table or the exact sentence): 01 states the mandated sentence then adds one benign clarifier ("No costs in this artifact. This artifact states the 4,000 PLN all-in budget ceiling as a requirement only…"); 02-weather, 03-entertainment, 03-logistics, 04-timeline each carry exactly `No costs in this artifact.`; 02-venue, 03-catering, 04-budget use the mandated table. Passed — the required sentence is present verbatim in 01; the appended clarifier does not change its meaning.
- C5 (`Open issues` has a bullet or `None.`): all eight carry bullets; `03-entertainment.md` reads `- None. One observation worth passing upstream, not a blocker: …` (the `None.` plus a non-blocking note).
- C6 (`Sources` has a bullet unless explicitly `Not applicable` with reason): all eight have at least one bullet; 02-weather/02-venue/03-catering/04-budget carry real URL/artifact bullets; 01, 03-entertainment, 03-logistics, 04-timeline carry an explicit "No external sources used (…)" bullet, and the latter three are marked `Not applicable` with reasons.
- C7 (source-bullet shape): URL-bearing bullets use `- <title> — <URL> (fetched 2026-10-15; supports: …)`. `02-venue.md` prefixes each with an `S<n> — ` label (e.g. `- S2 — The Alchemist — Imprezy … — https://thealchemist.pl/imprezy.html (fetched 2026-10-15; supports: …)`); this is an added identifier, not a deviation from the citation shape, so PASS. `04-budget.md`'s bullets are upstream-artifact traces without URLs (recorded as the accepted deviation under G7).
- C8 (URLs real, no placeholders): all URL bullets are `https://`, no `example.com`/`localhost`/`TODO`/`...`.
- C9 (every named venue/caterer/price/figure traces to a source): 02-venue and 03-catering tag every venue, dish and price band with S-refs; the `Not applicable` artifacts (03-entertainment, 03-logistics) and 04-timeline name the venue/dishes only as explicit cross-references to `02-venue.md`/`03-catering.md` and make no independent recommendation, so nothing is unsourced; 04-budget traces every figure to an upstream-artifact bullet.
- C10 (prices sourced or marked `price on request` with basis): every price in 02-venue, 03-catering and 04-budget is either user-confirmed (4,000 limit) or marked `price on request` with an explicit estimate basis; 04-budget's contingency is labelled "**my own proposal, not sourced**".
- C11 (no cross-agent ownership claimed): each artifact stays in its remit; 02-venue's cost note explicitly defers the total to the budget-aggregator, 03-catering's §2 cost model defers the total likewise, and 04-timeline attributes course names to `03-catering.md` ("reused here, not re-derived").
- C12 (nothing requests writing `output/event-plan.html` or `approval.json`): none of the eight does.

No responsible agent (PASS).

## Costs

No costs in this artifact. This artifact judges the gates only; it produces no prices, quotes or estimates.

## Sources

All URLs below were re-fetched by this validator on 2026-10-15 and returned their claimed content (HTTP success). Listed with the claim each supports.

- The Alchemist | Grill & Cocktail (official site) — https://www.thealchemist.pl/ (fetched 2026-10-15; supports: ul. Grzybowska 5a address; alchemy/magic brand language)
- The Alchemist — Imprezy (official) — https://thealchemist.pl/imprezy.html (fetched 2026-10-15; supports: Sala VIP 40 seated / 40–50 standing; main hall 80/100; individual offers; "wersji Vege")
- The Alchemist — Menu (official) — https://thealchemist.pl/menu.html (fetched 2026-10-15; supports: menu published only as three .webp images; no prices)
- The Alchemist — Rezerwacje (official) — https://www.thealchemist.pl/rezerwacje.html (fetched 2026-10-15; supports: Grzybowska 5a; booking channels; no published terms)
- In Your Pocket — The Alchemist Grzybowska — https://www.inyourpocket.com/warsaw/the-alchemist-grzybowska_165895v (fetched 2026-10-15; supports: interior, lava plates, hours; no prices)
- Europe Tourist Guide — The Alchemist — https://europetouristguide.com/poland/warsaw/places/the-alchemist (fetched 2026-10-15; supports: signature drinks "Philosopher's Stone"/"Elixir of Life"/"Alchemist's Secret"; dim alchemical interior)
- Piszę Sobie — The Alchemist Grill & Cocktail — https://piszesobie.pl/jedzenie/the-alchemist-grill-coctail-w-restauracji-czarodziejow/138 (fetched 2026-10-15; supports: dish names; drinks smoke/bubble/hiss/change colour, with and without alcohol)
- U Fukiera (official) — https://www.ufukiera.pl/ (fetched 2026-10-15; supports: Rynek Starego Miasta 27; Fri–Sat to 23:30; "oldest restaurant in Warsaw")
- U Fukiera — Menu — https://www.ufukiera.pl/menu/ (fetched 2026-10-15; supports: comparator prices starters 49–92, soups 43–49, mains 53–210, desserts 39–59, prosecco 40 PLN/15 cl)
- U Fukiera — Przyjęcia — https://www.ufukiera.pl/przyjecia/ (fetched 2026-10-15; supports: groups over 10 by direct arrangement; private dining; no prices)
- U Fukiera — Imprezy firmowe — https://www.ufukiera.pl/przyjecia/restauracja-spotkania-imprezy-firmowe/ (fetched 2026-10-15; supports: corporate events in cosy interiors; no prices)
- U Fukiera — History (EN) — https://www.ufukiera.pl/en/history/ (fetched 2026-10-15; supports: wine store in cellars from the early 16th c.; oldest restaurant in Warsaw)
- SaleBiznesowe.pl — Restauracja U Fukiera — https://www.salebiznesowe.pl/warszawa/restauracja-u-fukiera (fetched 2026-10-15; supports: Winiarnia hall former wine cellar; "Przyjazny dla osób z niepełnosprawnościami"; capacities/prices as placeholder dashes)
- Konferencje.pl — Browar Warszawski — https://www.konferencje.pl/o/browary-warszawskie-browar-warszawski.html (fetched 2026-10-15; supports: Sala Kosmos/Czerwona 30 seated; Stara Warzelnia 6 000 zł netto/day)
- Cennik — loftowe sale konferencyjne — https://www.sale-konferencyjne-warszawa.pl/wycena/ (fetched 2026-10-15; supports: group catering "od 136 zł netto / os."; room grid 2 775/3 700/5 550/6 500 zł; bar service quoted individually)
- Muzeum Warszawy — Powierzchnie do wynajęcia — https://muzeumwarszawy.pl/wynajempowierzchni/ (fetched 2026-10-15; supports: Old Town cellars at ul. Brzozowa; Pharmacy Museum; "intimate dinners"; no prices/capacities)
- Muzeum Warszawy — rental catalogue (PDF) — https://muzeumwarszawy.pl/wp-content/uploads/2026/09/Katalog_wynajem_powierzchni_Muzeum_Warszawy.pdf (fetched 2026-10-15; supports: genuine PDF whose text layer is compressed/image-heavy — consistent with the artifact's "could not be text-extracted")
- Muzeum Farmacji (Museum of Warsaw) — https://muzeumfarmacji.muzeumwarszawy.pl/ (fetched 2026-10-15; supports: recreated pharmacy interior; ul. Piwna 31/33; link to the rental page)
- Saleilokale.pl — Stara Prochownia (SCEK) — https://saleilokale.pl/pl/6081/Stara-Prochownia---Stoleczne-Centrum-Edukacji-Kulturalnej/ (fetched 2026-10-15; supports: ul. Boleść 2; listing flagged "Ta oferta jest nie aktywna"; no real prices)
- Konferencje.pl — Stara Prochownia, sala — https://www.konferencje.pl/o/stara-prochownia-stoleczne-centrum-edukacji-kulturalnej,18190/18491-sala.html (fetched 2026-10-15; supports: 100 m²; 100 theatre / 110 banquet; no prices)
- Mazovia Warsaw Film Commission — Stara Prochownia — https://mwfc.pl/lokacja/stara-prochownia-stolecznego-centrum-edukacji-kulturalnej-warszawa/ (fetched 2026-10-15; supports: late-Gothic Bridge Gate; formerly gate/defence tower and powder magazine; no terms)
- Południk Zero (official) — https://poludnikzero.pl/ (fetched 2026-10-15; supports: ul. Wilcza 25; "Klimatyczna piwnica"; rooms/booths across two floors; travel library)
- Południk Zero — Menu — https://poludnikzero.pl/menu (fetched 2026-10-15; supports: snacks 15–29, pinsa 32–39, toasts 22, cake+coffee 25 PLN)
- Południk Zero — Napoje — https://poludnikzero.pl/menu-napoje (fetched 2026-10-15; supports: water 10, cola 12, tonic 15, fresh juice 22 PLN)
- Południk Zero — Alkohole — https://poludnikzero.pl/menu-alko/ (fetched 2026-10-15; supports: cocktails 30–35, alcohol-free 27–30, prosecco 24 PLN/glass)
- Cybermachina (official) — https://www.cybermachina.pl/ (fetched 2026-10-15; supports: "Gry, mikstury, smocze piwo…" brand phrase only — Warsaw not named on this page; see G7 finding)
- Cybermachina — Menu — https://www.cybermachina.pl/menu (fetched 2026-10-15; supports: "MIKSTURY I DRINKI"; "Smocze piwo"; food limited to snacks; no prices)
- Cybermachina — Warszawa — https://www.cybermachina.pl/cybermachina-warszawa (fetched 2026-10-15; supports: ul. Nowy Świat 54/56; Fri–Sat to 03:00; tournaments/quizzes; no private room, no prices)
- Podwale 25 / Kompania Piwna (official) — https://podwale25.pl/ (fetched 2026-10-15; supports: ul. Podwale 25; daily 11:00–24:00; "Grupowa Biesiada"; no interior/capacity/price)
- Konferencje.pl — Restauracje dla grup — https://www.konferencje.pl/restauracje-dla-grup/ (fetched 2026-10-15; supports: capacities only, no per-person catering/minimum-spend figures)
- Konferencje.pl — Warszawa — https://www.konferencje.pl/warszawa/ (fetched 2026-10-15; supports: capacities and a promotion only; catering/prices not published)
- MojeKonferencje.pl — Imprezy firmowe w Warszawie — https://www.mojekonferencje.pl/blog/imprezy-firmowe-w-warszawie-miejsca-ktore-cie-zachwyca/ (fetched 2026-10-15; supports: venues by capacity, catering qualitative, no prices; Hotel Bellotto cellars)
- Echo Investment — historic cellars of Browary Warszawskie — https://www.echo.com.pl/news,2404,echo-investment-ratuje-historyczne-piwnice-browarow-warszawskich.html (fetched 2026-10-15; supports: 19th-c. vaulted brick cellars; "Piwnice Czasu")
- Open-Meteo Weather Forecast API documentation — https://open-meteo.com/en/docs (fetched 2026-10-15; supports: documentation of the daily/hourly variables the weather artifact quotes)
- Open-Meteo Geocoding API documentation — https://open-meteo.com/en/docs/geocoding-api (fetched 2026-10-15; supports: place-name → latitude/longitude/elevation/timezone resolution used by the weather artifact)

## Open issues

- **Booking risk carried forward (not a gate failure).** The recommended venue publishes no prices anywhere, so `04-budget.md` is still `Status: draft` and every figure is a `price on request` estimate built on other venues' published comparators. Nothing can be booked and no figure is bankable until The Alchemist issues a written offer. The coordinator should treat G1/G2 as PASS-on-estimate and re-check G1 against the venue's real minimum spend before approval.
- **Minimum-spend sizing risk.** Sala VIP seats 40 for a party of 10; the venue may size a compulsory minimum spend for the larger room. `04-budget.md` §8 quantifies this as bounded (a floor up to ≈3,900 PLN still passes G1); above ≈4,000 PLN it would fail and must be surfaced to the user, not absorbed.
- **Catering menu rests on comparators, not the venue's menu.** The venue's menu is published only as images (`menu_*.webp`), so the dish list was assembled from the venue's text and independent reviews; the exact set-menu content and per-person price must be confirmed with the manager.
- **Accepted deviation recorded (G7/G8-C7).** `04-budget.md` cites six upstream-artifact paths rather than web URLs in `## Sources`. Recorded as accepted; my independent view is that it is honest and not a fresh failure, though it technically departs from the template's URL-bullet shape.
- **Two minor source-wording notes for a possible future polish (no gate impact).** `02-venue.md` S22 over-claims Warsaw for the Cybermachina homepage, and S5 carries a non-recommended branch address (Plac Piłsudskiego 9). Neither affects the recommendation or any gate.
- **Timeline start/setup times and course durations are assumptions** (`04-timeline.md` open issues), and venue availability for Friday 2026-10-23 is unconfirmed — all contingent on the venue's offer. Not gate failures.
