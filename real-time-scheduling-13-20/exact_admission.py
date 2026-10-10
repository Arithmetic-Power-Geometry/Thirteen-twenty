"""Exact rational reference oracle for phase-aligned 13/20 scheduling.

Research software; not a novel algorithm or a claim of Q1 readiness.
Usage: python3 exact_admission.py 1 14 0 1 1/100
"""
from fractions import Fraction as Q
from math import gcd
from sys import argv


def phase_safe(t, v):
    x = (t * v) % 1
    return Q(1, 16) <= x <= Q(15, 16)


def safe_windows(a, b):
    """Return maximal nonempty closed safe intervals on [0,1]."""
    if min(a, b) <= 0:
        raise ValueError("positive frequencies required")
    ends = {Q(0), Q(1)}
    for v in (a, b, a + b):
        for j in range(v):
            ends.add(Q(16*j + 1, 16*v))
            ends.add(Q(16*j + 15, 16*v))
    points = sorted(ends)
    cells = []
    for left, right in zip(points, points[1:]):
        mid = (left + right) / 2
        if all(phase_safe(mid, v) for v in (a, b, a+b)):
            if cells and cells[-1][1] == left:
                cells[-1] = (cells[-1][0], right)
            else:
                cells.append((left, right))
    return cells


def measure(a, b):
    return sum((v-u for u, v in safe_windows(a, b)), Q(0))


def admit(a, b, release, deadline, duration):
    """Return (YES, rational start) or (NO, complete safe-window list).

    Positive-duration jobs only. For zero duration, boundary-only
    feasibility needs a separate convention.
    """
    r, d, p = map(Q, (release, deadline, duration))
    if not (Q(0) <= r <= d <= Q(1) and p > 0):
        raise ValueError("require 0 <= release <= deadline <= 1, duration > 0")
    windows = safe_windows(a, b)
    for left, right in windows:
        start = max(r, left)
        if start + p <= min(d, right):
            return ("YES", start)
    return ("NO", windows)


def verify_yes(a, b, r, d, p, start):
    r, d, p, start = map(Q, (r, d, p, start))
    if not (0 <= r <= start and start+p <= d <= 1 and p > 0):
        return False
    return any(left <= start and start+p <= right
               for left, right in safe_windows(a, b))


def verify_no(a, b, r, d, p, windows):
    """Independent endpoint-cover check of supplied complete windows.

    Completeness is checked by reconstructing the safe set from exact
    phase boundaries; not a succinct NO proof.
    """
    if list(windows) != safe_windows(a, b):
        return False
    return admit(a, b, r, d, p)[0] == "NO"


if __name__ == "__main__":
    if len(argv) != 6:
        raise SystemExit("usage: python3 exact_admission.py a b release deadline duration")
    a, b = int(argv[1]), int(argv[2])
    ans, cert = admit(a, b, argv[3], argv[4], argv[5])
    print("measure =", measure(a, b))
    print("decision =", ans)
    print("certificate =", cert)
