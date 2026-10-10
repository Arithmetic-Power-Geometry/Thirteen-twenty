# Formal problems and proof obligations

## Fixed phase-aligned availability model

Let a,b be positive integers, c=a+b, epsilon=1/16. Write ||x||=min_{k integer}|x-k|. Define the closed feasible set S(a,b)={t in [0,1]: ||at||>=epsilon, ||bt||>=epsilon, ||ct||>=epsilon}. Its boundaries are rational. The underlying sharp safe-time result is measure(S)>=13/20; it does not directly constrain contiguous length or the placements of jobs with release/deadline windows.

Input integers a,b are encoded in binary unless otherwise stated. Rational numbers are given in reduced numerator/denominator form; complexity results must specify bit complexity or arithmetic-operation complexity. An O(a+b) interval enumeration is pseudopolynomial in the binary input length.

## P1: Single-job exact admission

Input: a,b, rational r,d,p with 0<=r<=d<=1 and p>0. Decide whether there exists rational s such that r<=s, s+p<=d, and [s,s+p] subset S(a,b). Output YES with exact rational witness s and verifiable inclusion proof, or NO with full feasible-window certificate showing none accommodates [s,s+p]. A sorted feasible-interval list solves the straightforward explicit-interval version; this is a **baseline, not novel**.

## P2: Multiple nonpreemptive jobs on one resource

Input: a,b and jobs J_i=(r_i,d_i,p_i), all rational and nonpreemptive. Decide whether there exist nonoverlapping starts s_i, each [s_i,s_i+p_i] subset S(a,b) and [r_i,d_i]. Clarify whether all jobs must be scheduled, weighted maximum throughput or other objective. An NP-hardness claim requires a rigorous polynomial reduction using the specially constrained family S(a,b), not the complexity of generic scheduling alone. Explore tractable restrictions such as common release/deadline, unit processing times and bounded distinct durations.

## P3: Repeated admission queries and updates

For fixed a,b preprocess S, then answer many P1 queries or support reservation updates. Measure query time, preprocessing time, update time, certificate size and exactness. Compare against predecessor search, interval trees, segment trees and prefix maxima. Novelty requires a **proven** improvement under explicit model assumptions.

## P4: Robust admission

Let adversarial phase offsets phi_v lie in declared bounds, or job timing errors lie within intervals. Decide whether a schedule is valid for **all** perturbations. The 13/20 original theorem assumes aligned phases and cannot automatically certify offset robustness. Establish new independent claims with correct quantifiers.

## P5: Proof-carrying schedules

Design compact YES certificates (rational starts, exact phase guards, nonoverlap checks) and NO certificates checkable by a simpler independent verifier. Feasibility witness is easy; short infeasibility certificates may be hard for the general multi-job problem. Make no complexity-class claims until proven.

## Baseline mathematical observation to verify

There are at most 4(a+b) phase-boundary points in one horizon. The published paper's averaging argument gives a contiguous slot of length at least 13/[20(4(a+b)+1)]. An exploratory improvement can count at most 2(a+b) excluded neighborhoods on the circle, giving a candidate non-wrapping bound 13/[20(2(a+b)+1)]. This observation must be formally checked, compared with elementary interval-count arguments and never advertised as breakthrough without a novelty audit.

## General correctness obligations

- Exact open versus closed endpoint conventions.
- Boundary at t=0 and t=1 and wraparound treatment.
- Rational arithmetic without overflow.
- Equality, common-scaling invariance and a=b corner cases.
- Generator-validation of every purported certificate.
- Algorithm bounds in both numerical frequencies and input bits.
