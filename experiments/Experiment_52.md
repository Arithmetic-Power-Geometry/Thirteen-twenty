# Experiment 52 — Arithmetic pair correlations: exact formula and research gate

Date: 2026-10-10
Status: literature-grounded exact identity, general-dimensional conditional certificate; NOT a proof of unrestricted LRC and NOT a new theorem.

## Goal
Replace abstract pairwise overlaps from Experiments 49 and 51 with explicit arithmetic functions of the integer speeds. This is an exact known result, not a breakthrough.

## Exact published pairwise overlap (Perarnau–Serra 2016, Proposition 8)
For distinct positive integers a,b, d=gcd(a,b), A=a/d, B=b/d, and 0<delta<1/4, let
epsilon_A={delta*A}, epsilon_B={delta*B}, where {x}=x-floor(x).
Define h(x,y)=min(x,y)+max(x+y-1,0)-2*x*y.
For forbidden-time sets B_a={t mod 1: ||a*t||<delta} and B_b similarly,
mu(B_a intersect B_b) = 4*delta^2 + 2*h(epsilon_A,epsilon_B)/(A*B).
This is the exact formula in Perarnau and Serra (2016), Proposition 8, with reduced speeds A,B. Boundary choices (< versus <=) do not change Lebesgue measure.

## Proof of reduction to coprime speeds
Multiplication by d on the circle is measure-preserving, hence mu(B_a intersect B_b)=mu(B_A intersect B_B). The coprime formula is Proposition 7 of the cited paper. No independent originality is claimed.

## Certified all-dimensional consequence
For k>=2 distinct positive integer speeds and delta=1/(k+1) with k>=4 (so delta<1/4), compute each exact overlap p_ij from the formula. Define W=sum_{i<j}p_ij. Experiment 51 then proves
mu(safe set) >= 1 - 2*k/(k+1) + 2*W/k.
In particular W > k*(k-1)/(2*(k+1)) certifies safe-time existence. Failure to meet the threshold is inconclusive, NOT a counterexample.

## Exact computation protocol
Represent delta, reduced speeds, fractional parts and h by rational arithmetic. For each speed vector, independently compute pair overlaps using interval-sweep rational endpoints and compare with the published formula. Then compare the second-moment lower bound with the exact safe-time measure. No numerical run is claimed in this file.

## Novelty assessment
The arithmetic pair-overlap identity is already published (2016), and the moment inequality is classical. Combining them gives a useful exact audit baseline but is not established Q1-level novelty. A future original result must prove a uniform arithmetic lower bound strong enough to satisfy the displayed W threshold for every vector, or construct another universal certificate.

## Verified primary source
Perarnau, Guillem and Serra, Oriol (2016). Correlation Among Runners and Some Results on the Lonely Runner Conjecture. The Electronic Journal of Combinatorics 23(1), P1.50. DOI: 10.37236/5123. Primary journal: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i1p50 ; PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p50/pdf/ . Existing bibliography key PerarnauSerra2016 in references/lonely_runner.bib; no duplicate entry.

## Open question
Does this exact pairwise correlation certificate suffice for all k and all distinct speeds? This experiment does not establish that, and no general LRC solution is claimed.
