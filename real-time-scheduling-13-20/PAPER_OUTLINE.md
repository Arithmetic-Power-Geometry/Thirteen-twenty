# Paper architecture (research outline, not submission-ready manuscript)

**Working title:** Certified Real-Time Task Admission under Additively Coupled Periodic Constraints: Sharp Safe-Time Bounds and Exact Algorithms

1. Introduction: computing problem, why measure alone is insufficient, precise new claims.
2. Related work: periodic resource constraints, real-time scheduling, interval algorithms, formal certificates, additive frequency measures.
3. Model: aligned a,b,a+b, threshold 1/16, rational jobs, endpoints, complexity input length.
4. Foundations: independently verified sharp 13/20 bound; explicit statement of what it does and does not imply.
5. New algorithms / complexity: only proven novel contributions; exact pseudocode and matching proofs.
6. Independent checker and certificate format: soundness, completeness where established, bit complexity.
7. Experimental methodology: workloads, baselines, reproducibility, data controls.
8. Results and ablation: speed, memory, certificate size, sensitivity and failed cases.
9. Discussion: real-world realism; phases, jitter, releases, arbitrary deadlines; limitations.
10. Conclusion: claims strictly supported by proofs and artifacts.
11. Verified bibliography; supplementary software/data provenance.

**Required theorem boxes prior to drafting:** theorem on exact decision correctness; theorem on complexity; genuinely new restricted scheduling/certification theorem (to be discovered and proven). If the final box is absent, do not claim a Q1-caliber breakthrough.

**Scope restrictions:** fixed 13/20, not general all-q, not unrestricted Lonely Runner Conjecture. Do not confuse aggregate safe-time fraction with contiguous execution or schedulable throughput.
