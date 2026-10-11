# Additive-triple safe-time measures — reproducibility

**Sole author:** Mohammad Amir Khusru Akhtar.

This folder supports *Sharp Safe-Time Measures for Additive Frequency Triples: Sixteen Certified Sharp Bounds and Rational Threshold Geometry*.

## Mathematical scope

For the sixteen reciprocal thresholds q=5,...,20, the computer-assisted exact minimum is (q-3)(q-4)/(q(q-1)), with primitive equality (1,q-2), up to transposition. At q=16 the minimum is 13/20. The all-q global assertion remains conjectural.

## Reproducibility

The source programs under `certificate/` include the exact integer forbidden-interval union generator for all sixteen q, the independent C++ midpoint checker for q=16, and a second Python interval-union checker for q=16.

An automated regeneration workflow is stored at [additive-triple-certificates.yml](../../../.github/workflows/additive-triple-certificates.yml). It is designed to regenerate four CSVs with 129,568 records and the two q=16 CSVs with 11,698 records, check exact inequalities and equality cases, write SHA-256 checksums, and commit the results into `results/`.

**Publication status:** Source files and the workflow are committed. The generated CSVs and checksum manifest must be confirmed present in `results/` before claiming the complete certificate dataset is publicly archived. A separate supplementary ZIP contains the full compiled manuscript, source, saved CSVs, and the verified rerun log.

## Independent local rerun (2026-10-11)

All four q-family CSVs were regenerated and matched the archived files byte-for-byte. A freshly compiled C++ midpoint program recomputed q=16, and the independent Python interval-union program reported 11,698 exact agreements, zero violations, and one equality. Both regenerated q=16 outputs matched their archived counterparts byte-for-byte.

This computational evidence does not establish historical novelty or the all-q conjecture.
