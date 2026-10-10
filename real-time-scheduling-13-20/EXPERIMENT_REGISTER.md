# Numbered experiment and artifact plan (PROPOSED; no experiment executed)

Each experiment gets a separate immutable Markdown log, program version, machine-readable result, test assertions and reproducibility command. Suggested local numbering 001 onward avoids collision with parent experiments 11–84.

| ID | Research activity | Required outputs | Decision gate |
| --- | --- | --- | --- |
| CS-001 | Reproduce parent 13/20 certificate | per-pair digest, exact independent result, compiler info | No mismatch |
| CS-002 | Correctness of phase-window extraction | exhaustive small oracle and random exact comparisons | No failed invariant |
| CS-003 | One-job admission, YES and NO proofs | rational verifier, correctness theorem, tests | All certificates validate |
| CS-004 | Classical interval and scheduling baselines | documented runtime and complexity | Fair competitors |
| CS-005 | Component-count and slot-length audit | complete derivation and extremal search | Proven and correctly cited |
| CS-006 | Compressed structure and repeated queries | algorithm, proof, memory / latency profiles | Improvement over strong baselines |
| CS-007 | Multi-job scheduling complexity | explicit restrictions, proof/reduction or honest open status | Theorem checked |
| CS-008 | Independent feasibility verifier | proof of soundness, adversarial tests | Invalid evidence rejected |
| CS-009 | Robust offset/timing variant | explicit uncertainty model and results | No misuse of 13/20 |
| CS-010 | End-to-end reproducibility and Q1 gate | scripts, hashes, benchmark report, novelty table | Claims fully supported |

## Minimum benchmark controls

- Verify exact answers against an independent solver or exhaustive oracle at small scale.
- Include a=b, gcd>1, (1,14), large coprime a,b and tight boundary jobs.
- Use binary-encoded input complexity and report pseudopolynomial effects.
- Benchmark preprocessed-query speed **including and excluding preprocessing**, with honest break-even analysis.
- Baselines must include ordinary sorted-interval search; compare similar numerical and implementation conditions.
- Report failures, counterexamples and negative results, not only favorable results.
- Ensure no overlapping workloads are mistaken for independent replications.
