# Experiment 46 — Exact strict-versus-tight classification in every finite integer dimension

Date: 2026-10-10. Status: rigorous exact decision theorem and completed finite enumeration. **General LRC not solved.**

## Theorem 46.1 (exact safe-measure decomposition)

Let V=(v_1,...,v_k) be positive integer speeds, q=k+1. Define
E={0,1}∪{(qj±1)/(qv_i)∈[0,1]: i=1,...,k, j=0,...,v_i}.

Sort E as 0=e_0<...<e_s=1. On each open cell (e_j,e_{j+1}), every indicator 1[||v_i t||>=1/q] is constant, because every transition of the i-th inequality occurs at a member of E. Therefore the exact safe measure is

μ(V)=Σ_{j: all i satisfy ||v_i(e_j+e_{j+1})/2||>=1/q}(e_{j+1}−e_j).

All safe times are the union of the closed safe cells and isolated safe endpoints. Consequently the configuration falls into exactly one of three categories:
1. μ(V)>0: a nonempty open interval of strictly safe times exists.
2. μ(V)=0 but at least one endpoint in E is safe: safe times exist only at isolated boundary points (tight-only).
3. No safe endpoint or safe cell: the configuration is a counterexample to LRC for that particular V.

**Proof.** Each individual safe set is a finite union of closed intervals with endpoints where ||v_i t||=1/q, and these are precisely members of E. Between consecutive members of E no indicator can change. Midpoint evaluation therefore gives the exact length contribution. A safe point with all inequalities strict has a safe neighborhood by continuity; hence if μ(V)=0 every safe point must lie on E. Conversely, a safe open cell yields μ(V)>0. QED.

This is an exact all-dimensional finite classification, not a proof that category 3 is empty.

## Executed exact enumeration

Every distinct k-element subset of {1,...,9} was checked for k=2,...,5, using Python fractions without floating point.

| k | Total | Positive measure | Tight-only | No witness |
|---|---:|---:|---:|---:|
| 2 | 36 | 32 | 4 | 0 |
| 3 | 84 | 81 | 3 | 0 |
| 4 | 126 | 123 | 3 | 0 |
| 5 | 126 | 124 | 2 | 0 |
| **Total** | **372** | **360** | **12** | **0** |

Illustrations:
- V=(1,2,3), q=4: safe measure 0; 2 isolated safe times.
- V=(1,2,3,4), q=5: safe measure 0; 4 isolated safe times.
- V=(1,2,3,4,5), q=6: safe measure 0; 2 isolated safe times.
- V=(1,2,4,8), q=5: safe measure 1/10; 2 positive-length intervals.

## Relation to Experiment 45

Beck and Everett (2026), *Lonely Runner Relations*, arXiv:2609.06259, prove short integer relations for counterexamples **or tight instances**. The 12 tight-only instances in this bounded search illustrate why a short relation is not evidence of a counterexample. The theorem is already present under citation key BeckEverett2026.

## Reproducibility and literature

Exact executable: src/experiment_46_safe_measure.py.
Machine-readable summary: data/experiment_46_results.csv.
No new external reference is used: Beck–Everett (2026), the Perarnau–Serra survey, and earlier exact-certification work are already in the append-only BibTeX library. No duplicate or unverified bibliographic entry is introduced.

## Novelty / unresolved

Finite breakpoint integration is a classical technique, not a new theorem in analysis. The experiment contributes an independently reproducible strict/tight classification audit for the selected finite speed sets. The all-dimensional theorem classifies any given integer speed vector, but does not establish that every vector is safe. General LRC remains unsolved.
