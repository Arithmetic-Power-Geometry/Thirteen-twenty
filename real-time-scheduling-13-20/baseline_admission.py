"""CS-004 exact classical admission baselines, with correct segment-tree index."""
from bisect import bisect_left, bisect_right
from fractions import Fraction as Q
from exact_admission import safe_windows


def linear_query(windows, release, deadline, duration):
    r, d, p = map(Q, (release, deadline, duration))
    for left, right in windows:
        s = max(r, left)
        if s+p <= min(d, right):
            return s
    return None


def binary_query(windows, release, deadline, duration):
    """Binary-search start, then linear scan: worst-case O(k), not O(log k)."""
    r, d, p = map(Q, (release, deadline, duration))
    if p <= 0 or not (0 <= r <= d <= 1):
        raise ValueError("invalid job")
    rights = [u for _, u in windows]
    for left, right in windows[bisect_left(rights, r+p):]:
        s = max(r, left)
        if s+p <= min(d, right):
            return s
        if left+p > d:
            break
    return None


class AdmissionIndex:
    """Segment tree of window lengths: O(k) build, O(log k) query."""
    def __init__(self, a, b):
        self.windows = safe_windows(a, b)
        self.rights = [u for _, u in self.windows]
        self.lefts = [u for u, _ in self.windows]
        self.n = len(self.windows)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [Q(0)] * (2*self.size)
        for i, (u,v) in enumerate(self.windows):
            self.tree[self.size+i] = v-u
        for i in range(self.size-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def _first_long_enough(self, start, end, duration):
        """Find leftmost index in [start,end) with interval length >= duration."""
        def visit(node, lo, hi):
            if hi <= start or lo >= end or self.tree[node] < duration:
                return None
            if hi-lo == 1:
                return lo if lo < self.n else None
            mid = (lo+hi)//2
            candidate = visit(node*2, lo, mid)
            return candidate if candidate is not None else visit(node*2+1, mid, hi)
        return visit(1, 0, self.size)

    def query(self, release, deadline, duration):
        r, d, p = map(Q, (release, deadline, duration))
        if p <= 0 or not (0 <= r <= d <= 1):
            raise ValueError("invalid job")
        # Candidate overlapping release may fit despite being shorter than p
        # as a whole? It must be at least p; check exact r.
        i = bisect_left(self.rights, r+p)
        if i >= self.n:
            return None
        left, right = self.windows[i]
        s = max(r, left)
        if s+p <= min(d, right):
            return s
        # Search later windows with length >= p and left <= d-p.
        begin = i+1
        end = bisect_right(self.lefts, d-p)
        j = self._first_long_enough(begin, end, p)
        return self.windows[j][0] if j is not None else None
