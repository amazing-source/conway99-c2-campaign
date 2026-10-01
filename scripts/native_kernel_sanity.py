#!/usr/bin/env python3
"""Sanity checks for the canonical 42 D7-root labels and Theorem-C four-state alphabet.

This is NOT a solver and proves nothing about existence/nonexistence.
"""
import numpy as np

def roots_d7():
    rows = []
    labels = []
    for i in range(7):
        for j in range(i+1, 7):
            for sign in (+1, -1):
                r = np.zeros(7, dtype=int)
                r[i] = 1
                r[j] = sign
                rows.append(r)
                labels.append((i+1, j+1, "+" if sign == 1 else "-"))
    return labels, np.array(rows, dtype=int)

labels, R = roots_d7()
M = np.abs(R)

assert R.shape == (42, 7)
assert len({tuple(r) for r in R}) == 42
assert np.array_equal(R.T @ R, 12*np.eye(7, dtype=int))
assert np.array_equal(M.sum(axis=1), 2*np.ones(42, dtype=int))
assert np.array_equal(M.T @ M, 10*np.eye(7, dtype=int) + 2*np.ones((7,7), dtype=int))

states = {
    "n": (0, 0),
    "d": (2, 0),
    "m": (1, -1),
    "p": (1, +1),
}

seen_ab = set()
for name, (q,n) in states.items():
    assert (q-1)**2 + n*n == 1
    a = (q-n)//2
    b = (q+n)//2
    assert a in (0,1) and b in (0,1)
    seen_ab.add((a,b))
assert seen_ab == {(0,0),(1,1),(1,0),(0,1)}

contrib = sorted(set((q1*q2, n1*n2)
                     for q1,n1 in states.values()
                     for q2,n2 in states.values()))
assert contrib == [(0,0),(1,-1),(1,1),(2,0),(4,0)]

print("OK")
print("labels:", len(labels))
print("all roots distinct:", len({tuple(r) for r in R}) == 42)
print("R^T R = 12 I:", True)
print("M^T M = 10 I + 2 J:", True)
print("four states:", states)
print("two-step contribution alphabet:", contrib)
