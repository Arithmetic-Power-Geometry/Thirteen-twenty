# Novelty audit — preliminary, 2026-10-10

## Candidate contribution
Sharp safe-time measure F(a,b)>=13/20 for additive triples (a,b,a+b) at separation 1/16, attained at (1,14), with elementary grid discrepancy and finite exact-arithmetic proof.

## Closest work to inspect fully
1. Perarnau & Serra, *Correlation among runners and some results on the Lonely Runner Conjecture*, Electronic Journal of Combinatorics 23(1), P1.50 (2016), DOI 10.37236/5123. Relevant: overlapping forbidden times.
2. Giri & Kravitz, *The structure of Lonely Runner spectra* (2025). Relevant: torus measures, finite reduction and spectrum geometry.
3. Beck & Everett, *Lonely Runner Relations*, arXiv:2609.06259 (2026). Relevant: short additive relations in candidate obstructions.
4. Tao, *Some remarks on the lonely runner conjecture* (2017). Relevant: quantitative Bohr-set and measure arguments.

## Claims NOT established
- Not established that no author previously proved this exact bound or a theorem implying it.
- Not established independent reproduction of the entire finite certificate by a different implementation.
- Not established that the additive triple measure estimate controls 12 arbitrary further runners.
- Not a solution to 16-runner conjecture, nor a verified breakthrough.

## Audit to complete before submission
Check full statements, constants, special configurations, intersection formulas and computational certificates in prior work. Request independent referee review of both the circle-arc discrepancy lemma and the integer verification program. Keep this report updated with exact citations and theorem numbers.

## Verified reference library update — 2026-10-10
The reusable manuscript bibliography is at [references/lonely_runner.bib](../references/lonely_runner.bib). Entries were checked against publisher/arXiv metadata, including Perarnau–Serra (2016), Tao (2018), Giri–Kravitz (online 2025), Beck–Everett (2026), Jensen (2026), Allikvere (2026), and Zhang (2026). The cited preprints must not be presented as peer-reviewed journal articles.

Allikvere arXiv:2609.02604v2 reports computer-assisted proofs for **fourteen and fifteen total runners**. This does not settle the sixteen-runner case. The paper's independent proof verification and peer-review status have not been established here.

Experiment 29 finds the proposed global minimum in a bounded search for 11 thresholds, but the universal variable-threshold minimization remains conjectural. Avoid treating bounded data as a theorem.
