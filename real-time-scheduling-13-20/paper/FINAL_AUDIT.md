# First-draft integrity audit — 10 October 2026

| Check | Status | Explanation |
|---|---|---|
| Full first-pass narrative | COMPLETE | Paper draft includes abstract, model, propositions, proofs, methods, limitations and references |
| Explicit proof for admission/capacity/robustness | COMPLETE ON PAPER | Independent mathematical referee audit pending |
| Fixed-frequency NP-completeness | PROOF WRITTEN | Reduction from PARTITION, weak hardness only |
| Executed full test suite | NOT VERIFIED | No inspected GitHub Actions results |
| Benchmark raw data and timings | NOT VERIFIED | No performance claims included |
| Independent implementation | PARTIAL | Forbidden-neighborhood checker separate from reference oracle |
| Parent 13/20 sharp theorem | EXTERNAL DEPENDENCY | Requires separate independently audited full proof |
| Bibliography | PARTIAL | Five grounded scheduling sources, not exhaustive closest-work audit |
| Q1-level originality | NOT ESTABLISHED | Standard interval methods and PARTITION reduction |
| Journal-specific formatting | NOT STARTED | Working markdown draft, no selected journal |
| Author instructions or AI-facing prose in manuscript | REVIEW NEEDED | Working-paper caveats and artifact notes are scientific status statements, not journal-ready |
| Submission decision | HOLD | Do not submit as Q1-ready without originality and evidence gates |

## Concrete next actions

1. Inspect CI and benchmark logs, repair any failed tests and save verified run metadata.
2. Independently review every theorem, including the parent 13/20 claim and finite exact verification.
3. Expand closest-prior-work search to forbidden-interval, machine-calendar, and availability-constrained scheduling.
4. Identify and establish a genuinely nontrivial arithmetic-specific improvement, or recast as transparent applied/methodological working paper.
5. Select a journal only after scope and contribution are established; format, check figures/tables/algorithms and finalize bibliography.
