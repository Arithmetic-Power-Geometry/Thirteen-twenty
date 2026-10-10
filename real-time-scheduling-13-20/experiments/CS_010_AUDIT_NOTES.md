# CS-010 audit notes — execution not yet independently confirmed

Date: 2026-10-10.

## Evidence status

GitHub Actions YAML and a deterministic benchmark harness are committed. An attempted direct clone of the public repository in the available execution environment failed with DNS resolution error for github.com. This is an environment/network failure, **not** a failed unit test and **not** evidence of a passing test. No benchmark performance result is asserted.

The GitHub connector available for this audit can fetch files and commit updates, but does not expose a general list of recent workflow runs. Therefore Actions pass/fail and archived artifact contents have not been inspected in this audit.

## Mandatory next checks

1. Open https://github.com/Arithmetic-Power-Geometry/Thirteen-twenty/actions and select 'Thirteen-twenty CS-010 reproducibility'.
2. Check both Python 3.11 and 3.12 jobs, then download each run's artifacts.
3. Confirm `python -m unittest discover -s tests -v` exits zero and inspect all tests.
4. Verify JSON benchmark cases, source hashes, exact-oracle comparisons and independent certificates.
5. Repair any failures, rerun, archive successful run IDs and raw logs.
6. Perform repeated, controlled timing experiments; one-pass shared-runner measurements cannot establish meaningful speedup.

## Research integrity

Do not claim 10/10 stages validated. Only source artifacts have been committed. The original-CS-result gate and closest-prior-work verification remain unresolved.
