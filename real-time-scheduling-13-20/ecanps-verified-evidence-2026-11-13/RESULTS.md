# ECANPS verified research results — 13 November 2026

Scope: Exact additive-frequency safe-calendar verification and nonpreemptive scheduling tests. The companion `code/` directory contains 18 Python verification/benchmark programs and one C++ source snapshot, copied byte-for-byte from ECANPS. Recorded results below are sourced from ECANPS reports and linked GitHub Actions runs; results are not represented as fresh executions in this transfer.

## Exact arithmetic and proof verification

| Test | Observed evidence | Provenance |
|---|---|---|
| Primitive finite sharp-measure census | 11,698 primitive pairs with 1<=a<=b<=196; zero violations; sole primitive equality (1,14), measure 13/20 | ECANPS P03-23, CI run 43433965022 |
| Canonical ordered-record fingerprint | SHA-256 ff2f21b9027c255d6236ba8c70e693c8f8989ed384dc33942194589e833ca1a8 | ECANPS P03-23 / P03-24 |
| Independent midpoint sample | 490 primitive pairs with 1<=a<=b<=40; no violation, sole equality (1,14) | CI run 43433595720 |
| Analytic arithmetic constants | Torus mean 169/256; strict analytic cutoff 197; witness 13/20 | CI run 43433806615 |
| C++ midpoint vs Python union | All 11,698 per-pair exact comparisons; zero mismatches | ECANPS P03-25 proof-evidence closure |
| Threshold-parametric comparison | Thresholds 1/20, 1/16, 1/12, 1/8, 1/5; 230 exact cross-algorithm comparisons, 230 discrepancy checks, 460 gcd-scaling checks; all passed locally | ECANPS P03-31 |
| Parametric torus means | 289/400, 169/256, 9/16, 25/64, 4/25 respectively | ECANPS P03-31 |

## Calendar query and weighted scheduling tests

| Test | Observed evidence | Provenance |
|---|---|---|
| Implicit primitive calendar vs fully expanded exact oracle | 2,400 comparisons per Python environment; zero mismatches | CI run 43420656902 |
| Indexed calendar benchmark | 8 configurations x 2,000 query comparisons; zero mismatches in Python 3.11 and 3.12 | CI run 43420656902 |
| Generic periodic index | 4,000 exact comparisons; zero mismatches | CI run 43422213166 |
| Component-packing relaxation | 250 exact randomized assignments; zero mismatches; stricter than individual filtering in 55/250 | CI run 43422213166 |
| Exact weighted schedule / permutation oracle | 270 synthetic scheduling cases; zero mismatches; packing strictly improves individual bound in 10/270 | CI run 43422462282 |
| Window-aware component assignment bound | 210 exact comparisons; zero mismatches; improvement over packing in 79/210 | CI run 43422850788 |
| Independent OR-Tools CP-SAT | 15 exact proven optima; zero objective mismatches | CI run 43423246478 |
| Matched tiny exact DP vs CP-SAT | 27 matched cases; zero mismatches; medians DP 0.000223 s and CP-SAT 0.001003 s | CI run 43425627599 |
| Stratified scheduling comparisons | 27 matched cases with 8, 10 and 12 jobs; zero mismatches; neither solver consistently dominates | CI run 43426124018 |
| Equal external wall-budget comparisons | 9 matched cases, 9 jointly proven optima, no mismatches/timeouts under two-second cap | CI run 43432290580 |
| Warm-process matched comparisons | 45 matched cases across 3 calendars, job counts 8/12/16 and 5 replicates; zero mismatches | CI run 43433235501 |

## Warm-process medians (seconds)

| Calendar | Jobs | Exact DP | CP-SAT |
|---|---:|---:|---:|
| (1,1) | 8 | 0.002146 | 0.002741 |
| (1,1) | 12 | 0.010646 | 0.003693 |
| (1,1) | 16 | 0.056899 | 0.004155 |
| (1,14) | 8 | 0.000474 | 0.000963 |
| (1,14) | 12 | 0.000685 | 0.001031 |
| (1,14) | 16 | 0.000501 | 0.001231 |
| (2,3) | 8 | 0.000281 | 0.000848 |
| (2,3) | 12 | 0.000882 | 0.001190 |
| (2,3) | 16 | 0.003708 | 0.002424 |

## Verified boundaries of interpretation

- The 13/20 bound is supported by an analytic argument and complete finite exact certificate; exhaustive code alone does not prove the infinite-domain bound.
- The threshold-parametric result is an analytic discrepancy estimate, not a claim of sharpness at every threshold.
- Generic periodic compression replicates the arithmetic-index representation; arithmetic-specific algorithmic superiority is **not established**.
- The subset DP is not consistently faster than CP-SAT; these timings are small synthetic benchmarks, not industrial scalability evidence.
- The scientific novelty or priority of the sharp 13/20 measure theorem relative to all literature remains **unresolved**.

Source project: https://github.com/Arithmetic-Power-Geometry/ECANPS
