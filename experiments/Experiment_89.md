# Experiment 89 — Counterexample deletion obstruction and primitive fragmentation barrier

Date: 2026-10-10
Status: two rigorously proved all-dimensional structural theorems, exact tests executed. **Unrestricted Lonely Runner Conjecture not solved.**

## Theorem 89.1 — Necessary deletion inequality for zero-measure safe sets

Let V be k>=2 distinct positive integer speeds, q=k+1. For v in V, let S_{-v} be the safe set at the FINAL threshold 1/q for all speeds V excluding v. Write A_v=mu(S_{-v}) and m_v for the number of positive-length interval components of S_{-v} (split at t=0 if needed). If the full k-speed safe set has zero measure, then for EVERY v in V,

    A_v <= 2*m_v/(q*v).

In particular every genuine counterexample to unrestricted LRC must satisfy these inequalities for all its deletions.

**Proof.** Experiment 88's bounded-primitive estimate gives
mu(S_{-v} intersect {t:||vt||>=1/q}) >= (1-2/q)(A_v-2m_v/(qv)).
The left side is the full safe-set measure. If it is zero, since 1-2/q>0, the expression in parentheses must be <=0. This is the asserted necessary inequality. QED.

**Important:** zero safe-set measure does NOT mean LRC fails: tight instances can have isolated safe times. Therefore this inequality is necessary for counterexamples but does NOT characterize them.

## Theorem 89.2 — No dimension-only component/measure control, even for primitive vectors

For every integer h>=1, let N=3h+1 and V=(1,N). At threshold q=3, the exact safe set is the disjoint union of the h+1 closed intervals

    [(n+1/3)/N, (n+2/3)/N], n=h,h+1,...,2h.

Thus

    m=h+1=(N+2)/3,
    A=(h+1)/(3N)=(N+2)/(9N),
    m/A=3N.

These vectors are primitive (gcd(1,N)=1), their safe measure tends to 1/9>0, but m/A tends to infinity. Hence no bound on m/A depending ONLY on the number of speeds k is possible, even for primitive speed vectors. Consequently, attempting to close Experiment 88's extension argument solely by a dimension-dependent bound m/A<=C(k) is impossible.

**Proof.** The speed-one safe set at threshold 1/3 is [1/3,2/3]. For speed N, its safe intervals are [(n+1/3)/N,(n+2/3)/N]. For N=3h+1, the first interval meeting [1/3,2/3] starts exactly at n=h and the last ends exactly at n=2h. All other intervals are disjoint from [1/3,2/3], and each retained interval has length 1/(3N). Their count and total length are as displayed. Since the intervals have positive gaps, they are separate components. QED.

## Exact computation (executed, not merely committed)

experiments/experiment_89_deletion_obstruction.py uses only Fraction arithmetic, intersects complete safe-interval lists, and checks:
- 522 primitive vectors with positive-measure safe sets for (k,N)=(3,12),(4,10),(5,9).
- 274 individual deletion cases where A_v>2m_v/(qv), all with a positive-measure full safe set as predicted.
- 21 deletion cases from zero-measure full safe sets, all satisfying the necessary inequality. These may be tight vectors with isolated safe times, NOT established counterexamples.
- The exact formula m/A=3N for N=7,10,31,100.

The theorem holds for all dimensions and speeds; the finite computation is a regression audit only.

## Novelty, priority, and next route

Theorem 89.1 is a direct contrapositive of Experiment 88; it is not independently new mathematics. Theorem 89.2 gives a sharp elementary fragmentation family, but originality in the wider discrepancy literature has not been established. Neither constitutes a Q1-level breakthrough on its own.

The barrier points to the genuinely harder task: exploit the ARITHMETIC LOCATION of safe-set components and forbidden arcs, rather than only their number and total measure. Such overlap structure may be combined with Beck–Everett's 2026 short-relation restriction (arXiv:2609.06259). The stronger known dimension-dependent finite reduction of Malikiosis–Santos–Schymura (2025, DOI 10.1017/fms.2025.10107) is an essential comparison.

## Verdict

**No unrestricted LRC proof. No established Q1-level mathematical novelty.** Two exact theorems and a reproducible computation; the method's remaining obstruction is precisely identified.
