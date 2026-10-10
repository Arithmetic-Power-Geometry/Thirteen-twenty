"""Exact arithmetic verification of CS-006 linear component witness family."""
from fractions import Fraction as F
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from exact_admission import phase_safe, safe_windows


def witnesses(b):
    if b < 8:
        raise ValueError("b>=8 required")
    return [(j, F(4*j+1, 4*b)) for j in range(b+1)
            if F(1,4) <= F(4*j+1,4*b) <= F(1,2)]


def verify(b, enumerate_windows=True):
    pairs = witnesses(b)
    assert len(pairs) >= b//4-1
    for j, t in pairs:
        assert all(phase_safe(t,v) for v in (1,b,b+1))
        assert all(min((t*v)%1, 1-(t*v)%1)>F(1,16)
                   for v in (1,b,b+1))
    for (j,t),(k,u) in zip(pairs,pairs[1:]):
        assert k==j+1
        assert t < F(j+1,b) < u
        assert not phase_safe(F(j+1,b), b)
    if enumerate_windows:
        intervals=safe_windows(1,b)
        assert len(intervals)>=len(pairs)
        for j,t in pairs:
            assert sum(left<t<right for left,right in intervals)==1
    return len(pairs)


if __name__=="__main__":
    for b in (8,9,10,14,16,31,64,128):
        print(f"b={b} distinct_components_witnessed={verify(b)} lower_bound={b//4-1}")
