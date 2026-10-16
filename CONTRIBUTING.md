# Contributing

## The three kinds of contribution, easiest first

1. **Verify a number.** Find the issue labeled `verify`, locate the primary source
   (filing, transcript, standard, dataset), quote the exact figure and page, and open a PR
   that (a) updates `source` / `source_date` in `parameters.json` and (b) removes the
   `\verify` mark in `paper/paper.tex`. No modeling required.

2. **Improve a range.** Open the input's issue. State: the range you propose
   (min / mode / max), why, and the source. If it is judgment, say so — judgment with a
   stated reason is a valid contribution; an unexplained number is not. Then open a PR
   changing that one entry. CI will post what it does to the result.

3. **Decompose a variable.** The best contributions replace one judgment range with a
   chain of sourced components (see Appendix "Decomposing the Dominant Uncertainties").
   Propose the chain in the issue first. A decomposition PR adds the components to the
   register, adds the derived parameter to `model5.py` if needed, and must show the
   variance budget before and after.

## Rules that keep the estimate honest
- **Provenance or it did not happen.** Every register value has a source a stranger can open.
- **Ranges, not points.** Triangular min / mode / max. If you only know the mode, say what
  bounds you would defend.
- **Say who benefits.** If your source is a company, a forecaster or an advocacy group,
  note which direction it is likely to shade the number.
- **No result-driven edits.** A PR whose only rationale is the result it produces is closed.
  Move inputs for input reasons.
- **Secondary variables stay swept.** An input the maintainers have declared secondary is
  shown across its range in a figure, not collapsed to a mode, until data arrive.
- **The re-issue rule is mechanical.** CI decides minor vs material; maintainers decide
  when to cut a release, not whether the label was right.

## Review
Each PR needs one maintainer review; decomposition and model PRs need two, from different
disciplines (finance / engineering / economics). Reviewers check the source, not the
conclusion.

## Etiquette
Argue about numbers, not people. State uncertainty. It is fine to be wrong in public; it is
not fine to be unsourced in public.
