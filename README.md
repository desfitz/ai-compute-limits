# The Macroeconomic Limits of AI Compute — a community estimate

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23428319.svg)](https://doi.org/10.5281/zenodo.23428319) [![License: CC BY 4.0](https://img.shields.io/badge/text%20%26%20figures-CC%20BY%204.0-lightgrey.svg)](paper/LICENSE) [![License: MIT](https://img.shields.io/badge/model-MIT-lightgrey.svg)](model/LICENSE)

Version 27, 15 October 2026.

**Links**
- Paper, version 27.1 (PDF): https://doi.org/10.5281/zenodo.23428319
- All versions (concept DOI): https://doi.org/10.5281/zenodo.23406475
- The fourteen-slide deck (PDF): https://zenodo.org/records/23428319/files/ai_compute_easy_deck_v28-2_2026-10-15.pdf?download=1
- This repository (model, register, code): https://github.com/desfitz/ai-compute-limits
- First open question (facility-opex dispute): https://github.com/desfitz/ai-compute-limits/issues/1
- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7620359
- Comments and corrections: desmond.fitzpatrick@nvara.ai

**Start here:** the fourteen-slide version, `paper/easy_deck_v28-2.pdf` (PowerPoint: `paper/easy_deck_v28-2.pptx`). The paper is `paper/paper_v27.pdf`.

This repository is the canonical home of a living estimate: can the AI data-center
build-out earn its carry, and under what demand growth? The paper is one *rendering*
of the estimate. The estimate itself lives in `model/parameters.json` — a register of
every input with its value, source, source date, next expected update and the model
parameter it feeds — and in the model that turns the register into numbers and figures.

The working method is borrowed from collaborative mathematics (Polymath; the Equational
Theories Project): one public object of record, small verifiable contributions, machinery
that checks every contribution, complete provenance, and collective credit.

## How it works
- **One input, one issue.** Every register entry has an open issue (`inputs/` label)
  containing the appraisal from Appendix G of the paper: what is known, the range in use,
  the likely bias of the source, what would improve it. Propose a better range there.
- **Contributions are pull requests that change `parameters.json`** (and nothing else,
  unless you are changing the model — see below). A PR must cite a source that a
  stranger can check. Judgment is welcome; label it as judgment.
- **CI rebuilds on every PR** and comments the delta: 2030 plateau z-score, break-even
  growth g*, P(profit | rationalize, 2030), and whether the change is *minor* or
  *material* under the re-issue rule.
- **Material changes** re-issue the paper with a delta log. Minor ones update tables.
- **Model changes** (new variables, new decompositions, changed structure) go through a
  `model/` PR with a written rationale and must reproduce the previous numbers when the
  new variable is set to its neutral value.
- **Verification bounties.** Entries marked `[VERIFY]` in the paper are open issues
  labeled `verify`; closing one with a primary source is the most valuable contribution
  a newcomer can make.

## Rebuild
    cd model && python3 rebuild.py          # numbers + delta vs last run
    cd model && python3 rebuild.py --figs   # also regenerates all figures

## Author
Desmond Fitzpatrick is the CEO of Nvara, an AI venture for enterprise systems, which he founded after resigning from IBM in May 2026. He spent his career at IBM: the first half on almost every aspect of chip technology, the second on IBM Z systems quality and resilience — ensuring some of the highest-quality products in the world — including responsibility for AI resilience on Z in his last three years. He is the principal author of the eight-nines availability claim for both z/OS and Linux on the mainframe, holds six IBM Outstanding Achievement Awards for work ranging from the impact of cosmic rays to the world's first copper metallurgy, and for his last four years presented the status of quantum computing for IBM, mostly to CTOs. At IBM he was responsible for many critical Fermi calculations over the years. He writes on issues of public importance, supported by data, in his occasional Substack column Data Democracy (datademocracy.substack.com). He holds a Ph.D. in physics from Brown University and lives in New York City. desmond.fitzpatrick@nvara.ai · ORCID 0009-0001-0534-2793

Citation metadata: `CITATION.cff`.

## Credit
Contributors are listed in `CONTRIBUTORS.md` in order of first merged contribution.
Re-issues of the paper carry the author line "D. Fitzpatrick and the AI Compute Limits
Project contributors"; anyone with a merged material contribution is a named contributor.

## Structure
    model/        parameters.json (the register), model5.py, rebuild.py, figure scripts, data
    paper/        LaTeX master and the current PDF
    figures/      generated figures (f1..f22)
    blueprint/    dependency graph: which inputs feed which outputs
    .github/      issue templates and the CI rebuild
