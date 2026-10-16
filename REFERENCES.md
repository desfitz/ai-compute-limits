# Reference library
Every link pasted or found during the project, with what it was used for, a quality rating, and — for rejected sources — the reason. Rejected links stay on the list. The bibliography in paper/paper.tex is the curated subset; this file is the full record.

Quality: P = primary (filing, standard, company statement, dataset); S = reputable secondary (major press, research firm); B = blog/SEO/aggregator (use only to locate a primary); R = rejected.

## Added 2026-09-29 — token pricing, batch and caching discounts, local alternatives (pasted by author)
Bears on: Section 14 (commodity floor), register entries `token_price_index`, `marginal_cash_cost`; realized prices for heavy workloads are far below list.

| # | Link | Quality | Note |
|---|------|---------|------|
| 1 | https://www.resumelens.org/blog/ai/ai-model-pricing-comparison | B | Pricing comparison table; SEO site. Use only as pointer to lab pricing pages. |
| 2 | https://intuitionlabs.ai/articles/batch-ai-processing-cost-turnaround | B | Batch discount 50–75%, 24-hour windows. Claim consistent with lab pricing pages; cite those instead. |
| 3 | https://dev.to/robinbanner/every-ai-models-real-cost-in-2026-the-complete-developer-pricing-guide-2an9 | B | Developer pricing guide; individual post, unverified. |
| 4 | https://www.g2.com/articles/ai-api-pricing | B | Vendor-marketplace article; caching up to 90% off cached prefixes. |
| 5 | https://www.mindstudio.ai/blog/hybrid-ai-architecture-local-models-cloud-frontier | B | Vendor blog; "5–10x TCO reduction" from batch+cache stacking — vendor claim, no data. |
| 6 | https://www.edgerunnerai.com/news/frontier-ai-is-pricing-itself-into-a-corner-local-models-are-the-way-out | B/R | Vendor of local-AI products arguing for local AI; interested party. Rejected as evidence; kept as an example of the on-premise pitch. |
| 7 | https://benchlm.ai/llm-pricing | B | Pricing aggregator; useful for a snapshot, not citable. |
| 8 | https://computecomparison.com/guides/batch-processing-cost-guide | B | Guide; aggregator. |
| 9 | https://www.youtube.com/watch?v=vjSN3J70v1w&t=30 | R | Video; not citable. |

Primary sources to cite instead (to fetch): OpenAI API pricing page (Batch API 50% discount; prompt caching), Anthropic pricing page (Message Batches 50%; prompt caching read/write rates), Google Cloud Vertex AI pricing (batch 50–75%). Model names in the pasted table ("GPT-5", "Claude 4.5 Opus", "Gemini 1.5 Pro", "o4-mini") and the list prices need checking against those pages before any are quoted.

What it changes: the v25 statement "realized prices are about ten times the marginal cash cost" is a list-price statement. For high-volume pipelines that stack batch (−50 to −75%) and caching (−90% on the cached prefix), effective prices are 5–10x lower, i.e. within 1–3x of the floor — and routine classification/annotation already runs locally at electricity cost. The commodity convergence is not a forecast for those workloads; it has happened. For v26: split `token_price_index` into interactive (list) and batch/cached (effective) tiers, and note that the price the carry actually sees is the volume-weighted effective one.

## Earlier references
All sources in the paper's bibliography (paper/paper.tex, \begin{thebibliography}) are in this library by construction; entries marked \verify there are those still needing a primary source. Sources consulted and not used in the bibliography are listed in FEEDBACK.md and in the appraisal appendix where relevant.

