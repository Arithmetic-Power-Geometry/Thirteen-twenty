# Experiment 34 — Sharp reciprocal-threshold bound at q=19

Date: 2026-10-10.

**Computer-assisted theorem:** For all positive integers a,b,
`F_(1/19)(a,b)>=((19-3)(19-4))/(19(19-1))=240/342=40/57`.
Equality at (a,b)=(1,17), up to symmetry and common scaling.

## Infinite-to-finite proof
By common-speed scaling and symmetry, assume coprime 1<=a<=b. The established discrepancy bound from Experiment 26 gives
`F_(1/q)(a,b)>=(1-3/q)^2-2/b`.
The gap to the proposed sharp minimum is `3(q-3)/(q²(q-1))`, so all `b>=ceil(2q²(q-1)/(3(q-3)))` are covered. For q=19 this cutoff is 271.

The exact endpoint partition of the remaining `1<=a<=b<271`, gcd(a,b)=1, checked **22,204** coprime pairs, with **zero violations** and **one equality**, at (1,17). All arithmetic decisions used integers, not floats. The exact special-family equality was proved in Experiment 28.

## Reproducibility
`python3 src/experiment_34_verify.py` independently checks the finite certificate; `data/experiment_34_results.csv` stores the summary. A separate JavaScript integer endpoint sweep generated the primary result.

## Scope and literature
This extends the project-level fixed-threshold proofs to every integer q=5,...,19. The conjectured sharp formula for all q>=5 remains open. It does not solve the sixteen-runner Lonely Runner Conjecture. Novelty is not established.

New verified literature relevant to the research frontier:
- Bedert, *Riesz products and the Lonely Runner Conjecture: A wider gap of loneliness* (2025), arXiv:2511.16636.
- Blanco, Criado, Santos, *Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture* (2026), arXiv:2603.24784v3.
- Cordella, *Odd denominators in the Lonely Runner spectrum for six speeds* (2026), arXiv:2609.03444. This item is background, not a proof of our sharp measure inequality.

All new entries are recorded in `references/lonely_runner.bib`. The most direct novelty risk remains Perarnau–Serra's 2016 paper on correlations, which needs a proposition-level comparison before claiming originality.
