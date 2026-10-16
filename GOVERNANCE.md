# Governance — how this project runs

Modeled on the collaborative-mathematics projects (Polymath 2009–; the Equational Theories
Project 2024–): a public object of record, small verifiable contributions, machinery that
checks them, complete provenance, collective credit. Adapted for an estimate rather than a
proof: the object of record is a register of ranges, and "checked" means sourced and
propagated, not proved.

## Roles
- **Maintainer** (initially one): merges, cuts releases, owns the re-issue rule. Adds
  co-maintainers by discipline as contributors emerge.
- **Discipline reviewers**: at least one each in corporate finance, data-center
  engineering, and economics. Review sources and reasoning, not conclusions.
- **Contributors**: anyone with a merged PR. Listed in CONTRIBUTORS.md.

## The object of record
`model/parameters.json`. The paper is derived from it. If the paper and the register
disagree, the register is right and the paper is out of date.

## Community review
See COMMUNITY_REVIEW.md: inputs are graded J / S / P (judgment, secondary, primary); the work is moving them up. Propose in the input's issue, change the register by PR, CI computes the consequence, a reviewer checks the source, releases are versioned.

## What counts as a contribution
Verifying a flagged figure; improving a range with a source; decomposing a variable into
sourced components; adding a variable with a rationale; finding an error in the model or
the propagation; improving a figure or an explanation. In roughly that order of value for
newcomers.

## What does not
Point estimates without ranges; ranges without sources or stated reasoning; edits
justified by the result they produce; rewriting conclusions without changing inputs.

## Releases
- **Minor**: after any merged input change that CI labels minor. Tables regenerated,
  version bumped, no announcement.
- **Material**: when CI labels a change material (|Δz| ≥ 0.5, |Δg*| ≥ 5 points,
  |ΔP(profit, rationalize, 2030)| ≥ 15 points, or a registered observable outside its
  P10–P90), or after each Big-5 earnings cycle. Re-issued with a delta log; deposited on
  Zenodo with a new DOI; contributors since the last material release named.

## Disagreement
If two contributors defend different ranges for the same input with defensible sources,
the maintainer does not pick one. The input becomes a *secondary variable*: shown across
both ranges in its own figure until data settle it. This is the project's answer to
"who is right": show the result across both and wait for the disclosure.

## Corporate participation
Company employees are welcome and their contributions valuable — they have the data.
Disclose affiliation. A contribution from an interested party is held to the same source
standard as any other, and the bias note in the issue template applies to oneself.

## Retiring the project
The estimate ends when the question is settled: when calendar-2028 revenue and the 2028–29
impairment record are public. The final release records which inputs were right, which
were wrong, and by how much. That post-mortem is part of the deliverable.
