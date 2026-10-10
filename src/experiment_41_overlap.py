#!/usr/bin/env python3
"""Experiment 41: exact overlap-corrected finite-shift certificate."""
from fractions import Fraction
from itertools import product

def dist(x):
    r=x%1
    return min(r,1-r)

def certificate(q,m,stable,moving,t0):
    assert all(a%m==0 and dist(a*t0)>=Fraction(1,q) for a in stable)
    bad=[{h for h in range(m) if dist(b*(t0+Fraction(h,m)))<Fraction(1,q)} for b in moving]
    edges=sorted(((len(bad[i]&bad[j]),i,j) for i in range(len(bad)) for j in range(i+1,len(bad))),reverse=True)
    parent=list(range(len(bad)))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=[]
    for w,i,j in edges:
        x,y=root(i),root(j)
        if x!=y:
            parent[x]=y
            tree.append((i,j,w))
    bound=sum(map(len,bad))-sum(w for _,_,w in tree)
    valid=[h for h in range(m) if all(h not in s for s in bad)]
    assert len(set().union(*bad))<=bound
    return bad,tree,bound,valid

if __name__=="__main__":
    q,m=5,11
    stable=(11,);moving=(1,2,3);t0=Fraction(1,55)
    bad,tree,bound,valid=certificate(q,m,stable,moving,t0)
    print("q,m,stable,moving,bad_sizes,naive_bound,tree,tree_bound,actual_bad,valid_shifts,first_witness")
    print(q,m,stable,moving,[len(s) for s in bad],sum(map(len,bad)),tree,bound,len(set().union(*bad)),valid,t0+Fraction(valid[0],m),sep=",")
    assert sum(map(len,bad))>=m and bound<m and valid==[2,8]
    sets=[{i for i in range(4) if mask>>i&1} for mask in range(16)]
    for family in product(sets,repeat=3):
        edges=sorted(((len(family[i]&family[j]),i,j) for i in range(3) for j in range(i+1,3)),reverse=True)
        parent=[0,1,2];gain=0
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for w,i,j in edges:
            x,y=root(i),root(j)
            if x!=y:parent[x]=y;gain+=w
        assert len(set().union(*family))<=sum(map(len,family))-gain
    print("Exhaustive 4096 three-set systems: PASS")
