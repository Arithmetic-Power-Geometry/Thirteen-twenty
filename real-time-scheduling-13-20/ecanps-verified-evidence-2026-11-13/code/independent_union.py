"""Independent exact finite verification by forbidden-interval union."""
from math import gcd, lcm
import json, time, hashlib

def measure(a, b):
    vals = (a, b, a+b)
    D = 16*lcm(*vals)
    bad = []
    for v in vals:
        h = D//(16*v)
        step = D//v
        for j in range(v+1):
            center = j*step
            lo, hi = max(0,center-h), min(D,center+h)
            if lo < hi:
                bad.append((lo,hi))
    bad.sort()
    covered = 0
    left = right = 0
    for lo,hi in bad:
        if lo > right:
            covered += right-left
            left,right = lo,hi
        elif hi > right:
            right = hi
    covered += right-left
    return D-covered,D

def main():
    t=time.perf_counter()
    count=0
    failures=[]
    equalities=[]
    minimum=None
    digest=hashlib.sha256()
    for b in range(1,197):
        for a in range(1,b+1):
            if gcd(a,b)!=1:
                continue
            good,D=measure(a,b)
            count+=1
            digest.update(f"{a},{b},{good},{D}\n".encode())
            if 20*good<13*D:
                failures.append([a,b,good,D])
            if 20*good==13*D:
                equalities.append([a,b,good,D])
            if minimum is None or good*minimum[3]<minimum[2]*D:
                minimum=[a,b,good,D]
    result={"method":"exact union of excluded intervals; integer endpoints; no midpoint classification","domain":"1<=a<=b<=196, gcd(a,b)=1","count":count,"failures":failures,"equalities":equalities,"minimum":minimum,"records_sha256":digest.hexdigest(),"elapsed_seconds":round(time.perf_counter()-t,3),"status":"PASS" if count==11698 and not failures and len(equalities)==1 and equalities[0][:2]==[1,14] else "FAIL"}
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    main()
