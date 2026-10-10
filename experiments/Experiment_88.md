# Experiment 88 — Component-sensitive safe-measure extension theorem

Date: 2026-10-10. Status: rigorous all-dimensional conditional theorem; 4,800 exact rational regressions. Unrestricted LRC is NOT solved.

## Theorem 88.1 (component-sensitive one-runner extension)
Let k>=2 and q=k+1. Suppose S is a finite union of m pairwise disjoint closed intervals on the unit circle (interval endpoints can be split at 0), all safe at threshold d=1/q for an existing collection of k-1 distinct positive integer speeds. Let A=mu(S)>0. For any new positive integer speed v distinct from the core,
mu(S intersect {t: ||vt||>=d}) >= (1-2d)*(A-2*d*m/v).
In particular, v>2*m/(q*A) implies that the enlarged k-speed vector satisfies LRC with a positive-measure safe set.

## Proof
Write f(x)=1_{||x||>=d}-(1-2d), a 1-periodic zero-mean step function. In each period, f equals -(1-2d) on the forbidden arc of length 2d and equals 2d on the allowed arc of length 1-2d. The range (maximum minus minimum) of any continuous periodic primitive F of f is exactly 2d(1-2d): the primitive rises by 2d(1-2d) over the allowed arc and falls by the same amount over the forbidden arc.

For any interval [L,R], substitution x=vt and the primitive identity give
integral_L^R f(vt)dt=[F(vR)-F(vL)]/v >= -2d(1-2d)/v.
Summing over m disjoint intervals composing S gives
integral_S 1_{||vt||>=d}dt
=(1-2d)A+integral_S f(vt)dt
>= (1-2d)*(A-2dm/v).
The left side is exactly the safe overlap measure. Since 1-2d>0, the strict threshold v>2dm/A implies positive overlap. QED.

## Example beyond the previous full-interval gluing condition
Take k=6, q=7, and core speeds (1,2,3). The interval S=[1/7,2/7] is safe for all three at threshold 1/7. Thus A=1/7 and m=1. For speed v=4, the new criterion v>2m/(qA)=2 holds. The lower bound is (5/7)*(1/7-2/(7*4))=5/98>0. Direct exact intersection yields S intersect {||4t||>=1/7}=[1/7,3/14], measure 1/14. By contrast the full-interval gluing hypothesis of Experiment 86 requires v*A>=2(1-1/7)=12/7; here v*A=4/7, so it fails. This is a genuine improvement of that proof method.

## Iteration and limits
The bound may be applied successively after recomputing the total measure A_j and the component count m_j of the retained safe set. It does not assert that the same fixed threshold works for all subsequent speeds; fragmentation may increase m_j and A_j may shrink. No universal all-speed proof follows.

## Exact computational audit
The script experiments/experiment_88_component_discrepancy.py independently sweeps rational endpoints and computes exact overlap measures for q=3,...,12, v=1,...,24, and 1- or 2-component rational test sets. It verifies 4,800 cases, including the example above. The analytical theorem is independent of the test.

## Literature and priority
The discrepancy-of-a-periodic-zero-mean-function argument is classical, so independent novelty is NOT established. Compare Tao (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728; Beck–Everett (2026), Lonely Runner Relations, arXiv:2609.06259; and Dubickas (2011), The lonely runner problem for many runners, Glasnik Matematicki 46(1), DOI 10.3336/gm.46.1.01. All three already occur in references/lonely_runner.bib. The specific component-sensitive bound is proved here, but no first-priority claim is made.

## Verdict
All-dimensional conditional extension: PROVED. Previous interval-containment criterion strictly strengthened: YES. Unrestricted Lonely Runner Conjecture: NOT SOLVED.
