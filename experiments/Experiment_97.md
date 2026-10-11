# Experiment 97 — Exact modular enumeration of all isolated safe times

Date: 2026-10-11. All-dimensional theorem PROVED; 776 primitive vectors independently tested. Unrestricted LRC is NOT solved.

## Theorem 97.1 — Complete isolated-witness classification
Let V be k>=2 distinct positive integer speeds, q=k+1, and S={t mod 1: ||vt||>=1/q for all v in V}. For each unordered pair a<b in V put g=gcd(a,b), A=a/g, B=b/g. Discard the pair unless q divides A+B. For a qualifying pair put c=(A+B)/q, and let m0 be the unique residue modulo A satisfying B*m0 = -c (mod A). When A=1, take m0=0. For j=0,...,g-1 define

 t_j=(q*(m0+j*A)+1)/(q*a).

Let D(V) be the union over qualifying pairs of t_j and (1-t_j) modulo 1. Then

  {isolated points of S} = {t in D(V): ||vt||>=1/q for every v in V}.

Every member of D(V) is an opposite-boundary collision; no isolated safe time lies outside D(V). The candidate set has size at most 2 sum_{qualifying pairs} gcd(a,b), recovering Experiment 96's bound.

## Proof
For a fixed pair a=gA,b=gB, a collision with {at}=1/q and {bt}=(q-1)/q must have t=(qm+1)/(qa) for an integer 0<=m<a. The second phase constraint is b(qm+1)+a divisible by qa. After dividing by g, this is qBm+A+B divisible by qA. Thus q divides A+B, and writing c=(A+B)/q reduces the condition to Bm=-c (mod A). Since gcd(A,B)=1, there is exactly one residue m0 modulo A, and exactly g representatives m0+jA in [0,a). Reflection t->1-t produces all reverse-orientation collisions.

If t is safe and simultaneously has a speed at phase 1/q and another at phase (q-1)/q, then the first speed is forbidden immediately to the left of t, and the second immediately to the right. Hence t is isolated in S. Conversely, Experiment 96 Theorem 96.1 proves that any isolated safe time has both opposite boundary types, so it must appear in the modular construction. This proves equality. QED.

## Corollary 97.2 — Exact finite isolated-witness decision
The complete isolated-safe-point set is computable by generating at most 2 sum_{qualifying pairs} gcd(a,b) rational candidates and checking all k phase constraints. The algorithm does not need the full q*lcm(V) grid or a boundary-event sweep. If it returns no points, S may still have a safe interval; it does NOT follow that LRC fails.

## Executed exact verification
The committed Python script experiments/experiment_97_isolated_modular.py independently compares the modular generator (filtered by exact Fraction phase checks) with direct full-grid enumeration of isolated safe vertices, using exact integer tests for both grid vertices and open cells.

k=3,N=14: 325 primitive vectors; 432 generated candidates; 256 isolated safe times.
k=4,N=11: 325 vectors; 788 candidates; 378 isolated safe times.
k=5,N=9: 126 vectors; 110 candidates; 60 isolated safe times.
TOTAL: 776 vectors, 1,330 candidates, 694 isolated safe times. All exact set equalities passed.

Examples: (1,2,3) has isolated witnesses {1/4,3/4}; (1,3,4,7) has {1/5,2/5,3/5,4/5}; (1,3,9) has {1/4,5/12,7/12,3/4} after filtering six candidates.

## Novelty and Q1 gate
This is an exact constructive strengthening of the elementary opposite-boundary argument of Experiments 77 and 96. Modular inverses and collision enumeration are classical; independent mathematical priority is not established. In particular, it does NOT rule out hypothetical speed vectors with empty safe sets, and does NOT prove unrestricted LRC.

Literature checked: Beck–Everett (2026), arXiv:2609.06259, on short relations of tight/counterexample configurations; Zhang (2026), arXiv:2608.13599v2, on tight configurations; Malikiosis–Santos–Schymura (2025), DOI 10.1017/fms.2025.10107, on finite checking. All three already occur in references/lonely_runner.bib.

Verdict: theorem PROVED; 776 exact audits PASS; unrestricted LRC OPEN; Q1-journal-level independent novelty NOT ESTABLISHED.
