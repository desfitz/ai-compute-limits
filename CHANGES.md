# What's new

Each version opens with what changed and why. Click a line to expand it.

## Version 28 - 29 October 2026 (post-Q3 earnings)

**Result:** a material change, because the count is now complete. With every builder whose rent the model already counted, the 2030 plateau deficit is about **$420B/yr (z = -5.56)**; break-even growth 57%/yr; the sector chains deliver about 33%. For the five largest alone nothing moved (about $260B, z = -3.54). Nvidia (19 Nov), Oracle (Dec), CoreWeave (10 Nov) and Anthropic's amended S-1 enter as v28.1.

### Headline

<details><summary><b>Every builder counted: SpaceX/xAI, CoreWeave, Nebius and others add ~$140B in 2026 - the 2030 shortfall is ~$420B, not ~$260B</b></summary>

**Why they were left out:** the model counted the builders reported in SEC filings and tracked by Epoch AI (Microsoft, Alphabet, Amazon, Meta, Oracle). Until 2026 the others were private, small, or both.

**Why they are added now:**
- **Scale:** 2026 AI capex, company-stated: SpaceX/xAI ~$75B (Q1 7.7 + Q2 15.8 + Q3 16.4 + Q4 guided 35-40 total); CoreWeave $35-39B; Nebius $20-25B; IREN and Applied Digital ~$6B. About $140B - 18% on top of the Big-5's $780B.
- **Symmetry (the main reason):** the model counts revenue reaching *any* owner of AI data centers. Anthropic pays SpaceX $1.25B a month for Colossus 1; Microsoft provides about two-thirds of CoreWeave's revenue. That rent was already counted; the buildings and chips that earn it were not. Revenue in, cost out flattered the build-out.
- **No double count:** the Big-5 buy this capacity as a service, not as property - it is not in their cash capex or finance leases. The register flags the check for each filing.
- **A new builder adds cost, not customers:** rent moves from Azure, AWS or Google Cloud to SpaceX or CoreWeave; it does not grow. Captive uses (Grok, robotaxis) are still paid for by end customers already in the sector chains. Compute in orbit would be capex like any other, with a shorter life.

**What it does (all in the base, same vintage model, same paths as the Big-5):**
- 2030 flat path: carry $725B -> $890B; shortfall $260B -> $420B; z -3.5 -> -5.6; break-even growth 49% -> 57%.
- 35% cut: was about even in 2030; now $110B short, profitable year by year from 2032.
- With the cost of money, **no path is repaid by 2035**.

