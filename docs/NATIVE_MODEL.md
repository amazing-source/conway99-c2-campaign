# Native 42-label model

This file states the exact finite problem without requiring the reader to begin from the 99×99 adjacency matrix.

## Labels

For every pair `1 <= i < j <= 7`, take the two roots

\[
r_{ij,+}=e_i+e_j,\qquad r_{ij,-}=e_i-e_j.
\]

These 42 roots are all distinct.

Let `R` be the 42×7 matrix of these rows and `M=|R|`.

Useful identities:

\[
R^TR=12I_7,
\]

\[
M\mathbf1_7=2\mathbf1_{42},
\]

\[
M^TM=10I_7+2J_7.
\]

Set

\[
H=RR^T,\qquad K=MM^T.
\]

## Four-state pair relation

Every unordered pair `{x,y}` has one state in

\[
\{n,d,m,p\}.
\]

Numerical projections:

| state | `q` | `s` |
|---|---:|---:|
| `n` | 0 | 0 |
| `d` | 2 | 0 |
| `m` | 1 | -1 |
| `p` | 1 | +1 |

The matrices are recovered by

\[
Q_{xy}=q(c_{xy}),\qquad N_{xy}=s(c_{xy}).
\]

## Exact row rules

For every label `x`:

- exactly one `d`;
- exactly ten states in `{m,p}`;
- exactly thirty `n`.

## Coordinate balance

For every label `x` and coordinate `a`:

\[
\sum_y s(c_{xy})r_y(a)=0,
\]

and

\[
\sum_y q(c_{xy})m_y(a)=
\begin{cases}
2,&a\in\operatorname{supp}r_x,\\
4,&a\notin\operatorname{supp}r_x.
\end{cases}
\]

## Pair-composition rules

For every distinct `x,y`:

\[
\sum_z q(c_{xz})q(c_{zy})=4-k_{xy}-q(c_{xy}),
\]

\[
\sum_z s(c_{xz})s(c_{zy})=s(c_{xy})-h_{xy},
\]

where

\[
k_{xy}=m_x\cdot m_y,\qquad h_{xy}=r_x\cdot r_y.
\]

The same intermediate labels must satisfy both equations. That joint realizability is the essential coupling.

## Meaning of `d`

The `d` state defines the matrix

\[
D=[Q=2].
\]

In any complete solution, `D` is a fixed-point-free perfect matching on the 42 exterior involution-orbits.

## Positive verification endpoint

From an exact coupled solution, reconstruct the full 99×99 adjacency and verify exactly

\[
A^2+A=12I+2J.
\]
