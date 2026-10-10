# Electronic Journal of Combinatorics — Submission Plan for the Sharp 13/20 Theorem

Date: 2026-10-10. Target: The Electronic Journal of Combinatorics (E-JC). This is a planning note, not an acceptance or novelty certification.

## Journal requirements (from official E-JC About and Submissions pages, supplied by author)
- Scope: original, self-contained and substantial contributions to discrete mathematics, combinatorics, graph theory and combinatorial algorithms.
- No page limit. Practical target: 18–25 pages if the proofs and computational audit require it; this is a recommendation, not a journal rule.
- Initial submission: PDF with a self-contained abstract; do not upload source files initially. HTML abstract entered separately.
- Final accepted manuscript: e-jc.sty and ejc-sample.tex conventions; single self-contained LaTeX file including bibliography; figures bundled in one archive as needed.
- No simultaneous submission elsewhere; author must comply with three-calendar-month E-JC submission restriction.
- Authors must personally check, rewrite and vouch for every AI-assisted proof and statement.
- Free for authors and readers. Median time submission-to-publication reported as six months, not a guarantee.
- Official links: https://www.combinatorics.org/ojs/index.php/eljc/about/submissions ; https://www.combinatorics.org/ojs/index.php/eljc/about

## Proposed title
Sharp Safe-Time Measure Bounds for Additive Triples of Integer Frequencies

## Central theorem under independent verification
For positive integers a,b, define F(a,b)=mu{t in [0,1]: ||at||, ||bt||, ||(a+b)t|| >= 1/16}. Claimed sharp universal bound F(a,b)>=13/20, with equality at primitive (1,14), up to swapping and common scaling. See experiments/Experiment_25.md and docs/RESEARCH_REPORT.md. This is not a solution to the unrestricted Lonely Runner Conjecture.

## Recommended outline
1. Abstract and main results (1 page).
2. Introduction, related work and exact novelty comparison (2–3 pages).
3. Notation, scaling invariance, circle and torus geometry (2 pages).
4. Torus average and grid discrepancy lemmas (3–4 pages).
5. Sharp theorem, analytic cutoff, equality analysis (4–5 pages).
6. General reciprocal-threshold extensions from Experiments 25–35, only after separate proof validation (3–4 pages).
7. Exact certificate: all primitive pairs below cutoff, executable code, integer/rational arithmetic, hashes and independent reproduction (3–4 pages).
8. Discussion, limitations, optional short periodic-scheduling interpretation (1 page).
9. Verified references and any necessary appendices.

## Pre-submission gates
- Confirm the torus average 169/256 and rigorous discrepancy bound 2/max(a,b).
- Independently reproduce the exhaustive finite range max(a,b)<=196, including claimed 11,698 coprime pairs, zero violations, unique equality.
- Check correctness of exact sweep and equality classification, and archive code, environment and checksums.
- Read closest original publications theorem-by-theorem (especially Perarnau–Serra 2016, Tao 2018 and recent 2025–2026 work); avoid originality claims based on keyword searches.
- Check all generalizations independently; label conjectures as conjectures.
- Verify every bibliographic record and cross-reference.
- The journal is mathematically focused: applications can be a short rigorous interpretation but must not replace a substantial original proof. Any 65% scheduling statement requires three integer-related frequencies a,b,a+b, aligned phases and a 1/16 exclusion neighborhood.
- Submit only once novelty, proof and certificate audits pass. No acceptance guarantee.

## Journal fit
A potentially suitable venue, but E-JC demands originality, correctness and substantial interest. The target is not an endorsement by the journal. Quartile/indexing should be checked against current authoritative databases separately.
