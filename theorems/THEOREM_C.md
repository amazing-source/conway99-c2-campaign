# Theorem C · Coupled exact system in `(Q,N)`

**Status:** proved in the campaign by an elementary derivation.  
**Nature:** exact reformulation; no complexity claim; no candidate excluded by the theorem alone.

Let

\[
M=|R|,\qquad H=RR^T,\qquad K=MM^T.
\]

Consider integer symmetric 42×42 matrices `Q,N` with zero diagonal and the conditions

\[
NR=0,\qquad N^2=N+12I-H, \tag{C2}
\]

\[
Q^2+Q+K=12I+4J, \tag{C3}
\]

\[
QM=4J_{42,7}-2M, \tag{C4}
\]

and for all `x != y`

\[
(Q_{xy}-1)^2+N_{xy}^2=1. \tag{C5}
\]

## Statement

### (a)

If `N` is a complete signed candidate and `D in L_N` is integral, then

\[
Q=|N|+2D
\]

satisfies `(C1)-(C5)`.

### (b)

Conversely, if `(Q,N)` satisfies `(C1)-(C5)`, define off diagonal

\[
B=[Q=1],\qquad D=[Q=2].
\]

Then

\[
B=|N|,\qquad Q=B+2D,
\]

`D` is a fixed-point-free perfect matching, `D\circ B=0`, and `D in L_N`.

### (c)

The two constructions are inverse between integral completion pairs `(N,D)` and solutions `(Q,N)`.

With T4, the campaign existence statement

\[
\exists N\in\mathcal N\text{ with }L_N\ne\varnothing
\]

is equivalent to existence of an integer solution of `(C1)-(C5)`.

## Proof

Off diagonal set

\[
a=\frac{Q-N}{2},\qquad b=\frac{Q+N}{2}.
\]

Condition `(C5)` says `(Q_xy-1,N_xy)` is exactly one of

\[
(-1,0),(1,0),(0,-1),(0,1).
\]

Equivalently `(a_xy,b_xy)` is one of

\[
(0,0),(1,1),(1,0),(0,1).
\]

Therefore

\[
N_{xy}\in\{0,\pm1\},\qquad B_{xy}=|N_{xy}|=[Q_{xy}=1],
\]

and

\[
D=[Q=2]=a\circ b.
\]

### Forward direction

For integral `D in L_N`, nonnegativity and `D1=1` make `D` a 0/1 matrix with one 1 per row; symmetry and zero diagonal make it a fixed-point-free involution, hence `D^2=I`.

Using `Q=B+2D` and the completion equation `BD+DB+D=E` gives

\[
Q^2+Q+K=12I+4J.
\]

Likewise

\[
QM=BM+2DM=4J-2M.
\]

The four possible pair types give `(C5)` directly.

### Reverse direction

Apply `(C4)` to `1_7`. Since `M1_7=2 1_42`, we get `Q1=12 1`.

The diagonal of the signed quadratic equation gives `B1=10 1`.

Hence

\[
2D1=Q1-B1=2 1,
\]

so `D1=1`. Together with symmetry, 0/1 entries, and zero diagonal, `D` is a fixed-point-free perfect matching.

Also `D\circ B=0`.

From `(C4)`,

\[
DM=\frac{(Q-B)M}{2}=\frac{4J-2M-BM}{2}=T.
\]

Finally expand `(C3)` using `Q=B+2D` and `D^2=I`; reversing the forward calculation gives

\[
BD+DB+D=E.
\]

Thus `D in L_N`.

## Structural reading

The signed and unsigned layers each have their own quadratic system. Their only direct interface is the pointwise four-state condition `(C5)`.

This is structural progress, but because it is bijective with the old exact solution set, it does not by itself reduce the set of candidates.
