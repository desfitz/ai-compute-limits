# What's new

Each version opens with what changed and why. Click a line to expand it.

## Version 28 - 29 October 2026 (post-Q3 earnings)

**Result:** unchanged within its uncertainty. 2030 plateau deficit about $260B/yr (z = -3.54); break-even growth 49%/yr; the sector chains deliver about 33%. Minor under the re-issue rule. Nvidia (19 Nov), Oracle (Dec) and Anthropic's amended S-1 enter as v28.1.

### Headline

<details><summary><b>How long investors wait: an ordinary return, early losses included, arrives in 2034-35 at best</b></summary>

- Spending that follows revenue: an ordinary return (~9.5%), early losses included, only in 2034-35; a 35% cut in 2033.
- Flat spending: ~1% a year on average by 2035. Rising spending: a loss on average every year to 2035.
- The losses cost money too - interest on debt or earnings given up - so the hole compounds: with ~9.5%/yr on the losses, the flat path's hole is ~$2.4T by 2035.
- That delay, not whether AI is useful, is what investors are pricing. Tables below.
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

<details><summary><b>New table: cumulative surplus or deficit by year, 2027-2035, by spending path</b></summary>

The yearly cost already includes a normal return on the money (about 9-10% a year), so break-even means earning an ordinary investor's return.

| Path ($B, cumulative from 2027) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -150 | -360 | -600 | -860 | -1,080 | -1,280 | -1,420 | -1,520 | -1,550 |
| Arms race | -190 | -510 | -940 | -1,490 | -2,070 | -2,640 | -3,210 | -3,750 | -4,260 |
| 35% cut | -120 | -210 | -260 | -260 | -180 | -30 | +190 | +490 | +870 |
| Spending tracks revenue | -150 | -330 | -470 | -550 | -500 | -340 | -100 | +180 | +480 |

- Flat spending is never repaid by 2035; an arms race never earns its return; cutting back is repaid by 2033-34.
- On a flat path, average growth of ~49%/yr breaks even in 2030 and ~64%/yr makes up the 2027-28 losses by then. The sector chains deliver ~33%.
- The losses are not part of capex: capex is the money spent; the yearly cost is what it costs to hold; the losses come out of profits and cash. Charging ~9.5% a year on the losses themselves deepens the hole (spending-tracks-revenue: ~$650B instead of ~$550B) and moves payback from 2034 to 2035.

Average return on the money invested, 2027 to each year, before tax (%; an ordinary return is ~9.5%):

| Path | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -4 | -4 | -4 | -4 | -3 | -2 | -1 | 0 | 1 |
| Arms race | -6 | -7 | -8 | -9 | -9 | -9 | -8 | -8 | -7 |
| 35% cut | -2 | -1 | 1 | 4 | 6 | 9 | 12 | 14 | 17 |
| Spending tracks revenue | -4 | -4 | -3 | -1 | 2 | 5 | 9 | 11 | 13 |

Computed by `model/roi.py`.

- **The losses cost money: interest or lost earnings.** Spending ahead of revenue is financed by borrowing (Alphabet's long-term debt $21.6B -> $125.1B in a year) or by giving up other earnings, so the hole compounds. With ~9.5%/yr charged on the losses:

| Path ($B, cumulative from 2027, with cost of money) | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| Flat spending | -150 | -370 | -650 | -970 | -1,290 | -1,600 | -1,890 | -2,170 | -2,410 |
| Arms race | -190 | -520 | -1,010 | -1,650 | -2,390 | -3,190 | -4,050 | -4,970 | -5,950 |
| 35% cut | -120 | -220 | -300 | -320 | -270 | -140 | +70 | +370 | +800 |
| Spending tracks revenue | -150 | -340 | -520 | -640 | -650 | -540 | -350 | -90 | +210 |

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

<details><summary><b>Six register entries changed; delta log in Appendix H of the paper</b></summary>

| Entry | v27 | v28 |
|---|---|---|
| 2026 revenue base ($B) | 171 / 187 / 202 | 161 / 179 / 198 |
| Anthropic 2026 bookings ($B) | 50 / 57 / 65 | 53 / 56 / 60 |
| OpenAI 2026 bookings ($B) | 26 / 29 / 33 | 29 / 32 / 35 |
| Big-5 capex 2026 ($B) | 780 | 780 (sources refreshed to Q3) |
| Street capex 2027 / 2028 ($B) | 1,050 / 1,150 | 1,100 / 1,150 |
| Shell and silicon lives | 15/20/25; 4/5/6 | unchanged; Microsoft anchors added |

Effect: plateau 2030 deficit -255 -> -259; z -3.47 -> -3.54; g* 48% -> 49%; P(profit, rationalize, 2030) 54% -> 52%.
</details>

### Easier to read

- The abstract is rewritten as eleven short points in plain language, followed by a reading guide with page numbers (what's new, errata, summary, inputs, delta log, glossary). The technical detail is in the Executive Summary.

### Errata (where earlier versions erred) - full list in [ERRATA.md](ERRATA.md)

<details><summary><b>v26.x-v27.1: abstract and tables disagreed ($187B / $255B vs $179B / ~$260B)</b></summary>

- v27's abstract quoted a register run on the superseded $187B base ($255B deficit, g* 48%). The body tables were on the $179B base. v28 states $179B and about $260B throughout.
</details>

### Still waiting on

- Anthropic amended S-1 with filed Q3 (expected November; statements go stale ~11-12 Nov)
- Nvidia Q3 FY27 (19 Nov); Oracle FY27 Q2 (December); a post-earnings 2027-28 capex consensus
