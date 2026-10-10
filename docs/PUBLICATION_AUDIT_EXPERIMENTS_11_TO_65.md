# Publication selection audit: Experiments 11–65

Date: 2026-10-10. This audit retrieved the 55 individual experiment reports numbered 11 through 65 from the connected GitHub repository. Experiments 1–10 are not included in the numbered experiment archive and therefore were **not** reviewed. This is a mathematical-content and publication-positioning screening, not independent reproduction of all software or peer-review-level certification.

## Recommendation

**Top candidate: sharp additive-triple safe-time measures, Experiments 25–35.**

For integer q=5,...,20 and positive integers a,b, define

F_q(a,b) = mu{t in [0,1] : ||at||, ||bt||, ||(a+b)t|| >= 1/q}.

The experiment archive claims a sharp fixed-q computer-assisted theorem

F_q(a,b) >= (q-3)(q-4)/[q(q-1)],

with equality at (a,b)=(1,q-2), up to swapping and common integer scaling. The q=16 result gives 13/20, and q=20 gives 68/95. The explicit family equality is proved analytically for all q>=5 (Experiment 28), whereas **global minimization is only certified for q=5,...,20**. The conjectured global formula for all q>=5 is **not proved**.

### Why this is the strongest candidate

1. A specific sharp quantitative inequality rather than a conditional witness.
2. Equality cases and an explicit infinite one-parameter family.
3. Infinite-to-finite reduction via torus average and discrepancy.
4. Exact rational/integer finite verification, with archived source and result tables.
5. A coherent standalone mathematical question different from proving the unrestricted Lonely Runner Conjecture.

### Publication gate: mandatory before submission

- Re-run each q=5,...,20 certificate from a clean checkout, verify exact pair counts, zero violations, equality uniqueness, and the claimed cutoff; compare independent implementations.
- Formally audit the torus-average formula, interval component count, discrepancy constant 2/max(a,b), and integer sweep denominators.
- Compare full text of Perarnau–Serra (2016), Perarnau–Serra (2025), Tao (2018), Giri–Kravitz (2026), and the closest Bohr-set/three-frequency intersection literature. **No independent novelty is established yet.**
- State the scope precisely: three speeds with additive relation c=a+b, 16 fixed reciprocal thresholds. Do not call this an unrestricted all-dimensional LRC proof.
- Present q=5,...,20 as one theorem with a parameterized finite verification, and the exact (1,q-2,q-1) family as a separate analytic theorem.
- Provide machine-verifiable certificates, build/run instructions, artifact hashes, and independent reimplementation.

## Other experiment clusters

| Rank | Experiments | Theme | Publication decision |
|---|---|---|---|
| 1 | 25–35 | Sharp additive-triple safe-time measure | Best conditional publication candidate; novelty and certificates must pass |
| 2 | 37, 43, 46–47, 54–55 | Exact critical-time optimization, threshold endpoints, safe-set measure | Could support a software/artifact note with benchmarking, not a new theorem claim |
| 3 | 40–42, 57–58 | Modular fibers, shifts, overlaps | Conditional family; substantial overlap with earlier methods and internal experiments |
| 4 | 36, 48–52, 62 | Fourier, union/Bonferroni, pair correlations, discrepancy | Established analytic techniques; supporting background |
| 5 | 44–45, 63–64 | Kronecker rank and short relations | Useful reductions and methodological limitations; little independent novelty |
| 6 | 59–61, 65 | Fast-runner extension, safe components | Experiment 65 acknowledges the key speed-extension inequality is Fan–Sun (2026), Lemma 13; not original |

## Integrity observations

- Experiment 11 concerns the **Frankl union-closed sets conjecture**, not the Lonely Runner Conjecture. It must not be silently included in an LRC paper as evidence.
- Experiments 12–24 are retrospective summaries, not reconstructed original proofs.
- Experiments 38 and 56 substantially duplicate the same modular witness.
- Experiments 43, 54 and 55 cover closely overlapping endpoint certificates.
- Experiments 45 and 63 implement the same Beck–Everett relation-exclusion principle; Experiment 64 explains why the relation-bearing stratum cannot be excluded.
- Experiments 49–52 build on known correlation/Bonferroni methods; Experiment 50 acknowledges Perarnau–Serra's prior tree inequality.
- Experiments 59–62 are conditional extension and safe-set refinements; Experiment 65 identifies direct prior art for the fast-runner threshold.
- The original Experiment 48 is the first-moment union-bound report, not a separate quantitative-gap report.
- Experiment 65 cites Sebastian Czerwiński (2018), *The lonely runner problem for lacunary sequences*, DOI 10.1016/j.disc.2018.02.002, which is **not among the 31 existing BibTeX keys**. This should be added after primary-source metadata verification.
- The experiment index is stale and does not reflect 49–65. Do not infer completion from that index.

## Suggested manuscript title

**Sharp Safe-Time Bounds for Additive Triples of Integer Frequencies: Analytic Reduction and Exact Certificates**

Alternative: **Exact Safe-Time Measures for Additively Related Runners at Reciprocal Thresholds**

## Verdict

**Promising research manuscript after independent validation, not currently submission-ready.** A peer-reviewed mathematics journal is more appropriate than presenting the existing experiment archive as an unrestricted breakthrough. Acceptance probability cannot responsibly be quantified without novelty comparison and external referee assessment.
