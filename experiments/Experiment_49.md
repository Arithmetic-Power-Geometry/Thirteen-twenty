# Experiment 49 — Tree-correlation lower bound in arbitrary dimension

Date: 2026-10-10
Status: rigorous sufficient condition, not a proof of the unrestricted Lonely Runner Conjecture. The method is classical (tree/forest union bound); novelty not claimed.

## Theorem 49.1
Let k>=2, 0<delta<=1/2, and let v_1,...,v_k be nonzero integers. Put B_i={t in [0,1): ||v_i*t||<delta}. For any spanning tree T on vertices 1,...,k,

mu(intersection_i B_i^c) >= 1 - 2*k*delta + sum_{ij in E(T)} mu(B_i intersection B_j).

## Proof
For each t let A(t) be the set of vertices i for which t belongs to B_i. The subgraph of the tree T induced by A(t) is a forest. If A(t) is nonempty, its number of edges is at most |A(t)|-1. Therefore
1_{union_i B_i}(t) <= sum_i 1_{B_i}(t) - sum_{ij in E(T)} 1_{B_i intersection B_j}(t).
This also holds if A(t) is empty. Integrate and use mu(B_i)=2*delta, since multiplication by a nonzero integer preserves circle measure. QED.

## Corollary 49.2 (strict positive-measure certificate)
At delta=1/(k+1), if there exists a spanning tree T with
sum_{ij in E(T)} mu(B_i intersection B_j) > (k-1)/(k+1),
then the simultaneous safe-time set has positive measure and the LRC instance is satisfied.

The strict inequality is essential for this measure-based certificate; equality alone gives only a zero lower bound.

## Algorithmic experiment
Compute pairwise overlaps by exact rational interval arithmetic, assign each pair its overlap as edge weight, and compute a maximum-weight spanning tree. If the sum exceeds (k-1)/(k+1), emit the tree, rational overlaps and positive lower bound as a certificate. Failure of the test is inconclusive.

## Sanity check
For k=2, speeds (1,2), delta=1/3, the tree has one edge. The bound is valid but may be nonpositive; existence can still hold. Thus the condition is sufficient, not necessary.

## Literature and novelty
This is a classical spanning-tree improvement to the union bound (often associated with Hunter-type bounds); its application here does not establish originality. Related direct runner-correlation research: Guillem Perarnau and Oriol Serra, Correlation Among Runners and Some Results on the Lonely Runner Conjecture, Electronic Journal of Combinatorics 23(1), P1.50 (2016), DOI 10.37236/5123. Publisher metadata independently checked on 2026-10-10. Bibliography key PerarnauSerra2016 already exists in references/lonely_runner.bib; do not duplicate it.

## Remaining open problem
Show that the tree-overlap threshold holds for every admissible vector, or develop higher-order correlation certificates where it fails. Neither has been proved here.
