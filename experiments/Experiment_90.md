# Experiment 90 — Exact cyclic covering and safe-set Euler identity

Date: 2026-10-10
Status: complete all-dimensional equivalence and exact counting identity; 279 independently executed primitive-vector checks. **Unrestricted LRC is not solved.**

## Definitions
Let V=(v_1,...,v_k) consist of k>=2 distinct positive integers, q=k+1, L=lcm(v_1,...,v_k), and M=qL. Set
S={t mod 1: ||v_i*t||>=1/q for every i}.
For j in Z/MZ, call j a safe grid vertex when for every i
L <= (v_i*j mod M) <= (q-1)*L.
Call the open grid cell (j/M,(j+1)/M) safe when every interior time belongs to S. Let G be the number of safe grid vertices, H the number of safe grid cells, and C the number of connected components of S on the circle (including singleton components).

## Theorem 90.1 — finite cyclic equivalence
S is nonempty if and only if at least one safe grid vertex exists.

Proof. Every boundary point of the individual allowed set {||v_i*t||>=1/q} satisfies v_i*t=n+1/q or n-1/q modulo integers, hence lies at an integer multiple of 1/(q*v_i), and therefore at an integer multiple of 1/(qL)=1/M because v_i divides L. Consequently the boundary of S is contained in the grid. If S is nonempty and proper, its boundary is nonempty and contains a safe grid vertex because S is closed. S is proper since t=0 is excluded. Conversely, a safe grid vertex j/M has fractional part (v_i*j mod M)/M, so the modular inequalities are exactly the loneliness inequalities. QED.

## Theorem 90.2 — exact discrete topology/measure identity
For every V,
G=H+C, and mu(S)=H/M.
In particular, S has positive measure iff H>0; if H=0 and G>0, all safe times are isolated and C=G.

Proof. All endpoints of S lie on the M-grid, so S is a finite disjoint union of nonempty closed arcs, possibly singleton points. Since S is a proper subset of the circle, each component consisting of h>=1 consecutive elementary closed grid cells contains exactly h+1 grid vertices; each singleton contains one vertex and zero cells. Summing componentwise gives G=H+C. Each elementary cell has length 1/M and boundary points have measure zero, so mu(S)=H/M. QED.

## Theorem 90.3 — exact forbidden-grid cardinalities
For any speed v in V, the number of j in Z/MZ for which ||v*j/M||<1/q is precisely 2L-v.

Proof. Write h=L/v. The residue (v*j mod M) equals v times (j mod qh), so the bad condition is that the residue r=j mod qh satisfies 0<=r<h or (q-1)h<r<qh. These ranges contain h+(h-1)=2h-1 residues. The full grid Z/MZ contains v complete periods of length qh, hence v(2h-1)=2L-v bad grid points. QED.

## Exact integer audit (executed)
The script experiments/experiment_90_cyclic_grid.py exhaustively enumerates primitive vectors for (k,N)=(2,18),(3,10),(4,8), 279 total, and independently checks all three theorems by modular arithmetic. Examples:
V=(1,2,3,4): M=60, G=4, H=0, C=4.
V=(1,3,4,7): M=420, G=4, H=0, C=4.
V=(1,3,9): M=36, G=7, H=2, C=5.
V=(2,3,5): M=120, G=10, H=6, C=4.

## Why this matters, and limitations
Theorem 90.1 replaces the individual-anchor modular search of Experiment 84 with one common cyclic modulus. Theorem 90.2 retains topological information lost by measure-only methods: tight instances have H=0 but G>0. Theorem 90.3 yields exact forbidden-set cardinalities, which can support future residue-overlap and CRT analysis.

The common modulus q*lcm(V) can be enormous; this is NOT a dimension-only finite reduction, unlike the stronger published work of Malikiosis–Santos–Schymura (2025). Elementary cell decomposition and cyclic counting are classical, so independent mathematical novelty and Q1 significance are NOT established.

## Verdict
Exact all-dimensional equivalence: PROVED.
Exact grid measure and component identity: PROVED.
Unrestricted LRC: NOT SOLVED.
Q1-journal-level novelty: NOT ESTABLISHED.
