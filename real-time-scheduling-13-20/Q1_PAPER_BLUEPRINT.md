# Q1-oriented research blueprint: 13/20 certified real-time admission

**Working title:** Certified Real-Time Task Admission under Additively Coupled Periodic Constraints: Sharp Safe-Time Bounds and Exact Algorithms

**Research question:** Can the special arithmetic structure behind the sharp 13/20 safe-time theorem enable a new, provably stronger admission, scheduling or verification result than standard interval algorithms for real-time workloads?

**Caution:** Q1 quartiles depend on database and year; acceptance cannot be guaranteed. A plan is not evidence of a solved research problem.

## Hypothesis and decisive go/no-go test

Hypothesis H1: a structural representation of S(a,b) supports significantly smaller certificates or asymptotically improved online admission operations for a well-defined query family. H2: for a restricted multi-job family, the additive frequencies yield a new tractability theorem or approximation/adversarial bound. **Null outcome:** standard interval methods already match proposed bounds; in this case do not claim algorithmic novelty and pivot to a rigorously distinct question.

## Work packages

**WP0 — Parent theorem and reproducibility.** Recover exact verification programs, independently verify 13/20 and primitive equality (1,14), log compiler/runtime/hash, test edge cases. Not a new claim.

**WP1 — Mathematical computer model.** Formalize S, rational boundaries, releases/deadlines, job ordering, conflict constraints, bit size, wraparound, throughput vs feasibility.

**WP2 — Baseline implementations.** Exact boundary sweep; sorted-interval admission; binary-search predecessor; interval tree; generic CP-SAT or MILP with documented discretization/exactness conditions. Separate exact competitors from approximate competitors.

**WP3 — Theory first.** Derive useful certified length, gap, component, recurrence or arithmetic-structure bounds. Seek a new complexity reduction, lower bound or certificate scheme; prove before labeling novel.

**WP4 — Verified algorithms.** Independent Python rational oracle plus optimized C++ implementation. YES and NO evidence; property-based and differential tests, overflow and bit-complexity checks.

**WP5 — Evaluation.** Controlled gcd-normalized frequency families, extremal (1,14), nearby and random coprime pairs, increasing bit lengths, diverse rational job workloads, feasible/infeasible balance, adversarial deadlines, multiple jobs. Report p50/p95/p99 latency, memory, proof-check time, certificate size, scheduling objective and scalability. Multiple seeds with independent replication. Never infer general throughput from 65% measure.

**WP6 — External/realistic validation.** Use openly licensed industrial/embedded traces only where phase-aligned additive-frequency assumptions are physically justified. If no such data exist, label experiments synthetic and avoid unsupported application claims.

**WP7 — Novelty review.** Proposition-by-proposition comparison with foundational exact scheduling, periodic resource models, real-time feasibility, interval/data-structure methods, proof-carrying computation and the closest runner-correlation work. Verify DOI/title/year and BibTeX.

**WP8 — Paper and submission.** Draft claims only after source-code, proof, tests, data and immutable result summaries agree. Select journal based on actual theorem and validated application, then verify its current indexing, scope and author rules.

## Suggested eight-stage milestones

M1 model accepted; M2 independent oracle and reference baselines; M3 at least one nontrivial theorem with full proof; M4 solver + independent verifier; M5 reproducible exact results; M6 fair baseline studies; M7 closest-prior-work novelty matrix; M8 independently audited paper.

## Success criteria

The paper's main contribution cannot merely be: '13/20 safe time', 'sorting rational interval boundaries', 'a greedy earliest-deadline scheduler', or 'a new illustrative simulation'. Require at least one genuinely new algorithmic theorem or relevant complexity/certificate result, proof, evidence and demonstrated significance.

## Recommended paper structure

See PAPER_OUTLINE.md. The source research process is concept -> software -> generated experiment artifacts -> analysis -> paper. This repository contains software/evidence, not a claim that a manuscript is auto-generated.
