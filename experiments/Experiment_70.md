# Experiment 70 — Spanning-tree overlap certificate for safe-time existence

Date: 2026-10-10
Status: proved rigorous all-dimensional SUFFICIENT condition. No universal LRC proof; the underlying probability inequality is classical.

## Theorem 70.1
Let k>=2, q=k+1, and v_1,...,v_k distinct positive integers. Define forbidden events B_i={t mod 1: ||v_i*t||<1/q} and exact pair-overlap weights w_ij=mu(B_i intersect B_j). For any spanning tree T on {1,...,k},
mu({t: ||v_i*t||>=1/q for all i}) >= 1 - 2k/q + sum_{(i,j) in T} w_ij.
Consequently, if the maximum spanning-tree weight W satisfies W>2k/q-1=(k-1)/(k+1), then the LRC instance has a positive-measure set of safe times.

## Proof
Root T at any vertex and enumerate its vertices so every parent precedes its children. The union of the forbidden sets is the disjoint union of B_root and the successive differences B_i \ (union of earlier B_j). Each difference is contained in B_i \ B_parent(i). Hence
mu(union B_i) <= mu(B_root)+sum_{i!=root}[mu(B_i)-mu(B_i intersect B_parent(i))]
= sum_i mu(B_i)-sum_{edges of T}w_ij.
Each mu(B_i)=2/q, since multiplication by a positive integer preserves normalized circle measure. Take complements. Maximizing the tree weight improves the bound. QED.

## Exact finite rational computation of w_ij
Each B_v is a finite union of open intervals on [0,1] with rational endpoints (m +/- 1/q)/v, clipped to [0,1]. Sort all endpoints for B_a and B_b, and sum lengths of subintervals whose midpoint belongs to both forbidden sets. Every comparison and length is rational, so all weights and W can be verified in exact arithmetic. Strictness of forbidden arcs does not affect their Lebesgue measures.

## Structural significance and limitations
This certificate explicitly exploits overlap between the runners' forbidden regions, instead of adding their measures by a crude union bound. It applies to closely spaced and relation-bearing speeds without a large-speed hypothesis. However, a nonpositive lower bound is INCONCLUSIVE: it does not establish that no safe time exists, and it misses isolated safe times because they have measure zero. The spanning-tree inequality is a standard classical union bound refinement, not a new theorem. A new advance would require a provable arithmetic lower bound on W that beats (k-1)/(k+1) for a previously unresolved infinite class.

## Literature
- Matthias Beck, Ricardo Diaz and Sinai Robins, *The Frobenius problem, rational polytopes, and Fourier-Dedekind sums*, Journal of Number Theory 96(1) (2002), 1–21: related exact rational polytope counting, not asserted to contain this theorem.
- *Bounds for the Lonely Runner Problems Via Linear Programming*, Bulletin of the Brazilian Mathematical Society (2021/2022), DOI 10.1007/s00574-021-00272-7: relevant prior art for bounds using analytic methods; official publisher record checked 2026-10-10. Do not add a BibTeX entry without verified author metadata.
- Yuhan Zhang (2026), *Tight instances of the Lonely Runner Conjecture*, arXiv:2608.13599v2: prior art on tight relation-bearing examples; already in bibliography.

## Verdict
A correct, dimension-uniform positive-measure certificate based on exact pairwise arithmetic overlaps. It does NOT solve unrestricted LRC. No independent novelty is claimed for the spanning-tree bound.
