"""CS-007: exact multi-job capacity for equal-duration jobs, common window.

Classical tractable subcase, not a claimed novel complexity breakthrough.
"""
from fractions import Fraction as F
from exact_admission import safe_windows


def equal_job_capacity(a, b, release, deadline, duration):
    r, d, p = map(F, (release, deadline, duration))
    if not (0 <= r <= d <= 1 and p > 0):
        raise ValueError("require 0 <= r <= d <= 1 and p > 0")
    schedule = []
    capacity = 0
    allocation = []
    for left, right in safe_windows(a, b):
        lo, hi = max(left, r), min(right, d)
        if hi <= lo:
            continue
        count = int((hi - lo) // p)
        if count:
            allocation.append((lo, hi, count))
            capacity += count
            schedule.extend((lo + i*p, lo + (i+1)*p) for i in range(count))
    return capacity, schedule, allocation


def decide_equal_jobs(a, b, release, deadline, duration, jobs):
    if not isinstance(jobs, int) or jobs < 0:
        raise ValueError("jobs must be nonnegative integer")
    capacity, schedule, allocation = equal_job_capacity(a,b,release,deadline,duration)
    if jobs <= capacity:
        return {"decision":"YES","capacity":capacity,"schedule":schedule[:jobs],
                "allocation":allocation}
    return {"decision":"NO","capacity":capacity,"allocation":allocation}


def verify_equal_jobs(a,b,r,d,p,jobs,result):
    """Recompute independently from phase-defined safe windows.

    Not a compact independent proof checker: it trusts the reference
    safe-window constructor, so external cross-implementation audit needed.
    """
    expected = decide_equal_jobs(a,b,r,d,p,jobs)
    return result == expected
