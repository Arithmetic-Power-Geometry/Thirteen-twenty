#!/usr/bin/env python3
"""Experiment 48: exact rational threshold-gap audit."""
from fractions import Fraction as F
from itertools import combinations

def score(v,t):
    return min(min((a*t)%1,1-(a*t)%1) for a in v)

def optimum(v):
    C={F(0),F(1)}
    for a in v:
        C.update(F(j,2*a) for j in range(2*a+1))
    for a,b in combinations(v,2):
        for d in (a+b,abs(a-b)):
            if d:C.update(F(j,d) for j in range(d+1))
    return max((score(v,t),t) for t in C)

print("k,total,strict,tight,below,min_gap,min_gap_speeds,witness")
for k in range(2,6):
    strict=[];tight=below=count=0
    for v in combinations(range(1,10),k):
        val,t=optimum(v);threshold=F(1,k+1)
        assert val.denominator<=2*max(v)
        assert val==threshold or abs(val-threshold)>=F(1,2*(k+1)*max(v))
        if val>threshold:strict.append((val-threshold,v,t))
        elif val==threshold:tight+=1
        else:below+=1
        count+=1
    gap,v,t=min(strict)
    print(k,count,len(strict),tight,below,gap,':'.join(map(str,v)),t,sep=",")
