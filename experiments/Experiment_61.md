# Experiment 61 — Exact safe-component extension beyond the kM barrier

Date: 2026-10-10
Status: proved conditional theorem for every finite dimension, including non-lacunary examples. Not an unrestricted solution; novelty unverified.

## Setup
For k>=2, q=k+1, and k-1 distinct positive integer speeds A, define the old safe set at the NEW threshold
S_A(q)={t in R/Z: ||a*t||>=1/q for every a in A}.
Let J be any connected closed arc contained in S_A(q), with length L (measured in units of one full circle).

## Theorem 61.1 (component-length extension)
If V is an additional positive integer speed and L>=2/(q*V), then there is t in J with ||V*t||>=1/q. Thus A union {V} is safe at threshold 1/q.

## Proof
The forbidden set of the new runner on the real line is the disjoint union of open intervals
((n-1/q)/V,(n+1/q)/V), n in Z,
each of length 2/(qV). If every point of a lift of J were forbidden, its connectedness would force that closed interval to lie in one such open component. But a closed interval of length at least 2/(qV) cannot be contained in an open interval of that length. Hence J contains a new-runner-safe time. All old speeds are safe there by construction. QED.

## Exact component algorithm
At fixed q, each old speed a supplies boundaries (q*n +/- 1)/(q*a) modulo one. Sort the finitely many rational boundaries, test a rational midpoint in each open cell, and include boundary points where equality holds. Merge consecutive safe cells to obtain maximal closed components. This exact rational process determines their lengths, including singleton components (L=0). The theorem applies whenever a positive-length component has L>=2/(qV).

## Strict improvement over Experiment 60
Experiment 60 derives a guaranteed safe arc from a lower-dimensional t0 and proves V>=k*M sufficient. Theorem 61.1 uses actual geometry at the relaxed threshold and can succeed with V<k*M. It does NOT automatically give a universal lower bound on component length.

## Non-lacunary worked example
Take k=3, q=4, old speeds A={1,3}, new V=4. At t0=1/2 the old runners are each at distance 1/2. In fact J=[5/12,7/12] is safe for both old speeds at threshold 1/4: for t in J, ||t||>=5/12>=1/4 and ||3t||>=1/4. Its length L=1/6 exceeds 2/(4*4)=1/8. Hence the theorem certifies V=4 although Experiment 60 would demand V>=3*3=9. Explicit witness t=5/12: distances for (1,3,4) are (5/12,1/4,1/3), all >=1/4.

## Crucial limitation
The existence of a positive-length old safe component is not universal. At the sharp old threshold, tight configurations can have isolated safe points (Experiment 53). More importantly, establishing a sufficient component-length bound for arbitrary A at the new threshold is a separate unresolved problem; simply assuming such a bound would hide the original conjecture. This theorem does not solve unrestricted LRC.

## Literature, novelty, and priority
- Yuhan Zhang (2026), Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound, arXiv:2608.13599v2, DOI 10.48550/arXiv.2608.13599. Primary arXiv metadata verified on 2026-10-10. The paper analyzes uncovered connected components and therefore is especially relevant prior art. This experiment's arc criterion is elementary and NOT claimed original.
- Guillem Perarnau and Oriol Serra (2025), The Lonely Runner Conjecture turns 60, Computer Science Review 58, 100798. Existing bibliography record.

## Research verdict
Theorem proved in all finite dimensions under an exact component-length hypothesis; certified a clustered case outside Experiment 60. Novelty relative to prior component methods is not demonstrated. General LRC remains unsolved.
