# Experiment 69 — Exact arithmetic classification of isolated safe times

Date: 2026-10-10
Status: proved exact if-and-only-if characterization in arbitrary finite dimension. This is not a proof of the unrestricted Lonely Runner Conjecture. Novelty over prior critical-time algorithms is unverified.

## Theorem 69.1 (all isolated witnesses from normalized pairs)
Let k>=2, q=k+1, and let v_1,...,v_k be distinct positive integers. Put S={t mod 1: ||v_i t||>=1/q for every i}. Then S contains an isolated point if and only if there are distinct indices i,j with a=v_i, b=v_j, g=gcd(a,b), A=a/g, B=b/g, such that:
1. q divides A+B;
2. for the unique residue r0 in {0,...,q-1} satisfying A*r0=1 (mod q), at least one h in {0,...,g-1} gives r=r0+q*h with
   g <= (v_l*r mod q*g) <= (q-1)*g for every l=1,...,k.
In that case t=r/(q*g) mod 1 is an isolated safe time. The condition includes the pair i,j automatically.

## Proof
First suppose t* is isolated. By the local orientation argument of Experiment 68, some distinct active speeds a,b satisfy a*t*=n+1/q and b*t*=m-1/q. Let g=gcd(a,b), A=a/g, B=b/g. Eliminating t* yields q divides A+B. Since gcd(A,B)=1 and B=-A mod q, gcd(A,q)=1. Also A*(q*g*t*)=q*n+1, so r=q*g*t* is an integer with A*r=1 mod q. Thus r=r0+q*h. Changing t by one changes r by q*g, so h can be chosen from {0,...,g-1}. Since t* is safe, each integer residue (v_l*r mod q*g) lies between g and (q-1)*g inclusive: this is exactly the condition ||v_l*t*||>=1/q.

Conversely, suppose the arithmetic conditions hold. Let t=r/(q*g). Since A*r=1 mod q, write A*r=q*n+1. Then a*t=A*r/q=n+1/q. Because B=-A mod q, B*r=-1 mod q, so b*t=m-1/q for an integer m. The residue inequalities make every speed safe at t. The active speed a permits sufficiently small perturbations only to the right, and active speed b only to the left, so t is isolated in S. QED.

## Exact algorithmic implication
For each ordered pair (i,j), calculate gcd, test q|(A+B), compute the modular inverse A^{-1} mod q, and enumerate exactly g residues r=r0+q*h. Check all speeds with integer modular arithmetic. This enumerates all isolated safe times, with possible duplicates across pairs. The number of tests is bounded by sum over ordered eligible pairs of gcd(v_i,v_j), times k; it is a finite-instance algorithm, NOT a universal existence proof.

## Examples
k=2, q=3, speeds (1,2): g=1, A=1, B=2, r0=1. The candidate t=1/3 is isolated and safe; reversing the pair gives t=2/3.
k=3, q=4, speeds (1,3,4): pair (1,3) has A+B=4 and t=1/4, but speed 4 has distance zero there, so the pair alone does not yield an isolated simultaneous witness. This shows why checking all remaining speeds is indispensable.

## Novelty/prior art
This is a precise integer-only form of a critical-time classification. It extends the pair congruence in Experiments 67–68 into a necessary-and-sufficient certificate for isolated witnesses, but it is likely related to established finite critical-time enumeration. Do NOT assert first discovery, Q1 novelty, or solution of LRC.
Relevant verified published literature: Fan, Ho Tin and Sun, Alec (2026), Amending the Lonely Runner Spectrum Conjecture, Electronic Journal of Combinatorics 33(1), P1.38, DOI 10.37236/13840. The publisher article and its PDF were checked 2026-10-10; bibliography entry already exists. Recent relevant preprint: Cordella, Francesco (2026), Odd denominators in the Lonely Runner spectrum for six speeds, arXiv:2609.03444; primary arXiv abstract checked 2026-10-10.

## Open gap
The exact characterization only finds isolated safe points when they exist. It cannot establish nonemptiness of S in arbitrary configurations, nor detect positive-length components by itself. General LRC remains unsolved.
