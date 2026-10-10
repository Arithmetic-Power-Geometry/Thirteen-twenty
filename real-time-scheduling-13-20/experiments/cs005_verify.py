"""CS-005 exact rational test: python3 experiments/cs005_verify.py"""
from fractions import Fraction as Q
from math import gcd

def safe_windows(a,b):
    pts={Q(0),Q(1)}
    for v in (a,b,a+b):
        for j in range(v):
            pts.add(Q(16*j+1,16*v))
            pts.add(Q(16*j+15,16*v))
    p=sorted(pts)
    out=[]
    for l,r in zip(p,p[1:]):
        t=(l+r)/2
        if all(Q(1,16) <= (v*t)%1 <= Q(15,16) for v in (a,b,a+b)):
            if out and out[-1][1]==l:
                out[-1]=(out[-1][0],r)
            else:
                out.append((l,r))
    return out

def run(limit=34):
    tested=0
    equality=[]
    for b in range(1,limit+1):
        for a in range(1,b+1):
            if gcd(a,b)!=1:continue
            w=safe_windows(a,b)
            measure=sum((r-l for l,r in w),Q(0))
            longest=max((r-l for l,r in w),default=Q(0))
            assert measure >= Q(13,20),(a,b,"measure",measure)
            assert len(w)<=2*(a+b),(a,b,"components",len(w))
            assert longest>=Q(13,40*(a+b)),(a,b,"longest",longest)
            if measure==Q(13,20):equality.append((a,b))
            tested+=1
    print(f"tested={tested} violations=0 equality={equality}")
    assert (1,14) in equality
if __name__=="__main__":
    run()
