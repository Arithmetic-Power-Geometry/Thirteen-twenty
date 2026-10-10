# Originality and closest-prior-work audit — 10 October 2026

## Verdict

**HOLD for Q1 novelty.** The additive-frequency calendar is an interesting specialized input model, but the current exact interval oracle, segment-tree admission, equal-job capacity, certificate checking, and interval erosion are generic algorithms. The CS-011 weak NP-completeness reduction is a two-bin PARTITION construction; earlier work establishes NP-hardness for nonpreemptive single-machine scheduling with unavailable intervals. The proof is valid for the explicitly fixed triple (1,1,2), but it is not established as a new complexity frontier.

## Directly relevant primary literature (metadata checked against public publisher/institutional pages)

1. Schmidt, G. (2000). Scheduling with limited machine availability. European Journal of Operational Research 121(1), 1–15. DOI 10.1016/S0377-2217(98)00367-1. Publisher https://www.sciencedirect.com/science/article/abs/pii/S0377221798003671 . Surveys known complexity and algorithms for machines with availability gaps.
2. Ma, Y., Chu, C., and Zuo, C. (2010). A survey of scheduling with deterministic machine availability constraints. Computers & Industrial Engineering 58(2), 199–211. DOI 10.1016/j.cie.2009.04.014. Publisher https://www.sciencedirect.com/science/article/pii/S0360835209001168 . Survey of single-machine and other scheduling settings with maintenance holes.
3. Kolen, A. W. J., Lenstra, J. K., Papadimitriou, C. H., and Spieksma, F. C. R. (2007). Interval scheduling: A survey. Naval Research Logistics 54(5), 530–543. DOI 10.1002/nav.20231. Institution https://research.tue.nl/en/publications/interval-scheduling-a-survey/ . Fixed interval scheduling is not identical to our flexible-start calendar but shows breadth of established interval algorithms.
4. Kovalyov, M. Y., Ng, C. T., and Cheng, T. C. E. (2007). Fixed interval scheduling: Models, applications, computational complexity and algorithms. European Journal of Operational Research. DOI 10.1016/j.ejor.2006.01.049. Publisher https://www.sciencedirect.com/science/article/pii/S0377221706003559 . Another related but not identical problem.
5. Jacobs, T., and Longo, S. (2014). A New Perspective on the Windows Scheduling Problem. arXiv:1410.7237. https://arxiv.org/abs/1410.7237 . Important to distinguish: recurring-task frequency constraints, not finite-horizon availability windows.
6. Single-machine scheduling with machine unavailability periods and resource dependent processing times (2022), European Journal of Operational Research, publisher https://www.sciencedirect.com/science/article/pii/S0377221721002605 . **Authors and complete bibliographic metadata still require verification**. The publisher abstract explicitly describes a before/after-gap partition and cites older NP-hardness results.

## Novelty matrix

| Result | Prior general framework | Audit decision |
|---|---|---|
| Exact enumeration of phase-defined availability | Periodic exclusions + general interval calendar construction | Correct special-case technique; original algorithm unproven |
| Single-job admission | Feasible gap search | Standard |
| Segment-tree acceleration | Range maximum and successor search | Standard |
| Equal-job capacity | Sum of per-gap floor capacities | Elementary |
| Two-gap NP-completeness | Classical PARTITION / nonpreemptive machine downtime hardness | No broad hardness novelty claim |
| YES/NO verifier | Direct rational feasibility and recomputation | Engineering value; no new proof-system complexity |
| Common-shift jitter | Interval erosion | Standard |
| Parent sharp 13/20 safe measure | Additive arithmetic geometry / lonely runner-related measure problems | **Priority unresolved**: audit parent mathematical literature and exact computer-assisted proof independently |

## Potential genuinely new questions

A. Does the additive structure permit a sublinear-time **implicit** exact admission index, after polynomial-in-bit-length preprocessing, for some nontrivial family? CS-006 only rules out explicit enumeration.
B. Can one prove a stronger additive-specific bound on longest safe component than the generic measure/component bound, with sharp extremizers?
C. For restricted correlated phase offsets, can one prove a new universal measure/contiguous-slot bound? Arbitrary independent phase offsets cannot inherit the aligned 13/20 result without proof.
D. Can a compressed proof certificate for negative admission avoid enumerating all phase boundaries, with a nontrivial bit-complexity theorem?

These are research questions, **not established results**.

## Audit limits and gate

This is a substantive targeted closest-prior-work audit, **not an exhaustive systematic review**. Six sources are recorded here; some earlier bibliography entries in the repository have not been independently rechecked in this pass. No comprehensive negative priority claim is possible. A Q1 originality gate must remain OPEN until a specific new theorem or demonstrated systems contribution survives full priority comparison.
