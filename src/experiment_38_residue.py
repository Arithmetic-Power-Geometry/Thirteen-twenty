#!/usr/bin/env python3
"""Experiment 38: all-dimensional residue certificate and exact density audit."""
from fractions import Fraction
from itertools import product

def residue_certificate(q, speeds):
    if q<2 or not speeds or any(not isinstance(v,int) or v<=0 for v in speeds):
        raise ValueError("q>=2 and nonempty positive integer speed vector required")
    if any(v%q==0 for v in speeds):
        return None  # no claim that no other witness exists
    t=Fraction(1,q)
    assert all(min((v*t)%1,1-(v*t)%1)>=t for v in speeds)
    return t

def main():
    print("k,q,certified_residue_vectors,total_residue_vectors,density")
    for k in range(1,9):
        q=k+1
        certified=(q-1)**k
        total=q**k
        if k<=5:
            observed=sum(all(r!=0 for r in rs) for rs in product(range(q),repeat=k))
            assert observed==certified
        print(f"{k},{q},{certified},{total},{Fraction(certified,total)}")
    assert residue_certificate(16,tuple(range(1,16)))==Fraction(1,16)
    assert residue_certificate(16,tuple(range(1,30,2)))==Fraction(1,16)
    assert residue_certificate(16,(16,1,2)) is None
    print("q=16: two 15-speed witness examples passed; one out-of-class example flagged.")
if __name__=="__main__":
    main()
