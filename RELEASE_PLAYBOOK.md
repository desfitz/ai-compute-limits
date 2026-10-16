---
title: "Release Playbook v3 — The Macroeconomic Limits of AI Compute"
subtitle: "The paper is finished (v27). This is the release-and-maintenance protocol only: no further analysis."
date: 14 October 2026
---

# 1. What is final

| Item | File | Status |
|---|---|---|
| Paper, posting version | `ai_compute_limits_v27_2026-10-14.pdf` / `.tex` (105 pp., 24 figures) | **Final.** Goldman Sachs note reconciled (Section 16); first-round arguments recorded; register flags added; no model numbers changed. |
| Change-marked copy | `ai_compute_limits_CHANGES_v26-7_to_v27_2026-10-14.pdf` | Blue = added, red = removed. Read only the colour. |
| Complete bundle | `ai_compute_limits_v27_bundle_2026-10-14.zip` | tex + figures/ + PDF + change copy + BUILD.txt + the GS note (private copy; see 2.0). |
| Repository package | `community_repo_v27_2026-10-14.zip` | Register (`parameters.json`), model, rebuild script, figure scripts, data, paper v27, deck, one-pager, README/CONTRIBUTING/GOVERNANCE, FEEDBACK, REFERENCES, seed issues, CI, blueprint. |
| Easy-access deck | `ai_compute_easy_deck_v27_2026-10-14.pdf` / `.tex` (14 slides, 16:9, light) | **New.** The argument in twelve slides for readers who will not open the paper. Every number is the paper's. |
| Technical deck | `ai_compute_deck_v26-5_2026-10-01.pdf` (28 slides) | Still valid; numbers unchanged since v26.5. Add two slides (GS reconciliation; first-round arguments) only if you present to a technical audience. |
| One-pager | `ai_compute_summary_onepage_v23_2026-09-09.pdf` | Numbers are v23 (carry $725B, g* 48%, base $187B are close but not identical to v27). Either refresh (15 minutes) or retire it in favour of the easy deck's last slide. Recommendation: retire; the deck's "whole argument" slide is the one-pager. |

What is **not** final and never will be: the register. It is the live object; the paper is a dated rendering of it.

## 1.1 Two prerequisites before anything goes on a permanent record

1. **The nvara.ai mailbox.** The byline now carries desmond.fitzpatrick@nvara.ai. Zenodo, SSRN and arXiv records are permanent. Send yourself a test message from another account and receive it before step 2.1. If the mailbox is not live by posting day, post with the gmail address only and add the nvara.ai address at the first re-issue.
2. **ORCID.** orcid.org → Register (five minutes; use the gmail address as primary, add nvara.ai later). Put the ORCID iD on the paper's title page before upload (one line under the byline). Every venue below asks for it.

# 2. The posting sequence (do in order; each step links to the previous)

## 2.0 One rule about George's note
The Goldman Sachs PDF is proprietary client research watermarked to a named recipient. It stays in your bundle. It does **not** go into the public repository, Zenodo, SSRN or arXiv, and is not forwarded. The paper cites it as unlinkable; that is correct and sufficient.

## 2.1 Zenodo (first — everything else cites the DOI)
1. zenodo.org → sign in with ORCID → New upload.
2. Files: the v27 PDF, the v27 .tex, the figures/ folder (as a zip), `parameters.json`, `numbers.json`, the repository zip, the easy deck PDF. **Not** the GS note.
3. Metadata: title as on the paper; author with ORCID; type Preprint; license CC BY 4.0 (text, figures) and MIT (code) — state both in the description; keywords from the paper's keyword line; description = the abstract.
4. Publish → copy both DOIs. Cite the **concept DOI** (always resolves to latest) in the paper; use the **version DOI** in delta logs.
5. Put the concept DOI into the paper's Method section (the line now marked \verify), rebuild, and upload the rebuilt PDF/tex as a new version of the same record. That rebuilt file is v27.1 and is the file everything else links to.

