# Experiment 94 — Reflection parity of safe vertices, cells and components

Date: 2026-10-10. Status: exact all-dimensional theorem, 527 integer-verified primitive vectors. Unrestricted LRC remains unsolved.

## Definitions
Let V be k>=2 distinct positive integer speeds; q=k+1, L=lcm(V), M=qL. Let S={t mod 1: ||vt||>=1/q for all v in V}. Write G for the number of safe vertices j/M, H for the number of safe open elementary grid cells (j/M,(j+1)/M), and C for the number of connected components of S on the circle. Experiment 90 proved G=H+C.

## Theorem 94.1 — Exact parity classification
Let o=1 if every speed in V is odd, and o=0 otherwise. Then

G mod 2 = o*(k mod 2),
H mod 2 = o*(1-(k mod 2)),
C mod 2 = o.

In particular, if any speed is even, all three counts are even. If all speeds are odd, C is odd. These statements hold in every dimension and also for zero-measure safe sets.

## Proof
Reflection R(t)=1-t preserves S because ||v(1-t)||=||vt||. On the M-grid it maps the vertex j to M-j modulo M. The fixed grid vertices are t=0, and, only when M is even, t=1/2. The vertex t=0 is never safe. The vertex t=1/2 is safe if and only if every speed is odd. If all speeds are odd then L is odd, so M=qL is even exactly when q=k+1 is even, equivalently k odd. Every nonfixed safe vertex is paired with a distinct reflected safe vertex. Thus G mod 2=o*(k mod 2).

Reflection maps the open grid cell with index j to the open grid cell with index M-1-j. If M is even, this involution has no fixed cell. If M is odd, it has precisely one fixed cell, whose midpoint is t=1/2. This midpoint is safe iff all speeds are odd, in which case the entire open cell is safe because all forbidden boundaries lie on the M-grid. M odd requires both q and L odd, which is equivalent to k even and all speeds odd. All other safe cells occur in reflected pairs, giving H mod 2=o*(1-(k mod 2)). Finally C=G-H, and modulo 2 subtraction equals addition, so C mod 2=o. QED.

## Corollary 94.2 — Minimum multiplicities
If some speed is even and S is nonempty, then G>=2. If all speeds are odd, the point t=1/2 is safe and C is odd. In particular, all-odd speed vectors satisfy LRC trivially. These are elementary consequences, not new general solutions.

## Exact verification
experiments/experiment_94_reflection_parity.py uses exact integer modular tests on primitive vectors:
(k,N)=(3,12),(4,10),(5,9), total 527. For each vector it computes G, H and C independently and checks all three parity formulas and G=H+C. All tests passed locally. The theorem does not depend on the computation.

## Literature and priority
The reflection argument is elementary and independent novelty is not established. It is a reproducibility check for the repository's grid method, not a Q1-journal-level breakthrough. Compare Malikiosis, Santos and Schymura (2025), DOI 10.1017/fms.2025.10107, and Blanco, Criado and Santos (2026), arXiv:2603.24784v3. The latter gives counterexamples to the SHIFTED LRC, not the ordinary LRC. Its primary arXiv record was checked on 2026-10-10, and its bibliography entry updated from v2 to v3.

## Verdict
Parity invariant for every dimension: PROVED. Exact audit: 527 passed. Unrestricted LRC: NOT SOLVED. Independent Q1-level novelty: NOT ESTABLISHED.
