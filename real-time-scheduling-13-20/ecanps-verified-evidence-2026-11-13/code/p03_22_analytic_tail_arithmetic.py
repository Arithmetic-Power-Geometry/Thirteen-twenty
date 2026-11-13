"""P03-22: standalone exact analytic-tail arithmetic and torus-area audit.

This is an independent rational verification of displayed constants, NOT a
machine proof of the circular interval-component discrepancy lemma.
"""
from fractions import Fraction as F
from math import gcd

def torus_mean():
    h=F(1,16)
    # Three exclusion strips of width 2h, three pairwise intersections
    # of area (2h)^2, and central triple intersection of area 3h^2.
    return 1-3*(2*h)+3*(2*h)**2-3*h*h

def cutoff():
    target=F(13,20)
    mean=torus_mean()
    delta=mean-target
    # Smallest positive m with 2/m strictly smaller than delta.
    m=(F(2)/delta).__floor__()+1
    assert mean==F(169,256)
    assert delta==F(13,1280)
    assert m==197
    assert mean-F(2,196)<target
    assert mean-F(2,197)>target
    return m

def independent_measure(a,b):
    q=F(1,16)
    knots={F(0),F(1)}
    for k in (a,b,a+b):
        for j in range(k):
            for t in (F(16*j+1,16*k),F(16*j+15,16*k)):
                if 0<t<1:knots.add(t)
    knots=sorted(knots)
    total=F(0)
    for left,right in zip(knots,knots[1:]):
        mid=(left+right)/2
        if all(min((k*mid)%1,1-(k*mid)%1)>=q for k in (a,b,a+b)):
            total+=right-left
    return total

def run():
    m=cutoff()
    witness=independent_measure(1,14)
    assert witness==F(13,20)
    for g in (1,2,3,5):
        assert independent_measure(g,14*g)==witness
        assert independent_measure(14*g,g)==witness
    print(f"PASS: torus_mean={torus_mean()} gap={torus_mean()-F(13,20)} "
          f"strict_cutoff={m} witness={witness}; exact rational arithmetic")
    print("LIMIT: discrepancy interval-component lemma and full finite range "
          "are separate proof obligations; no novelty inference")

if __name__=="__main__":
    run()