## Added 2026-09-30 — September disclosures (search, pre-earnings update)
| Link | Quality | Note |
|---|---|---|
| https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/ | S (transcript) | Oracle Q1 FY27: RPO $664B, OCI +121%, 97.9% GPU utilization, 850 MW delivered. Cited. |
| https://finance.yahoo.com/markets/stocks/articles/oracle-corp-orcl-q1-2027-090101356.html | S | Same call, highlights. Cited. |
| https://finance.yahoo.com/markets/stocks/articles/oracle-q1-earnings-call-highlights-230310387.html | S | Same call; guidance. Used. |
| https://marketwise.com/investing/oracle-earnings-openai-risk/ | S/B | OpenAI ~half of RPO; "prepay or bring your own hardware". Cited with the caveat that it is a newsletter. |
| https://www.top1markets.com/insights/stocks/oracle-orcl-q1-fy2027-rpo-earnings-guide-2026 | B | FY26 capex $55.7B, FCF -$23.7B, financing plan; BofA >50% OpenAI share. Used for figures, not cited. |
| https://www.datacenterdynamics.com/en/news/oracle-has-455bn-in-remaining-performance-obligations-at-end-of-q1-2026/ | S | Prior-year baseline (RPO $455B, Sept 2025; OCI trajectory $18B->$144B). Context only. |
| https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx | P | Oracle FY26 results and FY27 guidance ($90B revenue). Primary. |
| https://sacra.com/c/openai/ | S | OpenAI Q1/Q2 2026 revenue, run-rate growth, ads ARR; Claude 56M MAU; OpenRouter token volumes. Cited. |
| https://valueaddvc.com/blog/openai-revenue-2026-20b-arr-4b-month-path-to-profitability | B | Anthropic >$100B pace (Bloomberg via NYT, 15 Sep); OpenAI IPO 2027; FT $278B burn plan. Secondary; flagged VERIFY. |
| https://aibusinessweekly.net/p/openai-statistics | B | ChatGPT 1B MAU / 900M WAU; subscriber counts. Flagged VERIFY. |

## Added 2026-09-30 — Q2-2026 earnings (Jul 22-30) for the observables table
| Link | Quality | Note |
|---|---|---|
| https://www.sec.gov/Archives/edgar/data/0000789019/000119312526380280/d291965dex991.htm | P | Microsoft 8-K FY27 investor metrics: M365 commercial seat growth +6-7% y/y each quarter FY26; Azure 39-43%. Cited; drives the incumbent seat trend. |
| https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html | S | Alphabet Q2: capex $44.9B, cloud +82% to $24.8B, backlog $514B. Cited. |
| https://www.metirai.com/blog/alphabet-q2-2026-earnings-google-cloud-ai-capex | B | Alphabet Q2 summary; capex guide $195-205B. Cited as coverage. |
| https://valueaddvc.com/pulse/alphabet-google-q2-2026-cloud-earnings-capex | B | Same; not cited. |
| https://tech-insider.org/google-cloud-82-percent-growth-aws-earnings-2026/ | B | Backlog Q1 $462B -> Q2 $514B; MSFT ~$190B/$175B calendar capex. Used for the backlog delta. |
| https://www.digitalapplied.com/blog/ai-capex-scorecard-earnings-week-july-2026 | S/B | Scorecard: MSFT FY26 capex $115.9B, ~$175B CY26, Copilot seats >30M; Meta guide; Amazon no FY capex guide. Cited. |
| https://futurex.capital/en/ai-lab/reports/big-tech-ai-capex-2026q2 | S/B | Quarterly capex all four; Amazon ~$220B on memory prices; AWS +37%. Cited. |
| https://www.directionsonmicrosoft.com/microsoft-expect-capacity-constraints-capex-acceleration-to-continue/ | S | MSFT FY26 Q4: Azure +43%, >$100B annual, capex $41B. Cited. |
| https://samexpert.com/microsoft-q2-fy2026-earnings-licensing-impact/ | B | MSFT FY26 Q2 (Jan): capex $37.5B, ~1 GW added, Azure guide 37-38%. Context; not cited. |

