#!/usr/bin/env python3
"""Experiment 37: exact all-dimensional finite-grid equivalence.
The full grid may be exponentially large in the binary input size.
"""
from math import lcm
from fractions import Fraction

def witness(q,speeds):
    assert q>=2 and speeds and all(isinstance(v,int) and v>0 for v in speeds)
    L=lcm(*speeds)
    M=2*q*L
    for j in range(M+1):
        if all(q*min((v*j)%M,M-(v*j)%M)>=M for v in speeds):
            return Fraction(j,M)
    return None

if __name__=="__main__":
    cases=[(4,(1,2,3),Fraction(1,4)),(5,(1,2,3),Fraction(1,5)),
           (16,(1,14,15),Fraction(1,16)),
           (6,(1,2,3,4,5),Fraction(1,6))]
    for q,vs,expected in cases:
        w=witness(q,vs)
        print(f"q={q} speeds={vs} L={lcm(*vs)} witness={w}")
        assert w==expected
