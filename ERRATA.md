# Errata

Every error found in a published version is listed here and kept. Nothing is corrected silently.
Newest first. Each entry: what was wrong, in which versions, the correction, and the effect on the conclusion.

## Found in v28 (29 October 2026)

### E4. Edge-siphon arithmetic off by 1,000 (v19 - v27.1, text)
- **Wrong:** 6.6x10^14 routine tokens a year at $0.10-0.50 per million tokens was printed as $70-330B a year (and "$40-280B never billed").
- **Correct:** $66-330 million a year ($40-280 million never billed).
- **Effect:** none on any result - no register input used the figure. The text now says the siphon matters through seat- and outcome-priced work moving on-device, which the cloud-capture shares carry, not through token dollars. Found by the v28 independent review.

### E3. Cost counted for five builders, revenue for all (v1 - v27.1, model scope) - the largest
- **Wrong:** receipts counted revenue reaching every owner of AI data centers (the labs' compute bills, whoever is paid), but the carry counted only the Big-5's capex. SpaceX/xAI, CoreWeave, Nebius, IREN and Applied Digital - about $140B of 2026 AI capex - had their rent in and their cost out.
- **Why it was an error:** revenue and cost must be counted on the same set of owners. The asymmetry flattered the build-out.
- **Correction (v28):** register entry `other_builders_ai_capex` (company-stated figures) added to the carry; same vintage model and paths. Builders without a stated figure (Meta Hyperion, Anthropic/Fluidstack, Crusoe, Lambda, Nscale, Tesla, the Gulf) are listed and still excluded; each would widen the gap.
- **Effect:** material. 2030 plateau deficit -259 -> -422 ($B/yr); z -3.54 -> -5.56; g* 49% -> 57%; P(profit, rationalize, 2030) 52% -> 7%; with the cost of money no path is repaid by 2035 (was 2034-35 at best).

### E2. Revenue base raised on a run-rate report (v26.x - v27.1, register)
- **Wrong:** on 29 Sept 2026 the register's calendar-2026 revenue base was raised from 179 to 187 ($B, mode) on a press report of Anthropic's expected $100B+ exit run-rate.
- **Why it was an error:** it broke the paper's own rule that run-rates overstate bookings.
- **Correction (v28):** base re-derived from Anthropic's filed S-1 (H1 revenue $16.286B) and reported Q3 ($16.8B): 161 / 179 / 198. From v28 a lab component moves only on a filing or a booked-revenue figure.
- **Effect:** g* 2030 48% -> 49%; plateau 2030 deficit -255 -> -259 ($B/yr). Inside the propagated uncertainty; conclusion unchanged.

### E1. Abstract and results tables disagreed (v26.x - v27.1, paper)
- **Wrong:** the abstract quoted a $187B base, a $255B 2030 plateau deficit and g* = 48%, from the register run in E2. The body tables (break-even growth; bottom-up results) were on a $179B base and showed ~$260B and 49%.
- **Correction (v28):** $179B and ~$260B throughout; the abstract, tables and register agree.
- **Effect:** none on the conclusion; the paper disagreed with itself by about 2%.