## Added 2026-10-01 — Copilot seat quality; Chinese hyperscalers; productivity-lag history
| Link | Quality | Note |
|---|---|---|
| https://ai2.work/blog/microsoft-365-copilot-hits-30m-paid-seats-backlog-tops-678b | B | E7 bundling and usage billing behind the seat jump; 20-30% weekly active estimate. Cited with VERIFY. |
| https://windowsforum.com/news/microsoft-365-copilots-60-million-seat-forecast-e7-bundles-pricing-and-renewal-risks.446453/ | B | Seat series and E7 dates; cited. |
| https://www.fool.com/investing/2026/09/29/prediction-microsoft-will-double-its-paid-copilot-seats-in-the-next-12-months/ | S | FY26: seats +6%, revenue +17%, segment cost of revenue +12%. Cited. |
| https://www.uctoday.com/... copilot-passes-30-million | S | Nadella quote; Hood on E7 driving ARPU. Not cited (duplicative). |
| https://finance.yahoo.com/technology/ai/articles/microsofts-copilot-just-crossed-30-183023723.html | S | Engagement claims; usage-based billing rollout. Not cited. |
| https://2-data.com/knowledge-hub/microsoft-365-copilot-passed-30-million-seats-... | B | 6.5% penetration; warns of inflated companion stats. Not cited. |
| https://lumienai.com/news/microsoft-q4-2026-earnings-azure-cloud-copilot-revenue | B | Q4 summary. Not cited. |
| https://aibusinessweekly.net/p/microsoft-copilot-statistics | B | Aggregator. Not cited. |
| https://www.tmtpost.com/8119172.html | S | Alibaba/Tencent/Baidu Q2 2026 capex, FCF, ROIC comparison. Cited. |
| https://eu.36kr.com/en/p/3948069327591304 | S | Same quarter, capex figures. Cited. |
| https://www.163.com/dy/article/L5BSTOLI05118O92.html | S | Duplicate of TMTPost piece. Not cited. |
| https://evertiq.com/news/2026-05-06-ai-boom-pushes-hyperscaler-capex-towards-usd-830-billion-in-2026 | S | TrendForce top-9 CSP capex ~$830B. Cited. |
| https://iconnect007.com/article/149904/... | S | Same TrendForce release. Cited. |
| https://www.taiwannews.com.tw/en/news/6414153 | S | TrendForce Sept update: >$886.7B; Chinese four +80%. Cited. |
| https://dramexchange.com/WeeklyResearch/PrinterFriendly/2/12623.html | S | TrendForce: Google TPUs ~78% of its AI servers in 2026. Context for the cost curve; not cited. |
| https://www.itiger.com/news/1122946249 | B | BOCI expert call: Alibaba cloud +33%, capex RMB 160-180B 2026. Not cited. |
| David (1990) AER; Jorgenson-Ho-Stiroh (2008) JEP; Brynjolfsson-Hitt (2000) JEP; BLS productivity; Census BTOS | P | Historical productivity-lag evidence. Cited. |

## Added 2026-10-01 — a16z State of Markets, September 2026 (uploaded by author; copy in references/)
| Source | Quality | Note |
|---|---|---|
| a16z, State of Markets, Sept 2026 (90 slides) | S (investor deck; interested party) | The strongest statement of the bull case; taken point by point in the paper's new Section. Charts carry their own primary attributions, listed below. Kept in references/. |
| S&P Capital IQ consensus Big-5 capex, as of 2026-09-18 (slide 16) | S | 2027 ~$1.05T, 2028 ~$1.15T. Cited; arms-race path relabelled consensus. |
| BofA Global Research, capex as % of US GDP by cycle (slide 16) | S | Railroads ~2%, telecoms ~1.5%, hyperscalers ~1.5% lease-adjusted. Cited. |
| J.P. Morgan AM Guide to the Markets, Aug 2026 (slide 17) | S | Hyperscaler capex 2019-28E; FCF % of sales. Cited. |
| Bloomberg / Goldman: hyperscaler IG issuance and SPV/off-balance-sheet (slide 18) | S | Debt markets stepping in. Context for the SPV paragraph; not separately cited. |
| BofA: hyperscaler ROIC vs cost of debt (slide 19) | S | ROIC ~20% vs debt 4-5%. Cited with the existing-business caveat. |
| Watten, Bistline, Blanford (2026), "Have Data Centers Raised Your Electric Bill?" (slide 21) | P (study; quoted) | Rates fell ~6% 2019-24 where DC capacity grew 160%. Cited; VERIFY against the original. |
| OpenAI + Anthropic ARR ramp; "labs added more revenue in 2026 than all public software" (slide 23) | S | Consistent with register base. Not separately cited. |
| Cloud backlogs ~$1.7T, +150% y/y (slide 24); FactSet/Goldman FCF consensus (slide 24) | P/S | Cited as observables. |
| Silicon Data GPU rental index, 2026-09-07 (slide 26) | S | H100 $2.63, A100 $1.59, H200 $3.29, B200 $5.69/hr; residuals rising. Cited; the counter-evidence on economic depreciation. VERIFY. |
| Enterprise AI budget surveys (slide 29) | S | 20% cite cost as constraint; cloud ~4% of IT in year 2. Cited. |
| Power-user concentration (slide 33) | S | Top 1% drive demand. Cited. |
| Jevons: H100 rental vs token price index (slide 34) | S | Compute prices rising as token prices fall. Cited. |
| OpenRouter token/spend shares, 2026-09-28 (slide 36) | S | Frontier labs ~69% of spend on ~35% of tokens; tokens +600x. Cited. VERIFY. |
| Software fundamentals, CapIQ (slides 60-63) | S | Growth slowed but stable; newspaper analogy. Cited. |

