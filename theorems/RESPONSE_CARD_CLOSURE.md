# Response-card boundary experiment · closure result

The raw fresh-session derivation is preserved in [`../archive/RESPONSE_CARD_RAW.md`](../archive/RESPONSE_CARD_RAW.md).

## Intended compression

For a completed-row set `S`, a candidate row `y`, and a remaining label `z`, the experiment defined four response cards

\[
W_z^S(c),\qquad c\in\{n,d,m,p\},
\]

recording exactly what choosing `c_yz=c` contributes to row counts, coordinate balances, and pair-composition debts against all rows in `S`.

The equivalence relation was

\[
z\sim_{S,y}z'\iff W_z^S(c)=W_{z'}^S(c)\quad\forall c.
\]

The abstract derivation found

\[
z\sim_{S,y}z'\iff r_z=r_{z'}\text{ and }c_{xz}=c_{xz'}\ \forall x\in S.
\]

Thus a type is simply a root together with its complete relation history to `S`.

## Concrete C2 correction

In the actual Conway C2 model, the 42 positive `D7` roots

\[
e_i+e_j,\quad e_i-e_j
\]

are all distinct.

Therefore

\[
r_z=r_{z'}\Longrightarrow z=z'.
\]

So in the concrete model the response-card classes are already singleton identities at `S=empty` (after excluding the candidate `y`).

The raw note's later threshold `|S|>=22` is valid for a generalized system permitting repeated root labels, but it is unnecessary for the actual C2 root set.

## Verdict

The response-card boundary is exact for one-step attachment but is not a compressed global state.

Its exact residual update law is valid bookkeeping, but retaining the type already retains label identity.

**Route status: CLOSED as a global compression mechanism.**
