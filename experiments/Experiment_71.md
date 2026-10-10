# Experiment 71 — Exact classification of all safe times for the tight consecutive-speed family

Date: 2026-10-10
Status: complete all-dimensional theorem, classical arithmetic; explicit no-go for positive-measure-only proof strategies. General LRC not solved.

## Theorem 71.1
For each k>=2, q=k+1, and speed vector V=(1,2,...,k), let S(V)={t mod 1: ||j*t||>=1/q for j=1,...,k}. Then
S(V)={m/q mod 1: 1<=m<q, gcd(m,q)=1}.
In particular, |S(V)|=Euler_phi(q) and mu(S(V))=0.

## Proof
Suppose t belongs to S(V). The q points x_j=j*t mod 1, j=0,...,k, are distinct: if x_i=x_j with i<j then ||(j-i)*t||=0, contrary to safety since 1<=j-i<=k. Their pairwise circular distances are all >=1/q, because each difference |j-i| is among 1,...,k. Order the q points cyclically and consider their q successive circular gaps. Each gap is >=1/q, and their sum is one, hence every gap equals 1/q. Since x_0=0, the set of points is precisely the regular q-point grid {m/q:0<=m<q}. In particular t=m/q for some 1<=m<q. The points j*t are distinct, so multiplication by m modulo q is injective; equivalently gcd(m,q)=1.
Conversely, if t=m/q and gcd(m,q)=1, then j*m is nonzero mod q for every 1<=j<=q-1, so ||j*t||>=1/q. Hence t is safe. QED.

## Corollary 71.2 — Zero-measure obstruction
For every k>=2 there exists a valid k-speed configuration whose safe set is nonempty but has Lebesgue measure zero. Thus any certificate whose conclusion requires mu(S)>0, including Experiment 70's strict spanning-tree overlap threshold, cannot by itself establish the unrestricted Lonely Runner Conjecture.

## Corollary 71.3 — Tightness
For this family the optimal minimum distance equals 1/q, by the same q-point circular gap argument. Hence the bound in LRC, if universally true, is best possible.

## Exact checks
k=2, q=3: safe times 1/3,2/3 (phi(3)=2).
k=3, q=4: safe times 1/4,3/4 (phi(4)=2).
k=5, q=6: safe times 1/6,5/6 (phi(6)=2).
k=6, q=7: safe times m/7, m=1,...,6 (phi(7)=6).

## Literature and priority
The consecutive-speed tightness construction is classical and is described in the Lonely Runner Conjecture literature, including Perarnau and Serra, *The Lonely Runner Conjecture turns 60*, arXiv:2409.20160 (updated 2025), and Tao, *Some remarks on the lonely runner conjecture*, Contributions to Discrete Mathematics 13 (2018), arXiv:1701.02048. The classification by coprime grid points is an elementary sharpening of this classical example; it is NOT claimed as new research. Both works were previously indexed in references/lonely_runner.bib; no duplicate citation is needed.

## Research decision
Do not continue treating a positive-measure lower bound as a potential universal proof. Any viable global strategy must permit finite, isolated safe sets, and must handle configurations with many short integer relations. The remaining universal nonemptiness statement is open.

## Verdict
Theorem proved for all k; strategy-level no-go established. Novelty: no independent publishable claim. Unrestricted LRC: UNSOLVED.
