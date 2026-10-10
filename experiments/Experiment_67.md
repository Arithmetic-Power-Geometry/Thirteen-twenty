# Experiment 67 — Opposite-boundary arithmetic at isolated safe times

Date: 2026-10-10
Status: rigorous all-dimensional necessary condition for an isolated safe time. Does not prove universal LRC. Originality against the full critical-time literature remains unverified.

## Definitions
Let k>=2, q=k+1, and v_1,...,v_k be distinct positive integers. Write S={t mod 1: ||v_i*t||>=1/q for every i}. A point t* in S is isolated if a neighborhood of t* contains no other point of S.

## Theorem 67.1 (opposite-boundary divisibility)
If t* is isolated in S, then there exist distinct indices i,j such that q divides v_i+v_j.

## Proof
At any safe t*, an active constraint has ||v_i*t*||=1/q. Since q>=3, the two boundary orientations are distinct. Write v_i*t*=n_i+epsilon_i/q with epsilon_i in {+1,-1}; locally, an epsilon_i=+1 active constraint permits motion only to the right, and an epsilon_i=-1 active constraint permits motion only to the left. Inactive constraints remain safe under sufficiently small perturbations. If all active constraints had the same orientation, a sufficiently small displacement in the permitted direction would preserve every constraint, contradicting isolation. Hence two distinct active constraints i,j have epsilon_i=+1 and epsilon_j=-1. Their equations are
v_i*t*=n_i+1/q,
v_j*t*=n_j-1/q.
Eliminating t* yields v_j*n_i-v_i*n_j=-(v_i+v_j)/q, whose left side is integral. Therefore q divides v_i+v_j. QED.

## Corollary 67.2 (no isolated witnesses without complementary residues)
If v_i+v_j is nonzero modulo q for every pair i!=j, then S has no isolated points. In particular, if S is nonempty, it has positive Lebesgue measure: S is a finite union of closed intervals and singleton points, and the theorem rules out singleton components.

## Example
For k=2, q=3, v=(1,2), the safe set consists exactly of {1/3,2/3}; the speeds satisfy 1+2=3. Thus the necessary condition correctly detects the arithmetic possibility of isolated witnesses. It is not sufficient: having a complementary pair does not force isolation or even existence.

## Sign and topology audit
The proof uses positive speeds and q>=3. For an active lower boundary x=n+1/q, the safe side is locally to the right; for upper boundary x=n-1/q, the safe side is locally to the left. The intersection of finitely many safe arcs is closed with finitely many connected components, so if it has no isolated points and is nonempty it contains a positive-length arc. The theorem does not imply nonemptiness.

## Research significance
This creates a nontrivial arithmetic filter for zero-measure safe sets and identifies a condition under which measure-based arguments cannot miss an existing safe time. It does NOT solve the general Lonely Runner Conjecture. Independent novelty must be assessed against existing critical-time and tight-instance work; no Q1 novelty is asserted.

## Relevant literature
- Fan, Ho Tin and Sun, Alec (2026), Amending the Lonely Runner Spectrum Conjecture, Electronic Journal of Combinatorics 33(1), P1.38, DOI 10.37236/13840. Their critical-time lemmas are relevant prior art; existing bibliography entry.
- Zhang, Yuhan (2026), Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound, arXiv:2608.13599v2. Existing bibliography entry.
- Allikvere, Jaan (2026), Fourteen and fifteen lonely runners, arXiv:2609.02604v2. Relevant recent finite-dimensional frontier, existing bibliography entry.

## Next proof obligation
Find a universal nonemptiness argument. The absence of complementary residue pairs only rules out isolated safe times; it does not rule out an empty safe set. A proof must not confuse these.
