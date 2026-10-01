# Native four-state exact solver

## Goal

Decide Theorem C directly instead of translating the mathematics into a very large generic Boolean encoding.

There are

\[
\binom{42}{2}=861
\]

unordered pair variables, each in four states

\[
\{n,d,m,p\}.
\]

## Native constraints

The solver should enforce directly:

- row counts: one `d`, ten signed, thirty null;
- signed coordinate balances;
- unsigned coordinate quotas;
- both pair-composition sums jointly.

For a two-step path `x-z-y`, possible contribution pairs are only

\[
(0,0),\ (4,0),\ (2,0),\ (1,+1),\ (1,-1).
\]

The same intermediate states must hit both exact targets.

## Core propagator

For a fixed endpoint pair `(x,y)`, each remaining `z` has a small set of possible contribution pairs determined by the current domains of `c_xz,c_zy`.

Use an exact reachable-sum dynamic program / bitset calculation to test whether the target pair remains attainable.

With prefix/suffix support tables, remove a state value if it participates in no completion of the pair sum.

This is generalized arc consistency on the native equation rather than unit propagation on a clause expansion.

## Search layer

After deterministic propagation:

- domain-based decisions;
- learned nogoods;
- nonchronological backtracking;
- restarts;
- activity/LBD-style scoring adapted to four-valued literals.

AI may be used offline to optimize branching from recorded search trajectories, but not in the inner propagation loop.

## Certificates

Design proof logging from the beginning.

A complicated fast solver should emit a trace checked by a small independent verifier that knows only:

- the original native rules;
- domain restrictions;
- exact propagation certificates;
- learned nogoods;
- branch exhaustion.

SAT is easier to certify: reconstruct the 99×99 adjacency and verify exactly

\[
A^2+A=12I+2J.
\]

## First benchmark

Do not run for weeks immediately.

Measure:

- root-level domain reduction;
- average propagation after one decision;
- median decisions to conflict;
- nodes per second;
- learned-nogood quality;
- depth of surviving randomized branches.

Three possible regimes:

1. propagation avalanche → desktop decision may be realistic;
2. healthy learning → hours/days may be realistic;
3. late contradiction with huge depth → stop and redesign rather than blindly add CPU.

## Important positive control

Generic search heuristics in the campaign also failed on `m=11` BvLS, where a solution is known.

Therefore heuristic failure is not evidence for C2 nonexistence.
