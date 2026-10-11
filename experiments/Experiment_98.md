# Experiment 98 — Residue-anchored safe intervals in every dimension

Date: 2026-10-11. All-dimensional theorem proved. Unrestricted LRC remains open.

## Theorem 98.1: explicit guaranteed safe witness
Let k>=2, q=k+1, and V be k distinct positive integer speeds. If q does not divide any v in V, then t0=1/q is safe: for every v, the fractional part {v/q}=(v mod q)/q belongs to [1/q,(q-1)/q].

## Theorem 98.2: exact local safe interval
Write r_v=v mod q (so 1<=r_v<=q-1), and put

 alpha=min_{v in V} (r_v-1)/(q*v),
 beta=min_{v in V} (q-1-r_v)/(q*v).

Then the connected component of the safe set S={t mod 1: ||vt||>=1/q for all v} containing t0=1/q is exactly the closed interval [t0-alpha,t0+beta]. In particular its length is alpha+beta.

**Proof.** At t0, speed v has phase r_v/q. The nearest forbidden boundary to the left occurs after time (r_v-1)/(qv); the nearest forbidden boundary to the right occurs after time (q-1-r_v)/(qv). Until these boundaries are reached, every phase remains in its permitted arc. The first left boundary among all speeds is at t0-alpha, and the first right boundary is at t0+beta. Immediately beyond either endpoint, the corresponding active speed enters its forbidden arc, so the connected safe component cannot extend farther. QED.

## Corollary 98.3: exact isolated-witness criterion
The safe time t0=1/q is isolated if and only if V contains at least one speed congruent to 1 mod q and at least one speed congruent to q-1 mod q. Equivalently alpha=beta=0. Otherwise the component has positive length. This holds for every k>=2.

## Corollary 98.4: a dimension-uniform positive-density family
For k independently sampled residue classes uniformly modulo q, the probability that none is 0 modulo q is exactly (1-1/q)^k=(k/(k+1))^k > 1/e. Thus a constant fraction of residue vectors admit the explicit t0=1/q certificate. This is a statement about independent residue classes, not the exact density among ordered DISTINCT primitive speed vectors of a fixed finite range.

## Exact independently executed verification
The code experiments/experiment_98_residue_anchor.py uses Fraction arithmetic and checks that the stated endpoints are safe, interior midpoints are safe, and points immediately beyond each endpoint are unsafe. It also independently checks the isolated criterion and that q-divisible speeds forbid t0.

- k=3, speeds<=14: 325 primitive vectors; 160 q-free, 77 isolated anchors, 83 positive intervals.
- k=4, speeds<=11: 325 primitive vectors; 125 q-free, 76 isolated anchors, 49 positive intervals.
- k=5, speeds<=10: 251 primitive vectors; 126 q-free, 55 isolated anchors, 71 positive intervals.
- TOTAL 901 primitive vectors; 411 q-free certified, 208 isolated anchors, 203 positive safe intervals. All checks passed locally.

## Novelty and publication gate
This is a genuine existence proof for a residue-defined family in EVERY dimension, but it is elementary and follows directly from evaluating the phases at t=1/(k+1). It is not a proof of unrestricted LRC, and no first-priority or Q1-journal-level novelty is claimed. The local interval formula is a useful exact certificate for subsequent perturbation or modular-sieving work, but does not by itself improve the published finite-checking theorem.

Literature compared: Beck and Everett, *Lonely Runner Relations* (2026), arXiv:2609.06259; Malikiosis, Santos and Schymura (2025), DOI 10.1017/fms.2025.10107. Both sources already exist in references/lonely_runner.bib, so no duplicate entries are needed.
