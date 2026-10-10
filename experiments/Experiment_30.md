# Experiment 30 — Six globally sharp reciprocal-threshold bounds

Date: 2026-10-10

**Result: PROVED by analytic reduction and exact finite computation**, for q=5,6,7,8,9,10.

For every positive integer pair a,b, define
`F_(1/q)(a,b)=μ{t in [0,1]: ||at||,||bt||,||(a+b)t||≥1/q}`.

For each integer `q∈{5,6,7,8,9,10}`:

`F_(1/q)(a,b) ≥ (q-3)(q-4)/(q(q-1))`.

Equality holds at `(a,b)=(1,q-2)`, up to swapping a,b and common integer scaling. Among coprime pairs with a<=b, the exact certificate found this unique equality pair.

## Analytic reduction

For coprime a,b, Experiment 26 proves
`F_(1/q)(a,b) ≥ (1-3/q)^2 − 2/max(a,b)`.

The difference between the torus average and the proposed sharp constant is exactly
`(1-3/q)^2 − (q-3)(q-4)/(q(q-1)) = 3(q-3)/(q²(q-1))`.

Consequently, every coprime pair with
`max(a,b) >= B_q := ceil(2q²(q-1)/(3(q-3)))`
automatically satisfies the target inequality.

Scaling invariance reduces arbitrary a,b to coprime ones. Therefore it remains only to check
`1<=a<=b<B_q` and `gcd(a,b)=1`.

## Exhaustive finite certificate

A freshly compiled C++17 exact-arithmetic verifier was run for all remaining pairs. The program partitions time into exact rational intervals using denominator D=q*a*b*(a+b), tests integer midpoints and compares fractions by integer cross multiplication. No floating-point decisions.

| q | B_q | coprime pairs tested | violations | equality cases |
|---:|---:|---:|---:|---|
| 5 | 34 | 344 | 0 | (1,3) |
| 6 | 40 | 474 | 0 | (1,4) |
| 7 | 49 | 712 | 0 | (1,5) |
| 8 | 60 | 1086 | 0 | (1,6) |
| 9 | 72 | 1564 | 0 | (1,7) |
| 10 | 86 | 2230 | 0 | (1,8) |

Total: 6410 exact finite cases. Full stdout is in `data/experiment_30_results.csv`. Source: `src/experiment_30.cpp`. Compile using `g++ -O2 -std=c++17 src/experiment_30.cpp -o experiment_30` and run `./experiment_30`.

The exact equality formula at (1,q-2) for all q>=5 was analytically proved in Experiment 28.

## Limits

This is a computer-assisted theorem for six fixed q, not a theorem for all q>=5. It does not solve the 16-runner Lonely Runner Conjecture. Novelty relative to existing results on runner correlations, threshold spectra, and Bohr sets has not been established.

## Literature

See `references/lonely_runner.bib` for verified metadata, including Perarnau–Serra 2016, Tao 2018, Giri–Kravitz, Beck–Everett, and the newer computational results of Rosenfeld 2025, Sungkawichai–Trakulthongchai 2026, and Allikvere 2026. Prior-art full-text comparison remains required.