**Still out - their rent is counted, their cost is not yet - and what brings each in (paper, table "Builders whose rent is counted but whose cost is not yet in the carry"):**
- Meta Hyperion (Blue Owl JV, $27B at signing, ~$56B financing reported, off Meta's books): JV financing filings or Meta's VIE note.
- Anthropic's own sites with Fluidstack ($50B announced): the amended S-1 or later filings.
- Crusoe (Abilene for Oracle/OpenAI and Microsoft): an IPO filing, bond or project-finance prospectus.
- Lambda (Microsoft agreement): its S-1, expected 2027.
- Nscale (~$23B Microsoft contract): a stated capex figure or financing filings.
- Tesla (Cortex training clusters, ~400 MW by end-2026): an AI split of its capex.
- Gulf builders - **Saudi Arabia:** Humain (PIF; 1.9 GW by 2030, 6.6 GW later; 500 MW Nvidia AI factory; $3B AirTrunk campus; $10B Google Cloud hub), Project Transcendence (PIF, $100B announced 2024), Groq with Aramco Digital ($1.5B). **UAE:** Stargate UAE (G42 with OpenAI, Oracle, Nvidia, Cisco, SoftBank; 1 GW in the 5 GW UAE-US AI Campus, first 200 MW in 2026; >$30B for 5 GW per the AI minister), Khazna (G42, 650 MW planned), du (~1 GW site). **Qatar:** Qai (QIA, no figures yet). **Kuwait:** KIA in the AI Infrastructure Partnership (MGX, BlackRock, Microsoft). Gulf-wide ~$5-7B in 2026 (analyst estimate). Annual company or ministerial figures bring them in; until then a separate overlay with the Chinese four. (Microsoft's $15.2B UAE commitment is already in Microsoft's capex.)

Each one left out flatters the build-out. Each moves into the base as soon as a stated figure appears, and the delta log will say so.
</details>

<details><summary><b>How long investors wait: longer than the horizon - no path earns an ordinary return by 2035</b></summary>

- A 35% cut, or spending that follows revenue, turns a yearly profit only from 2032 and has averaged 8-9% by 2035 - just short of an ordinary ~9.5%.
- Flat spending: about -4% a year on average by 2035. Rising spending: about -10%.
- The losses cost money too - interest on debt or earnings given up: with ~9.5%/yr on the losses, the flat path's hole is ~$4.5T by 2035; spending that follows revenue is still ~$800B short.
- That delay, not whether AI is useful, is what investors are pricing. Tables below.
</details>

<details><summary><b>Inflation, counted once: after inflation the flat path is losing ~6.5% a year in 2035</b></summary>

Over a nine-year wait inflation matters, so v28 states it explicitly - and makes sure it is not counted twice.

- **Already in:** the cost of money (9.45%) is a nominal rate, so it already contains expected inflation. Stated in 2026 dollars, the hole and the recovery shrink together, so whether and when the hole closes does not change.
- **Not added to revenue:** receipts are counted in today's prices - multi-year contracts are fixed in dollars when signed, AI unit prices are falling, and the sector ceilings use today's prices. No inflation uplift.
- **What changes:** the return investors keep. Inflation 2.0 / 2.6 / 3.7% a year (Fed 2% goal; September 2026 core CPI 2.6%; headline CPI 3.7% - BLS, 14 Oct). An ordinary return becomes ~6.5% real; flat spending averages ~-6.5% a year in 2035; an arms race ~-12%.
- **Fixed prices, rising costs:** a contract signed in 2026 is worth about a fifth less in real terms by 2035, while power, labour and site costs rise. Letting facility opex rise with prices would add ~$16B to the 2030 carry and ~$50B by 2035 on the flat path - left out of the base (no source yet for escalation clauses), shown as a sensitivity. It makes the result worse.
- **Worked example - one dollar lost in 2027, recovered in 2035:** at 9.45% the owner needs 1.0945^8 = $2.06 back; inflation accounts for 1.026^8 = 1.23 of that; the rest, 2.06 / 1.23 = 1.67 = 1.067^8, is ~6.7% a year of real earnings given up. About a fifth of the cost of waiting is inflation; four-fifths is real return forgone.
- New register entry `inflation` (presentation only; no effect on g*, z or payback). New: real-return rows in the return table, a 2026-dollar block in the cost-of-money table, the formula term by term in the equations appendix, a paragraph in the 2035 horizon appendix, and glossary entries (Nominal vs real; pi; rho).

| Return in today's money (%; ordinary ~6.5%) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -10 | -10 | -11 | -11 | -10 | -9 | -8 | -8 | -7 |
| Arms race | -11 | -12 | -13 | -14 | -14 | -13 | -13 | -13 | -12 |
| 35% cut | -8 | -8 | -6 | -5 | -3 | -1 | 1 | 3 | 5 |
| Spending tracks revenue | -10 | -10 | -9 | -7 | -5 | -2 | 1 | 3 | 6 |

| Hole with cost of money, in 2026 dollars ($B) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -220 | -530 | -920 | -1,350 | -1,800 | -2,240 | -2,670 | -3,090 | -3,500 |
| Arms race | -260 | -700 | -1,300 | -2,050 | -2,880 | -3,750 | -4,670 | -5,630 | -6,620 |
| 35% cut | -180 | -360 | -540 | -670 | -750 | -780 | -760 | -690 | -550 |
| Spending tracks revenue | -220 | -490 | -740 | -930 | -1,020 | -1,000 | -920 | -790 | -630 |

</details>

<details><summary><b>Tax, counted honestly: it widens the 2030 gap by ~$20-45B, not narrows it</b></summary>

- The returns are before tax by design: the 9.45% cost of money is an after-tax rate, compared with pre-tax profit.
- The 2025 law made 100% first-year write-off of equipment permanent (IRS Notice 2026-11); builders' 2025 tax bills fell sharply (Amazon ~$9B -> $1.2B; Meta $9.6B -> $2.8B; Alphabet $21.1B -> $13.8B).
- But the write-off delays tax; it does not cancel it - Amazon: the policy "ultimately doesn't change the amount of tax we pay". Its value is the interest on the deferred tax: ~$11-33B a year by 2030.
- Earning 9.45% after a 15-21% tax needs ~$42-63B a year more profit by 2030 than the carry charges.
- Net: tax widens the 2030 gap by ~$20-45B a year (`model/tax_check.py`).
</details>

<details><summary><b>The market asked the paper's question: Alphabet's worst day ever, down ~13%, ~$480-500B of value</b></summary>

- Investors sold two things: the spending, and a slowdown in search advertising (below).

- 29 October: shares fell nearly 13%, the biggest one-day loss of value in the company's history, on results in which Google Cloud revenue doubled.
- The spending: Q3 capex $51.4B, free cash flow -$9.1B, long-term debt up from $21.6B to $125.1B in a year, and the CFO's "we continue to expect our capex to increase significantly in 2027".
- Sources: [CNBC](https://www.cnbc.com/2026/10/29/alphabet-google-microsoft-msft-shares-today-earnings.html); [Yahoo Finance](https://finance.yahoo.com/markets/article/alphabet-heads-for-a-500-billion-drop-in-market-value-the-biggest-in-its-history-134824763.html); [Alphabet Q3 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)
</details>

<details><summary><b>Flat spending is now the conservative case - every company pointed 2027 up</b></summary>

- Alphabet: "increase significantly in 2027" (no figure; the widely quoted "$300B" is a press estimate, not guidance).
- Amazon: "spend meaningfully more in 2027". Meta: "continue investing aggressively". Microsoft: fiscal-2027 capex to grow; Q2 above $50B.
- Street 2027 about $1.1T (Goldman Sachs, Sept 25). The paper's arms-race path, not its plateau, is the one the companies describe.
</details>

### What spooked investors: AI and the search business

<details><summary><b>More searches, less money per search: Google Search +12% (from 17% in Q2) while query growth was the highest in five years</b></summary>

- Revenue per query grew more slowly, or fell. The paper's reading: AI answers are replacing some of the ad-bearing results beside them.
- Also: EPS $2.67 vs $3.00 expected; long-term debt $125.1B vs $21.6B a year earlier ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/nasdaq-drops-365-points-alphabets-200822565.html)).
- The paper already counts AI only as an uplift to advertising (25/40/55 $B) and assumes AI answers defend search share rather than expand it. If AI takes from search, the uplift belongs at its low end (about $15B less in the 2026 base). No input changed yet: one quarter is a signal; on the watch list for v28.1.
</details>

