# T4 · Exact completion / reconstruction theorem

## Input

Fix a complete signed candidate `N` satisfying

\[
N=N^T,\qquad \operatorname{diag}N=0,\qquad N_{uv}\in\{0,\pm1\},
\]

\[
NR=0,\qquad N^2=N+12I-RR^T.
\]

Set

\[
B=|N|,\qquad M=|R|,
\]

\[
T=2J_{42,7}-M-\frac12BM,
\]

\[
E=\frac12(8I+4J-MM^T-B^2-B).
\]

Define `L_N` as the real-linear feasibility system

\[
D=D^T,\quad D\ge0,\quad \operatorname{diag}D=0,\quad D\mathbf1=\mathbf1,
\]

\[
D_{uv}=0\quad\text{when }B_{uv}=1,
\]

\[
DM=T,
\]

\[
BD+DB+D=E.
\]

No binary constraint on `D` and no equation `D^2=I` is imposed.

## Theorem

For every complete signed `N` above, `L_N` is either empty or consists of exactly one point. If it is nonempty, that point is automatically an integral fixed-point-free perfect matching.

A feasible completion reconstructs the full normalized 99-vertex graph.

## Core proof mechanism

1. `DM=T` plus convexity forces every positive entry of a feasible `D` toward a prescribed target cell.
2. The residual matching components are tiny; ambiguous components are `K_{2,2}` blocks.
3. A nonempty real feasible set has a canonical half-integral point.
4. Half/free components define a nonzero whole-cell difference space `L` and a defect projector `P_L` with

\[
\bar D^2=I-P_L.
\]

5. The even quotient then satisfies

\[
\bar Q^2+\bar Q=12I+4J-MM^T-4P_L.
\]

6. The defect space is `B`-invariant; on it the restriction `X` satisfies

\[
X^2+X=8I.
\]

7. Signed-origin parity forces even row sums and zero diagonal, hence `tr X=0`.
8. The irreducible polynomial `t^2+t-8` forces equal multiplicities of its conjugate irrational roots, hence strictly negative trace on any nonzero defect space.

Contradiction. Therefore the defect space is zero and every feasible completion is integral and unique.

## Scope

T4 **does not** prove that any suitable `N` exists.

The remaining question is

\[
\exists N\in\mathcal N\text{ with }L_N\ne\varnothing\ ?
\]

The full proof, graph reconstruction, historical notes, and caveats are preserved in [`../archive/FULL_DOSSIER.md`](../archive/FULL_DOSSIER.md).

## Review status

Campaign record: a blind independent agent reportedly rederived the theorem and reconstruction and found no mathematical gap, with only minor wording corrections.

This is not the same as peer review or a formal proof assistant certificate.
