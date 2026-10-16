# Weather outlook — Warsaw, 2027-04-23

- **Owner agent:** weather
- **Run:** run-002-corporate-offsite
- **Revision:** 1
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` (Warsaw area, 2027-04-23, outdoor-capable with mandatory
  indoor fallback)

## Summary

Open-Meteo MCP data (real calls, 2026-10-10) shows a typical mild Warsaw spring day for
23 April: the seasonal outlook for 2027-04-23 gives **+11.9 °C / +4.5 °C** (precipitation
and wind not yet available at this lead time — the MCP returned nulls), while the same
date in 2025–2026 was dry and overcast at **+16.8…+21.4 °C**. Outdoor parts of the day
are realistic, but April variability makes the **indoor fallback mandatory** — which the
chosen venue already commits to.

## Details

All figures come from real calls to the **Open-Meteo MCP server** (`open-meteo-mcp-server`,
as registered in the project MCP config), retrieved 2026-10-10.

### MCP call log

| # | Tool | Parameters | Result used |
|---|------|------------|-------------|
| 1 | `geocoding` | `{"name":"Warsaw","countryCode":"PL"}` | Warsaw → 52.22977, 21.01178, elevation 113 m |
| 2 | `seasonal_forecast` | lat 52.2297, lon 21.0122, `start_date=2027-04-18`, `end_date=2027-04-24`, daily: temperature max/min, precipitation, wind max, weather code, `timezone=Europe/Warsaw` | outlook week around the event |
| 3 | `weather_archive` | same point, `2026-04-18…2026-04-24`, same variables | last year's same-date reference |
| 4 | `weather_archive` | same point, `2025-04-18…2025-04-24`, same variables | two-years-back reference |

### Seasonal outlook (2027, event week)

| Date | °C max | °C min | Precip. mm | Wind max km/h | WMO code |
|------|--------|--------|------------|---------------|----------|
| 2027-04-22 | 11.8 | 5.4 | n/a | n/a | n/a |
| **2027-04-23 (event)** | **11.9** | **4.5** | **null** | **null** | **null** |
| 2027-04-24 | — | — | — | — | — |

`null` means the seasonal model returned no value for that variable at this lead time
(not zero) — reported as unavailable rather than guessed. The temperature series is the
usable part of this call.

### Same-date archive reference (climatology)

| Year, 23 Apr | °C max | °C min | Precip. mm | Wind max km/h | WMO code |
|--------------|--------|--------|------------|---------------|----------|
| 2026 | 16.8 | 6.6 | 0.0 | 24.0 | 3 (overcast) |
| 2025 | 21.4 | 9.3 | 0.0 | 9.2 | 3 (overcast) |

### Implications

- Expect **+10…+17 °C, mostly dry but overcast** — comfortable for the outdoor
  team-building block with light jackets; wind can freshen (up to ~24 km/h observed).
- Late April can turn wet and cold quickly → the **indoor fallback is mandatory**:
  the venue commits to a parallel under-roof variant, and the team-building organiser's
  guidance is to move activities indoors (covered in the logistics and entertainment
  artifacts).
- Decision rule for the day: the morning workshop is always indoors; the city game runs
  outdoors unless there is rain or feels-like below +8 °C, in which case it moves to the
  indoor variant (no schedule change needed).

## Costs

No costs in this artifact.

## Sources

- Open-Meteo documentation (APIs behind the MCP server) — https://open-meteo.com/en/docs
  (fetched 2026-10-10; supports: tool semantics, meaning of null values)
- Open-Meteo MCP server project — https://github.com/cmer81/open-meteo-mcp (fetched
  2026-10-10; supports: the MCP tool names and parameters used above)

## Open issues

- Re-check with `weather_forecast` (MCP) after 2027-04-07 when the date enters the 16-day
  horizon; today's seasonal precipitation/wind values are unavailable at this lead time.
