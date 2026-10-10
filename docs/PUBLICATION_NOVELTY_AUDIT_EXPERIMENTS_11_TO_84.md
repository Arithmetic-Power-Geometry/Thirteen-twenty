# Research portfolio audit — Experiments 11–84 (10 October 2026)

## Coverage and caveats
The experiments directory contains numbered reports Experiment_11.md through Experiment_84.md (74 reports). Experiments 1–10 have no individual report there. Although requested through experiment 83, experiment 84 was also available and inspected. This screening read the repository INDEX, individual reports 25, 28–35, 36–84 (with focused extraction for routine reports), earlier novelty audit, and comparison of primary literature records; it is NOT a line-by-line independent execution or specialist priority certification of every proof. The index is stale and still says 11–48 despite presence through 84.

## Ranked claims
1. **25–35: sharp quantitative additive-triple measures.** For q=5,...,20 reports state F_q(a,b)>=M_q=(q-3)(q-4)/(q(q-1)), equality at coprime (1,q-2). Experiment 28 analytically evaluates equality family for every integer q>=5; fixed-q global lower bounds rely on analytic discrepancy plus exact finite computation. q=16 is 13/20, q=20 is 68/95. The general all-q bound is conjectural. This whole family, rather than 13/20 alone, is the strongest paper candidate; priority against Perarnau–Serra 2016 and spectrum literature remains uncertain.
2. **67–69,77: gcd-normalized arithmetic obstruction for isolated safe witnesses/tight cases.** The claimed divisibility q | (v_i+v_j)/gcd(v_i,v_j) necessary for tight instances and a modular test for isolated witnesses can be framed as a structural note if substantially extended and compared to Fan–Sun 2026, Zhang 2026, Goddyn–Wong 2006 and Beck–Everett 2026. As it stands it is an elementary critical-point consequence. Absence of a complementary pair does not prove LRC: either strict safety OR a counterexample remains.
3. **79,81–83: provable limitations of pair-tree and fixed odd-order Bonferroni certificates.** Exp 79 no-go for large reduced pair-products. Exp 81 negative third-order truncation on lacunary family for k>=8; Exp 82 positive fifth-order asymptote on that family; Exp 83 any fixed odd truncation fails to give a universally positive certificate on consecutive speeds. Intrinsically interesting methodological comparison, but all rely on classical Bonferroni, Fourier decorrelation, and known tight examples. Exp 83 is nearly immediate from zero-measure safety and pointwise Bonferroni; low standalone novelty.
4. **70,78,80 and 48–52: exact pair overlap and higher-order certificate calculations.** Exp 78 Bernoulli polynomial identity and 630 rational checks; closest Jensen 2026 equal/unequal threshold formula and Perarnau–Serra 2016. Exp 80 uses standard third-order Bonferroni. Not independently novel as stated.
5. **37,43,46,47,54,55,74–76,84: exact rational finite instance optimization/certification.** Useful reproducible software, but the critical-time/boundary principle is classical; Exp 75's (1,3,4,7) was recognized in Exp 76 as Wills' classical example, not newly discovered.
6. **39–42,56–62,72–73: restricted modular witnesses/fibers/fast-runner inductions.** Explicitly conditional or classical. Exp 65 corrects 59–62's fast-runner lemma as already in Fan–Sun 2026 Lemma 13.
7. **44–45,63–66: Kronecker rank or short-relation criteria and counts.** Most derived from classical geometry or Beck–Everett 2026; Exp 66 expressly weaker than Czerwinski random-runners result.
8. **11–24: archival background and some retrospective summaries.** Exp 11 is a different union-closed-set problem. Do not claim full originally recovered proofs from summaries.

## Theorem and citation gates
- **Crucial:** Re-run all full exact certificates independently for every q=5..20. Check q=16 has 11,698 primitive pairs below analytic cutoff 197, q=20 has 27,054 below cutoff 299. Inspect sources for integer overflows, endpoint cases, and exact arithmetic. Current audit has NOT reproduced all of them.
- Compare exact proposition statements of Perarnau and Serra (2016), *Correlation among runners and some results on the Lonely Runner Conjecture*, EJC 23(1), P1.50, DOI 10.37236/5123, whose published subject is quantitative correlation of near-origin runner sets. https://arxiv.org/abs/1407.3381
- Compare Beck and Everett (2026), *Lonely Runner Relations*, arXiv:2609.06259. Their short-relation theorem concerns counterexamples/tight sets, unlike an exact safe-time measure. https://arxiv.org/abs/2609.06259
- Check Fan and Sun (2026), *Amending the Lonely Runner Spectrum Conjecture*, EJC 33(1), P1.38, DOI 10.37236/13840 and Yuhan Zhang (2026), arXiv:2608.13599.
- Avoid implying general LRC is solved or three frequencies settle 16 runners.
- Seeking a uniform proof for all integers q>=5 would dramatically strengthen Paper 1; absent that, exact fixed-q sharp theorem family still deserves an original-work audit.
- First target E-JC (requires substantial original math; no page limit; initial PDF, self-contained; reproducible supplementary computation), conditional on originality verification. Experimental Mathematics alternative for well-explained computer-assisted certificates.
- A separate CS/scheduling application paper requires real phase/sensor data and calibrated physical assumptions; cannot replace pure-math novelty.

## Publication strategy
**Paper A** (priority): *Sharp Safe-Time Measure Bounds for Additive Triples of Integer Frequencies*. Present verified q=5..20 family and full analytic cutoff + finite certificate. Include exact equality classification, source code, reproducible verification and honest limitation. No invented novelty percentages.
**Paper B** (contingent): *Arithmetic Characterizations of Isolated Witnesses in Tight Lonely Runner Configurations*. Only if a clear genuinely new strengthening beyond classical critical-time methods emerges.
**Paper C** (methods/software): Combine precise no-go certificates (79,81–83) with new optimal/adaptive higher-order correlation scheme; do not submit classical identities alone.

## Open high-value problems
1. Prove or disprove global sharp formula for all q>=5.
2. Improve discrepancy from O(1/max(a,b)) or derive exact minimized expression uniformly in q.
3. Find nontrivial new infinite family or density bounds for tight instances not subsumed by Beck–Everett/Fan–Sun.
4. Derive an adaptive signed/higher-order certificate that handles canonical zero-measure tight sets, or make a genuine computational complexity advance for exact safe-set enumeration.
