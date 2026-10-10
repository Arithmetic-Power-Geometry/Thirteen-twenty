# Deep novelty and prior-art audit — 10 October 2026

**Purpose:** Theorem-level screening for Experiments 11–31 and preparation for a short mathematical paper. **No verified breakthrough or priority claim.** Bibliography: `references/lonely_runner.bib` (12 entries).

## 1. Research claims that survived mathematical testing

**A. Universal fixed-threshold additive-triple bound (Experiment 25).**
For all positive integers a,b, `F_(1/16)(a,b)>=13/20`, equality (1,14). Analytic coprime discrepancy `|F−169/256|<=2/max(a,b)` and 11,698 exact finite checks.

**B. Parameterized torus estimate (Experiment 26).**
For coprime a,b, 0<δ<=1/4:
`|F_δ(a,b)−(1−3δ)^2|<=2/max(a,b)`.
This follows from a 2D torus mean and discrepancy of equally spaced points against a union of at most two circle intervals. The *method* is standard; novelty not established.

**C. Exact symbolic special-family formula (Experiment 28).**
For every integer q>=5, `F_(1/q)(1,q-2)=(q-3)(q-4)/(q(q-1))`, by exact forbidden-interval overlap counts. Likely elementary; originality unverified.

**D. Global sharp lower bounds for q=5,...,16 (Experiments 25,30,31).**
Combining the discrepancy finite cutoff and exact arithmetic shows the formula from C is the global minimum for all a,b for each integer q=5,...,16. New q=11..16 certificate has 40,998 exact cases; q=5..10 certificate has 6,410 cases. This is the strongest cumulative research result. No theorem for every q>=5 is claimed.

**E. Global minimization for every q>=5.**
OPEN. Finite experiments suggest the same formula, but q>=17 is not proved by the existing experiments.

## 2. Closest verified prior literature

| Work | What primary metadata establishes | Relation to our work | Overlap risk |
|---|---|---|---|
| Perarnau & Serra, *Correlation Among Runners...*, Electronic Journal of Combinatorics 23(1), P1.50 (2016), DOI 10.37236/5123 | Quantitative correlation of time runners spend near the origin | **Directly** adjacent to our forbidden-interval intersection method | HIGH: must read exact propositions and intersection formulas |
| Perarnau & Serra, *The lonely runner conjecture turns 60*, Computer Science Review 58, 100798 (2025), DOI 10.1016/j.cosrev.2025.100798 | Peer-reviewed 2025 survey of results and open problems | Principal prior-art map; follow citations and precise theorem statements | HIGH: essential before claiming novelty |
| Tao, *Some remarks on the lonely runner conjecture*, Contributions to Discrete Mathematics 13(2) (2018), DOI 10.55016/ojs/cdm.v13i2.62728 | Quantitative loneliness bounds and finite reduction for integer speeds | Finite reduction and harmonic/measure methods have precedent | MODERATE-HIGH |
| Giri & Kravitz, *The structure of Lonely Runner spectra*, Cambridge journal DOI 10.1017/S0305004125101497 | Studies spectral structure and thresholds | Closely related parameterization of threshold values | HIGH: full theorem audit needed |
| Beck & Everett, *Lonely Runner Relations*, arXiv:2609.06259 (2026) | Short integer relations characterize counterexamples/tight instances; shifted and varying thresholds | Our additive triple is the relation (1,1,-1) | HIGH for structural motivation, uncertain for exact measure bound |
| Jensen, *Mixed thresholds...*, arXiv:2605.27941 (2026) | Mixed separation thresholds | Threshold generalization overlaps our parameterized study | MODERATE-HIGH; full text not audited |
| Zhang, *Tight instances...*, arXiv:2608.13599v2 (2026) | Classification of tight modified speed sets and growth bound | Extremal structures, but focuses on maximal minimum separation, not our safe-time measure | MODERATE |
| Rosenfeld, *...eight runners*, arXiv:2509.14111 (2025); *...nine runners*, arXiv:2512.01912 (2025) | Computer-assisted proofs for higher runner counts | Shows computer-assisted certification itself is not novel | LOW for exact additive-triple measure; HIGH for methodological positioning |
| Trakulthongchai, *Nine and Ten Lonely Runners*, Electronic Journal of Combinatorics 33(2), P2.46 (2026), DOI 10.37236/14972 | Peer-reviewed computer-assisted nine/ten runner results | Establishes high contemporary standard for computation certificates | LOW for exact measure theorem |
| Sungkawichai & Trakulthongchai, *Eleven, twelve, and thirteen lonely runners*, arXiv:2604.23906 (2026) | Computer-assisted thirteen-runner result | Frontier context; not directly our three-speed measure bound | LOW |
| Allikvere, *Fourteen and fifteen lonely runners*, arXiv:2609.02604v2 (2026) | Preprint reports fourteen/fifteen total runners, with Zenodo code/certificates | Frontier context, different lattice/prime-sieve approach | LOW for our bound, HIGH importance for honest open-problem statement |

