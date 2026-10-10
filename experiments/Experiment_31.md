# Experiment 31 — Global sharp reciprocal-threshold bounds for q=11–16

Date: 2026-10-10.

**Result: computer-assisted sharp theorem for each fixed integer q=11,12,13,14,15,16.**

Define F_(1/q)(a,b)=μ{t∈[0,1]: ||at||,||bt||,||(a+b)t||≥1/q}. For every positive integer pair a,b and each q in {11,...,16},

**F_(1/q)(a,b) ≥ (q-3)(q-4)/(q(q-1)).**

The bound is attained at (1,q-2), by the exact analytic formula proved in Experiment 28.

## Proof structure
By scaling, reduce to coprime a,b and a<=b. The uniform two-torus discrepancy bound from Experiment 26 yields

F_(1/q)(a,b) >= (1-3/q)^2 - 2/b.

The gap between the torus mean and proposed sharp minimum is
3(q-3)/(q²(q-1)). Thus all b>=B_q are automatically covered, where

B_q = ceil(2q²(q-1)/(3(q-3))).

The remaining finitely many coprime pairs a<=b<B_q are exhaustively verified by exact rational endpoint partition and integer midpoint tests.

## Complete finite certificates
| q | B_q | coprime pairs checked | violations | equality pair |
|---:|---:|---:|---:|---|
| 11 | 101 | 3044 | 0 | (1,9) |
| 12 | 118 | 4200 | 0 | (1,10) |
| 13 | 136 | 5570 | 0 | (1,11) |
| 14 | 155 | 7236 | 0 | (1,12) |
| 15 | 175 | 9250 | 0 | (1,13) |
| 16 | 197 | 11698 | 0 | (1,14) |

Total **40,998** exact coprime-pair cases. No floating-point decisions. Dataset: `data/experiment_31_q11_to_16.csv`. Reproduce: `python3 src/experiment_31_verify.py`.

## Scope and novelty
Together with Experiment 30 (q=5..10), this establishes the sharp formula for **all integer q=5..16** through twelve separate finite computer-assisted certificates. It does not prove it for all q>=5, nor the 16-runner Lonely Runner Conjecture. A specialist literature audit remains necessary. Existing literature uses correlated safe-time sets and Fourier/Bohr-set methods; elementary interval discrepancy is unlikely to be independently novel.

## Deep novelty comparison
See `docs/DEEP_NOVELTY_AUDIT_2026_10_10.md` and `references/lonely_runner.bib`. Perarnau–Serra (2016) directly concerns correlations of near-origin runner times; the 2025 survey is a broad guide to prior results. Beck–Everett (2026) emphasizes short integer relations, including additive triples as a special example. Rosenfeld, Trakulthongchai, Sungkawichai–Trakulthongchai, and Allikvere address increasing runner counts using quite different computer-assisted methods. The global sharp **measure** inequality is narrower than a proof of the full Lonely Runner Conjecture.
