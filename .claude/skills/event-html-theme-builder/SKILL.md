---
name: event-html-theme-builder
description: HTML rendering rules and the predefined standalone template for the final event plan. Use when rendering the approved event plan into output/event-plan.html so the document structure and visual style are identical across runs.
---

# event-html-theme-builder

Render `artifacts/06-event-plan.md` (after human approval) into a single standalone
`output/event-plan.html` using the template in `template.html` next to this file.

## Hard rules

1. **Standalone**: one `.html` file, all CSS inline in a `<style>` block. No external
   stylesheets, fonts, scripts, images or CDNs. Use inline SVG for any decoration.
2. **Responsive + printable**: viewport meta, fluid layout up to `max-width: 920px`,
   tables wrapped in `.table-wrap { overflow-x: auto; }`, and a `@media print` block
   (white background, black text, no shadows, avoid page breaks inside rows).
3. **Identical structure across runs**: the section order is fixed and must not change:
   Header → Overview → Venue → Weather & contingency → Catering → Entertainment →
   Logistics → Run of show → Budget → Risks & notes → Sources → Footer.
   A section whose content is "Not applicable" is still rendered with that reason.
4. **Public content only** (enforced by the no-leak-guard hook): never mention internal
   file names, run folders, state keys, gate ids or retry machinery. Speak about the
   event, not about the workflow. Never invent facts not present in the plan.
5. **Links**: render every source from the plan's Sources section as an anchor
   `<a href="...">` with the page title as link text. Do not add links that are not
   in the plan.
6. **Accessibility**: semantic landmarks (`header`, `main`, `section`, `footer`), one
   `h1` (event title), `h2` per section, table headers with `<th scope>`, sufficient
   color contrast, `lang` attribute set.
7. Dates rendered human-readably (e.g. `Saturday, 14 November 2026`), money rendered
   with thousands separators and the currency code (e.g. `6 000 PLN`).

## Template

Start from [`template.html`](./template.html). Replace every `{{PLACEHOLDER}}`:

| Placeholder | Content |
|-------------|---------|
| `{{LANG}}` | language code, e.g. `en` |
| `{{EVENT_TITLE}}` | occasion headline, e.g. `30th Birthday Party` |
| `{{EVENT_SUBTITLE}}` | `40 guests · Warsaw · 14 November 2026` |
| `{{GENERATED_DATE}}` | render date, e.g. `10 October 2026` |
| `{{OVERVIEW_ROWS}}` | `<tr><th scope="row">…</th><td>…</td></tr>` per fact |
| `{{VENUE_HTML}}`, `{{WEATHER_HTML}}`, `{{CATERING_HTML}}`, `{{ENTERTAINMENT_HTML}}`, `{{LOGISTICS_HTML}}`, `{{RISKS_HTML}}` | rendered body HTML per section |
| `{{TIMELINE_ROWS}}` | `<tr><td>…</td><td>…</td><td>…</td><td>…</td></tr>` per run-of-show line |
| `{{BUDGET_ROWS}}` | `<tr><td>…</td><td>…</td></tr>` per category |
| `{{BUDGET_TOTAL}}`, `{{BUDGET_LIMIT}}`, `{{BUDGET_DELTA}}` | money strings |
| `{{SOURCE_ITEMS}}` | `<li><a href="URL">Title</a> — supports …</li>` per source |

Delete any placeholder row/list item you cannot fill; never leave `{{...}}` in output.

## Self-check before finishing

- No `{{` remains in the file.
- No string from the forbidden list (internal artifact names, `runs/`, state keys).
- Opens correctly offline (no network requests in the markup).
- `grep`-level sanity: exactly one `<h1>`, all `<a href>` values start with `https://`.
