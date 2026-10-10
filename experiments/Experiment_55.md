# Experiment 55 — Exact endpoint obstruction and a tight-instance regression

Date: 2026-10-10
Status: proved exact finite-instance criterion in arbitrary dimension; not a proof of the unrestricted Lonely Runner Conjecture; novelty not established.

## Problem
For distinct positive integer speeds v_1,...,v_k and q=k+1, decide whether some t satisfies ||v_i t||>=1/q simultaneously.

## Theorem 55.1 (boundary cover criterion)
Let E be the set of residues (q*n+sigma)/(q*v_i) mod 1, for i=1,...,k, n=0,...,v_i-1, sigma=+-1. Let A_i={t mod 1: ||v_i*t||>=1/q}. Then the following are equivalent:
(1) intersection_i A_i is nonempty;
(2) some e in E belongs to every A_i;
(3) the closed safe arcs are not completely eliminated by the open forbidden arcs and a boundary witness exists.

## Proof
(2) implies (1) trivially. If S=intersection_i A_i is nonempty, it is closed and proper since 0 is excluded. Every nonempty proper closed subset of the circle has a boundary point e. Such e must be a boundary point of some A_i, for otherwise all A_i would be locally constant (inside or outside) near e; as e belongs to all A_i, it would be interior to S. The boundaries of A_i are exactly the indicated rational residues (up to repetitions). Hence e belongs to E, proving (1) implies (2). (3) is the same set-theoretic assertion. QED.

## Why this is not the missing universal proof
This criterion reduces each fixed instance to at most 2*sum_i v_i rational tests. It does not show that one test must succeed for all v_1,...,v_k. It is essentially a reformulation of Experiment 54 and a classical finite-candidate idea. It is NOT a novel breakthrough.

## Exact boundary regression
For k=2, v=(1,2), q=3, S={1/3,2/3}. Both points are in E and neither lies in the interior of S. Any numerical procedure that only samples open intervals will miss them.

## New direction
Develop an arithmetic invariant forbidding complete coverage of E by the other runners' open forbidden arcs. A successful invariant must be proven for all k and all distinct integer vectors, and must respect known tight examples. No such invariant is proved here.

## Literature
Ho Tin Fan and Alec Sun (2026), Amending the Lonely Runner Spectrum Conjecture, Electronic Journal of Combinatorics 33(1), P1.38, DOI 10.37236/13840, discusses sharper critical-time principles. Malikiosis, Santos and Schymura (2025), Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants, addresses finite checking. Both already cited in the repository bibliography.
David Alcántara, Francisco Criado, and Francisco Santos (2026), Covering Radii of 3-Zonotopes and the Shifted Lonely Runner Conjecture, Experimental Mathematics, published online 7 May 2026, DOI 10.1080/10586458.2026.2651085. Publisher metadata checked 2026-10-10. This concerns shifted LRC for five runners and is NOT a proof of unrestricted LRC.

## Novelty and resolution
Experiment 55 is a rigorous baseline and regression criterion, not a new Q1-level theorem. Unrestricted LRC remains UNSOLVED in this project.