Primary URLs and verified metadata are stored in the bibliography. A source's existence and abstract do NOT prove that it lacks a special-case result; absence of a matching search phrase is not a novelty proof.

## 3. What is mathematically new *within this project* versus potentially new to the field

- **Internally new and fully scoped:** explicit sharp additive-triple measure and 12 reciprocal thresholds, complete exact rational certificates, reproducible files.
- **Probably routine mathematical tools:** inclusion–exclusion, coprime grid equidistribution, 1D interval discrepancy, scaling, rational boundary enumeration.
- **Candidate paper-level novelty:** exact **global minimum safe-time measure** for additive triples at specified thresholds; possibly a general q-formula if proved. We have **not** verified whether the exact minimum follows immediately from a prior theorem.
- **No support for claims:** 'solved the Lonely Runner Conjecture', 'solved sixteen runners', 'first ever correlation bound', or 'independently novel theorem'.

## 4. Potential hidden problems requiring independent checks

1. Independently reimplement and run each full finite certificate (not just trust stored CSV). Check integer-overflow safety for any extended q.
2. Verify the circle-arc discrepancy lemma for all endpoint and wrap-around configurations; measure-zero endpoints are harmless, but connected-component counting must be rigorous.
3. Inspect 2016 Perarnau–Serra PDF and 2025 survey full theorem/proposition lists for the exact F_δ measure question.
4. Audit the spectral literature for already known extremal values, especially q=5..16.
5. Check whether global minimization for all q follows from a simple general overlap identity or is false for some q>=17.
6. Validate citation metadata and all cited claims against final publisher/arXiv versions before journal submission. Existing BibTeX contains explicit publication-status caveats where appropriate.
7. Verify precise runner-count conventions: k relative speeds corresponds to k+1 total runners in some formulations; never equate a three-speed measure theorem with sixteen runners.

## 5. Publication-readiness verdict

**Not yet submission-ready.** We have a plausible short paper centered on a narrow sharp additive-triple measure problem, but the highest-value step is to prove the formula for *all* q>=5 or identify the precise first exception. Even then, specialist novelty review and independent reproducibility are essential. A short note should not assert resolution of the Lonely Runner Conjecture.

## 6. Source verification register
- Perarnau–Serra 2016: publisher DOI 10.37236/5123; title/authors/issue/number verified.
- Perarnau–Serra 2025 survey: university publication repository and dblp; DOI 10.1016/j.cosrev.2025.100798, volume 58 article 100798 verified.
- Trakulthongchai 2026: publisher page; DOI 10.37236/14972, volume 33(2), P2.46 verified.
- Rosenfeld 2025 nine-runner: arXiv:2512.01912 title/author verified.
- Allikvere 2026: arXiv:2609.02604v2 abstract, code/certificate claims verified as **author-reported**, not independently reproduced.
- Zhang 2026: arXiv:2608.13599v2 title/author/version verified.
- Tao: arXiv:1701.02048 and journal DOI metadata from earlier bibliography; 2018 journal version.
- Other existing references: retain recorded identifiers; full theorem comparison remains open.
