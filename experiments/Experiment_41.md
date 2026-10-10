# Experiment 41 — Overlap-corrected modular-fiber theorem in every dimension

Date: 2026-10-10. Status: **proved finite-set theorem; exact code executed locally**. No unrestricted Lonely Runner Conjecture proof.

## Theorem 41.1 (spanning-tree correction)

Let q>=2 and m>=2 be integers, and let a finite integer-speed list V=A∪B be partitioned so m divides each a∈A. Suppose t0 satisfies ||a*t0||>=1/q for all a∈A. For each b∈B define its forbidden shift set

E_b={h∈{0,...,m−1}: ||b*(t0+h/m)||<1/q}.

For any spanning tree T on the speeds B, define

U(T)=Σ_(b∈B)|E_b| − Σ_({b,c}∈T)|E_b∩E_c|.

Then the number of successful shifts h is at least m−U(T). In particular, **if U(T)<m, at least one shift makes all speeds safe**. The strongest tree certificate chooses a maximum-weight spanning tree with edge weight |E_b∩E_c|. This holds for arbitrary finite dimension k and arbitrary integer speeds.

**Proof.** Root the tree and add its vertex sets one at a time, with parents preceding children. The root contributes at most |E_root| elements to the union. Every other E_b contributes at most |E_b|−|E_b∩E_parent(b)| new elements, because the parent's entire set was already included. Summing gives |∪E_b|<=U(T). At least m−U(T) shifts avoid all E_b. The A-speeds remain invariant under shifts by h/m. QED.

This is a standard finite-set union inequality, not claimed as a novel combinatorial theorem. Its application is a sharper, reproducible certificate than the plain union bound used in Experiment 40.

## Exact example where Experiment 40's naive bound fails but the tree certificate succeeds

Take q=5, m=11, stable A=(11), moving B=(1,2,3), and t0=1/55. The stable speed has position 11*t0=1/5, exactly safe.

The three forbidden sets each have size 4, so the naive sum is 12>=11 and **cannot certify** a witness. A maximum spanning tree has pairwise-overlap weights 2 and 1. Thus

U(T)=4+4+4−2−1=9<11.

The certified successful-shift lower bound is 11−9=2. Exact enumeration finds precisely h=2 and h=8, with first witness t=1/55+2/11=1/5. This is an exact witness for the four-speed set (11,1,2,3) at threshold 1/5, corresponding to five total runners.

## Reproducibility

Executed `python /tmp/exp41.py` with exact Python Fraction arithmetic:
- bad sizes: [4,4,4];
- tree edges (index 0,1, weight 2), (1,2, weight 1);
- tree upper bound: 9; actual forbidden union: 9;
- valid shifts: [2,8].
Additionally enumerated all 16³=4096 triples of subsets of a four-element universe and checked the spanning-tree union inequality; zero failures. Archived executable: `src/experiment_41_overlap.py`. Results: `data/experiment_41_results.csv`.

## Prior literature and limits

Finite time shifts, residue orbit counting, and correlation/overlap reasoning are established techniques in LRC. Relevant existing bibliography entries include Perarnau–Serra (2016) and Bienia et al. (1998). A newly checked September 2026 arXiv paper by Daria Poliakova, *More (shifted) runners, less loneliness* (arXiv:2609.23952), concerns the **shifted** LRC, which is different from the common-start classical conjecture; it is appended to the bibliography solely to distinguish the problem variants. No peer-reviewed status is asserted for the preprint.

## What remains open

The tree bound can still be >=m even when successful shifts exist. No theorem guarantees a favorable modulus, stable set, or tree for every speed vector. This is an improved sufficient certificate in all dimensions, **not a solution for sixteen runners or arbitrary k**.
