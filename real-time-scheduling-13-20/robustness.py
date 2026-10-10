"""CS-009: exact phase-shifted safe windows and bounded timing jitter.

Phase convention: ||v*t + phi_v|| >= 1/16, independent rational phases.
For a nominal interval [s,s+p] with unknown common time shift
delta in [-eps,eps], require all shifted execution points to be safe
and remain in [0,1]. This is a worst-case, not probabilistic model.
"""
from fractions import Fraction as F


def shifted_safe_windows(a,b,phases=(0,0,0)):
    if not (isinstance(a,int) and isinstance(b,int) and a>0 and b>0):
        raise ValueError("a,b must be positive integers")
    if len(phases)!=3:
        raise ValueError("three phases required")
    phases=tuple(map(F,phases))
    ends={F(0),F(1)}
    for v,phi in zip((a,b,a+b),phases):
        # Boundary crossings for v*t+phi = k +/- 1/16.
        for k in range(-abs(phi.numerator)-2, v+abs(phi.numerator)+3):
            for offset in (-F(1,16),F(1,16)):
                t=(F(k)+offset-phi)/v
                if 0<t<1:
                    ends.add(t)
    points=sorted(ends)
    out=[]
    for l,u in zip(points,points[1:]):
        t=(l+u)/2
        if all(F(1,16)<=((v*t+phi)%1)<=F(15,16)
               for v,phi in zip((a,b,a+b),phases)):
            if out and out[-1][1]==l:
                out[-1]=(out[-1][0],u)
            else:
                out.append((l,u))
    return out


def shifted_measure(a,b,phases=(0,0,0)):
    return sum((u-l for l,u in shifted_safe_windows(a,b,phases)),F(0))


def robust_admit(a,b,phases,release,deadline,duration,jitter):
    """Exact robust admission for a common adversarial time translation.

    Release/deadline apply to the ACTUAL execution interval. Nominal
    interval [s,s+p] must satisfy [s-eps,s+p+eps] subset of one safe
    window intersected with [release,deadline].
    """
    r,d,p,e=map(F,(release,deadline,duration,jitter))
    if not (0<=r<=d<=1 and p>0 and e>=0):
        raise ValueError("invalid release/deadline/duration/jitter")
    for l,u in shifted_safe_windows(a,b,phases):
        s=max(l+e,r+e)
        if s+p+e<=min(u,d):
            return ("YES",s)
    return ("NO",None)


def verify_robust_yes(a,b,phases,r,d,p,e,s):
    r,d,p,e,s=map(F,(r,d,p,e,s))
    if not (0<=r<=d<=1 and p>0 and e>=0):
        return False
    return any(max(l,r)<=s-e and s+p+e<=min(u,d)
               for l,u in shifted_safe_windows(a,b,phases))
