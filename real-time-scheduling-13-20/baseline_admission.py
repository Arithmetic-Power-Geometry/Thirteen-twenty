"""CS-004: classical exact one-job admission baselines.

All algorithms take a precomputed, sorted disjoint safe-window list.
No asymptotic novelty is claimed. Binary search works by monotonicity
of right endpoints; preprocessing is excluded from query times.
"""
from bisect import bisect_left
from fractions import Fraction as Q
from exact_admission import safe_windows


def linear_query(windows, release, deadline, duration):
    r, d, p = map(Q, (release, deadline, duration))
    for left, right in windows:
        s = max(r, left)
        if s + p <= min(d, right):
            return s
    return None


def binary_query(windows, release, deadline, duration):
    """O(log k) predecessor-style admission for one job, k safe windows.

    The earliest window whose right endpoint >= release+duration
    is the only candidate needed. Later windows cannot help if it
    fails solely because of deadline.
    """
    r, d, p = map(Q, (release, deadline, duration))
    if p <= 0 or not (0 <= r <= d <= 1):
        raise ValueError("invalid job")
    rights = [u for _, u in windows]
    idx = bisect_left(rights, r + p)
    if idx == len(windows):
        return None
    left, right = windows[idx]
    s = max(left, r)
    return s if s + p <= min(right, d) else None


class AdmissionIndex:
    """Preprocess right endpoints once; O(log k) query comparisons."""
    def __init__(self, a, b):
        self.windows = safe_windows(a, b)
        self.rights = [u for _, u in self.windows]

    def query(self, release, deadline, duration):
        r, d, p = map(Q, (release, deadline, duration))
        if p <= 0 or not (0 <= r <= d <= 1):
            raise ValueError("invalid job")
        idx = bisect_left(self.rights, r + p)
        if idx == len(self.windows):
            return None
        left, right = self.windows[idx]
        start = max(left, r)
        return start if start + p <= min(d, right) else None
