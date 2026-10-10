# Novelty audit — Experiment 25, sharp 13/20 safe-time measure

Date: 2026-10-10. Status: **preliminary full-text/metadata literature screening; originality NOT certified.**

## Mathematical claim

For positive integers a,b, F(a,b)=mu{t in [0,1]: ||at||, ||bt||, ||(a+b)t|| >= 1/16}. Experiment 25 claims F(a,b)>=13/20, equality for coprime (a,b)=(1,14) up to interchange and scaling.

The proposed distinguishing feature is a **sharp global lower bound on safe-time measure** for a three-frequency additive relation, not merely existence of a safe time or a general Lonely Runner result.

## Verified mathematical spot checks

A fresh independent exact rational endpoint sweep (Python Fraction, separate from the archived C++ program) returned:
- (1,14): 13/20
- (1,13): 237/364
- (1,15): 1261/1920
- (2,7): 331/504
- (3,14): 941/1428
- (1,1): 13/16

Torus mean 169/256; difference from 13/20 is 13/1280. This independently confirms the equality witness and sample values, **not** the entire 11,698-case certificate.

## Primary literature and priority risks

| Source | Established subject | Relation to proposed claim | Assessment |
|---|---|---|---|
| Perarnau & Serra (2016), DOI 10.37236/5123 | Pairwise runner correlations and overlap estimates; Hunter's inequality | **Very high conceptual overlap**: measure estimates and forbidden-set intersections | Need full-text theorem/proposition-by-proposition comparison; exact 13/20 theorem not located in current searches |
| Tao (2018), DOI 10.55016/ojs/cdm.v13i2.62728 | Rank-three Bohr-set estimates, Fourier methods and generalized arithmetic progressions | **High technique overlap**: triple intersection and measure | Does not by itself demonstrate prior publication of this exact sharp additive-triple inequality |
| Perarnau & Serra, survey (2025) | Review of classical LRC methods | High background and bibliographic tracing relevance | Review all cited measure/correlation papers |
| Jensen (2026), arXiv:2605.27941 | Mixed thresholds and exact two-function integral formula | Medium overlap in threshold-measure methods | Different mixed-threshold setting; verify full text before declaring distinct |
| Bohman, *Coprime mappings and lonely runners* (2022), DOI 10.1112/mtk.12131 | Coprime maps and LRC | Moderate structural overlap | Not an identified duplicate of 13/20 |
| Bounds for the Lonely Runner Problems via Linear Programming (2021/2022), DOI 10.1007/s00574-021-00272-7 | LP bounds and critical time geometry | Lower overlap with measure-minimization claim | Relevant methodological contrast |

Searches for the exact string 13/20 with 'lonely runner', '1/16' and the triple '1,14,15' did **not locate a published exact duplicate**. This is negative search evidence, **not proof of originality**. Searches also checked additive triple Bohr-set measure and three-frequency intersections.

## Novelty separation

**Not original in isolation:** inclusion–exclusion, torus integration, grid discrepancy for unions of arcs, exact rational boundary sweeps, scaling to coprime pairs, or the existence of a safe time for three speeds.

**Potentially original combination:** the exact sharp universal numerical minimum 13/20 for all integer pairs under c=a+b; unique normalized equality (1,14); complete analytic cutoff plus exact certificate; and fixed-threshold extensions q=5,...,20.

**Unproved extensions:** global minimization formula for every integer q>=5; an unrestricted LRC result for arbitrary numbers of speeds; any claim that 13/20 alone resolves sixteen runners.

## Proof and code audit gates

1. Derive torus mean 169/256 with full geometry of triple forbidden intersections; independently check 3/256 overlap.
2. Prove discrepancy <=2/max(a,b) rigorously for each x, including circular component count and endpoint conventions.
3. Check threshold cutoff: 169/256−13/20=13/1280; 2/b<=13/1280 when b>=ceil(2560/13)=197.
4. Rebuild and rerun C++ exact certificate for all coprime 1<=a<=b<=196 (reported 11,698 cases). Independently implement a second rational sweep. Verify no overflow and uniqueness of equality.
5. Compare precise theorems and proofs in the complete Perarnau–Serra 2016 article and Tao 2018, not only abstracts or search hits. Review citing papers and the recent survey's reference list.
6. If priority is not displaced, write a focused theorem/proof/computation paper with a cautious novelty statement.

## Proposed novelty wording (provisional)

'We investigate the Lebesgue measure of simultaneous safe times for the additively constrained speed triple (a,b,a+b). At the fixed threshold 1/16, we establish a sharp universal lower bound of 13/20, attained by the normalized pair (1,14). The proof combines a two-torus average, a uniform finite-grid discrepancy estimate, and an exact finite certificate. This measure-extremal question is distinct from the existence formulation of the Lonely Runner Conjecture.'

**Priority caveat:** Do not state 'first-ever' or 'previously unknown' before the full closest-prior-work comparison.

## Source links

- https://doi.org/10.37236/5123
- https://doi.org/10.55016/ojs/cdm.v13i2.62728
- https://arxiv.org/abs/2605.27941
- https://doi.org/10.1112/mtk.12131
- https://doi.org/10.1007/s00574-021-00272-7
