# CS-006 — Linear-size safe-window lower bound (proved)

**Status:** proved structural limitation, with independent executable witness tests. This is an elementary observation, not a demonstrated novel breakthrough.

## Theorem

For every integer b>=8, the phase-aligned safe set S(1,b) at threshold 1/16 has at least floor(b/4)-1 distinct positive-length connected components in [0,1].

### Proof

For each integer j satisfying b/4 <= j+1/4 <= b/2, put t_j=(j+1/4)/b. Then 1/4 <= t_j <= 1/2, so ||t_j||>=1/4>=1/16. Also bt_j=j+1/4, hence ||bt_j||=1/4. Finally (b+1)t_j=j+1/4+t_j has fractional part in [1/2,3/4], so ||(b+1)t_j||>=1/4. All three inequalities are strict relative to the exclusion threshold, so every t_j lies in the interior of a positive-length safe component.

For consecutive eligible j, the time (j+1)/b lies strictly between t_j and t_(j+1) and has ||b t||=0. Therefore t_j and t_(j+1) lie in different safe components. The number of integers j in the interval [b/4-1/4,b/2-1/4] is at least floor(b/4)-1 for b>=8. This proves the claim.

## Computing consequence

Any algorithm that explicitly outputs every maximal safe window must emit Omega(b) intervals on the family a=1, b growing. In the ordinary unit-cost output model this gives Omega(b) output time and space for that family, even though b occupies only O(log b) input bits. Therefore a blanket poly(log b) total-time claim for **explicit enumeration** is impossible.

This lower bound does NOT rule out succinct symbolic representations, implicit queries, specialized arithmetic algorithms, or new complexity results for multi-job scheduling. It is not a lower bound on every admission query.

## Research significance

This prevents a false target: improving explicit full-window enumeration to polynomial in binary input length. The meaningful CS-006 target is now an **implicit representation** with correctness guarantees, or a new restricted multi-job scheduling theorem. Standard interval trees already give O(log k) indexed queries after explicit preprocessing, so matching that bound is not novel.

## Verification

Run `python3 experiments/cs006_verify.py` from the folder root. The program independently checks exact rational witnesses and separation, and compares a small family with maximal safe windows. It is a finite sanity check, not the proof.

## Next

CS-007: formalize multi-job complexity with precise input encoding and restricted arithmetic availability. CS-008: independent certificate checking and proof-carrying schedule format. A publishable Q1-level theorem is still open.
