# Ternary signing + capacity exactness

The full source note is archived as [`../archive/TERNARY_PROOF.md`](../archive/TERNARY_PROOF.md).

## Bounded-residue lemma

Let `N` be symmetric, zero-diagonal, with entries in `{0,+1,-1}`. Suppose

\[
NR\equiv0\pmod3,
\]

\[
N^2-N-12I+H\equiv0\pmod3,
\]

and the unsigned support `B=|N|` passes two pointwise capacity tests.

Define

\[
T=2J-M-\frac12BM,
\]

\[
E=\frac12(8I+4J-K-B^2-B).
\]

Capacities:

- `T-cap`: every row of `T` is binary of weight 2;
- `E-cap`: `E` is entrywise nonnegative and integral.

Then the modular equations lift to the exact integer signed equations

\[
NR=0,\qquad N^2=N+12I-H.
\]

### Key bounded-window mechanism

`T-cap` gives entries of `BM` in `{0,2,4}`. Every entry of `NR` is therefore even and lies in `[-4,4]`. Mod-3 vanishing forces it to be zero.

For the quadratic error

\[
F=N^2-N-12I+H,
\]

`E-cap` yields the pointwise bound `|F_uv|<=4`.

Integrality of `E` gives evenness, the ternary equation gives divisibility by 3, hence every off-diagonal `F_uv` is divisible by 6 and has absolute value at most 4. Therefore `F_uv=0`.

## Ternary projector formulation

Over `F_3`, a genuine signed solution supplies a symmetric idempotent

\[
P^2=P,\qquad P=P^T,\qquad P\bar R=0,\qquad \operatorname{diag}P=1,
\]

of rank 15.

Conversely, center-lifting

\[
N=\operatorname{center}(P+\bar H)
\]

and imposing the two capacities recovers the complete integer signed equations.

## Caveats

The bare projector conditions are not contradictory. The archived note contains an explicit finite-field countermodel satisfying the projector axioms but failing the integer capacities.

A special lifting family is excluded in the note, but no exhaustiveness claim is made.

The ternary representation is therefore exact and useful, but not a completed C2 proof.
