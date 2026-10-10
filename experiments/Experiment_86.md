# Experiment 86 — Core-to-tail gluing theorem without global lacunarity

Date: 2026-10-10. Status: proved an all-dimensional extension theorem and an infinite hybrid family. Unrestricted Lonely Runner Conjecture NOT solved.

## Theorem 86.1 (exact safe-core extension)
Fix k>=2, q=k+1 and d=1/q. Let a nonempty collection C of distinct positive integer speeds have a common closed safe interval I=[L,R] with R-L=w>0, i.e. ||c*t||>=d for all c in C and t in I. Let b_1<...<b_s be additional distinct positive integer speeds, disjoint from C, with
b_1*w >= 2(1-d),
b_(j+1)/b_j >= 2(1-d)/(1-2d)=2k/(k-1) for 1<=j<s.
Then the entire k-speed vector V=C union {b_1,...,b_s}, where k=|C|+s, has a common safe interval of length (1-2d)/b_s (for s>=1), and hence a positive-measure safe set. The first threshold depends on the ACTUAL core interval width, not on a global consecutive-speed ratio.

## Proof
For any speed b and any closed interval [L,R] with b(R-L)>=2(1-d), choose n=ceil(bL-d). The full b-allowed interval J=[(n+d)/b,(n+1-d)/b] lies in [L,R]: its left endpoint is >=L and its right endpoint is <=L+2(1-d)/b<=R. Thus J is safe for b and inherits safety for all earlier speeds. Apply this containment once with b=b_1 and width w. Thereafter the retained interval has length (1-2d)/b_j, so the next growth inequality guarantees containment again. After s steps the last interval is safe for all speeds, with length (1-2d)/b_s. QED.

## Explicit non-lacunary core family, all k>=4
For each k>=4 set q=k+1, d=1/q. The three-speed core C=(1,2,3) is safe throughout
I=[d,(1-d)/3], because for t in I:
t in [d,1-d], 2t in [d,1-d], and 3t in [d,1-d].
The width is w=(1-4d)/3=(k-3)/[3(k+1)]>0.
Therefore ANY tail of k-3 increasing speeds b_1,...,b_(k-3) satisfying
b_1 >= 6k/(k-3),
b_(j+1)/b_j >= 2k/(k-1)
is safe together with (1,2,3). This infinite family fails the global growth hypothesis of Experiment 85 at its first two ratios (2 and 3/2), so Theorem 86.1 genuinely broadens that method's applicability.

Example k=6: q=7, I=[1/7,2/7], b=(12,29,70). The vector (1,2,3,12,29,70) is certified, with final safe interval length 5/(7*70)=1/98.

## Arbitrary core, arbitrary dimension
The theorem is NOT restricted to (1,2,3). Any previously certified core safe interval, whether obtained by a theoretical argument or an exact boundary sweep, can be extended by a sufficiently fast tail. A core with only isolated safe points has w=0 and cannot be used by this theorem. The dimension k and threshold d must be fixed at the FINAL vector size; a core witness at its original smaller dimension does not automatically satisfy the required final threshold with positive width.

## Reproducibility
The script experiments/experiment_86_core_tail_gluing.py implements exact rational interval construction and audits the hybrid (1,2,3) families in dimensions k=4,...,30, including the displayed six-speed example. The proof is analytic and independent of computation.

## Prior work, priority and limitations
The result is an elementary interval-nesting extension of Experiment 85, not a first-discovery claim. The broad topic of lacunary LRC sufficient conditions predates these experiments:
Arturas Dubickas (2011), The lonely runner problem for many runners, Glasnik Matematicki 46(1), 25–30, DOI 10.3336/gm.46.1.01; primary publisher record https://web.math.pmf.unizg.hr/glasnik/vol_46/no1_05.html .
Sebastian Czerwiński (2018), The lonely runner problem for lacunary sequences, Discrete Mathematics 341(5), 1301–1306, DOI 10.1016/j.disc.2018.02.002.
The present theorem proves a direct hybrid class but independent journal-level novelty is not established. The unrestricted LRC remains open.
