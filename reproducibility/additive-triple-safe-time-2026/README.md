# Additive triple safe-time measure — reproducibility index

Author: Mohammad Amir Khusru Akhtar (sole author).

This folder documents the 2026 exact-certificate study titled *Sharp Safe-Time Measures for Additive Frequency Triples: Sixteen Certified Sharp Bounds and Rational Threshold Geometry*.

## Mathematical claim
The proven computer-assisted global sharp minimum is `(q-3)(q-4)/(q(q-1))` for the 16 integers `q=5,...,20`. The corresponding global theorem for every `q>=5` is conjectural. The `q=16` specialization gives `13/20`.

## Certification
The 16 finite domains contain 129,568 primitive pairs. A local package compiled 2026-10-11 with the TeX source, compiled PDF, figure, Python/C++ programs, four exact CSVs and SHA-256 manifest. The saved CSV audit checked complete pair coverage, duplicates, integer inequalities and equality cases.

## Reproduction commands (from package root)
- `python certificate/verify_all_csv.py`
- `python certificate/independent_q_family.py --q-start 5 --q-end 8 --out results/regenerated_q5_q8.csv` (repeat for ranges 9–12, 13–16, 17–20)
- `cd paper && pdflatex -halt-on-error main.tex && pdflatex -halt-on-error main.tex`

## Important artifact status
This GitHub folder currently contains the **reproducibility index**, not the full manuscript and dataset upload. The complete 2 MB ZIP is available separately in the ChatGPT conversation that produced it and should be uploaded into this folder before this URL is described as a complete public artifact archive. The existing repository's experiments and source directories are background research, not necessarily byte-identical to the October 11 package.

Independent human proof and historical-originality review remain open. Hashes prove file identity, not mathematical validity.
