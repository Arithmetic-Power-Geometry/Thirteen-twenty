"""P03-21 independent exact breakpoint-cell measure audit.

Uses only Fraction and interval midpoint classification; does not import
the project's component-generation or measure implementation.
"""
from fractions import Fraction as F
from math import gcd

Q=F(1,16)

def independent_measure(a,b):
    assert isinstance(a,int) and isinstance(b,int) and a>0 and b>0
    knots={F(0),F(1)}
    for k in (a,b,a+b):
        for j in range(k):
            for x in (F(j,k)+Q/k,F(j+1,k)-Q/k):
                if 0<x<1:knots.add(x)
    knots=sorted(knots)
    total=F(0)
    for left,right in zip(knots,knots[1:]):
        t=(left+right)/2
        if all(min((k*t)%1,1-(k*t)%1)>=Q for k in (a,b,a+b)):
            total+=right-left
    return total

def run():
    expected={(1,14):F(13,20),(1,1):F(13,16),(2,3):F(83,120)}
    for pair,value in expected.items():
        assert independent_measure(*pair)==value,(pair,independent_measure(*pair))
    for g in (2,3,7):
        assert independent_measure(g,14*g)==F(13,20)
    assert independent_measure(14,1)==F(13,20)
    tested=0
    equality=[]
    for a in range(1,41):
        for b in range(a,41):
            if gcd(a,b)!=1:continue
            mu=independent_measure(a,b)
            assert mu>=F(13,20),(a,b,mu)
            if mu==F(13,20):equality.append((a,b))
            tested+=1
    assert (1,14) in equality
    print(f"PASS: {tested} primitive pairs with 1<=a<=b<=40; "
          f"zero violations; equality_pairs={equality}; "
          "exact independent midpoint breakpoint oracle")
    print("LIMIT: finite sample does not prove the global 13/20 bound or uniqueness")

if __name__=="__main__":
    run()
