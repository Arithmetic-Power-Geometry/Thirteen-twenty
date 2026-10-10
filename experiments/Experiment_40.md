# Experiment 40 — All-dimensional modular-fiber extension theorem

Date: 2026-10-10. Status: **proved sufficient-condition theorem**, independently checked by exact arithmetic. Not a solution of the unrestricted Lonely Runner Conjecture.

## Theorem 40.1

Fix integers q>=2 and m>=2 and any finite list of positive integer speeds V=A ∪ B. Suppose m divides each speed in A and some real t0 satisfies ||a*t0||>=1/q for all a∈A. For each b∈B let g_b=gcd(b,m), d_b=m/g_b. If

    Σ_(b∈B) g_b ceil(2*d_b/q) < m,

then there is h∈{0,...,m−1} such that t=t0+h/m satisfies ||v*t||>=1/q for every v∈V.

**Proof.** Every a∈A remains fixed modulo 1 because a*h/m is an integer. For each b∈B, as h ranges modulo m, the values b*h/m modulo 1 visit each point of a uniformly spaced orbit of d_b points exactly g_b times. For any phase shift, the forbidden open arc {x: ||x||<1/q} has length 2/q. An open arc of length 2/q contains at most ceil(2*d_b/q) points of a uniform d_b-grid (including when its endpoints fall on grid points). Thus b rules out at most g_b ceil(2*d_b/q) choices of h. The union bound gives fewer than m forbidden shifts, leaving at least one valid h. QED.

This is a *sufficient* condition, not a necessary one. The theorem does not assume that the B speeds are coprime to m and holds in any finite dimension. At q=k+1 it supplies explicit certificates for some k-relative-speed Lonely Runner instances.

## Exact computed examples

| q | m | total speeds | stable | moving | sum of individual upper bounds | actually successful shifts | first witness |
|---|---|---|---|---|---|---|---|
| 6 | 11 | 5 | 3 | 2 | 8 | 6 | 13/66 |
| 16 | 31 | 15 | 10 | 5 | 20 | 18 | 33/496 |

For q=16, A=(31,62,...,310), B=(1,2,3,4,5), and t0=1/496. This is one certified sixteen-total-runner configuration, not the general sixteen-runner theorem.

Per-runner forbidden counts:
- q=6, m=11: b=1 excludes 3 shifts (bound 4); b=2 excludes 4 shifts (bound 4).
- q=16, m=31: b=1 excludes 3 shifts (bound 4); b=2,3,4,5 each exclude 4 (bound 4).

The Python script `src/experiment_40_fiber.py` was executed with exact Fraction arithmetic. It also exhaustively checked the orbit-count bound for all q=3,...,8, m=2,...,19, b=1,...,2m, and 2q rational phase offsets.

## Literature and originality audit

The finite-shift/pigeonhole mechanism has substantial precedent. In particular, the 2026 paper *Amending the Lonely Runner Spectrum Conjecture* (Electronic Journal of Combinatorics 33(1), P1.38) contains a related gcd-preserving pre-jump argument. A July 2026 Arbiter research update also reports a p-adic valuation rigidity theorem using invariant time shifts; it is not treated as peer-reviewed priority evidence. The broader literature includes Bienia–Goddyn–Gvozdjak–Sebő–Tarsi (1998), *Flows, View Obstructions, and the Lonely Runner*, Journal of Combinatorial Theory Series B 72(1), 1–9, DOI 10.1006/jctb.1997.1770. That verified publisher entry is appended to `references/lonely_runner.bib`.

**No claim of original discovery** is made for the shift method. This report's explicit composite-modulus counting inequality is rigorously established here but has not been cleared against all prior variants.

## What is not solved

No argument here guarantees the sufficient condition for every integer speed vector. Therefore the unrestricted LRC and the full sixteen-runner case remain unsolved. A further research goal is to combine different moduli m, recursively preserve already-safe groups, and prove that at least one such decomposition must exist.
