# Experiment 53 — Zero-measure witnesses invalidate positive-measure-only proof strategies

Date: 2026-10-10
Status: exact elementary obstruction established. This is NOT a counterexample to the Lonely Runner Conjecture and is NOT novel.

## Exact example
Take k=2 relative speeds V=(1,2), so the Lonely Runner threshold is delta=1/(k+1)=1/3.
The inequalities ||t||>=1/3 and ||2t||>=1/3 on t mod 1 yield respectively
S_1=[1/3,2/3],
S_2=[1/6,1/3] union [2/3,5/6].
Their intersection is exactly S={1/3,2/3}. Therefore the LRC instance is true but mu(S)=0.

## Consequence
Any proposed proof of LRC whose universal final step requires mu(S)>0 is impossible: this valid instance has mu(S)=0. In particular, the strictly-positive sufficient conditions in Experiments 49-52 cannot hold for all admissible speed vectors. This does NOT invalidate their conditional inequalities, only their potential use as universal sufficient conditions.

## Exact failure of Experiment 51 threshold
B_1={||t||<1/3}, B_2={||2t||<1/3}. Both have measure 2/3, while mu(B_1 intersect B_2)=1/3, since mu(S)=1-4/3+mu(B_1 intersect B_2)=0.
Experiment 51 requires P_2>k(k-1)/(2(k+1))=1/3. Here P_2=1/3 exactly, so its strict certificate fails although a safe time exists.

## New research gate
Replace positive-measure-only certificates by nonemptiness arguments permitting isolated boundary points. Candidate tools include exact endpoint-cover obstructions, topological compactness, rational witnesses, or critical-time extremality; any proposed universal theorem must pass the (1,2) equality case and known tight families.

## Literature and novelty
The example (1,2) and its tightness are elementary, well known, and not original. For the general problem and correlation-based approaches see:
- Guillem Perarnau and Oriol Serra (2016), Correlation Among Runners and Some Results on the Lonely Runner Conjecture, The Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123.
- Guillem Perarnau and Oriol Serra (2025), The Lonely Runner Conjecture turns 60, Computer Science Review 58, 100798, DOI 10.1016/j.cosrev.2025.100798.
Both already exist in references/lonely_runner.bib. No duplicate BibTeX entry is required.

## Resolution status
General LRC: NOT SOLVED. This experiment rules out an overly strong proof target and gives an exact mandatory regression case.
