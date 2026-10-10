# Experiment 92 — Exact CRT formula for pairwise forbidden-grid overlap

Date: 2026-10-10. **Theorem valid for every number of speeds. Unrestricted Lonely Runner Conjecture remains unsolved.**

## Theorem 92.1

Let k>=2, q=k+1, and let a,b be two speeds in a k-speed vector. Put g=gcd(a,b), A=a/g, B=b/g, ell=lcm(a,b)=gAB, L=lcm(all k speeds), r=L/ell, M=qL. Let T_ab denote the number of grid indices j in {0,...,M-1} at which BOTH a and b are strictly forbidden: ||aj/M||<1/q and ||bj/M||<1/q.

Define two sets of residues modulo qh, for any h>=1:
- V(h) = {0,...,h-1} union {(q-1)h+1,...,qh-1} (strictly forbidden vertices);
- W(h) = {0,...,h-1} union {(q-1)h,...,qh-1} (strictly forbidden open grid cells).

For X in {V,W}, let c_X(h,s) be the number of residues in X(h) congruent to s modulo q. Define
G_ab = sum_(s=0)^(q-1) c_V(B,s)*c_V(A,s)
and
H_ab = sum_(s=0)^(q-1) c_W(B,s)*c_W(A,s).

Then the **exact pair-overlap formula** is

    T_ab = g * ((r-1)*H_ab + G_ab).

All quantities G_ab and H_ab can be computed in O(q(A+B)) time and O(q) memory, without enumerating the full M=qL grid.

## Proof

Because gcd(A,B)=1, the simultaneous phase pattern of speeds a and b has period 1/g in time. Its critical boundary times are on the grid j/(q*gAB). Restrict to one period, and write t=j/(q*gAB), j=0,...,qAB-1. The forbidden condition for a=gA depends only on j modulo qB and is exactly j mod qB in V(B); for b=gB it depends only on j modulo qA and is exactly j mod qA in V(A).

By the generalized Chinese remainder theorem, a pair of residues x modulo qB and y modulo qA is realized by exactly one j modulo lcm(qB,qA)=qAB precisely when x and y agree modulo gcd(qB,qA)=q. Therefore the number of simultaneously forbidden grid vertices in one period is G_ab.

On each open elementary cell (j/(q*gAB),(j+1)/(q*gAB)), neither runner crosses a forbidden boundary. Its midpoint is simultaneously forbidden exactly when j mod qB lies in W(B) and j mod qA lies in W(A). The same CRT argument counts H_ab simultaneously forbidden open cells per period.

Now refine each elementary cell by factor r=L/(gAB). The open set where both runners are strictly forbidden is a finite disjoint union of open arcs. On a circle, if an open set has H_ab elementary open cells and G_ab forbidden grid vertices, it has C=H_ab-G_ab connected components. On the refined grid it therefore has r*H_ab-C = (r-1)*H_ab+G_ab forbidden vertices per period (each open component contains exactly its interior refined vertices). There are g periods on the full unit circle, proving the formula. QED.

## Exact reproducibility

The Python script experiments/experiment_92_crt_pairs.py implements V/W residue histograms, the CRT formula and an independent direct modular-grid scan. It was executed locally on 3,157 primitive-vector pair instances from (k,N)=(2,16),(3,12),(4,10),(5,9), with all comparisons equal.

Examples: V=(1,2,3), q=4, pair counts (1,2):5, (1,3):3, (2,3):3; sum P=11. For V=(1,2,3,6), q=5, pair counts 5,3,3,3,2,3; sum P=19. These reproduce the pair-overlap inputs in Experiment 91.

## Novelty, complexity and limits

This formula is an exact CRT compression of pairwise overlap calculations and can accelerate the Experiment 91 pairwise certificate when qL is large but reduced speed ratios A,B are moderate. It does NOT bound the total overlap from below in a way that settles LRC; it does NOT improve the dimension-only finite-checking bound of Malikiosis–Santos–Schymura (2025). CRT counting and grid refinement are classical; independent novelty and Q1-journal-level significance are NOT established.

Literature compared: Malikiosis–Santos–Schymura (2025), DOI 10.1017/fms.2025.10107; Zhang (2026), arXiv:2608.13599v2; Allikvere (2026), arXiv:2609.02604v2. All three already appear in references/lonely_runner.bib; no duplicate records should be added.

## Verdict
All-dimensional exact formula: PROVED. 3,157 independent pair comparisons: PASSED. Unrestricted LRC solved: NO. Q1 journal-level breakthrough: NOT ESTABLISHED.
