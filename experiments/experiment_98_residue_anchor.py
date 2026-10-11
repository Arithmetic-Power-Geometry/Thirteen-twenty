from fractions import Fraction as F
from itertools import combinations
from math import gcd

def anchor(V):
    q=len(V)+1
    if any(v%q==0 for v in V): return None
    left=min(F(v%q-1,q*v) for v in V)
    right=min(F(q-1-v%q,q*v) for v in V)
    return F(1,q)-left,F(1,q)+right

def safe(t,V):
    q=len(V)+1
    return all(F(1,q)<=(v*t)%1<=F(q-1,q) for v in V)

def check(V):
    z=anchor(V)
    if z is None:
        assert not safe(F(1,len(V)+1),V)
        return None
    a,b=z; mid=F(1,len(V)+1)
    assert a<=mid<=b and safe(a,V) and safe(b,V)
    assert safe((a+mid)/2,V) and safe((b+mid)/2,V)
    eps=F(1,1000*max(V)*(len(V)+1))
    assert not safe(a-eps,V) and not safe(b+eps,V),(V,z)
    residues=[v%(len(V)+1) for v in V]
    assert (a==b)==(1 in residues and len(V) in residues)
    return z

def main():
    counts=[]
    for k,N in ((3,14),(4,11),(5,10)):
        total=good=isolated=interior=0
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            total+=1
            z=check(V)
            if z:
                good+=1
                isolated+=(z[0]==z[1])
                interior+=(z[0]<z[1])
        counts.append((k,N,total,good,isolated,interior))
    assert counts==[(3,14,325,160,77,83),(4,11,325,125,76,49),(5,10,251,126,55,71)]
    print('PASS',counts)
    for V in ((1,2,3),(1,3,4,7),(2,3,5),(1,7,13)):
        print(V,anchor(V))

if __name__=='__main__':main()
