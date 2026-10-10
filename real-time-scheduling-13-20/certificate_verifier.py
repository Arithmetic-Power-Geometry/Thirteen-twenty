"""CS-008: independently structured exact certificate verifier.

Uses direct forbidden-phase intersection, not safe_windows(). Handles
positive-duration equal-job common-window scheduling. All numbers rational.
"""
from fractions import Fraction as F


def _q(x):
    return F(x)


def _valid(a,b,r,d,p,n):
    if not (isinstance(a,int) and isinstance(b,int) and a>0 and b>0):
        raise ValueError("positive integer frequencies required")
    r,d,p=map(_q,(r,d,p))
    if not (0<=r<=d<=1 and p>0 and isinstance(n,int) and n>=0):
        raise ValueError("invalid job data")
    return r,d,p


def _forbidden_intervals(v):
    """Open unsafe neighborhoods on [0,1]; boundary equality is safe."""
    e=F(1,16*v)
    for j in range(v+1):
        center=F(j,v)
        yield max(F(0),center-e),min(F(1),center+e)


def _overlap_open(x,y,l,u):
    """Does positive-length segment [x,y] meet open forbidden (l,u)?"""
    return max(x,l)<min(y,u)


def _safe_execution(a,b,x,y):
    if not (F(0)<=x<y<=F(1)):
        return False
    for v in (a,b,a+b):
        for l,u in _forbidden_intervals(v):
            if _overlap_open(x,y,l,u):
                return False
    return True


def verify_yes_certificate(a,b,r,d,p,n,certificate):
    """Verify supplied rational intervals without calling scheduling solver."""
    r,d,p=_valid(a,b,r,d,p,n)
    if not isinstance(certificate,(list,tuple)) or len(certificate)!=n:
        return False
    previous_end=None
    for item in certificate:
        if not isinstance(item,(list,tuple)) or len(item)!=2:
            return False
        try:
            start,end=map(_q,item)
        except (ValueError,TypeError,ZeroDivisionError):
            return False
        if not (r<=start<end<=d and end-start==p):
            return False
        if previous_end is not None and start<previous_end:
            return False
        if not _safe_execution(a,b,start,end):
            return False
        previous_end=end
    return True


def _independent_safe_components(a,b):
    """Union forbidden open intervals; return positive-length complement gaps.

    Unsafe neighborhoods are open. Isolated safe points do not matter for
    positive-duration jobs.
    """
    forbidden=sorted((l,u) for v in (a,b,a+b)
                     for l,u in _forbidden_intervals(v) if l<u)
    merged=[]
    for l,u in forbidden:
        if merged and l < merged[-1][1]:
            merged[-1]=(merged[-1][0],max(merged[-1][1],u))
        else:
            merged.append((l,u))
    gaps=[]
    cursor=F(0)
    for l,u in merged:
        if cursor<l:
            gaps.append((cursor,l))
        cursor=max(cursor,u)
    if cursor<F(1):
        gaps.append((cursor,F(1)))
    return gaps


def verify_no_capacity_certificate(a,b,r,d,p,n,claimed_capacity):
    """Recompute exact capacity by independent forbidden-interval union.

    Sound NO only when n>capacity. No succinct certificate claim.
    """
    r,d,p=_valid(a,b,r,d,p,n)
    if not isinstance(claimed_capacity,int) or claimed_capacity<0:
        return False
    capacity=0
    for left,right in _independent_safe_components(a,b):
        lo,hi=max(left,r),min(right,d)
        if lo<hi:
            capacity+=int((hi-lo)//p)
    return claimed_capacity==capacity and n>capacity
