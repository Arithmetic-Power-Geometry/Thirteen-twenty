# CS-007 — Exact multi-job capacity theorem: common window and equal durations

**Status:** theorem proved, implementation and regression tests committed. Independent execution and novelty audit pending. **Not a Q1-level breakthrough**: this is a classical capacity formula applied to arithmetic safe windows.

## Problem

Given a,b>0 and N nonpreemptive jobs, all with the same positive rational processing time p and common rational release r and deadline d, 0<=r<=d<=1, decide whether every job can execute in the safe set S(a,b) for frequencies a,b,a+b with threshold 1/16. Only one job may execute at a time.

## Exact capacity theorem

Let [L_i,U_i] be the maximal positive-length safe intervals in [0,1]. Put l_i=max(L_i,r), u_i=min(U_i,d), and x_+=max(x,0). Then

C(a,b,r,d,p) = sum_i floor((u_i-l_i)_+/p).

All N jobs are feasible **if and only if** N<=C.

### Proof

Necessity: a positive-duration nonpreemptive job must be entirely contained in a single safe component. Within clipped component i, n_i disjoint duration-p jobs occupy n_i*p time, so n_i<=floor((u_i-l_i)_+/p). Sum over components. Sufficiency: in each clipped component schedule floor((u_i-l_i)_+/p) jobs back-to-back starting at l_i; these schedules do not overlap because the components are disjoint. Their union schedules C jobs; any N<=C can be selected. This is an exact constructive decision theorem.

## Complexity and certificate

With k precomputed maximal safe components, computing C takes O(k) rational arithmetic operations, with O(k) allocation output and O(N) job interval output if a full YES schedule is requested. Constructing components costs O((a+b)log(a+b)) rational comparisons. This is pseudopolynomial in binary-encoded a,b. The capacity/allocation is a checkable NO upper-bound witness if components are independently reconstructed and completeness is checked.

## Why 13/20 does not imply 65% job admission

Even when total safe measure is >=13/20, fragmentation wastes residual space in each safe component. For fixed p, the exact count is sum of floors, **not** floor(total safe measure/p). Thus a 65% measure theorem is not a throughput or schedulability theorem.

## Status of novelty

The formula is elementary for arbitrary disjoint availability intervals; arithmetic structure does not yet yield a new asymptotic algorithm or complexity classification. This stage establishes a correct restricted multi-job baseline and protects against misleading claims. The decisive original-result gate remains open.

## Reproduce

From project folder: `python3 -m unittest discover -s tests -v`.

## Next research steps

CS-008 independent certificate checker with corruption tests; CS-009 robustness analysis; CS-010 execution/benchmarks. In parallel pursue a genuine arithmetic-specific multi-job theorem, a lower bound, or a compressed symbolic representation beyond conventional interval methods.
