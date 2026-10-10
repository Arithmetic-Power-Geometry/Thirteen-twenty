#!/usr/bin/env python3
"""Experiment 47: exact maximum loneliness via rational breakpoints."""
from fractions import Fraction as F
from itertools import combinations

def score(v,t):
    return min(min((a*t)%1,1-(a*t)%1) for a in v)

def exact_max(v):
    v=tuple(sorted(set(v)))
    assert v and all(isinstance(a,int) and a>0 for a in v)
    C={F(0),F(1)}
    for a in v:
        C.update(F(j,2*a) for j in range(2*a+1))
    for a,b in combinations(v,2):
        for d in (a+b,abs(a-b)):
            if d:C.update(F(j,d) for j in range(d+1))
    return max((score(v,t),t) for t in C),len(C)

def independent_reference(v):
    # Full piecewise-affine partition, including all one-runner corners
    B={F(0),F(1)}
    for a in v:
        B.update(F(j,2*a) for j in range(2*a+1))
    B=sorted(B)
    # Each distance is affine on every B cell. Pairwise intersections
    # are calculated using the endpoint values on each cell.
    C=set(B)
    for l,r in zip(B,B[1:]):
        for a,b in combinations(v,2):
            dl=score((a,),l)-score((b,),l)
            dr=score((a,),r)-score((b,),r)
            if dl!=dr:
                t=l+(r-l)*(-dl)/(dr-dl)
                if l<t<r:C.add(t)
    return max(score(v,t) for t in C)

if __name__=='__main__':
    print('k,configurations,disagreements,tight,strict')
    for k in (2,3,4):
        count=tight=strict=0
        for v in combinations(range(1,9),k):
            (mx,t),n=exact_max(v)
            assert mx==independent_reference(v),(v,mx)
            count+=1
            if mx==F(1,k+1):tight+=1
            elif mx>F(1,k+1):strict+=1
            else:raise AssertionError(('counterexample',v,mx))
        print(k,count,0,tight,strict,sep=',')
    for v in ((1,3,4,7),(1,3,4,5,9),(1,2,4,8)):
        print('example',v,exact_max(v))
