# Experiment 85 — Primary-source verification and bibliography audit

Date: 2026-10-10. Scope: sources actually used to contextualize Experiment 85, not the entire repository bibliography.

1. Beck, Matthias; Hosten, Serkan; Schymura, Matthias (2016). *Lonely Runner Polyhedra*. arXiv:1606.01783. https://arxiv.org/abs/1606.01783 . The primary arXiv record verifies all three authors, title, submission year and geometric approach to LRC. The arXiv identifier, title and an existing BeckHostenSchymura entry are already present in references/lonely_runner.bib. No duplicate appended.
2. Beck, Matthias; Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259. https://arxiv.org/abs/2609.06259 . Primary arXiv record verifies authors, title and the bound 0<||m||_1<=2k+3 for short relations in tight or counterexample configurations. Existing key BeckEverett2026 verified in the repository. No duplicate appended.

The nested-interval proof is self-contained and does not assume the Beck–Everett theorem. Its lacunarity threshold 2k/(k-1) is a sufficient condition, not a universal bound. The specific threshold's priority relative to folklore and the polyhedral literature has NOT been established, so publication-level novelty must not be asserted.

Exact verification: an independent local Python Fraction execution checked 463 nested-interval constructions for k=2,...,30, with exact containment and length assertions. The committed script was corrected to assert the actual 463 cases (not 464). This tests finite cases; the theorem itself is proved analytically in Experiment 85.

All cited references were already in the existing bibliography; none needed adding. The full bibliography has not been comprehensively verified entry by entry.
