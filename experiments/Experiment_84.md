# Experiment 84 — Exact boundary-to-modular reduction for every dimension

Date: 2026-10-10. Status: rigorous equivalence for every finite set of distinct positive integer speeds; 1,674 exact primitive-vector tests. This does not settle unrestricted LRC.

## Theorem 84.1 (boundary witness equivalence)
Let V={v_1,...,v_k} be k>=2 distinct positive integers and q=k+1. The following are equivalent:

(i) There is a real t with ||v_i*t||>=1/q for every i.

(ii) There exist an anchor speed a in V and an integer n satisfying 1<=n<=floor(q*a/2), q does not divide n, and, for EVERY b in V,
    a <= (b*n mod (q*a)) <= (q-1)*a,
where the residue is the unique integer in {0,...,q*a-1}.

In that case t=n/(q*a) is an exact safe time. The finite search has at most sum_{a in V}floor(q*a/2) candidates, each checked using integer modular arithmetic, with no floating point.

## Proof
(ii)->(i): With t=n/(q*a), the fractional part of b*t is r/(q*a), r=(b*n mod q*a). The inequalities a<=r<=(q-1)*a are exactly 1/q<=fractional part<=1-1/q, equivalent to ||b*t||>=1/q.

(i)->(ii): The safe set S={t mod 1: ||b*t||>=1/q for every b in V} is closed and nonempty. It is a proper subset of the circle because t=0 is forbidden. Hence its topological boundary is nonempty. Choose a boundary point t0. Since S is the intersection of finitely many closed sets S_b={||b*t||>=1/q}, at least one b=a must satisfy ||a*t0||=1/q: otherwise all inequalities would be strict and t0 would be interior. Thus t0=n/(q*a) modulo 1 for some integer n, 0<n<q*a, with n not divisible by q. Since S is invariant under t->1-t, replace n by min(n,q*a-n) to obtain 1<=n<=floor(q*a/2). All modular inequalities hold by the first equivalence. QED.

## Corollary 84.2 (exact finite disjunction)
For fixed V, failure of LRC is equivalent to the failure of every finite modular predicate in (ii). This is an exact decision algorithm for each given finite integer-speed vector. It does NOT reduce infinitely many vectors to a dimension-only finite list and hence is NOT a proof of the unrestricted conjecture.

## Reproducible exact census
The independent Python script experiments/experiment_84_boundary_modular.py checks primitive sets:
- k=3, speeds <=15: 409 tested, 0 failures.
- k=4, speeds <=12: 479 tested, 0 failures.
- k=5, speeds <=12: 786 tested, 0 failures.
Total: 1,674 primitive vectors. These counts match the earlier Experiment 75/77 primitive census, but the witness engine here uses only integer modular predicates. This is a regression test, not a new dimensional proof.

## Relation to previous work
Experiment 74 gave an exact critical-time optimizer using pair-sum and half-integer candidates for the MAXIMUM of the minimum distance. Experiment 84 instead gives a substantially simpler exact criterion for mere threshold FEASIBILITY: a safe set must contain a forbidden-arc boundary. The latter is not an optimization formula. The finite candidate set depends linearly on sum of speeds, and can be much larger than the number of distinct pair-sum optimizer candidates in some instances. The boundary principle itself is elementary and should not be advertised as new without a comprehensive priority check.

## Literature and novelty
Malikiosis, Santos and Schymura (2025), Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants, Forum of Mathematics, Sigma 13 e164, DOI 10.1017/fms.2025.10107, establishes a much deeper dimension-dependent finite-checking reduction. Tao (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728, also addresses finite checking. Both are already in references/lonely_runner.bib. Our criterion is an elementary fixed-vector exact decision reduction, not a replacement for those results. Independent research novelty NOT established.

## Honest verdict
All-dimensional equivalence: proved. Finite census: passed. Unrestricted LRC: NOT solved. Next meaningful objective: prove that at least one of the modular predicates holds for EVERY distinct k-speed set, or derive a genuinely new arithmetic obstruction to all of them failing.
