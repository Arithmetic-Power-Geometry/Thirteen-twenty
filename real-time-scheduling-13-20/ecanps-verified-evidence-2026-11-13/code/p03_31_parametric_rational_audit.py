"""Exact rational cross-check of the threshold-parametric torus discrepancy lemma."""
from fractions import Fraction as Q
from math import gcd

THRESHOLDS = (Q(1, 20), Q(1, 16), Q(1, 12), Q(1, 8), Q(1, 5))
MAX_FREQUENCY = 12


def union_measure(a, b, h):
    """Independent excluded-interval union in rational coordinates."""
    intervals = []
    for v in (a, b, a + b):
        for k in range(v + 1):
            lo = max(Q(0), Q(k, v) - h / v)
            hi = min(Q(1), Q(k, v) + h / v)
            if lo < hi:
                intervals.append((lo, hi))
    intervals.sort()
    covered = Q(0)
    end = Q(0)
    for lo, hi in intervals:
        if hi > end:
            covered += hi - max(lo, end)
            end = hi
    return 1 - covered


def midpoint_measure(a, b, h):
    """Independent breakpoint-midpoint integral in rational coordinates."""
    points = {Q(0), Q(1)}
    for v in (a, b, a + b):
        for k in range(v + 1):
            for sign in (-1, 1):
                t = (Q(k) + sign * h) / v
                if 0 < t < 1:
                    points.add(t)
    pts = sorted(points)
    total = Q(0)
    for left, right in zip(pts, pts[1:]):
        t = (left + right) / 2
        if all(min((v * t) % 1, 1 - (v * t) % 1) >= h for v in (a, b, a + b)):
            total += right - left
    return total


def main():
    checks = 0
    gcd_checks = 0
    for h in THRESHOLDS:
        mean = 1 - 6 * h + 9 * h * h
        assert mean == (1 - 3 * h) ** 2
        for b in range(1, MAX_FREQUENCY + 1):
            for a in range(1, b + 1):
                if gcd(a, b) != 1:
                    continue
                u = union_measure(a, b, h)
                m = midpoint_measure(a, b, h)
                assert u == m, (h, a, b, u, m)
                assert abs(u - mean) <= Q(2, b), (h, a, b, u, mean)
                checks += 1
                for g in (2, 3):
                    assert union_measure(g * a, g * b, h) == u, (h, a, b, g)
                    gcd_checks += 1
        print(f"PASS h={h}: exact mean={mean}; independent union/midpoint, discrepancy and gcd invariance")
    assert checks == 230, checks
    assert gcd_checks == 460, gcd_checks
    print(f"PASS: {checks} cross-algorithm rational comparisons, {checks} discrepancy inequalities, {gcd_checks} scaling checks")


if __name__ == '__main__':
    main()