## 2.2 GitHub (second — the "open model" claim needs a URL)
1. Create a public repository (suggested: `ai-compute-limits`). Unzip `community_repo_v27` into it; commit.
2. Add LICENSE files: CC-BY-4.0 in `paper/`, MIT in `model/`.
3. Enable Issues; create the seed issues from `.github/seed_issues.json`. Open one issue per [VERIFY] mark that moves a number (the checklist's group A) and one for the **facility-opex anchor** (GS/Epoch 2% vs paper 6.65%) — this is the first issue you want the community to argue.
4. Zenodo → GitHub tab → toggle the repository; create release tag `v27.1`. Zenodo archives it automatically from now on.
5. Add the DOI badge and the easy deck link to the README. Enable Actions (the rebuild workflow is already in `.github/workflows/`).

## 2.3 SSRN
Submit the v27.1 PDF. Networks: Economics Research Network (Macroeconomics; Industrial Organization) and Information Systems & eBusiness. JEL: E22, L86, O33, G31. Last line of the abstract: concept DOI and GitHub URL. Approval takes 1–3 days.

## 2.4 arXiv
Upload the .tex and the 24 figure PDFs (arXiv compiles). Primary econ.GN, cross-list cs.CY. First submission needs an endorsement for econ.GN: ask Epoch AI staff (they post there) or wait for SSRN acceptance and cite it in the request. Comments field: "105 pages, 24 figures; register and model at <GitHub>; DOI <concept DOI>". Add the arXiv ID to the paper at the next re-issue, not before.

## 2.5 The easy-access deck — where it goes
- **README, first screen:** "Read the twelve-slide version" above the paper link. Most visitors stop here; that is its job.
- **Zenodo:** as a file on the same record.
- **Substack and LinkedIn:** the deck is the post. Substack: slides 1–13 as images with one paragraph each (the slide's own lead paragraph), the final slide as the closing with the links; 1,200 words, no new text. LinkedIn: slide 14 ("the whole argument") as the image, 150 words, the Substack link. Post both the morning SSRN approval lands so the links resolve.
- **Direct outreach (2.6):** attach the deck, not the paper. Link the paper.

## 2.6 Outreach — after the DOI exists, on the same day as Substack
Every note is two short paragraphs: which part of the paper rests on their work, and the one number you want them to dispute. Attach the deck; link DOI, GitHub, and the specific issue.

| Who | The one number to dispute |
|---|---|
| Epoch AI (Sevilla and data team) | The $836M/GW-yr opex figure GS attributes to them — is it all-in or power-only? (This settles the opex issue.) |
| Dylan Patel / SemiAnalysis | 57 GW in 2028 vs the paper's 22–40 GW/yr grid cap |
| Jim Covello / Eric Sheridan (Goldman) | Table 8: the per-dollar reconciliation; cohort stacking |
| David Cahn (Sequoia) | The carry construction (stock vs flow) |
| Erik Brynjolfsson | σ_slack = 0.65, ν_verify = 0.20 |
| Data Center Watch | Fraction of delayed projects ultimately built |
| Ben Thompson / Benedict Evans | Reallocation share 12–32% |
| Anthropic economics team | Overlap correction; a booked-revenue figure |
| George Kountouris, Viraj Mehta, Francis Pedraza, Matthew Fitzpatrick | Thank-you with the final; ask each for one forward |
| Kedrosky / Azhar; Odd Lots, Dwarkesh | Amplification and podcasts — after the paper has been shot at, not before |

# 2.7 Author biography (locked 15 Oct 2026)

**Short — LinkedIn, Substack byline, outreach-note signature, README:**

Desmond Fitzpatrick is the CEO of Nvara, an AI venture for enterprise systems, which he founded after resigning from IBM in May 2026. He spent his career at IBM: the first half on almost every aspect of chip technology, the second on IBM Z systems quality and resilience — ensuring some of the highest-quality products in the world — including responsibility for AI resilience on Z in his last three years. He is the principal author of the eight-nines availability claim for both z/OS and Linux on the mainframe, holds six IBM Outstanding Achievement Awards for work ranging from the impact of cosmic rays to the world's first copper metallurgy, and for his last four years presented the status of quantum computing for IBM, mostly to CTOs. At IBM he was responsible for many critical Fermi calculations over the years. He holds a Ph.D. in physics from Brown University and lives in New York City. desmond.fitzpatrick@nvara.ai · ORCID 0009-0001-0534-2793

**Long — SSRN author profile, podcast introductions, press:**

Desmond Fitzpatrick is the CEO of Nvara, an AI venture in trust and compliance for enterprise systems, which he founded after resigning from IBM in May 2026. He spent his career at IBM in two halves: the first on almost every aspect of chip technology, from the physics of the devices to how they are fabricated and tested; the second on IBM Z, where he managed systems quality, including reliability, availability and serviceability for the platform — ensuring some of the highest-quality products in the world — and, for his last three years, was responsible for AI resilience on Z. He is the principal author of the eight-nines availability claim for both z/OS and Linux on the mainframe, and holds six IBM Outstanding Achievement Awards for work ranging from the impact of cosmic rays to the world's first copper metallurgy. For his last four years he also presented the status of quantum computing for IBM, mostly to CTOs. He is a systems thinker by habit: the instinct to ask what a thing costs to keep running, year after year, before asking what it is worth, runs through everything he has been involved with.

At IBM he was responsible for many critical Fermi calculations over the years, and that discipline is the point of *The Macroeconomic Limits of AI Compute*. The paper does not ask whether AI is useful; it asks whether the revenue will arrive fast enough to pay for the data centers being built to serve it. It treats the build-out the way an engineer treats a fleet — cohort by cohort, with wear, running cost and the cost of capital counted every year — and sets that against demand counted sector by sector rather than assumed. Every input sits in a public register with its source and its range, so that anyone with a better number can replace his and see what changes. The aim is not to be right in October 2026 but to be correctable in October 2028.

He holds a Ph.D. in physics from Brown University and lives in New York City.

# 3. Maintenance — the only work that remains

You said no more analysis. The protocol honours that: from here the author's job is to (a) run the rebuild after each data event, (b) publish the delta log, (c) merge or decline pull requests under GOVERNANCE.md. Nothing else.

## 3.1 The update procedure (unchanged, one page)
1. Edit the entry in `model/parameters.json` (value, source, source_date). Never edit `model5.py` for an update.
2. `python3 rebuild.py` → read the DELTA line: **minor** (|Δz| < 0.5, |Δg*| < 5 pts, |ΔP| < 15 pts) or **material**.
3. Minor: new numbers.json and figures; note in FEEDBACK.md; no new paper version. Material: `rebuild.py --figs`, recompile `paper/paper.tex`, `make_changes_pdf.sh old new` for the colour copy, delta log into the update appendix, new Zenodo version, GitHub release tag, SSRN/arXiv replace, a short Substack note.
4. Anyone else can do steps 1–2 by pull request; CI posts the delta on the PR.

## 3.2 Calendar
| Date | Event | Register entries it touches |
|---|---|---|
| 28–30 Oct 2026 | Microsoft, Alphabet, Amazon, Meta Q3 calls | capex_history (2026 actual, 2027 guide); Copilot paid seats; Advantage+ run-rate; AI run-rates → base_2026; backlogs |
| by ~15 Nov | Anthropic listing (expected) | First audited lab figures: base_2026, theta_lab |
| 19 Nov | Nvidia Q3 FY27 | silicon_share; capex cross-check |
| by ~3 Dec | **v28** if the October–November rebuild is material; otherwise a delta note only | — |
| Dec | Oracle Q2 FY27 | RPO; capex; OpenAI concentration |
| Jan 2027 | Damodaran update; Big-5 10-Ks | wacc; calendar-2026 revenue test; useful lives; related-party notes; property-tax and opex disclosures (the opex issue) |
| Q1 2027 | OpenAI S-1 if filed | theta_lab; base |
| Jan 2028 | Calendar-2027 revenue | Interim marker: ~$330B is the paper's path; >$350B favours the build-out |
| Jan 2029 | Calendar-2028 revenue | **The test: >$400B overturns the central case** |

## 3.3 What a community contribution looks like (for the README)
A pull request that changes one register entry with a source. The CI comment says what it did to z, g* and P(profit). Maintainer merges if the source is better than the one it replaces (P over S over B; never R). Disagreements about judgment ranges go to an issue, not a PR. The author is one maintainer; invite one more from the first reviewers once the repository has ten merged PRs.

# 4. Files (outputs folder, 14 Oct 2026)
- Paper: `ai_compute_limits_v27_2026-10-14.pdf` / `.tex`; `ai_compute_limits_v27_bundle_2026-10-14.zip`; `ai_compute_limits_CHANGES_v26-7_to_v27_2026-10-14.pdf`
- Easy deck: `ai_compute_easy_deck_v27_2026-10-14.pdf` / `.tex`
- Repository: `community_repo/` and `community_repo_v27_2026-10-14.zip`
- Technical deck: `ai_compute_deck_v26-5_2026-10-01.pdf`; one-pager: `ai_compute_summary_onepage_v23_2026-09-09.pdf` (retire or refresh)
- Checklist: `pre_release_checklist_v19_2026-09-09.md`; this playbook: `release_playbook_v3_2026-10-14.docx` / `.md`
