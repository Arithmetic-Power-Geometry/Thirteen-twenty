# Experiment 89 — Literature verification, audit, and Q1 readiness

Date: 2026-10-10. Verification scope: cited sources used in Experiment 89, NOT a line-by-line audit of every entry in the full BibTeX file.

## Primary literature verified
1. Beck, Matthias; Everett, Samuel (2026), *Lonely Runner Relations*, arXiv:2609.06259, https://arxiv.org/abs/2609.06259 . Primary arXiv record confirms authors, title and short-integer-relation theorem for tight/counterexample speed vectors. Existing entry in references/lonely_runner.bib; no duplicate added.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025), *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107, https://doi.org/10.1017/fms.2025.10107 . Existing verified publisher record and BibTeX DOI; no duplicate added.
3. Tao, Terence (2018), *Some remarks on the lonely runner conjecture*, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728, https://cdm.ucalgary.ca/article/view/62728 . Primary publisher page reconfirmed author, title and DOI. Existing BibTeX entry; no duplicate added.

All three references already exist in references/lonely_runner.bib. There is no newly USED source requiring an append. The bibliography was deliberately preserved rather than creating duplicate records.

## Executed numerical audit
The exact Fraction interval-sweep script was run locally and produced:
- 522 primitive speed vectors with positive-measure safe sets.
- 274 successful one-runner deletion extension certifications.
- 21 checks for deletion sets when the full vector had zero safe-set measure, all satisfying the necessary inequality.
- Exact primitive fragmentation ratios m/A=3N at N=7,10,31,100.
These are finite checks, not a proof of unrestricted LRC. Zero measure must not be confused with an empty safe set: isolated tight witnesses can remain.

## Novelty and Q1 readiness
The deletion inequality is a direct contrapositive of Experiment 88, and the primitive fragmentation family is elementary. Priority relative to the wider literature has NOT been comprehensively established. These results alone do not meet a defensible Q1-journal-level originality and significance threshold for a mathematical research paper. The project could potentially support a rigorous methods/reproducibility article if it establishes a genuinely stronger algorithmic or structural contribution against current state of the art, with an independently verified literature comparison, complete experiments, and a coherent central theorem. It cannot be presented as a proof of the unrestricted conjecture.

## Next research obligation
Prove a constraint on the *positions* of the safe-set components or the exact residue structure of the forbidden arcs that eliminates candidate counterexamples not already ruled out by existing short-relation and finite-checking theorems. Merely adding experiments is not evidence of approaching a proof.
