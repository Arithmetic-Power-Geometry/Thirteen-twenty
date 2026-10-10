# Experiment 44 — Rational-rank decomposition: all-dimensional Kronecker product theorem

Date: 2026-10-10. Goal: escape repeated finite-shift/overlap methods. Status: proved a conditional all-dimensional theorem by rational linear independence and the continuous Kronecker theorem. **General LRC not solved.**

## Theorem 44.1 (direct-sum block transfer)

Let V be any finite set of positive **real** relative speeds, partitioned into nonempty blocks V_1,...,V_r. Write W_j=span_Q(V_j), and assume their sum is direct: W_1⊕...⊕W_r. Fix δ∈(0,1/2). If for each block j there exists a time s_j such that ||v*s_j||>δ for **every** v∈V_j (strict safe margin), then there exists a **single** time t>0 such that ||v*t||>δ for every v∈V. In fact the set of such t is relatively dense along the orbit (the latter assertion follows from minimality of a dense translation flow on its compact orbit closure).

### Proof

For each block let H_j be the closure in the torus T^{|V_j|} of its continuous one-parameter orbit t↦(t v mod 1)_{v∈V_j}. Let H be the closure of the combined orbit. By the continuous Kronecker theorem (equivalently, the character-annihilator description of a torus subgroup), the annihilating integer characters of H are exactly the integer vectors (n_v) with Σ_v n_v v=0. The direct-sum hypothesis forces each blockwise sum Σ_{v∈V_j} n_v v=0 separately. Thus the annihilator of H is the direct sum of those of H_j; consequently H=H_1×...×H_r.

For each j, the strictly safe block phase from s_j has an open neighborhood U_j⊂H_j on which all its speeds remain strictly δ-safe. The product ∏U_j is a nonempty open subset of H. Density of the combined orbit in H gives t>0 hitting that product. Every speed is then strictly safe. QED.

**Strictness is essential in this proof:** approximating a boundary-only safe phase need not preserve the non-strict inequality. It is NOT legitimate to omit the strict margin.

### Corollary 44.2 (dimension reduction for LRC)

For k relative speeds, let q=k+1. If the Q-span decomposes into independent blocks, and each block of size r<k is known to satisfy its own LRC at threshold 1/(r+1), then the entire k-speed configuration satisfies LRC at threshold 1/(k+1). Indeed 1/(r+1)>1/(k+1), so each block witness has the strict margin required by Theorem 44.1.

In particular, any speed set with a rationally independent decomposition into blocks of size at most **two** satisfies LRC for every k>=3, because the one- and two-relative-speed cases are elementary. This handles irrational-speed configurations inaccessible to the integer-only modular-fiber experiments.

### Exact irrational-speed example

V=(1,2,sqrt(2),2sqrt(2)), k=4, q=5. Rational spans Q and sqrt(2)Q are independent. The explicit time t=1/4 gives positions (1/4,1/2,sqrt(2)/4,sqrt(2)/2). Since 7/5<sqrt(2)<3/2, the last two positions lie respectively in (7/20,3/8) and (7/10,3/4). All four circular distances are **strictly** greater than 1/5. No floating-point approximation is required.

### Computational audit

Executed src/experiment_44_rank_blocks.py with exact Fraction inequalities to verify the explicit irrational example via squared rational bounds. Additionally, all 175 one-, two-, and three-element integer blocks selected from {1,...,10} admit strict 1/8-safe witnesses on the grid j/120, j=1,...,119. These finite checks illustrate strict margin; the all-dimensional theorem follows analytically from Kronecker, not the enumeration.

### Prior literature and novelty

The continuous Kronecker density theorem and rational-rank decomposition of torus flows are classical, not original claims. This experiment uses the existing verified survey Perarnau–Serra (2025) and the existing Giri–Kravitz (2025/2026) reference for the LRC context. No new bibliographic item was used or appended: retaining the 23 existing verified entries is preferable to padding the paper bibliography with unrelated citations.

### Remaining gap

The direct-sum theorem reduces mixed rational-rank configurations to smaller blocks, but a rationally indecomposable block of arbitrary size remains. In particular, all positive integer speeds lie in a one-dimensional Q-span, so this result does not settle the hardest classical integer-speed cases. No unrestricted proof of LRC is claimed.
