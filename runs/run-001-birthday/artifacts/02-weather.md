# Weather outlook — Warsaw, 2026-11-14

- **Owner agent:** weather
- **Run:** run-001-birthday
- **Revision:** 1
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` (Warsaw, 2026-11-14, indoor venue)

## Summary

Open-Meteo MCP data (real calls, 2026-10-10) gives a cool, damp mid-November picture for
Warsaw: the seasonal outlook for 2026-11-14 shows **+8.6 °C / +1.3 °C** with **6.5 mm**
precipitation and wind gusts up to **26.1 km/h** (drizzle), and the same calendar date in
2024–2025 ranged **+5.5…+10.9 °C**. This **confirms the indoor venue decision**; no
weather-driven backup planning is required.

## Details

All figures come from real calls to the **Open-Meteo MCP server** (`open-meteo-mcp-server`,
as registered in the project MCP config), retrieved 2026-10-10.

### MCP call log

| # | Tool | Parameters | Result used |
|---|------|------------|-------------|
| 1 | `geocoding` | `{"name":"Warsaw","countryCode":"PL"}` | Warsaw → 52.22977, 21.01178, elevation 113 m |
| 2 | `seasonal_forecast` | lat 52.2297, lon 21.0122, `start_date=2026-11-09`, `end_date=2026-11-15`, daily: temperature max/min, precipitation, wind max, weather code, `timezone=Europe/Warsaw` | outlook week around the event |
| 3 | `weather_archive` | same point, `2025-11-09…2025-11-16`, same variables | last year's same-date reference |
| 4 | `weather_archive` | same point, `2024-11-09…2024-11-16`, same variables | two-years-back reference |

### Seasonal outlook (event week, 2026)

| Date | °C max | °C min | Precip. mm | Wind max km/h | WMO code |
|------|--------|--------|------------|---------------|----------|
| 2026-11-13 | 3.3 | −0.2 | 3.6 | 21.1 | 51 (light drizzle) |
| **2026-11-14 (event)** | **8.6** | **1.3** | **6.5** | **26.1** | **53 (moderate drizzle)** |
| 2026-11-15 | 9.2 | 3.0 | 1.1 | 23.8 | 3 (overcast) |

### Same-date archive reference (climatology)

| Year, 14 Nov | °C max | °C min | Precip. mm | Wind max km/h | WMO code |
|--------------|--------|--------|------------|---------------|----------|
| 2025 | 10.9 | 7.2 | 0.0 | 14.4 | 3 (overcast) |
| 2024 | 5.5 | 0.6 | 1.3 | 17.4 | 51 (light drizzle) |

### Implications

- Expect **+5…+10 °C, damp and possibly drizzly** with fresh wind — unpleasant for any
  outdoor element, fine for an indoor party with covered arrival.
- Indoor venue → **backup plan not applicable (indoor event)**; guests should be advised
  to plan door-to-door transport (taxi/public transport) rather than walking between
  venues.
- No weather risk to the run-of-show; cloakroom and a covered entrance matter more than
  contingency space.

## Costs

No costs in this artifact.

## Sources

- Open-Meteo documentation (APIs behind the MCP server) — https://open-meteo.com/en/docs
  (fetched 2026-10-10; supports: tool semantics of forecast/seasonal/archive data)
- Open-Meteo MCP server project — https://github.com/cmer81/open-meteo-mcp (fetched
  2026-10-10; supports: the MCP tool names and parameters used above)

## Open issues

- Seasonal data is an outlook, not a forecast: re-check with `weather_forecast` (MCP)
  after 2026-10-29 when the date falls inside the 16-day forecast horizon.
