# CS-010 — Executable reproducibility and benchmark protocol

**Status:** benchmark harness and GitHub Actions workflow committed. Do not claim test passes or timing results without inspecting the completed Actions run artifacts.

## CI

The workflow at repository root `.github/workflows/thirteen-twenty-cs010.yml` runs the full unittest suite on Python 3.11 and 3.12, writes a test log, executes the benchmark, and uploads JSON/txt artifacts. It runs on pushes touching this research folder and supports manual dispatch.

## Benchmarks

Five fixed frequency pairs, 120 seeded rational admission queries each, classical linear scan, binary-search-plus-scan, and segment-tree index. Time preprocessing separately. Verify every query answer against exact oracle. Check sample equal-job YES/NO certificates with independent verifier. Record Python version, platform, random seed, source SHA-256, median, p95 and total nanosecond timings.

**Interpretation caution:** the script makes only one pass, runs under shared CI hardware, and has measurement overhead. Results are exploratory; no speedup claim is justified without repeated independent runs, warmups, error bars, controlled hardware, scaling experiments, and fairness review.

## Commands

From `real-time-scheduling-13-20/`:

```bash
python3 -m unittest discover -s tests -v
python3 experiments/cs010_benchmark.py > cs010-benchmark.json
```

## Publication gates

- [ ] Confirm GitHub Actions test outcomes and inspect any failures.
- [ ] Download archived test logs and JSON for both Python versions.
- [ ] Compare source SHA-256 to commit, retain provenance.
- [ ] Independent implementation/cross-language checks and adversarial instances.
- [ ] Repeated controlled performance experiments and confidence intervals.
- [ ] Verify closest-prior-work novelty. Classical baselines and interval erosion alone are insufficient for Q1 originality.
