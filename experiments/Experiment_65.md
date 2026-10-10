# Experiment 65 — Priority correction and exact one-fast-runner induction

Date: 2026-10-10
Status: proved, but NOT NEW: the main inequality is already in Fan and Sun (2026), Lemma 13. This experiment corrects the originality assessment of Experiments 59–62.

## Primary-source discovery
Fan and Sun, *Amending the Lonely Runner Spectrum Conjecture*, Electronic Journal of Combinatorics 33(1), P1.38 (2026), DOI 10.37236/13840, Lemma 13, explicitly state and prove the one-very-fast-runner inequality. Its condition, specialized below, is EXACTLY Experiment 60's V>=kM. Hence Experiment 60 is not independent novelty. Its safe-interval reformulation (Experiments 61–62) is also an elementary consequence, not a breakthrough.

## Theorem 65.1 (known result, correctly attributed)
For old speeds a_1,...,a_{k-1}, let L=max_t min_i ||a_i t||, and M=max_i a_i. For any desired target 0<d<L, if an additional speed V satisfies V>=d*M/(L-d), then the augmented vector has maximum loneliness at least d.

## Proof (self-contained)
Choose t0 attaining L. If ||V*t0||>=d, t0 works. Otherwise V*t0 lies in a forbidden arc of radius d. Move t0 by the shortest distance to the boundary of that forbidden arc; the move has magnitude at most d/V. At the new time the new runner is exactly d from an integer, and each old runner loses at most M*d/V in circular distance. Since V>=d*M/(L-d), each old distance remains >=L-M*d/V>=d. QED.

## Corollary 65.2 (Experiment 60 is already known)
Set L>=1/k, d=1/(k+1). Then d/(L-d)<=k, so V>=k*M is sufficient. This reproduces Experiment 60 exactly and must be cited to Fan–Sun Lemma 13 rather than claimed as a new result.

## Example and significance
If the old configuration has a stronger-than-required witness, the exact threshold d*M/(L-d) may be much smaller than k*M. This is an adaptive bound, but it is a direct application of Fan–Sun, not a new theorem.

## Research-level decision
The next independent work must NOT be another perturbation, interval, or one-fast-runner lemma. An original advance would require a mechanism addressing closely spaced relation-bearing vectors, ideally with an explicit infinite family outside existing arithmetic-progression, modular, and lacunary classes. No such result is established here.

## Further verified literature
- Sebastian Czerwiński, *The lonely runner problem for lacunary sequences*, Discrete Mathematics 341(5) (2018), 1301–1306, DOI 10.1016/j.disc.2018.02.002. Publisher metadata verified 2026-10-10. This provides prior work on lacunary families and undercuts novelty claims based only on rapid growth.
- Ho Tin Fan and Alec Sun, *Amending the Lonely Runner Spectrum Conjecture*, Electronic Journal of Combinatorics 33(1) (2026), P1.38, DOI 10.37236/13840, especially Lemma 13. Publisher PDF verified 2026-10-10. Already in references/lonely_runner.bib.

## Verdict
Proved and correctly attributed a general all-dimensional lemma. The work is a priority correction and stronger research gate, not a new mathematical solution. Unrestricted LRC is unsolved; Q1-level novelty of Experiment 65: none.
