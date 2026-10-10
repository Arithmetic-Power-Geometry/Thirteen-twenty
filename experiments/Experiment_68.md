# Experiment 68 — Exact gcd-normalized opposite-boundary criterion

Date: 2026-10-10
Status: proved exact two-speed boundary coincidence theorem in every finite dimension; does not solve unrestricted LRC. Independent priority not established.

## Theorem 68.1 (necessary and sufficient condition)
Fix integer q>=3 and distinct positive integer speeds a,b. There exists a real time t and integers n,m such that
a*t=n+1/q and b*t=m-1/q
if and only if q divides (a+b)/gcd(a,b).

## Proof
Put g=gcd(a,b), A=a/g, B=b/g, so gcd(A,B)=1. Eliminating t from the equations gives
b*(q*n+1)=a*(q*m-1), hence B*n-A*m=-(A+B)/q.
The left side is an integer, so q divides A+B. Conversely, if q divides A+B, the integer right-hand side can be expressed as B*n-A*m because gcd(A,B)=1 (Bezout). Define t=(n+1/q)/a. The displayed identity then gives b*t=m-1/q. Thus both orientations occur at one time. QED.

## Theorem 68.2 (isolated-witness filter)
For k>=2, q=k+1, and distinct positive integer speeds v_1,...,v_k, if the simultaneous safe set S={t mod 1: ||v_i*t||>=1/q for every i} has an isolated point, then there are distinct i,j such that q divides (v_i+v_j)/gcd(v_i,v_j).

## Proof
At an isolated safe time t*, at least one active constraint must forbid small motion to the left and another active constraint must forbid small motion to the right; otherwise all constraints would remain safe on one side. For positive speeds and q>=3 these orientations are precisely v_i*t*=n+1/q and v_j*t*=m-1/q. Apply Theorem 68.1. QED.

## Corollary
If q does not divide (v_i+v_j)/gcd(v_i,v_j) for every pair i!=j, then S has no isolated points. If S is nonempty it has positive measure, because S is a finite union of closed intervals and isolated singleton components.

## Strict improvement over Experiment 67
Experiment 67 only showed q divides v_i+v_j. Here the common gcd is removed before the congruence, giving a strictly stronger test. Example q=4, a=4,b=8: q divides a+b=12, but (a+b)/gcd(a,b)=3 is not divisible by 4, so opposite safety boundaries cannot coincide.

## Limitation
The pair criterion guarantees a time where the two chosen speeds are at opposite threshold boundaries. It does NOT guarantee the other k-2 speeds are safe. It is not a sufficient condition for an isolated simultaneous safe time, nor a proof that S is nonempty.

## Prior art and novelty
Related critical-time and spectrum arguments appear in Ho Tin Fan and Alec Sun, *Amending the Lonely Runner Spectrum Conjecture*, Electronic Journal of Combinatorics 33(1), P1.38 (2026), DOI 10.37236/13840 (publisher verified 2026-10-10). Exact gcd normalization is elementary number theory; no independent novelty or Q1-level breakthrough is asserted without theorem-level priority review. The Fan–Sun reference already exists in references/lonely_runner.bib.

## Verdict
Proved exact gcd-normalized characterization of two-speed opposite boundary coincidences and a stronger all-dimensional isolation obstruction. General LRC remains UNSOLVED.
