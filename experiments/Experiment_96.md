# Experiment 96 — Arithmetic collision bound for isolated safe witnesses

Date: 2026-10-11. Status: all-dimensional theorem proved and independently checked on 776 primitive vectors. Unrestricted Lonely Runner Conjecture remains open.

## Theorem 96.1 (Opposite-boundary collision)
Let V be k>=2 distinct positive integer speeds, q=k+1, and S={t mod 1: ||vt||>=1/q for all v in V}. If t is an isolated point of S, then there are two distinct speeds a,b in V such that {at}=1/q and {bt}=(q-1)/q, or the reverse.

**Proof.** For each v, the closed safe set {t:||vt||>=1/q} has a boundary of two types: entering a safe arc at {vt}=1/q (positive-side interior) or leaving a safe arc at {vt}=(q-1)/q (negative-side interior). If all active boundary constraints at a safe t have the same type, one of the two adjacent small one-sided neighborhoods remains safe for every active constraint; all inactive constraints are strictly safe near t. Hence t is not isolated. Therefore an isolated t must have both types, contributed by distinct speeds since q>=3. QED.

## Theorem 96.2 (Arithmetic bound, all dimensions)
Let g_ab=gcd(a,b), and let
P_q(V)={(a,b):a<b in V, q divides (a+b)/g_ab}.
Then the number of isolated safe points satisfies

N_iso(V) <= 2 * sum_{(a,b) in P_q(V)} g_ab.

**Proof.** Fix a pair (a,b), g=gcd(a,b), A=a/g, B=b/g. The simultaneous congruences {at}=1/q, {bt}=-1/q have a solution precisely when q divides A+B: necessity follows by multiplying the first congruence by B, the second by A and subtracting; sufficiency follows from the generalized CRT on the circle. If solvable, there are exactly g solutions modulo 1 because the homomorphism t -> (at,bt) has kernel of order g. The reversed orientation contributes at most g further solutions. By Theorem 96.1 every isolated safe time belongs to at least one such pair-collision set. Taking a union bound proves the inequality. QED.

## Corollary 96.3
If P_q(V) is empty, S has no isolated points. Consequently, if S is nonempty then S contains a nondegenerate safe interval. This does not assert S is nonempty and therefore does not solve LRC.

If S is finite and nonempty (a tight configuration with witnesses), its cardinality is at most the bound above. The condition P_q(V) nonempty was already obtained in Experiment 77; the quantitative bound is the new extension studied here.

## Exact reproducible audit
The program experiments/experiment_96_isolated_collisions.py was executed with Python Fraction and independent integer-grid calculations on primitive speed vectors:
k=3, max speed 14: 325 vectors, 256 isolated points;
k=4, max speed 11: 325 vectors, 378 isolated points;
k=5, max speed 9: 126 vectors, 60 isolated points.
Total 776 primitive vectors and 694 isolated points. Every isolated point was contained in the opposite-boundary candidate set, and every candidate set respected the gcd-weighted bound.

Examples:
V=(1,2,3): 2 candidates, bound 2, 2 isolated points (1/4,3/4).
V=(1,3,4,7): 4 candidates, bound 4, 4 isolated points (1/5,2/5,3/5,4/5).
V=(1,2,3,4): 4 candidates, bound 4, 4 isolated points.
V=(1,3,9): 6 candidates, bound 8, 4 isolated points.

## Novelty and priority
The opposite-boundary divisibility obstruction is already recorded in Experiment 77. This experiment adds a quantitative gcd-weighted count and exact enumeration. The proof uses elementary congruences, so independent research priority and Q1-journal-level novelty are NOT established. It is not a new solution to unrestricted LRC.

Literature compared: Malikiosis, Santos and Schymura (2025), Forum of Mathematics, Sigma 13 e164, DOI 10.1017/fms.2025.10107; Czerwiński (2018), Discrete Mathematics 341(5), 1301–1306, DOI 10.1016/j.disc.2018.02.002. Both already appear in references/lonely_runner.bib.

## Verdict
Theorems 96.1 and 96.2: PROVED. Exact tests: 776 PASS. Unrestricted LRC: NOT SOLVED. Q1 breakthrough: NOT ESTABLISHED.
