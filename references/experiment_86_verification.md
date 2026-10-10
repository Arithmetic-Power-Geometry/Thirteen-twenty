# Experiment 86 — Primary-source reference verification and execution register

Date: 2026-10-10.

## Newly appended reference
Dubickas, Arturas (2011). *The lonely runner problem for many runners*. Glasnik Matematicki, 46(1), 25–30. DOI 10.3336/gm.46.1.01. Primary journal record https://web.math.pmf.unizg.hr/glasnik/vol_46/no1_05.html confirms the author, exact title, year, journal volume/issue, pages, DOI, and a lacunary sufficient condition v_(j+1)/v_j >= 1+33 log(n)/n for n>=16342. New BibTeX key Dubickas2011ManyRunners appended to references/lonely_runner.bib; existing records preserved.

## Existing related reference
Czerwiński, Sebastian (2018). *The lonely runner problem for lacunary sequences*. Discrete Mathematics 341(5), 1301–1306. DOI 10.1016/j.disc.2018.02.002. Elsevier primary record https://www.sciencedirect.com/science/article/pii/S0012365X18300335 confirms author, title, journal, volume, issue, pages and DOI. Already in references/lonely_runner.bib; no duplicate appended.

## Reproducibility and correctness
An independent exact Fraction execution tested 135 constructed hybrid families: k=4,...,30 and core scales 1,2,3,5,11. All stage-by-stage containment and final interval length checks passed. For k=6 the speed set is (1,2,3,12,29,70) and the final interval is [53/245,111/490] of length 1/98. The committed Python program reproduces these assertions.

## Priority and solution scope
The nested-interval gluing theorem is proved directly but builds on elementary covering arguments and an established lacunary-LRC literature. The exact hybrid sufficient condition has not been exhaustively compared with prior work, so independent first-discovery or journal-level novelty is NOT claimed. It does not prove LRC for arbitrary speed vectors. This register verifies the two sources used here; the entire bibliography is not claimed fully audited.
