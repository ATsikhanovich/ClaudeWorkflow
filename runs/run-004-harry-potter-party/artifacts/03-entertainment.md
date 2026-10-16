# Entertainment — not applicable

- **Owner agent:** entertainment-planner
- **Run:** run-004-harry-potter-party
- **Revision:** 1
- **Status:** final

## Inputs used

- `artifacts/01-requirements.md` (rev 2, final) — "Required services (explicit list): 1) Venue; 2) Catering. That is the complete list." and "Anything explicitly NOT required: … entertainment (music, DJ, costumed host, activities); photography; transport; staffing".
- Same artifact, "Excluded services" table: "Entertainment (music, DJ, costumed host, activities) → entertainment-planner service work is not required."
- `artifacts/02-venue.md` (rev 1, final) — recommended venue's own interior character, used here only to state where the theme sits (not to book any act).
- Today's date: 2026-10-15.

## Summary

**Not applicable — no entertainment required (confirmed in requirements).** The
coordinator skipped this agent's planning work as part of plan adaptation: when asked
which services the plan should cover, the user selected only Venue and Catering and
explicitly listed entertainment (music, DJ, costumed host, activities), photography and
transport as not required. This artifact exists only to keep the artifact structure
stable and to make gate G5 (service coverage) decidable — it carries no researched or
booked acts. The evening's "program" is conversation among friends around a themed
dinner, organised by the host, not a purchased service.

## Details

The confirmed requirements carry no entertainment wishes ("Entertainment wishes: None")
and name entertainment among the explicitly not-required services. Accordingly:

- No performers, musicians, DJs, photographers, costumed hosts or activities were
  researched, shortlisted, quoted or booked for this run. Nothing is recommended here.
- The run-of-show will deliberately contain no entertainment blocks and no act
  load-in/load-out or soundcheck slots (see the timeline artifact).
- The Harry Potter theme for this event is carried entirely by two in-scope channels,
  both owned by other agents:
  1. **The venue's own alchemical interior character** — The Alchemist Grill & Cocktail,
     ul. Grzybowska 5a, Warsaw (Sala VIP, private), whose published brand and interior
     are explicitly alchemy/wizard-like (vintage alchemical decor, drinks such as
     "Philosopher's Stone" and "Elixir of Life"). This is the recommended venue in
     `02-venue.md`; the theme comes from the room itself, not from any booked act.
  2. **The themed catering concept** — the themed menu and themed welcome drink required
     from the catering service line.
- Because no act is booked, there are no sound limits, stage, power or curfew
  requirements to feed into the venue or logistics planning from this artifact.
- The per-person budget (≈400 PLN inside the 4,000 PLN all-in ceiling) is left entirely
  to venue and catering; no entertainment share is reserved.

## Costs

No costs in this artifact.

## Sources

No external sources used (service explicitly excluded — nothing researched).

## Open issues

- None. One observation worth passing upstream, not a blocker: the requirements make the
  theme depend wholly on the venue's interior character plus the catering concept, so
  there is no fallback entertainment or decorative layer if the recommended venue turns
  out to be unavailable on Friday 2026-10-23 (already flagged as an open issue in
  `02-venue.md`). Adding any act would be a scope change requiring user confirmation, not
  a silent substitution.
