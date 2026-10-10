# Experiment 63 — Exact short-relation sieve

2026-10-10. Mathematical status: a corollary of Beck and Everett (2026), not an original universal proof.

Let k>=2, q=k+1, and L=2k+3. Define LR(v)=max_{t mod 1} min_i ||v_i t||.

**Theorem.** If no nonzero integer vector m with sum_i |m_i|<=L satisfies sum_i m_i v_i=0, then LR(v)>1/q.

**Proof.** Beck and Everett, *Lonely Runner Relations* (2026), arXiv:2609.06259, establish that any counterexample or tight configuration has a nonzero relation of norm at most L. If LR(v)<=1/q, compactness implies v is either a counterexample or a tight configuration. This contradicts the hypothesis. Thus LR(v)>1/q. QED. The theorem is attributed to Beck and Everett; this is its immediate contrapositive.

**Exact verification.** Enumerate integer vectors m with 0<sum |m_i|<=L and evaluate each dot product exactly. No zero dot product certifies strict safety. A zero dot product is inconclusive: v=(1,2) has relation 2v_1-v_2=0 and still satisfies the conjecture.

**All-dimensional test family.** If increasing speeds satisfy v_j>L*v_{j-1} for j>=2, no bounded relation exists. Proof: take the largest index j with m_j nonzero. Its term has absolute magnitude at least v_j, whereas all smaller terms together have magnitude at most L*v_{j-1}<v_j. Therefore cancellation is impossible. This example is not new and is weaker than the speed-gap family from Experiment 60.

**Research significance.** Unlike finite time sampling, this tests an arithmetic obstruction for every dimension. But it cannot resolve the short-relation stratum, and that stratum includes many valid tight instances. No unrestricted proof or Q1-level novelty is established.

**References.** Beck, Matthias and Everett, Samuel, *Lonely Runner Relations*, arXiv:2609.06259 (2026). Allikvere, Jaan, *Fourteen and fifteen lonely runners*, arXiv:2609.02604v2 (2026). Both primary arXiv records checked 2026-10-10 and already present in references/lonely_runner.bib; do not duplicate.
