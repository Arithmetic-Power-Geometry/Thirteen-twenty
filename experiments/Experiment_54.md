# Experiment 54 — Boundary-inclusive finite witness theorem

Date: 2026-10-10
Status: proved exact finite-instance equivalence for arbitrary finite integer dimensions. This is NOT a universal proof of the Lonely Runner Conjecture; finite critical-time principles are established prior art.

## Theorem 54.1
Let k>=1, q=k+1, and v_1,...,v_k be distinct positive integers. Define S={t mod 1: ||v_i t||>=1/q for all i}. Define the finite boundary candidate set
C={ ((q*n+sigma)/(q*v_i)) mod 1 : 1<=i<=k, sigma in {-1,+1}, n in Z }.
Then S is nonempty if and only if S intersects C. Only finitely many distinct residues occur (take n modulo v_i).

## Proof
Each single-speed safe set is closed on the circle with boundary points in C. Their intersection S is closed. It cannot equal the entire circle because each speed excludes an open neighborhood of t=0. If S is nonempty and proper, it has a boundary point t*. If t* were interior to every single-speed safe set, it would be interior to S, contradiction. Thus t* lies on the boundary of at least one single-speed safe set, hence belongs to C. Conversely any t in S intersect C is a valid witness. QED.

## Exact certificate
Enumerate i=1..k, sigma=+-1, n=0..v_i-1, deduplicate rational residues mod 1, and test for each candidate t whether q*min((v_j*t mod 1),1-(v_j*t mod 1))>=1 for all j using exact integer/rational arithmetic. A passing candidate proves the particular instance. Exhausting candidates without success disproves the instance, but no such counterexample is reported here.

## Example
For V=(1,2), q=3, the safe set consists of {1/3,2/3}; both are included in C. This captures zero-measure equality cases missed by positive-measure certificates.

## Complexity
The raw candidate list has at most 2*sum_i v_i elements (with duplicates). Thus this is pseudopolynomial in the numeric speed values, not polynomial in their binary encoding, and is not a bounded-speed reduction uniform in k.

## Literature/novelty
The critical-time and rational-witness viewpoint is known. See Ho Tin Fan and Alec Sun, *Amending the Lonely Runner Spectrum Conjecture*, The Electronic Journal of Combinatorics 33(1) (2026), P1.38, DOI 10.37236/13840 (Lemma 11 gives a sharper characterization), and Romanos Diogenes Malikiosis, Francisco Santos, Matthias Schymura, *Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants*, arXiv:2411.06903 (finite-checking reduction). Both are already present in references/lonely_runner.bib; do not duplicate citations.

## Research status
No all-dimensional existence theorem follows. The open task is to show that at least one candidate succeeds for EVERY admissible speed vector, not merely to enumerate candidates. This experiment is a sound baseline but does not constitute new Q1-level mathematical novelty.
