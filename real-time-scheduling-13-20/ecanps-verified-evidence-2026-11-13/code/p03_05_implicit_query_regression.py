"""P03-05: independent exact-rational implicit-query regression (Python 3.11+)."""
from fractions import Fraction as F
from random import Random

def safe(t,a,b):
    def dist(x):
        y=x%1
        return min(y,1-y)
    return all(dist(t*k)>=F(1,16) for k in (a,b,a+b))

def components(a,b):
    cuts={F(0),F(1)}
    for v in (a,b,a+b):
        for k in range(v+1):
            for sign in (-1,1):
                t=F(16*k+sign,16*v)
                if 0<=t<=1: cuts.add(t)
    xs=sorted(cuts)
    elementary = [(x,y) for x,y in zip(xs,xs[1:]) if safe((x+y)/2,a,b)]
    merged = []
    for l,u in elementary:
        if merged and merged[-1][1] == l:
            merged[-1] = (merged[-1][0],u)
        else:
            merged.append((l,u))
    return merged

def implicit(prim,g,r,p,d):
    if r>=1 or p<=0 or r+p>d:return None
    h=g*p; R=g*r; k=R.numerator//R.denominator; x=R-k
    if k>=g:return None
    idx=next((i for i,(_,u) in enumerate(prim) if u>=x),len(prim))
    ans=None
    if idx<len(prim):
        l,u=prim[idx]; start=max(l,x)
        if start+h<=u:ans=F(k)+start+h
    if ans is None:
        for l,u in prim[idx+1:]:
            if u-l>=h:ans=F(k)+l+h;break
    if ans is None and k+1<g:
        for l,u in prim:
            if u-l>=h:ans=F(k+1)+l+h;break
    if ans is None:return None
    f=ans/g
    return f if f<=d else None

def run():
    rng=Random(20261113); checks=0; mismatches=[]
    for a,b in [(1,1),(1,14),(2,3),(3,5),(4,7),(5,9)]:
        prim=components(a,b)
        for g in (1,2,3,5):
            expanded=components(g*a,g*b)
            for z in range(100):
                r=F(rng.randrange(0,65),64)
                p=F(rng.randrange(1,33),64)
                d=F(rng.randrange(0,65),64)
                if z==0:r=F(1);d=F(1)
                if z==1:r=F(0);d=F(1)
                if z==2 and prim:p=(prim[0][1]-prim[0][0])/g;r=F(0);d=F(1)
                got=implicit(prim,g,r,p,d)
                expected=next((max(l,r)+p for l,u in expanded if max(l,r)+p<=u and max(l,r)+p<=d),None)
                checks+=1
                if got!=expected:mismatches.append((a,b,g,r,p,d,got,expected))
    print(f"checks={checks} mismatches={len(mismatches)}")
    assert not mismatches,mismatches[:5]
if __name__=="__main__":run()
