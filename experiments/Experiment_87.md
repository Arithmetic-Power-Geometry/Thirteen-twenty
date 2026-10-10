# Experiment 87 — Prime-adic shift reduction with an exact modular obstruction

Date: 2026-10-10
Status: rigorous all-dimensional conditional reduction; a special case of existing valuation-rigidity work, NOT a new proof of unrestricted LRC.

## Theorem 87.1 — prime-shift reduction
Let k>=2, q=k+1, and let V consist of k distinct positive integer speeds. Suppose a prime p divides all but b of the speeds, with 1<=b<k, and none of the b exceptional speeds is divisible by p. Assume LRC holds for the k-b divisible speeds (at their own, stronger threshold 1/(k-b+1)). Then V satisfies LRC whenever

b * ceil(2*p/q) < p.

In particular, if b=1 and q>=4, the conclusion holds for every prime p. The remaining case q=3, p=2 also holds by a separate two-point endpoint argument.

## Proof
Write V=D union E, where each d in D is divisible by p and each e in E is coprime to p. By the assumed lower-dimensional LRC theorem, choose t0 such that ||d*t0||>=1/(|D|+1)>=1/q for all d in D.

Consider the p shifts t_j=t0+j/p, j=0,...,p-1. For d in D, d*j/p is an integer, so every d-runner retains EXACTLY the same position and remains safe.

For each e in E, multiplication by e permutes residues modulo p. Hence {e*t_j mod 1: j=0,...,p-1} is a rotated uniform p-point grid. The open forbidden arc {x: ||x||<1/q} has length 2/q. It contains at most ceil(2p/q) grid points (indeed if it contains m points, their first-to-last span is (m-1)/p<2/q). Thus each exceptional runner excludes at most ceil(2p/q) shifts. If b*ceil(2p/q)<p, the union of excluded shifts cannot cover all p, so one t_j is safe for every speed.

For b=1, q>=4 and p>=2, 2p/q<=p/2, hence ceil(2p/q)<p except p=2,q=4 where ceil(1)=1<2 also. For q=3,p=2, two antipodal points cannot both lie in an open arc of length 2/3? They CAN both lie in an arc of length 2/3, so this endpoint argument is INVALID. Nevertheless the k=2 LRC theorem is elementary for arbitrary two speeds; use that independent result instead. QED.

## Exact modular obstruction
At any lower-dimensional witness t0, the full-vector question reduces to a finite covering problem on the cyclic group Z/pZ. For each exceptional speed e, the bad shifts are
Bad(e,t0)={j in {0,...,p-1}: ||e*(t0+j/p)||<1/q}.
A safe shift exists exactly when union_{e in E}Bad(e,t0) != Z/pZ.
The union-bound inequality is sufficient, NOT necessary. This exact finite modular obstruction suggests searching for arithmetic overlap restrictions among the bad-shift sets rather than repeatedly sharpening elementary union bounds.

## Example
V=(1,6,10,14,22), k=5, q=6, p=2. Only 1 is odd; the four other speeds are even. Their lower-dimensional LRC guarantee implies a t0 with margin >=1/5. One of t0 or t0+1/2 is safe for the exceptional speed at threshold 1/6. The method works despite arbitrary ratios among the even speeds.

## Independent novelty and provenance
This is a special case of the valuation-rigidity reduction reported at https://arbiter.wiki/problems/lonely-runner (Theorem R, 2026-07-29), which uses p-adic valuation strata and the same b*ceil(2p/q)<p criterion. The source's author/peer-review status has not been independently established. Do not claim this theorem as original or peer-reviewed. The Beck–Everett 2026 short-relation theorem is complementary, not used in this proof.

## Status
Proves a broad infinite family in every dimension CONDITIONAL on LRC for a smaller speed set; for k<=2 the base cases are elementary. It does not establish the unrestricted conjecture or an independently novel theorem. Next genuine target: use exact modular overlap of Bad(e,t0) to remove the union-bound hypothesis for a class not already covered in the literature.
