#!/usr/bin/env python3
"""Experiment 75: exhaustive primitive integer speed vectors, exact arithmetic."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import argparse

def exact_optimum(v):
    candidates = set()
    for a, b in combinations(v, 2):
        d = a+b
        for n in range(d):
            candidates.add(Fraction(n,d))
    for a in v:
        for h in range(a):
            candidates.add(Fraction(2*h+1,2*a))
    best = Fraction(-1)
    witness = None
    for t in candidates:
        residues = [(a*t) % 1 for a in v]
        score = min(min(x, 1-x) for x in residues)
        if score > best:
            best, witness = score, t
    return best, witness

def audit(k,N):
    checked=0
    tight=[]
    violations=[]
    for v in combinations(range(1,N+1),k):
        if gcd(*v)!=1:
            continue
        checked+=1
        score,t=exact_optimum(v)
        if score<Fraction(1,k+1):
            violations.append((v,str(score),str(t)))
        if score==Fraction(1,k+1):
            tight.append((v,str(t)))
    print("k",k,"N",N,"primitive",checked,"tight",len(tight),"violations",len(violations))
    print("tight tuples:",tight)
    print("violations:",violations)
    return checked,tight,violations

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--k",type=int,default=None)
    p.add_argument("--N",type=int,default=None)
    a=p.parse_args()
    if a.k is not None and a.N is not None:
        audit(a.k,a.N)
    else:
        audit(3,15)
        audit(4,12)
