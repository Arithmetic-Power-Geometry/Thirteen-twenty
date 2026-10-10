# CS-008 — Independent exact certificate checking

**Status:** verifier source and corruption tests committed. Execution evidence and full security audit pending. No Q1 novelty claim.

## Supported decision problem

N nonpreemptive equal-duration positive-length jobs on one resource, common rational release/deadline, availability S(a,b) with aligned integer phases and threshold 1/16.

## YES certificate

A list of N rational start/end pairs. Verify (i) exact length p, (ii) within release/deadline, (iii) sorted and pairwise nonoverlapping, (iv) no execution interval has positive-length overlap with any open forbidden neighborhood of any of a,b,a+b. The verifier uses forbidden-interval enumeration directly, not the reference safe-window constructor. Endpoint equality is allowed. Soundness follows immediately from all four conditions.

## NO certificate

A claimed integer maximum capacity. The verifier independently constructs the union of open forbidden neighborhoods and its positive-length complement components, then recomputes sum floor(clipped_component_length/p). It accepts only if claimed capacity equals the independently computed maximum and N exceeds it. This is a sound and complete NO check for the **restricted equal-job model only**. The certificate is not succinct and the verifier's complexity is pseudopolynomial in binary-encoded a,b.

## Tests

- Independent forbidden-union components must match the reference safe windows for small a,b.
- Accept generated YES/NO certificates.
- Reject omitted job, overlapping jobs, forbidden execution, wrong duration, tampered capacity and a false NO claim.

## Limitations

No arbitrary-duration multi-job completeness, no phase-uncertainty coverage, no machine-checked formal proof, and no novel complexity classification. Run `python3 -m unittest discover -s tests -v` from folder root and archive exact stdout/version/hash before reporting tests as passed.
