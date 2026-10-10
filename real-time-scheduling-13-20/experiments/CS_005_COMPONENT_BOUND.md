# CS-005: A certified contiguous execution window from the 13/20 theorem

**Result status:** elementary theorem with proof and a local exact-rational test over 360 primitive frequency pairs (1<=a<=b<=34). The underlying sharp 13/20 theorem remains dependent on the parent project's independent proof/certificate audit. This bound is NOT yet demonstrated to be original or sharp.

## Theorem

Let a,b be positive integers, c=a+b, and S={t in [0,1]: ||at||,||bt||,||ct||>=1/16}. Assuming the sharp safe-time measure theorem measure(S)>=13/20, S contains a non-wrapping closed interval of length at least

    13 / (40*(a+b)).

More generally, if a certified lower bound measure(S)>=M>0 is available, S contains a non-wrapping safe interval of length at least M/[2(a+b)].

## Proof

On the unit circle, for integer v>=1, the forbidden set B_v={t: ||vt||<1/16} consists of exactly v disjoint open circular arcs, each centered at j/v, j=0,...,v-1. The union B_a union B_b union B_c has at most a+b+c=2(a+b) connected components (unions cannot create more components than the sum). The safe set S is its closed complement. Because 0 belongs to every B_v, one of the forbidden components contains 0; hence no safe component crosses the cut at 0. The number k of nonempty positive-length safe components in [0,1] is at most 2(a+b). Isolated safe points, if any, do not increase the number of positive-length components or affect measure. The safe intervals are disjoint, their lengths sum to measure(S)>=M, so at least one has length >= M/k >= M/[2(a+b)]. Substituting M=13/20 gives 13/[40(a+b)]. QED.

**Subtlety:** Counting phase-boundary cells yields a weaker estimate. The present proof counts connected forbidden neighborhoods, and uses the fact that t=0 is forbidden to avoid an unnecessary '+1' for a cut circular component.

## Consequence for admission

For a task with duration p<=13/[40(a+b)] and an unrestricted unit-horizon release/deadline window [0,1], there exists a feasible nonpreemptive execution start. This is an existence statement, not a guarantee for arbitrary release/deadline windows, task sets, throughput or uncertain phase offsets. At equality p=bound, the eligible intervals are closed and endpoints satisfy the non-strict phase condition.

## Limitations and next research gate

This follows from elementary interval topology plus the parent measure theorem; it is not itself a major CS breakthrough. Test optimality of component count, compare to exact largest safe intervals and seek stronger structure-dependent guarantees. For binary-encoded frequencies, explicit interval generation remains pseudopolynomial.

## Local independent test record (10 Oct 2026)

A Python Fraction endpoint-sweep implementation evaluated every coprime 1<=a<=b<=34, totaling 360 pairs. Checks: measure>=13/20; positive-length component count<=2(a+b); longest component length>=13/[40(a+b)]. Result: zero violations; equality in measure only at (1,14). This is finite empirical evidence, not a proof of the theorem for all inputs. The reproducible script is `experiments/cs005_verify.py`.