### How long investors wait

<details><summary><b>New tables: cumulative surplus or deficit, return on the money, and the cost of the losses, 2027-2035 (all builders)</b></summary>

The yearly cost already includes a normal return on the money (about 9-10% a year), so break-even means earning an ordinary investor's return.

| Path ($B, cumulative from 2027) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -230 | -540 | -920 | -1,340 | -1,750 | -2,130 | -2,480 | -2,790 | -3,050 |
| Arms race | -270 | -710 | -1,320 | -2,060 | -2,860 | -3,670 | -4,480 | -5,300 | -6,100 |
| 35% cut | -180 | -370 | -530 | -640 | -680 | -660 | -580 | -420 | -190 |
| Spending tracks revenue | -230 | -500 | -740 | -900 | -920 | -830 | -650 | -410 | -140 |

- No path is repaid by 2035. Cutting back stops the losses growing: a yearly profit from 2032, close to even by 2035 before the cost of money.
- On a flat path, average growth of ~57%/yr breaks even in 2030 and ~74%/yr makes up the 2027-29 losses by then. The sector chains deliver ~33%.
- The losses are not part of capex: capex is the money spent; the yearly cost is what it costs to hold; the losses come out of profits and cash.

Average return on the money invested, 2027 to each year, before tax (%; an ordinary return is ~9.5%):

| Path | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -7 | -8 | -8 | -8 | -8 | -7 | -6 | -5 | -4 |
| Arms race | -8 | -10 | -11 | -11 | -11 | -11 | -11 | -10 | -10 |
| 35% cut | -6 | -5 | -4 | -2 | 0 | 2 | 4 | 6 | 8 |
| Spending tracks revenue | -7 | -7 | -7 | -5 | -2 | 1 | 4 | 6 | 9 |

Computed by `model/roi.py`.

