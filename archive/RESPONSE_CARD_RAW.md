## Verdict: **B — identity explosion**

The response-card boundary is exact for one-step attachment, but it does **not** remain a compressed state. Its equivalence classes are simply progressively longer labelled relation histories, and the native pair-composition law forces them to become singleton identities. No search-tree enlargement is needed.

I did not develop the known \\(D\\)-pair/\\(\zeta\\) equations further, and the receipt-ledger branch is closed.

---

## 1. Exact response card and exact equivalence relation

Let \\(S\subset L\\) be the set of already completed rows, let \\(y\notin S\\) be the candidate row to attach, and put

\\[ R\_{S,y}=L\setminus(S\cup\\{y\\}). \\]

For \\(z\in R\_{S,y}\\) and a prospective choice \\(c=c\_{yz}\\), define

\\[ W_z^S(c) = \left( \begin{array}{c} {\bf1}\_{c=d}\\\ {\bf1}\_{c\in\\{m,p\\}}\\\ (q(c)m_z(a))\_{a=1}^7\\\ (s(c)r_z(a))\_{a=1}^7\\\ (q(c\_{xz})q(c),\\,s(c\_{xz})s(c))\_{x\in S} \end{array} \right). \\]

These are exactly the contributions of \\(z\\) to the row counts, the two coordinate-balance systems, and the pair-composition debts between \\(y\\) and each \\(x\in S\\). The definitions use only the native \\(q,s\\) values and the stated exact rules.    Texte collé    Texte collé    Texte collé

Now take the equivalence requested:

\\[ z\sim\_{S,y}z' \iff W_z^S(c)=W\_{z'}^S(c) \quad\forall c\in\\{n,d,m,p\\}. \\]

There is an exact characterization:

