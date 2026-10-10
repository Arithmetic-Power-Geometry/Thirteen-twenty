# Experiment 29 — Bounded search for the global reciprocal-threshold minimizer

Date: 2026-10-10

## Objective
For integer q>=5, determine whether the exact value from Experiment 28,
`M_q=(q-3)(q-4)/(q(q-1))`,
is the minimum of `F_(1/q)(a,b)` over *all* positive integers a,b.

## Completed exact computation
For each q in `{5,6,7,8,9,10,12,16,20,24,32}`, evaluate every coprime pair `1<=a<=b<=100`, using rational integer endpoints and midpoint tests. There are 3,044 pairs per threshold and 33,484 exact pair-threshold tests in total.

For all 11 thresholds, the minimum equals `M_q`, attained **uniquely in the checked range** at `(a,b)=(1,q-2)`. No violations were found.

| q | exact minimum | sole minimizing coprime pair in tested range |
|---:|:---:|:---:|
| 5 | 1/10 | (1,3) |
| 6 | 1/5 | (1,4) |
| 7 | 2/7 | (1,5) |
| 8 | 5/14 | (1,6) |
| 9 | 5/12 | (1,7) |
| 10 | 7/15 | (1,8) |
| 12 | 6/11 | (1,10) |
| 16 | 13/20 | (1,14) |
| 20 | 68/95 | (1,18) |
| 24 | 35/46 | (1,22) |
| 32 | 203/248 | (1,30) |

Data: `data/experiment_29_summary.csv`. Reproduction: `python3 src/experiment_29_scan.py 100`. The script independently computes each pair using Python `Fraction`, and makes exact comparisons.

## The conjecture remains open
**Conjecture:** For all q>=5 and all positive a,b, `F_(1/q)(a,b)>=M_q`, with the expected equality family `(1,q-2)` up to symmetry and common scaling.

The finite tests above **do not prove** this. Experiment 26 gives the analytic bound
`F_(1/q)(a,b) >= (1-3/q)^2 - 2/max(a,b)`
for coprime a,b. For each fixed q, if `(1-3/q)^2>M_q`, this reduces the global conjecture to a *finite* but potentially very large exact computation. The positive gap is
`(1-3/q)^2 - M_q = (q-3)(q+3)/(q²(q-1))`.
The corresponding sufficient large-speed cutoff is
`max(a,b) >= ceil(2 q²(q-1)/((q-3)(q+3)))`.
The finite search here was only through b<=100, so it does not close that gap for every q.

## Novelty and literature
See `references/lonely_runner.bib` for primary-source metadata, and `docs/NOVELTY_AUDIT.md` for relevance and limitations. The techniques overlap existing correlation and Bohr-set approaches (Perarnau–Serra 2016; Tao 2018). Jensen (2026) studies mixed thresholds; Beck–Everett (2026) studies short relations. Priority for this conjecture and its fixed-q special cases is unverified.

A recent preprint by Allikvere (2026, arXiv:2609.02604v2) claims the fourteen- and fifteen-total-runner cases, with archived certificates; it does **not** establish the sixteen-runner case. Our three-speed measure result is not a sixteen-runner proof.

## Next step
For each fixed q, calculate the rigorous cutoff and verify *all* coprime pairs below it, starting with q=5 or 6. Alternatively derive a uniform stronger discrepancy bound that handles all q symbolically. Independent reproduction and a full literature theorem comparison remain essential.
