# Experiment 42 — Exact higher-order overlap certificate in arbitrary dimensions

Date: 2026-10-10. Status: rigorous exact combinatorial identity; verified nontrivial example. **Not a solution of unrestricted LRC.**

## Theorem 42.1 (complete inclusion-exclusion fiber criterion)

Let q>=2, m>=2, A and B be finite lists of positive integer speeds, every a∈A divisible by m. Let t0 satisfy ||a t0||>=1/q for all a∈A. For each b∈B set

E_b={h∈{0,...,m−1}: ||b(t0+h/m)||<1/q}.

Then the exact number of successful shifts is

N=m−Σ_{∅≠J⊆B} (−1)^{|J|+1} |∩_{b∈J}E_b|.

Consequently **N>0** is an exact necessary-and-sufficient criterion for a safe time *within this particular fiber* t0+Z/mZ, for arbitrary dimension |A|+|B|. It is only a sufficient condition for existence of an arbitrary safe time.

**Proof.** For each h, the indicator that h is forbidden by at least one b is the alternating sum of indicators of its nonempty forbidden-set intersections. Sum over h and subtract from m. The A-speeds are invariant under h/m, since a/m is integral. QED.

## Example defeating the earlier tree bound

Take q=6, m=8, A=(8), B=(1,4,6,7), t0=1/48. The stable speed 8 has position 1/6, which is safe.

The four forbidden shift sets have sizes 3,4,4,3. Their aggregate intersection totals by order are:
S1=14, S2=11, S3=5, S4=1.
Therefore forbidden count =14−11+5−1=7, and **one** shift survives: h=3. The exact safe time is t=19/48.

At t=19/48, distances to nearest integer for speeds (8,1,4,6,7) are respectively
(1/6,19/48,5/12,3/8,11/48), each >=1/6.

The maximum-spanning-tree pairwise correction yields an upper bound of 8 forbidden shifts, so Experiment 41's sufficient test is inconclusive; the exact higher-order calculation certifies the witness.

## Verification and reproducibility

Ran `python /tmp/exp42.py` with exact rational arithmetic: output sizes [3,4,4,3], inclusion-exclusion terms [14,11,5,1], forbidden=7, valid shifts=[3], witness=19/48. Exhaustively verified inclusion-exclusion on all 8^4=4096 four-set systems over a three-element universe. Zero failures.

Code: `src/experiment_42_inclusion_exclusion.py`; results: `data/experiment_42_results.csv`.

## Literature and originality

The inclusion-exclusion identity is classical and **not novel**. The application of time-shift fibers is closely related to the original LRC methods and the correlations studied by Perarnau–Serra (2016). Added the primary arXiv-verified Ludovic Rifford (2021) preprint *On the time for a runner to get lonely*, arXiv:2111.13688, to `references/lonely_runner.bib` as background on temporal and covering formulations. Its arXiv identity and author are verified; no peer-reviewed status is asserted.

## Unresolved general problem

For some configurations every chosen fiber may have N=0 even if other times are safe. Higher-order inclusion-exclusion is exponentially costly in |B|, and no theorem here guarantees N>0 for all speed vectors. Thus general LRC, including the sixteen-runner case, is **not solved**.
