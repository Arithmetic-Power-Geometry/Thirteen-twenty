"""Independent exact verifier: merge forbidden intervals rather than sample safe cells."""
import csv, math, hashlib, sys
from pathlib import Path
def check(a,b):
    c=a+b; D=16*a*b*c
    forbidden=[]
    for v in (a,b,c):
        step=D//(16*v)
        for j in range(v):
            left=16*j*step; right=(16*j+1)*step
            forbidden.append((left,right))
            left=(16*j+15)*step; right=(16*j+16)*step
            forbidden.append((left,right))
    forbidden.sort()
    covered=0; lo=hi=0
    for l,r in forbidden:
        if l>hi:
            covered+=hi-lo; lo,hi=l,r
        elif r>hi: hi=r
    covered+=hi-lo
    return D-covered,D
def main():
    inp=Path(sys.argv[1]); out=Path(sys.argv[2]); count=bad=eq=mismatch=0
    with inp.open(newline='') as f, out.open('w',newline='') as o:
        writer=csv.writer(o); writer.writerow(['a','b','safe_numerator','denominator','equal_13_20'])
        for row in csv.DictReader(f):
            a=int(row['a']); b=int(row['b']); n,d=check(a,b); count+=1
            if n!=int(row['numerator']) or d!=int(row['denominator']): mismatch+=1
            if 20*n<13*d: bad+=1
            if 20*n==13*d: eq+=1
            writer.writerow([a,b,n,d,int(20*n==13*d)])
    digest=hashlib.sha256(out.read_bytes()).hexdigest()
    print(f'count={count} violations={bad} equalities={eq} mismatches={mismatch} sha256={digest}')
    if (count,bad,eq,mismatch)!=(11698,0,1,0): raise SystemExit(1)
if __name__=='__main__': main()
