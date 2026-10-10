# Experiment 88 — Verified source register, exact tests, and novelty limits

Date: 2026-10-10. This is a verification of the three sources used in Experiment 88, not a claim that every entry in the complete bibliography has been audited.

## Source verification
1. Tao, Terence (2018), *Some remarks on the lonely runner conjecture*, Contributions to Discrete Mathematics 13(2). DOI 10.55016/ojs/cdm.v13i2.62728. Verified directly against the publisher record https://cdm.ucalgary.ca/article/view/62728 : author, title, DOI, journal, volume, issue and 2018 publication date. Existing entry in references/lonely_runner.bib, no duplicate.
2. Beck, Matthias; Everett, Samuel (2026), *Lonely Runner Relations*, arXiv:2609.06259v2, https://arxiv.org/abs/2609.06259 . Primary arXiv record verifies title, authors, v2 revision 23 September 2026 and short-integer-relation theorem. Existing entry in references/lonely_runner.bib, no duplicate.
3. Dubickas, Arturas (2011), *The lonely runner problem for many runners*, Glasnik Matematicki 46(1), 25–30, DOI 10.3336/gm.46.1.01. Journal, author and title also confirmed independently by Tao's 2018 publisher bibliography, entry 11. DOI and full citation were primary-source-verified in Experiment 86; the DOI redirect was unavailable in the present web session. Existing key Dubickas2011ManyRunners, no duplicate.

## Exact regression execution
A local Python Fraction audit was executed before committing the repository script. For q=3,...,12, speeds v=1,...,24, and 1- or 2-component rational intervals, 4,800 exact overlap inequalities passed. The core interval [1/7,2/7] and speed 4 gave exact actual overlap 1/14 and certified lower bound 5/98. The repository script reproduces the same checks.

## Mathematical novelty and limits
The component-sensitive bound is proved self-containedly in Experiment 88 and improves the sufficient condition of Experiment 86 for certain sets. Its proof uses classical periodic discrepancy / bounded-primitive reasoning; independent novelty or first priority is NOT established. It does not imply the unrestricted Lonely Runner Conjecture. There are no new sources not already in references/lonely_runner.bib, so the bibliography was deliberately not changed; appending duplicate references would harm citation quality.