## Added 2026-10-14 — Goldman Sachs Phase-2 ROIC note; first-round PPA sources
Bears on: new Section 16 (sell-side hurdle), Table 8 (per-dollar reconciliation), observables table, register entries `copex` (second anchor), `grid_cap` (high anchor). A copy of the note is in the author's bundle but NOT in this repository: it is proprietary Goldman Sachs research distributed to a named client and may not be reposted.

| Link / source | Quality | Note |
|---|---|---|
| Sheridan, Borges, Schneider, Vegliante, Fein-Ashley, Huang, Valenti, Hager, Zhang, Makkar — "Americas Technology: Sizing the AI Economy Needed to Justify ROIC on Hyperscaler AI Capex," Goldman Sachs Global Investment Research, 24 Sep 2026, 29 pp. | P (primary sell-side framework; interested party — GS rates all six covered names Buy) | Six US hyperscalers' 2026–27 AI capex $1.726T; $42.4B/GW (servers 24.1, network 12.6, facilities 5.4); 70/30 compute/shell at 5/15-yr lives; opex $836M/GW-yr (Epoch +10%); 15% ROIC on average annual capex; revenue needed $1.42T 2028–30 = $11.6B/GW-yr; sensitivity $0.91–1.89T over 0–30% ROIC and $34–51B/GW; three-CSP backlog $1.69T at Q2 2026, 59% conversion needed; semis build 20/35/57 GW and $861B/$1.34T/$2.0T total AI infra capex 2026–28. Reconciled per dollar of capital: GS 0.274 vs paper 0.284. Not linkable. |
| Epoch AI data-center cost inputs (cited by GS as the source of $42.4B/GW and $836M/GW-yr, YE2025, +10% inflation) | P (dataset) | To fetch: the specific Epoch page; the paper already cites Epoch's capex and revenue series. The opex figure is the one input where the frameworks differ materially. |
| Constellation Energy press release, 20 Sep 2024 — Crane Clean Energy Center (Three Mile Island Unit 1) restart; 20-year PPA with Microsoft | P (company statement) | Take-or-pay structure and volumes not disclosed; cited in Section 16.4 for the contracted-power argument. URL to confirm before posting. |
| Constellation Energy press release, 3 Jun 2025 — 20-year agreement with Meta, Clinton Clean Energy Center | P (company statement) | As above. |
| Talen Energy / Amazon Web Services — Susquehanna data-center power arrangements (2024 sale; 2025 revised PPA after the FERC co-location ruling) | P/S | Terms partly disclosed in Talen filings and press; FERC docket on co-located load. URL to confirm. |

Rejected / not sourced (kept as questions, Section 16.4): three-bloc five-year cost per MW (EU $42–50M, US $32–38M, China $14–18M) and rest-of-world demand sketch (India, ASEAN, Africa, LatAm) — derived in the first-round working notes without sources; marked \verify in the paper; a sourced replacement is invited.
