# Experiment 43 — Exact boundary-candidate theorem in arbitrary dimension

Date: 2026-10-10. Status: analytically proved finite-decision theorem, tested in Python 3; not a general Lonely Runner Conjecture proof.

## Theorem 43.1 (boundary-only exact decision)

Let q>=2 be an integer and V=(v_1,...,v_k) a nonempty finite list of positive integer speeds. Define the finite boundary set

E={ (qj±1)/(qv_i) ∈ [0,1] : 1<=i<=k, 0<=j<=v_i }.

There exists t∈[0,1] satisfying ||v_i t||>=1/q for every i **if and only if** there exists t∈E satisfying the same inequalities.

**Proof.** Let S=∩_i {t∈[0,1]: ||v_i t||>=1/q}. This is a closed subset of [0,1]. Suppose S is nonempty. Since the speed v_1>0, the safe set for that speed is a finite union of closed intervals contained in (0,1), and S is a finite union of closed intervals and isolated points. Let t* be the smallest point of S. It lies in (0,1). If no safe constraint is tight at t*, continuity implies every constraint remains strictly satisfied on a small neighborhood of t*, contradicting minimality. Hence ||v_i t*||=1/q for some i. This means v_i t*=j±1/q for some integer j, so t*∈E. Conversely any safe t∈E is a witness. QED.

The number of raw candidates is at most Σ_i 2(v_i+1), independent of lcm(v_1,...,v_k). This can be dramatically smaller than the 2q*lcm(v_i)+1-point grid in Experiment 37. Testing every candidate against k speeds gives O(k Σ_i v_i) exact rational modular comparisons before sorting (the implementation sorts for deterministic first witness). The dependence is pseudopolynomial in binary input size; no efficient algorithm or proof of LRC follows.

The theorem applies to **any finite number k of integer relative speeds**, including k=15. It does not apply as stated to arbitrary incommensurable real speed vectors.

## Executed verification

Ran Python 3 with exact Fraction arithmetic over all distinct subsets of {1,...,12}, sizes k=2,...,6, using threshold q=k+1. Counts:
k=2: 66 tested, maximum 47 candidates, 0 failures;
k=3: 220 tested, maximum 67 candidates, 0 failures;
k=4: 495 tested, maximum 83 candidates, 0 failures;
k=5: 792 tested, maximum 101 candidates, 0 failures;
k=6: 924 tested, maximum 107 candidates, 0 failures.
Total 2,497 configurations, no counterexamples. This finite evidence does NOT establish the universal conjecture.

Specific examples:
V=(8,1,4,6,7), q=6: first boundary witness 7/36, 51 candidates.
V=(1,...,15), q=16: witness 1/16, 233 candidates.
V=(16,17,18,19,20), q=6: witness 1/96, 179 candidates.

Source: src/experiment_43_boundary.py. Results: data/experiment_43_results.csv.

## Prior art / bibliography

Boundary-event enumeration for piecewise-linear circle-distance functions is elementary and must NOT be described as a novel solution. Czerwiński (2012), *Random runners are very lonely*, Journal of Combinatorial Theory Series A 119(6), 1194–1199, DOI 10.1016/j.jcta.2012.02.002, proves a probabilistic Fourier-analytic result for random speeds. Its author and journal metadata were independently checked against the publisher, author institution, and arXiv record; newly appended to references/lonely_runner.bib.

## Unsolved

No proof is supplied that a boundary candidate must be safe for every distinct speed vector at q=k+1. The unrestricted LRC, including the general sixteen-runner case, remains unresolved by this work.