\\[ \boxed{ z\sim\_{S,y}z' \iff r_z=r\_{z'} \ \text{and}\ c\_{xz}=c\_{xz'}\quad\forall x\in S. } \\]

### Proof

Take only the card for \\(c=p\\).

Because \\(q(p)=s(p)=1\\), its signed-coordinate component is exactly

\\[ r_z. \\]

Thus equality of the two cards gives \\(r_z=r\_{z'}\\).

For each \\(x\in S\\), its pair component is exactly

\\[ (q(c\_{xz}),s(c\_{xz})). \\]

But

\\[ n\mapsto(0,0),\quad d\mapsto(2,0),\quad m\mapsto(1,-1),\quad p\mapsto(1,1) \\]

is injective. Hence

\\[ c\_{xz}=c\_{xz'}. \\]

The converse is immediate.

So the response-card type is simply

\\[ \boxed{ \tau_S(z) = \bigl(r_z,\\;(c\_{xz})\_{x\in S}\bigr). } \\]

An important side observation is that the equivalence relation itself does **not depend on \\(y\\)**; \\(y\\) merely gets removed from the available-label set.

---

# 2. Exact \\(t(S,y)\\)

Therefore

\\[ \boxed{ t(S,y) = \\#\left\\{ \bigl(r_z,(c\_{xz})\_{x\in S}\bigr): z\notin S\cup\\{y\\} \right\\}. } \\]

For the smallest partial states:

| fixed rows            | exact value                                                   |
| --------------------- | ------------------------------------------------------------- |
| \\(S=\varnothing\\)   | \\(\\#\\{r_z:z\neq y\\}\\)                                    |
| \\(S=\\{x\\}\\)       | \\(\\#\\{(r_z,c\_{xz}):z\neq x,y\\}\\)                        |
| \\(S=\\{x_1,x_2\\}\\) | \\(\\#\\{(r_z,c\_{x_1z},c\_{x_2z}):z\notin S\cup\\{y\\}\\}\\) |
| general \\(S\\)       | number of distinct history signatures \\(\tau_S(z)\\)         |

The supplied finite-system statement does not enumerate the 42 fixed \\(r_z\\)'s, so a numerical value for these first few rows cannot be extracted without importing additional data. That is not needed for the diagnostic, because the composition axioms alone force eventual complete separation.

---

# 3. Equal-root labels are forcibly distinguished

This is the decisive step.

Suppose

\\[ r_z=r\_{z'}. \\]

Then

\\[ k\_{zz'}=2,\qquad h\_{zz'}=2. \\]

Put \\(c_0=c\_{zz'}\\). The pair-composition targets become

\\[ U=2-q(c_0) \\]

and

\\[ V=s(c_0)-2. \\]

Every possible intermediate contribution \\((Q,S)\\) satisfies

\\[ |S|\le Q, \\]

because the only possibilities in the native system are

\\[ (0,0),\\;(4,0),\\;(2,0),\\;(1,1),\\;(1,-1). \\]

&#x20;  Texte collé

Hence necessarily

\\[ |V|\le U. \\]

Check the four direct states:

\\[ \begin{array}{c|cc} c_0&U&V\\\ \hline n&2&-2\\\ d&0&-2\\\ m&1&-3\\\ p&1&-1 \end{array} \\]

Therefore

\\[ \boxed{c\_{zz'}\in\\{n,p\\}.} \\]

`d` and `m` are impossible.

Moreover in both surviving cases

\\[ |V|=U. \\]

So equality in \\(|S|\le Q\\) must occur for **every positive intermediate contribution**. The only allowed positive contribution with equality and negative sign is

\\[ (1,-1). \\]

Thus every common active intermediary sees \\(z,z'\\) through opposite signed states.

---

## Case \\(c\_{zz'}=n\\)

The targets are

\\[ (U,V)=(2,-2). \\]

Hence exactly two of the other 40 labels are active toward both \\(z\\) and \\(z'\\), and at each of those two labels their states are one \\(m\\), one \\(p\\).

Because \\(z,z'\\) are null-related, each has all of its 11 non-null relations among those 40 labels:

\\[ 1\ d+10\ \text{signed}=11. \\]

Their active-set intersection has size 2. Therefore the active symmetric difference has size

\\[ 11+11-2(2)=18. \\]

Those 18 labels certainly distinguish \\(z,z'\\), and the two common active labels also distinguish them because one relation is \\(m\\) and the other \\(p\\).

Therefore

\\[ \boxed{20} \\]

of the 40 other rows distinguish an equal-root null pair.

Only 20 agree.

---

## Case \\(c\_{zz'}=p\\)

Now

\\[ (U,V)=(1,-1). \\]

There is exactly one common active intermediary, again with opposite signs.

Since the mutual \\(p\\)-edge already consumes one of each endpoint's ten signed relations, each endpoint has

\\[ 10 \\]

active relations among the remaining 40 labels.

Thus the active symmetric difference has size

\\[ 10+10-2=18. \\]

The unique common active intermediary also distinguishes the pair.

Therefore

\\[ \boxed{19} \\]

of the 40 other rows distinguish an equal-root \\(p\\)-pair.

Only 21 agree.

---

# 4. Forced singleton threshold

We have proved:

\\[ r_z=r\_{z'},\quad z\neq z' \quad\Longrightarrow\quad \\#\\{x\neq z,z':c\_{xz}=c\_{xz'}\\}\le21. \\]

But two equal-root labels have the same response-card type precisely when

\\[ c\_{xz}=c\_{xz'} \quad\forall x\in S. \\]

Therefore, once

\\[ |S|\ge22, \\]

\\(S\\) cannot lie entirely inside their agreement set.

So equal-root labels are separated.

Different-root labels were already separated by the \\(r_z\\) component.

Hence:

\\[ \boxed{ |S|\ge22 \quad\Longrightarrow\quad \text{every remaining response-card type is a singleton}. } \\]

Consequently

\\[ \boxed{ t(S,y)=41-|S|, \qquad |S|\ge22. } \\]

At \\(|S|=22\\), for example,

\\[ t(S,y)=19 \\]

for 19 remaining labels: **zero compression**.

This is not a heuristic tendency. It is forced by the exact native equations.

---

# 5. Exact refinement law: why the explosion occurs

Suppose an old type \\(\tau\\) has multiplicity \\(n\_\tau\\).

When \\(y\\) is attached, let

\\[ n\_{\tau,c} = \\#\\{z:\tau_S(z)=\tau,\ c\_{yz}=c\\}. \\]

Then

\\[ \sum_c n\_{\tau,c}=n\_\tau. \\]

The new type is literally

\\[ \boxed{\tau'=(\tau,c).} \\]

So the new multiplicities are

\\[ \boxed{ n'\_{(\tau,c)}=n\_{\tau,c}. } \\]

Every new completed row simply appends another symbol to the history word:

\\[ (r_z,c\_{x_1z},\ldots,c\_{x_sz}) \longrightarrow (r_z,c\_{x_1z},\ldots,c\_{x_sz},c\_{yz}). \\]

Thus the native transition law exists, but it is a **refinement law**, not a compression law.

There is no mechanism merging states back together.

---

# 6. Is the multiset of response-card types itself Markovian?

No—not by itself.

For a current candidate \\(y\\), the cards tell us what each possible choice **pays**. We must also retain what remains **owed**.

Define the residual demand \\(\rho_y^S\\) by

\\[ d_y^S = 1-\\#\\{x\in S:c\_{xy}=d\\}, \\]\\[ g_y^S = 10-\\#\\{x\in S:c\_{xy}\in\\{m,p\\}\\}, \\]

and for each coordinate \\(a\\),

\\[ Q\_{y,a}^S = \begin{cases} 2,&m_y(a)=1\\\ 4,&m_y(a)=0 \end{cases} - \sum\_{x\in S}q(c\_{xy})m_x(a), \\]\\[ B\_{y,a}^S = -\sum\_{x\in S}s(c\_{xy})r_x(a). \\]

For each \\(x\in S\\), also retain

\\[ U\_{xy}^S = 4-k\_{xy}-q(c\_{xy}) - \sum\_{\substack{u\in S\\\u\neq x}} q(c\_{xu})q(c\_{uy}), \\]\\[ V\_{xy}^S = s(c\_{xy})-h\_{xy} - \sum\_{\substack{u\in S\\\u\neq x}} s(c\_{xu})s(c\_{uy}). \\]

Then current one-step attachment is determined exactly by

\\[ \boxed{ \bigl(\\{n\_\tau\\},\rho_y^S\bigr). } \\]

The raw multiset \\(\\{n\_\tau\\}\\) alone omits the right-hand side of the equations it is supposed to satisfy.

---

## 7. Minimal persistent augmentation for one more attachment

For arbitrary future candidates, the natural sufficient datum is:

\\[ \boxed{ \text{each type }\tau \text{ together with its common residual vector }\rho\_\tau^S. } \\]

If a member \\(z\\) of type \\(\tau\\) receives state \\(c=c\_{yz}\\) when \\(y\\) is added, its residual vector updates exactly as follows.

Row debts:

\\[ d'\_z=d_z-{\bf1}\_{c=d}, \\]\\[ g'\_z=g_z-{\bf1}\_{c\in\\{m,p\\}}. \\]

Coordinate debts:

\\[ Q'\_{z,a}=Q\_{z,a}-q(c)m_y(a), \\]\\[ B'\_{z,a}=B\_{z,a}-s(c)r_y(a). \\]

For every old \\(x\in S\\),

\\[ U'\_{xz}=U\_{xz}-q(c\_{xy})q(c), \\]\\[ V'\_{xz}=V\_{xz}-s(c\_{xy})s(c). \\]

The newly created pair debt against \\(y\\) is

\\[ U\_{yz} = 4-k\_{yz}-q(c) - \sum\_{x\in S}q(c\_{yx})q(c\_{xz}), \\]\\[ V\_{yz} = s(c)-h\_{yz} - \sum\_{x\in S}s(c\_{yx})s(c\_{xz}). \\]

So **type + residual demand has a completely exact native update law**.

The split table \\(n\_{\tau,c}\\) is the information specifying the chosen attachment move; after that move, the next multiplicities and residuals are determined.

---

# Conclusion

The response-card experiment gives a clean negative result:

\\[ \boxed{\text{the quotient is exact but not compressive}.} \\]

Its types are

\\[ (r_z,\text{relation history to }S), \\]

each newly attached row refines those histories, and pair composition guarantees that any two labels sharing the same root disagree on at least 19 of the other 40 rows.

Therefore

\\[ \boxed{ t(S,y)=41-|S| \quad\text{for every valid state with }|S|\ge22. } \\]

So this representation should be **killed as a candidate global boundary compression**. The useful residue of the experiment is narrower: it gives an exact native residual-update law, but retaining it eventually amounts to retaining individual labels rather than a bounded family of boundary types.