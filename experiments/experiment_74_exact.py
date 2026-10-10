#!/usr/bin/env python3
"""Experiment 74: exact rational maximum loneliness, no floating point."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import argparse


def distance_to_integer(x):
    x = x - (x.numerator // x.denominator)
    return min(x, 1 - x)


def exact_optimum(speeds):
    v = tuple(sorted(set(int(a) for a in speeds)))
    if len(v) < 2 or any(a <= 0 for a in v):
        raise ValueError("Supply at least two distinct positive integer speeds")
    candidates = {Fraction(0)}
    for a in v:
        for h in range(a):
            candidates.add(Fraction(2*h+1, 2*a))
    for a, b in combinations(v, 2):
        for n in range(a+b):
            candidates.add(Fraction(n, a+b))
    best = Fraction(-1)
    witness = None
    for t in sorted(candidates):
        score = min(distance_to_integer(a*t) for a in v)
        if score > best:
            best, witness = score, t
    return best, witness, len(candidates)


def test():
    for speeds, expected in [((1, 2), Fraction(1, 3)),
                             ((1, 2, 3), Fraction(1, 4)),
                             ((1, 3), Fraction(1, 2)),
                             ((1, 2, 3, 4), Fraction(1, 5))]:
        score, t, count = exact_optimum(speeds)
        assert score == expected, (speeds, score, expected)
        assert all(distance_to_integer(a*t) >= Fraction(1, len(speeds)+1)
                   for a in speeds)
        print("PASS", speeds, "optimum", score, "time", t, "candidates", count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("speeds", nargs="*", type=int)
    args = parser.parse_args()
    if args.speeds:
        score, time, count = exact_optimum(args.speeds)
        print("speeds:", args.speeds)
        print("exact optimum:", score)
        print("maximizing time:", time)
        print("candidates:", count)
        print("LRC threshold:", Fraction(1, len(set(args.speeds))+1))
        print("instance satisfies LRC:", score >= Fraction(1, len(set(args.speeds))+1))
    else:
        test()
