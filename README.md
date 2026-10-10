# Thirteen–Twenty: Additive-Triple Safe-Time Research

**Research status (10 October 2026):** A sharp, computer-assisted bound for a *three-speed safe-time measure*, not a solution of the Lonely Runner Conjecture. **Novelty not established.** Independent verification and specialist prior-art review are still required before submission.

## Main claim
For positive integers `a,b`, define
```
F(a,b) = measure{ t in [0,1]: ||a t||, ||b t||, ||(a+b)t|| >= 1/16 }
```
where `||x||` denotes distance to the nearest integer.

The result under investigation is **F(a,b) >= 13/20**, with equality at `(a,b)=(1,14)`.

## Proof structure
1. Scaling invariance: `F(da,db)=F(a,b)`; reduce to `gcd(a,b)=1`.
2. Set `A={x in R/Z: ||x||>=1/16}`. Inclusion–exclusion gives the independent two-torus average of `1_A(x)1_A(y)1_A(x+y)` as `169/256`.
3. For coprime `a,b`, partition `t=(k+x)/b`. For fixed `x`, the other phase is a rotated equispaced `b`-point grid. The allowed set is the intersection of two circle arcs, with at most two connected arcs. Elementary interval discrepancy yields `|F(a,b)-169/256|<=2/b`. By symmetry this is at most `2/max(a,b)`.
4. The discrepancy implies `F(a,b)>=13/20` whenever `max(a,b)>=197`.
5. An exact rational endpoint sweep evaluates all **11,698** coprime pairs `1<=a<=b<=196`: no violations; equality only at `(1,14)`. See `src/exact_check.cpp` and `data/exact_results.csv`.

The finite certificate must be independently reproduced. The analytic argument and code should be peer reviewed for hidden assumptions.

## Important limitations
- The result concerns *three* specified speeds, not fifteen arbitrary relative speeds.
- It does **not** resolve the 16-runner case.
- The grid-discrepancy technique and runner-correlation methods are not new by themselves.
- The exact sharp constant may overlap previous published results: originality is **unverified**.

## Repository organization
- `docs/RESEARCH_REPORT.md` — mathematical proof and novelty caveats.
- `src/exact_check.cpp` — reproducible standard C++ exact-arithmetic verifier.
- `data/exact_results.csv` — all finite-case results.
- `docs/RESEARCH_HISTORY.md` — concise Experiments 11–25 chronology.
- `docs/NOVELTY_AUDIT.md` — comparable literature and open checks.

## Reproduce
```bash
g++ -std=c++17 -O2 -Wall -Wextra src/exact_check.cpp -o exact_check
./exact_check data/exact_results_regenerated.csv
```
Expected stderr: `tested=11698 violations=0 equality=1 minimum=1,14=2184/3360`.

## Background research
- Perarnau & Serra, *Correlation among runners and some results on the Lonely Runner Conjecture* (2016), DOI: 10.37236/5123.
- Giri & Kravitz, *The structure of Lonely Runner spectra* (2025).
- Beck & Everett, *Lonely Runner Relations*, arXiv:2609.06259 (2026).

For detailed scope and caveats see the reports in `docs/`.
## Latest research update — Experiment 31 (2026-10-10)
The sharp reciprocal-threshold safe-time minimum has been established with analytic finite reduction and exact certificates for each integer **q=5,...,16**. The exact special-family formula is proved for all q>=5; global minimization for q>=17 remains open. See [Experiment 31](experiments/Experiment_31.md), [verification source](src/experiment_31_verify.py), and [results](data/experiment_31_q11_to_16.csv).

**Deep novelty audit:** [10 October 2026](docs/DEEP_NOVELTY_AUDIT_2026_10_10.md). **Reusable BibTeX:** [references/lonely_runner.bib](references/lonely_runner.bib), 12 entries. No proof of the general sixteen-runner conjecture or research priority is claimed.