- **The losses cost money: interest or lost earnings.** Spending ahead of revenue is financed by borrowing (Alphabet's long-term debt $21.6B -> $125.1B in a year) or by giving up other earnings, so the hole compounds. With ~9.5%/yr charged on the losses:

| Path ($B, cumulative from 2027, with cost of money) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -230 | -560 | -990 | -1,510 | -2,060 | -2,640 | -3,240 | -3,850 | -4,470 |
| Arms race | -270 | -740 | -1,410 | -2,290 | -3,300 | -4,420 | -5,660 | -7,010 | -8,470 |
| 35% cut | -180 | -380 | -580 | -750 | -860 | -930 | -920 | -860 | -700 |
| Spending tracks revenue | -230 | -520 | -810 | -1,040 | -1,160 | -1,180 | -1,120 | -990 | -800 |

</details>

### New sources

<details><summary><b>Anthropic's S-1: the first filed lab financials - and the $80.7B loss is mostly accounting</b></summary>

- Six months to 30 June 2026: revenue $16.286B (vs $1.163B); operating loss $0.693B; net loss $80.748B.
- $72.388B of the net loss is a non-cash change in the fair value of convertible notes, derivatives and SAFEs. It is not cash burn.
- Source: [Anthropic S-1](https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm)
</details>

<details><summary><b>The paper's Anthropic estimate held: Q3 $16.8B, inside v27's $16-19B</b></summary>

- v27 put Anthropic's 2026 bookings at 50/57/65 ($B). Reported Q3 (not yet filed): $16.8B, +45% on Q2 (CNBC, Oct 14; [FT via The Star](https://www.thestar.com.my/tech/tech-news/2026/10/15/anthropic-revenue-jumps-to-168-billion-in-third-quarter-ft-reports)).
- v28 narrows the component to 53/56/60.
</details>

<details><summary><b>The register's September revision is reversed: 2026 base back to $179B</b></summary>

- On 29 Sept the register base was raised to $187B on press reports of a $100B+ Anthropic exit run-rate. The filed figures do not support it.
- The paper's warning - run-rates overstate bookings - confirmed by the first filed figure.
</details>

<details><summary><b>Cloud growth accelerated again: Google Cloud +103%, Azure +48%, AWS +39%</b></summary>

- Backlogs: Google Cloud $561B; Microsoft commercial RPO $677B; AWS $578B. AWS guides growth above 40% in 2027 and 2028.
- The bull case realized, and already inside the sector chains' 2027 growth of 40-80%.
</details>

<details><summary><b>Oracle: the first signal of the "rationalize" path</b></summary>

- Investor Day, 28 Oct: "Following a period of peak capex in FY27-FY28, capital expenditures are expected to step-down in FY29"; positive free cash flow from H2 FY28.
- Source: [Oracle 8-K](https://www.sec.gov/Archives/edgar/data/1341439/000119312526435853/d75538dex991.htm)
</details>

<details><summary><b>Anthropic's compute commitments: up to $750B, $252B noncancelable to Google, AWS and Microsoft</b> (candidate new Fermi layer)</summary>

- Press reports of the draft S-1: Google $111B, AWS $110B, Microsoft $31B noncancelable ([Dealroom/WSJ](https://dealroom.co/news/164610-anthropics-draft-s-1-reveals-16-3b-revenue-80-7b-loss-and-up-to-750b-com/)).
- Much of the hyperscalers' future "AI revenue" is one lab's investor capital returning to them: the paper's circular flow, now in a filing. Open as an idea for v29.
</details>

### Accounting that makes the carry look smaller

<details><summary><b>Microsoft: building lives 15 -> 25 years; new leases booked as operating</b></summary>

- Both lower reported capex and depreciation; neither changes the economics. The paper's carry is economic; shell lives stay 15/20/25.
- Source: [CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/)
</details>

<details><summary><b>Three-quarters of Microsoft's capex is now chips</b></summary>

- CFO: "Roughly 3/4 of our CapEx was for short-lived assets, primarily CPUs and GPUs." Supports the upper half of the silicon share (45-65%); shortens the blended life.
- Source: [Microsoft FY27 Q1](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)
</details>

### Model changes (parameters.json)

<details><summary><b>Eight register entries changed (new: other builders, in the base; inflation); delta log in Appendix H of the paper</b></summary>

| Entry | v27 | v28 |
|---|---|---|
| 2026 revenue base ($B) | 171 / 187 / 202 | 161 / 179 / 198 |
| Anthropic 2026 bookings ($B) | 50 / 57 / 65 | 53 / 56 / 60 |
| OpenAI 2026 bookings ($B) | 26 / 29 / 33 | 29 / 32 / 35 |
| Big-5 capex 2026 ($B) | 780 | 780 (sources refreshed to Q3) |
| Street capex 2027 / 2028 ($B) | 1,050 / 1,150 | 1,100 / 1,150 |
| Shell and silicon lives | 15/20/25; 4/5/6 | unchanged; Microsoft anchors added |
| Other builders' AI capex (new; in the base) | - | 0.5, 14.3, 27.8, 140.4 (2023-26); follows the Big-5 path |
| Inflation (new; presentation only) | - | 2.0 / 2.6 / 3.7% (Fed goal; Sep 2026 core and headline CPI) |

Effect of the Big-5 inputs alone: plateau 2030 deficit -255 -> -259; z -3.47 -> -3.54; g* 48% -> 49% (minor).
Effect of adding the other builders: deficit -259 -> -422; z -3.54 -> -5.56; g* 49% -> 57%; P(profit, rationalize, 2030) 52% -> 7%. **Material** under the re-issue rule.
</details>

### Easier to read

- **A plain-language front:** the abstract is twelve short points, then an at-a-glance box and a reading guide with page numbers.
- **The argument in the titles:** every section and subsection opens with a one-line claim in blue; the longest open with an *In brief* box - the simple argument first, the detail below.
- **Short paragraphs with headlines:** long paragraphs are split, with a blank line between them; most open with a short headline in a contrasting colour, so the argument can be followed by scanning (`paper/HEADLINES.md`).
- **More bullets:** arguments made in steps (first, second, third) are set out as lists; the incumbent's dilemma and the assistant ceiling are rewritten as simple argument, then detail.
- **Symbols named first:** quantities are named in words before their symbols are used.
- **A cleaner page:** navy section headings, a running header, figures on a light-blue panel and tables on light tan; every figure is redrawn in colour (no grey curves); the flow diagram labels every box and arrow; every page fits its margins.
- **A sorted glossary:** every glossary list and the variable tables are alphabetical within each group (Greek letters by their names).
- **A web edition** shows only the claims and *In brief* boxes, with a "Dig deeper" button under each section for the full text, tables and figures.

### New analysis: labs and landlords

<details><summary><b>Where the labs and the infrastructure owners cooperate, squeeze each other, and are one and the same</b></summary>

- Cooperate: hyperscalers fund the labs; the labs spend it on their compute (Anthropic's reported $252B of noncancelable commitments to Google, AWS, Microsoft).
- Squeeze: labs spread across clouds, build their own capacity and grow their margins; landlords build their own chips and models and bundle AI into search, office suites and ads.
- Same company: Google and Meta are both lab and landlord - no margin to argue over, but no outside customer paying the carry either.
- For the model: the squeeze moves the gap between labs and landlords (theta_lab), not the gap with the customer.
</details>

### Errata (where earlier versions erred) - full list in [ERRATA.md](ERRATA.md)

<details><summary><b>v19-v27.1: edge-siphon arithmetic was off by 1,000 ($70-330B should be $66-330 million)</b></summary>

- No result used the figure; the text now says where the siphon matters (work priced per seat or outcome moving on-device), not in token dollars. Found by the independent review.
</details>

<details><summary><b>v1-v27.1: revenue counted for every data-center owner, cost for only the five largest - the gap was understated (~$260B, now ~$420B)</b></summary>

- The rent SpaceX/xAI, CoreWeave, Nebius and others earn was in the receipts; their buildings and chips were not in the carry. The error flattered the build-out.
- Corrected in v28 with company-stated capex for the other builders. Material: no path is now repaid with the cost of money by 2035 (it was 2034-35 at best).
</details>

<details><summary><b>v26.x-v27.1: abstract and tables disagreed ($187B / $255B vs $179B / ~$260B)</b></summary>

- v27's abstract quoted a register run on the superseded $187B base ($255B deficit, g* 48%). The body tables were on the $179B base. v28 states $179B throughout (about $260B for the five largest alone).
</details>

### Still waiting on

- Anthropic amended S-1 with filed Q3 (expected November; statements go stale ~11-12 Nov)
- Nvidia Q3 FY27 (19 Nov); Oracle FY27 Q2 (December); a post-earnings 2027-28 capex consensus
- CoreWeave Q3 (10 Nov); SpaceX Q4 (late January); lease notes in the Big-5 10-Ks (confirm no neocloud capacity is booked as a finance lease)
- Figures for the builders still out: Meta Hyperion, Anthropic/Fluidstack, Crusoe, Lambda, Nscale, Tesla, the Gulf
