# CS-011: NP-completeness at fixed frequencies (1,1,2)

## Formal decision problem

Input: a finite list of positive rational nonpreemptive processing times p_1,...,p_n, all jobs with common release 0 and deadline 1, single machine, and execution permitted only when ||t||, ||t|| and ||2t|| are each at least 1/16. Decide if every job can execute completely in permitted time.

## Theorem

The decision problem is NP-complete, even with fixed a=b=1, common release 0, common deadline 1, and exactly two available intervals.

### Exact safe components

The safe set for frequencies (1,1,2) is precisely [1/16,15/32] union [17/32,15/16]. Each component has length 13/32.

### NP-hardness

Reduce PARTITION. Given positive integers w_1,...,w_n with even sum 2B, create a job of duration p_i=(13*w_i)/(32*B). The input transformation is polynomial in binary bit length. The total processing time equals 13/16, exactly the sum of the two safe-window capacities. A feasible schedule must assign each whole nonpreemptive job to one of the two windows, with no unused capacity. Therefore the weights assigned to each window sum exactly B. Conversely, a partition into equal-sum groups yields a feasible schedule by placing each group back-to-back inside its assigned window. Thus feasibility is equivalent to PARTITION.

Restricting PARTITION to even total is still NP-hard: multiply every original weight by two, preserving yes/no status.

### Membership in NP

A certificate is the assignment of each job to one of the two windows. Check in polynomial-time rational arithmetic that the total assigned duration to each window does not exceed 13/32. For common release/deadline, this condition is sufficient by back-to-back scheduling. Hence the decision problem is NP-complete. The reduction from PARTITION establishes weak NP-hardness, not strong NP-hardness.

## Interpretive boundary

This is a correct formal complexity theorem for the specified model, but its mechanism is the classical two-bin PARTITION reduction. The restriction to arithmetic availability windows is explicit, yet **originality relative to scheduling/bin-packing literature is not established**. It must not be advertised as a breakthrough without a full priority review.

## Consequence

The equal-duration capacity formula from CS-007 does not extend to a general polynomial-time exact algorithm for arbitrary binary-encoded durations unless P=NP. This does not preclude approximation, pseudopolynomial algorithms, or other restricted cases.
