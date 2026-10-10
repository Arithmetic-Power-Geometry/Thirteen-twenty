# Experiment 33 — Sharp additive-triple bound at threshold 1/18

Date: 2026-10-10. Status: computer-assisted proof of one additional fixed threshold.

For every positive integer pair a,b,

**F_(1/18)(a,b) >= (18-3)(18-4)/(18*17) = 35/51**,

where F is the fraction of t in [0,1] such that ||at||,||bt||,||(a+b)t|| >= 1/18. Equality holds at (a,b)=(1,16), up to swapping and common scaling.

## Proof
For coprime a<=b, Experiment 26 gives
F_(1/q)(a,b)>=(1-3/q)^2-2/b.
The difference between the torus average and the proposed sharp bound is 3(q-3)/(q²(q-1)).
At q=18, the large-speed cutoff is
B=ceil(2*18²*17/(3*15))=245.
All b>=245 satisfy the bound analytically. For 1<=a<=b<245 and gcd(a,b)=1, exact integer endpoint sweeps were performed, yielding **18,176** checked pairs, **zero violations**, and a **unique coprime equality** at (1,16).

Data: `data/experiment_33_results.csv`. Independent reproducibility source: `src/experiment_33_verify.py`.

## Novelty and research scope
The exact special-family equality was analytically proved in Experiment 28. Experiments 25, 30, 31, 32, 33 now cover all integer q=5,...,18. A uniform proof for every q>=5 is NOT established; the full Lonely Runner Conjecture is NOT solved. Novelty relative to prior correlation and finite-checking theorems remains unverified.

## New literature
Malikiosis, Santos, and Schymura (2025), *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107. Its global finite-checking theorem for the ordinary LRC is distinct from our quantitative three-speed safe-time measure problem; its methods are important context. Publisher metadata verified and appended to `references/lonely_runner.bib`.
