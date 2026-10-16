# Community review — how the estimate is improved

The model is Wikipedia's in spirit (anyone can improve it, every claim needs a source, the
history is public) with one difference forced by the subject: a change to one number
propagates through every result, so edits are *proposed and checked* before they land,
not made live and reverted after. Wikipedia edits first and discusses on the talk page;
here the talk happens first and the edit lands when it passes.

## The five stages of an input
Every register entry carries a grade in `parameters.json`:

| Grade | Meaning | Community goal |
|---|---|---|
| **J** | Judgment range, no external anchor | Find any primary source; promote to S or P |
| **S** | Secondary source, or a chain of primaries with judgment steps | Replace the weakest link with a primary |
| **P** | Anchored on a primary source | Keep current; re-check on each disclosure |
| **secondary variable** | Too loose to trust at a range; swept in its own figure | Data that would let it collapse to a range |
| **settled** | Resolved by an outcome (e.g. calendar-2026 revenue once audited) | Record the outcome and the error |

Each entry's grade, and the count by grade, is the project's quality dashboard — the
analogue of Wikipedia's article classes. Moving inputs from J to S to P is the work.

## Where upgrades happen
1. **Discussion** — one GitHub Issue per input holds its appraisal (evidence, range, bias,
   what would improve it). Propose there. This is the talk page.
2. **Proposal** — a pull request changing that entry in `parameters.json` with source,
   date and bias note. This is the edit.
3. **Check** — CI rebuilds the model and comments the delta and the minor/material label.
   This is the part Wikipedia lacks: the consequence of the edit is computed before it lands.
4. **Review** — one maintainer (two, from different disciplines, for model or
   decomposition changes). Reviewers check the source and reasoning, never the conclusion.
5. **Release** — merged changes accumulate; a versioned release (Zenodo DOI, change-marked
   PDF, delta log) is cut when the rule says material or after each earnings cycle.

## Reviewer roster
Reviewers are contributors who have made two merged, sourced contributions and are
invited by a maintainer; listed in CONTRIBUTORS.md with their discipline. The first
reviewers (Francis Pedraza, Matthew Fitzpatrick, Viraj Mehta) are grandfathered.

## Disputes
Two defensible sourced ranges for one input: neither wins. The input becomes a secondary
variable and is shown across both until a disclosure settles it (GOVERNANCE.md).

## What a good first contribution looks like
- Close a `verify` issue with a filing citation (page and line).
- Find a primary for any J-grade entry.
- Add a link to REFERENCES.md with a quality rating — even a rejected one, with the reason.
