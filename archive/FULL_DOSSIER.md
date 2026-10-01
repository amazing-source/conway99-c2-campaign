# C2 reconstruction investigation — one-file review copy

Compiled 30 September 2026 from the supplied proof notes and the new handoff exposition. Written derivations remain subject to independent review. This is not a proof of existence or nonexistence. The three older proof notes below are retained in full, including their original status language. The shorter signed proof does not depend on the older unsigned proof.

For executable files and byte provenance use the full ZIP. The independent-review starting point is `REVIEWER_BRIEF.md`.

## Contents

1. Orientation and status — `README.md`
2. Theorem catalogue — `THEOREMS.md`
3. Notation — `NOTATION.md`
4. Current complete proof — `PROOF_CURRENT.md`
5. Full graph reconstruction — `GRAPH_RECONSTRUCTION.md`
6. Dependency graph — `DEPENDENCIES.md`
7. Mathematical development record — `DISCOVERY_RECORD.md`
8. Open obligations and implications — `OPEN_OBLIGATIONS_AND_IMPLICATIONS.md`
9. Independent reviewer brief — `REVIEWER_BRIEF.md`
10. Audit status and limitations — `AUDIT_STATUS_AND_LIMITS.md`
11. Source provenance — `PROVENANCE.md`
12. Original first proof, preserved in French — `originals/c2_reconstruction_2026_09_30/PREUVE_RELEVEMENT_FR.md`
13. Original unsigned uniqueness proof — `originals/c2_unique_completion_2026_09_30/UNIQUE_DOUBLE_MATCHING.md`
14. Original real-linear completion proof — `originals/c2_linear_completion_2026_09_30/LINEAR_COMPLETION.md`
15. Original research journal — `originals/c2_reconstruction_2026_09_30/JOURNAL.md`


---

# Part 1: Orientation and status

Source file within this handoff: `README.md`.

# Conway 99 · C2 reconstruction theorem dossier

**Version:** 1.0 · **Assembled:** 30 September 2026 · **Language of the new handoff:** English.

## What this package is

A self-contained record of the completion-theorem investigation: exact hypotheses, three successive proof notes, a consolidated proof of the latest theorem, detailed graph reconstruction, mathematical development history, executable checks, and a precise description of what remains unproved.

**Status: research arguments with written proofs, not independently certified theorems.** None of the supplied results has a recorded independent mathematical review or Lean verification in these materials. No claim of literature priority is made. The checks are bounded implementation and algebra checks, not an exhaustive search for Conway graphs.

**This package does not prove that a Conway graph exists or that C2 is empty.**

## The result to review first

Fix the 42 labelled exterior orbits, the signed label matrix R, and a COMPLETE matrix N satisfying

\[
N=N^T,\quad N_{uu}=0,\quad N_{uv}\in\{0,\pm1\},\qquad
NR=0,\quad N^2=N+12I_{42}-RR^T.
\]

Set

\[
B=|N|,\quad T=2J_{42,7}-M-\tfrac12 BM,\quad M=|R|,
\]
\[
E=\tfrac12(8I_{42}+4J_{42}-MM^T-B^2-B).
\]

Let L_N be the following system for a REAL matrix D:

\[
D=D^T,\quad D\ge0,\quad D_{uu}=0,\quad D\mathbf1=\mathbf1,
\]
\[
D_{uv}=0\text{ whenever }B_{uv}=1,\qquad DM=T,\qquad BD+DB+D=E.
\]

**Claim for independent review:** L_N is either empty or contains exactly one matrix, and in the latter case that matrix is an integral perfect matching. No binary constraint or equation D²=I is imposed in L_N.

A feasible solution therefore reconstructs a genuine 99-vertex graph with the prescribed involution. The theorem DOES NOT say that any suitable N with a feasible completion exists.

## The remaining existence question

\[
\mathsf{P}:\quad \exists N\text{ satisfying the complete signed equations with }L_N\ne\varnothing.
\]

| What is established later? | What it would imply |
|---|---|
| The reconstruction theorem survives review | This reformulation is valid; it does not decide P. |
| One explicit valid N with feasible L_N is found | Reconstruct and directly verify a Conway 99-graph with an involution; this settles Conway existence positively. |
| Every admissible N has infeasible L_N | C2 is excluded. Extending that conclusion from the normalized one-fixed-point model to all involutions uses the separate fixed-point input described below. |
| The reconstruction theorem is false or its proof has a gap | This proof/reduction needs repair. Neither graph existence nor nonexistence follows merely from that failure. |

**C2 false does not mean Conway false:** an asymmetric Conway graph could still exist. C3 and the other automorphism exclusions are not used to prove the completion theorem.

## Reading order

1. [THEOREMS.md](THEOREMS.md): exact theorem catalogue, scopes, and implications.
2. [PROOF_CURRENT.md](PROOF_CURRENT.md): the latest signed real-linear theorem, with every lemma written out.
3. [GRAPH_RECONSTRUCTION.md](GRAPH_RECONSTRUCTION.md): explicit 99×99 construction, all block identities, and the boundary of the fixed-point assumption.
4. [DEPENDENCIES.md](DEPENDENCIES.md): proof dependency graph and missing arrows.
5. [OPEN_OBLIGATIONS_AND_IMPLICATIONS.md](OPEN_OBLIGATIONS_AND_IMPLICATIONS.md): what review must establish and what would actually decide C2.
6. [REVIEWER_BRIEF.md](REVIEWER_BRIEF.md): a ready-to-use independent-review brief.

For the mathematical development sequence and older arguments, read [DISCOVERY_RECORD.md](DISCOVERY_RECORD.md) and the three complete original proof notes under `originals/`.

## Original material preserved

- `originals/c2_reconstruction_2026_09_30/`: affine parity completion; historical at-most-two result; original code, controls, and journal.
- `originals/c2_unique_completion_2026_09_30/`: stronger UNSIGNED uniqueness argument; 33-similitude, support classification, and the 32-versus-28 incidence contradiction.
- `originals/c2_linear_completion_2026_09_30/`: SIGNED real-linear integrality and uniqueness argument; parity/trace contradiction and half-integral defect.

These directories were extracted without changing their files. Older notes retain their original wording and theorem labels. Their status must be read with the qualifications above. The latest signed theorem does NOT supersede the unsigned theorem on every input: the unsigned theorem has weaker hypotheses but addresses only integral completions.

The new exposition follows the supplied proofs. Added explanatory expansions—especially the nine even-sector block calculations—are labelled as editorial derivations for review, not as independently verified results. See [PROVENANCE.md](PROVENANCE.md).

## Normalization boundary

The completion theorem is a finite matrix theorem, independent of any lattice classification. Its positive reconstruction direction directly builds a graph whose involution fixes one vertex.

The reverse reduction from EVERY graph with an involution uses the project input:

> Every involution of an srg(99,14,1,2) fixes exactly one vertex.

This input is cited in the supplied project material; its full external proof is not contained in the three completion archives. It must be separately verified before claiming the all-involutions equivalence. No source gap is silently replaced by an assumption of symmetry.

## Run the checks

Python, NumPy, and SymPy are required for the full suite. No SAT/LP service, cloud account, or repository credentials are used.

```bash
python -m pip install -r requirements.txt
python code/verify_manifest.py
python code/run_checks.py
```

The check runner works on temporary copies of the original scripts so that archived outputs are not overwritten. It reproduces the two small positive controls, the synthetic parity tests, and the explicit negative controls. It also checks the expanded reconstruction code on the positive controls and rejects deliberately corrupted inputs.

To test a supplied candidate N, rather than generate candidates:

```bash
python code/complete_candidate.py candidate_N.json --output completion_result.json
```

To check a claimed 99-vertex graph directly:

```bash
python code/verify_witness.py --graph candidate_A.json
```

An invalid input, exception, or audit discrepancy is NOT an exclusion. See [code/README.md](code/README.md).

## Scope in one sentence

**This dossier explains why the last completion of a fully valid signed core is exact and rigid; it does not yet explain why no such signed core can have a valid completion.**



---

# Part 2: Theorem catalogue

Source file within this handoff: `THEOREMS.md`.

# Exact theorem catalogue

## Status convention

**WRITTEN DERIVATION — REVIEW REQUIRED** means a proof is supplied, not that an independent reviewer or proof assistant has verified it. **PROJECT INPUT** means it is used from the supplied earlier project material and is not re-proved here. **OPEN TARGET** means no proof or witness is supplied.

This catalogue does not upgrade any historical “PROVED” or “DERIVED HERE” label to independent certification.

## Definitions shared by the statements

Let C be the set of two-element subsets of {1,…,7}, and Ω=C×{+,−}. Fix R and M exactly as in [NOTATION.md](NOTATION.md). Thus |Ω|=42.

Define 𝒩 to consist of matrices N satisfying

\[
N\in\mathbb Z^{42\times42},\quad N=N^T,\quad N_{uu}=0,\quad
N_{uv}\in\{0,\pm1\},\quad NR=0,\quad N^2=N+12I_{42}-RR^T. \tag{S}
\]

For N∈𝒩 put B=|N|. An **integral completion** is a symmetric binary matrix D with zero diagonal, D1=1, B∘D=0, such that Q=B+2D satisfies

\[
QM=4J_{42,7}-2M,\qquad Q^2+Q=12I_{42}+4J_{42}-MM^T. \tag{O}
\]

Here B∘D is entrywise multiplication. For such D, symmetry and the row-sum condition imply D²=I.

Define T and E, and the real feasible set L_N, by

\[
T=2J_{42,7}-M-\tfrac12 BM,\qquad
E=\tfrac12(8I_{42}+4J_{42}-MM^T-B^2-B),
\]
\[
L_N=\{D\in\mathbb R^{42\times42}:D=D^T,\ D\ge0,\ D_{uu}=0,
\ D\mathbf1=\mathbf1,\ B\circ D=0,\ DM=T,\ BD+DB+D=E\}.
\]

All symbols and quantifiers refer to a COMPLETE N, not a prefix or a modular skeleton.

## F0 · Fixed-point normalization input

**PROJECT INPUT.** Every involution of an srg(99,14,1,2) fixes exactly one vertex.

The supplied audit and earlier project notes attribute this to prior work. Its external proof is not reproduced in the three completion archives. The current completion theorem does not depend on F0 as an abstract matrix theorem. F0 is required for the claim that the normalized model exhausts ALL involutions.

The consequences of F0—local negation, the D7 labels, and the double matching—are expanded in [GRAPH_RECONSTRUCTION.md](GRAPH_RECONSTRUCTION.md).

## T0 · Exact normalized graph model

**WRITTEN DERIVATION — REVIEW REQUIRED.** There exists a labelled 99-vertex SRG with an involution fixing exactly one vertex if and only if some N∈𝒩 has an integral completion D.

For such a pair set

\[
Q=|N|+2D,\qquad a=\tfrac12(Q-N),\qquad b=\tfrac12(Q+N).
\]

The exterior adjacency is H=[[a,b],[b,a]]. The remaining incidences are specified by R and the seven interior edges. This yields a binary symmetric 99×99 adjacency of degree 14 satisfying A_Γ²+A_Γ=12I+2J. Conversely a graph in this normalized class provides such N,D.

**What it does not say:** not every N∈𝒩 necessarily has a completion.

**Sources:** original reconstruction note §1; original linear note §7. Expanded verification: [GRAPH_RECONSTRUCTION.md](GRAPH_RECONSTRUCTION.md).

## T1 · At most ten matching parameters; affine binary completion

**WRITTEN DERIVATION — REVIEW REQUIRED.** For N∈𝒩, target-cell tests and reciprocal-partner tests either exclude a completion or reduce all possible D to at most ten binary variables. The remaining integral equations are exactly unary pins and pairwise XOR constraints.

The partner cell is determined by DM=T. Components with two choices are K_(2,2), each consuming two entire cells. There are only 21 cells. Using D²=I, equation (O) becomes BD+DB+D=E. Each entry depends on at most two parameters and has an explicitly affine Boolean truth table.

**What it implies:** completion of a supplied complete N is a small exact problem; it is not a bound on the number of N matrices.

**Sources:** original reconstruction note §§2–4; current proof §§4–6.

## T2 · Historical intermediate bound: at most two completions

**WRITTEN DERIVATION — REVIEW REQUIRED; weaker signed conclusion superseded by T4.** For N∈𝒩, there are at most two integral completions. If there are two, they differ on exactly eight ambiguous blocks.

The difference space yields X²+X=8I and an integral r×r matrix Z with ZZ^T=33I. Entry counts give 5≤r≤10 and the mod-3 form argument gives 4|r, hence r=8. Hamming distance then excludes three completions.

**Scope:** this implication starts with TWO completions; it cannot be used to exclude one graph. T3 later rules out that remaining alternative. Keeping T2 records how the argument developed.

**Source:** original reconstruction note §§5–7, preserved in full.

## T3 · Unsigned completion uniqueness

**WRITTEN DERIVATION — REVIEW REQUIRED.** Let B be ANY symmetric binary 42×42 matrix with zero diagonal and row sum ten. Fix M as above. There is at most one integral D, disjoint from B, satisfying (O) with Q=B+2D.

This statement DOES NOT assume the existence of a signed N with |N|=B. It is consequently not subsumed, on arbitrary unsigned inputs, by T4.

Its proof eliminates the T2-style two-completion difference space: support constraints on Z force |A_0|=K_(4,4); restoring the original seven-block incidence permits at most four affected cells through each block, whereas sixteen two-element cells require 32 incidences. This contradicts 7×4=28.

**What it does not say:** it does not exclude a unique completion and does not assert integrality of the real relaxation for arbitrary unsigned B.

**Source:** `originals/c2_unique_completion_2026_09_30/UNIQUE_DOUBLE_MATCHING.md`, full §§1–7.

## T4 · Exact real-linear completion, integrality, and uniqueness

**WRITTEN DERIVATION — REVIEW REQUIRED.** For every N∈𝒩,

\[
L_N=\varnothing\quad\text{or}\quad L_N=\{D\},
\]

where in the second case D is an integral perfect matching. Thus the real-linear feasible set contains no fractional solution and no nontrivial segment.

The proof uses the additional signed parity Bχ≡0 mod 2, obtained from NR=0. A half-integral feasible point would create a nonzero invariant space of whole-cell differences on which X²+X=8I. Parity forces tr X=0 while irreducibility over Q forces tr X<0.

**What it implies:** real feasibility is an exact existence test for the last completion, once N is complete.

**What it does not imply:** no member of 𝒩 has yet been shown to give a nonempty L_N, and universal emptiness has not been established.

**Source:** original linear note §§1–7; consolidated proof [PROOF_CURRENT.md](PROOF_CURRENT.md). T4 does not use T2 or T3.

## T5 · Decision-exact equivalence

**WRITTEN DERIVATION FROM T0 AND T4 — REVIEW REQUIRED.** For the normalized one-fixed-point class,

\[
\exists(\Gamma,\sigma)\quad\Longleftrightarrow\quad
\exists N\in\mathcal N:\ L_N\ne\varnothing. \tag{EX}
\]

Under F0, this is equivalent to existence of any Conway-99 graph with an involution.

For a fixed labelled N, a feasible solution reconstructs at most one labelled graph in the prescribed root convention. This is not uniqueness of a Conway graph over all N, and not a graph-isomorphism classification.

## P · The remaining existence statement

**OPEN TARGET, NOT A THEOREM ALREADY ESTABLISHED.**

\[
\mathsf P=\bigl[\exists N\in\mathcal N:\ L_N\ne\varnothing\bigr].
\]

- A witness for P gives a genuine Conway graph after reconstruction and exact verification. The positive direction does not need F0: it explicitly supplies a one-fixed-point involution.
- A proof of ¬P excludes the normalized C2 model. Combined with F0, it excludes all involutions.
- Even after all involutions are excluded, graph nonexistence does not follow: the asymmetric branch may remain.
- Proving T4 correct does not prove P. Refuting T4 does not prove ¬P.

## What must be reviewed independently first

Check T4 and the explicit reconstruction T0, including F0's status for the reverse reduction. T2 and T3 are supplied for completeness and their own independent interest, but are not prerequisites for T4. All theorem-specific assumptions must be retained.



---

# Part 3: Notation

Source file within this handoff: `NOTATION.md`.

# Notation and index conventions

All norms mentioned in the historical notes are squared Euclidean norms unless explicitly stated otherwise. The current matrix theorem does not require any norm-minimum hypothesis.

| Symbol | Size / definition | Meaning |
|---|---|---|
| Γ, A_Γ | 99 vertices; 99×99 adjacency | The original graph and its full adjacency matrix. |
| σ, P_σ | involution; 99×99 permutation | The prescribed symmetry. |
| x | one vertex | The unique fixed vertex, when the external normalization input is invoked. |
| i,j | 1,…,7 | Interior blocks/lines through x. |
| c={i,j} | i<j | A cell: a two-element subset of the seven blocks. There are 21 cells. |
| u=(c,+) or (c,−) | 42 indices | An EXTERIOR ORBIT label. Each label represents two actual graph vertices. |
| p_u, σp_u | two vertices per u | Representative and its image. This sign is different from the cell-label sign. |
| R | 42×7 | Rows r_(c,+)=e_i+e_j and r_(c,−)=e_i−e_j. |
| M=|R| | 42×7 | Cell-incidence matrix, with each cell row repeated twice. Absolute values are entrywise. |
| a,b | 42×42, binary | a_uv=A_Γ(p_u,p_v), b_uv=A_Γ(p_u,σp_v). |
| N=b−a | 42×42, signed | The complete exterior signed core. Some older project sources use S_out=−N. |
| B=|N| | 42×42, binary | Support of single orbit adjacencies. NOT the full exterior adjacency. |
| D | 42×42 | The double matching; in the linear relaxation it is initially real, not assumed integral. |
| Q=B+2D | 42×42 | Ordinary exterior orbit quotient, entries 0,1,2 when valid. |
| T | 42×7 | T=2J_(42,7)−M−BM/2; target cell-incidence rows. |
| E | 42×42 | E=(8I+4J−MM^T−B²−B)/2; linear matching right side. |
| χ | length 42 | χ_(c,+)=1 and χ_(c,−)=0. One selected ORBIT index per cell. |
| J_(p,q), J_p | p×q; p×p | All-ones matrices. These are not matching operators. |
| 1_p | length p | All-ones column. |
| g_c | length 42 | e_(c,+)−e_(c,−), a difference of the TWO ORBIT INDICES within one cell. |
| L, P_L | subspace of R^42; 42×42 projector | Span of selected whole-cell differences, and its orthogonal projector. |
| X | dim L square | B restricted to L, expressed in the equally normed g_c basis. |
| J_0 | dim L square | Restriction of one matching in the older two-completion proof; not an all-ones matrix. |
| A_0,C_0,Z | r×r | Auxiliary matrices in the older 33-similitude argument; older originals call A_0 simply A. |
| t_i | scalar | A matching choice, binary in the parity theorem and in [0,1] in the real relaxation. |
| s | integer ≤10 | Number of ambiguous K_(2,2) partner components after target tests. |
| r | integer in the older comparison | Number of ambiguity blocks where TWO matchings differ, not a rank or a root count. |
| H | 84×84 | Exterior adjacency [[a,b],[b,a]], all representatives first, then their images. |
| S_- | 49×49 | Odd action [[−I_7,R^T],[R,−N]]. |
| A_+ | 50×50 | Action on orbit-constant functions; not symmetric in the unnormalized basis. |
| L_N | feasible set / linear system | The real completion constraints for a FIXED complete N. |
| 𝒩 | finite set | All complete N satisfying the displayed signed equations. |

## Three objects that must not be confused

A cell contains **two orbit labels**, and each orbit label contains **two graph vertices**. Thus:

- 21 cells = 42 exterior orbits = 84 exterior vertices;
- one ambiguous K_(2,2) partner block uses two cells = four orbit indices = eight graph vertices;
- the historical r=8 alternative would affect 16 cells =32 orbits =64 exterior vertices.

A graph root r∈D_7, a lattice root of squared norm 2, and an exterior graph vertex were all called “roots” in some project notes. The current dossier uses explicit labels instead.

## Identities fixed by these conventions

\[
R^TR=12I_7,\quad M\mathbf1_7=2\mathbf1_{42},\quad
M^T\mathbf1_{42}=12\mathbf1_7,\quad M^TM=10I_7+2J_7,
\]
\[
R\mathbf1_7=2\chi,\qquad J_{42,7}M^T=2J_{42}.
\]

The last identity is important: Q M=4J_(42,7)−2M implies
QMM^T=8J_42−2MM^T, not 48J_42−2MM^T.

## No implicit simplifying assumptions

None of the current proofs assumes N_(c,+;c,−)=0, t_cd=0, min K≥2, an extra automorphism, or a known embedding in one of the 156 rank-24 or nine rank-17 lattices. Labels are fixed and canonical; arbitrary orbit sign-switches must also change R consistently.



---

# Part 4: Current complete proof

Source file within this handoff: `PROOF_CURRENT.md`.

# Consolidated proof: real-linear completion is exact

**Status:** source-based mathematical derivation for independent review. This is a consolidated exposition of `originals/c2_linear_completion_2026_09_30/LINEAR_COMPLETION.md`, with elementary steps expanded. It is not a new independent verification and does not assert that C2 is empty.

The original file is preserved unchanged. The previous at-most-two and unsigned-uniqueness arguments are not prerequisites for this proof.

## 1. Fixed data and theorem

Let C=binom({1,…,7},2), and Ω=C×{+,−}. Order cells lexicographically, with + before − in each cell. For c={i,j}, i<j, set

\[
r_{c,+}=e_i+e_j,\qquad r_{c,-}=e_i-e_j.
\]

Let R have these 42 rows and put M=|R|, entrywise. Let χ have entry 1 at (c,+) and 0 at (c,−).

Assume N is a complete 42×42 matrix satisfying

\[
N=N^T,\quad \operatorname{diag}N=0,\quad N_{uv}\in\{0,\pm1\},
\]
\[
NR=0,\qquad N^2=N+12I_{42}-RR^T. \tag{S}
\]

Define

\[
B=|N|,\quad T=2J_{42,7}-M-\frac12BM,
\]
\[
E=\frac12(8I_{42}+4J_{42}-MM^T-B^2-B).
\]

For D real, impose

\[
D=D^T,\quad D\ge0,\quad \operatorname{diag}D=0,\quad D\mathbf1=\mathbf1,
\]
\[
B\circ D=0,\qquad DM=T,\qquad BD+DB+D=E. \tag{L}
\]

Let L_N be the feasible set of (L).

**Theorem T4.** L_N is empty or a singleton whose member is an integral perfect matching. In particular D²=I and all D entries are 0 or 1 in the feasible case, although neither condition is imposed in (L).

## 2. Label identities and parity

### Lemma 2.1 · Label identities

\[
R^TR=12I_7,\quad M\mathbf1_7=2\mathbf1_{42},\quad
M^T\mathbf1_{42}=12\mathbf1_7,\quad M^TM=10I_7+2J_7,
\]
\[
R\mathbf1_7=2\chi.
\]

**Proof.** A block belongs to six cells, each represented twice, giving each diagonal of R^TR and M^TM the value 12. For distinct i,j, the two signed rows belonging to {i,j} contribute +1 and −1 to R^TR, hence cancel. The same two rows contribute 2 to M^TM. Each row of M has exactly two ones. Finally the coordinate sum of e_i+e_j is 2 and that of e_i−e_j is 0. ∎

### Lemma 2.2 · Consequences for B, T, E

\[
B\mathbf1=10\mathbf1,\quad B\chi\equiv0\pmod2,\quad BM\equiv0\pmod2,
\]
\[
B^2+B\equiv MM^T\pmod2.
\]

In particular T,E are integral, and T1_7=2·1_42.

**Proof.** At a diagonal entry of (S),

\[
\sum_vN_{uv}^2=12-r_u\cdot r_u=10.
\]

Because every nonzero N entry has square 1, this is the row-sum assertion for B. Also
N R1_7=2Nχ=0 as an integer equality, so Nχ=0. Since N≡B mod 2, Bχ is even. Reducing NR=0 modulo 2, with R≡M, gives BM even. Reducing the other signed equation gives B²=B+MM^T in characteristic two, as claimed. Thus the numerators defining T,E are even. Finally,

\[
T\mathbf1_7=14\mathbf1-2\mathbf1-\tfrac12B(2\mathbf1)
=2\mathbf1.
\]

No graph, lattice, or matching has been assumed in these deductions. ∎

## 3. The cell-difference obstruction

This lemma supplies the contradiction in the real-linear proof. Its hypotheses are essential.

### Lemma 3.1

Let B be symmetric binary with zero diagonal, indexed by two-index cells, and let χ choose the + index in every cell. Suppose Bχ is even. There is no nonzero B-invariant space

\[
L=\operatorname{span}_{\mathbb R}\{g_c:c\in S\},\qquad
g_c=e_{c,+}-e_{c,-},
\]

where S is a nonempty collection of WHOLE cells, such that the restriction X=B|_L satisfies

\[
X^2+X=8I_L. \tag{3.1}
\]

**Proof.** Put the g_c in the columns of a matrix G. They are mutually orthogonal and have squared norm 2. Thus G^TG=2I. Since L is invariant there is a matrix X with BG=GX, and

\[
X=\tfrac12G^TBG,
\]

which is symmetric.

The coefficient of g_c in Bg_d is the (c,+) coordinate of Bg_d. It is an integer, so X is integral. At d=c this coefficient is

\[
X_{cc}=B_{c,+;c,+}-B_{c,+;c,-}=-B_{c,+;c,-}\in\{0,-1\}. \tag{3.2}
\]

Because χ^TG=1^T,

\[
\mathbf1^TX=\chi^TGX=\chi^TBG=(B\chi)^TG\equiv0\pmod2.
\]

The column sums, and by symmetry the row sums, of X are even. Take a diagonal entry of (3.1) modulo 2. As X is symmetric and integral,

\[
0=(X^2+X)_{cc}=\sum_dX_{cd}^2+X_{cc}
\equiv\sum_dX_{cd}+X_{cc}\equiv X_{cc}\pmod2.
\]

In view of (3.2), every diagonal entry is zero. Therefore tr X=0.

On the other hand f(t)=t²+t−8 is irreducible over Q, since its discriminant 33 is not a rational square. It has the two distinct roots α=(−1+√33)/2 and β=(−1−√33)/2. Equation (3.1) implies that all eigenvalues of X belong to {α,β}. The characteristic polynomial is rational. Applying the field conjugation √33↦−√33 shows that the multiplicities of α and β are equal. Since L is nonzero, both have a positive multiplicity a, hence

\[
\dim L=2a>0,\qquad \operatorname{tr}X=a(\alpha+\beta)=-a<0.
\]

This contradicts tr X=0. ∎

**Scope check.** The lemma does not prohibit every integral matrix satisfying X²+X=8I. The archived 33-similitude constructs such an X. Its associated binary lift fails Bχ≡0; this is why it is a valid negative control rather than a contradiction of the lemma.

## 4. What DM=T forces, even when D is fractional

Assume (L) is feasible. Do not assume D is integral.

### Lemma 4.1 · Targets are actual cells

Every row T_u is a binary vector of weight two. If D_uv>0 then M_v=T_u.

**Proof.** The row T_u=(DM)_u is a convex combination of the binary rows of M: the coefficients D_uv are nonnegative and sum to one. Every coordinate is therefore in [0,1]. By Lemma 2.2, it is also an integer, so each coordinate is 0 or 1. Its row sum is two. These are exactly the 21 distinct cell-incidence vectors.

If a coordinate of the convex combination equals 0, every positively weighted term has coordinate 0. If it equals 1, every positively weighted term has coordinate 1. Apply this to all seven coordinates: whenever D_uv>0, the whole row M_v must equal T_u. ∎

Write target(u) for the unique cell with incidence vector T_u. Symmetry then gives the reciprocal condition

\[
D_{uv}>0\Longrightarrow
\begin{cases}
u\ne v,\ B_{uv}=0,\
\operatorname{cell}(v)=\operatorname{target}(u),\
\operatorname{cell}(u)=\operatorname{target}(v).
\end{cases} \tag{4.1}
\]

### Lemma 4.2 · Only tiny partner components remain

Allowed edges satisfying (4.1) form components contained in K_2 or K_(2,2). Every feasible component is forced integral unless it is a full K_(2,2). A full K_(2,2) between two cells has the fractional form

\[
D_{c,d}=\begin{pmatrix}t&1-t\\1-t&t\end{pmatrix},\qquad0\le t\le1,
\]

and D_(d,c)=D_(c,d)^T. Distinct such components use disjoint whole cells. Their number s is at most ten.

**Proof.** Each index has one target cell. For two different cells c,d, allowed edges join only the indices in c targeting d to the indices in d targeting c. Each side has at most two indices. Different unordered target-cell pairs cannot share an index, because that index has a unique target. A within-cell component has at most the one edge between its two indices.

On a bipartite component, the sum of weights over its edges equals the number of vertices on each side, by the row sums. Hence a feasible component has equal side sizes. Size 1+1 forces its edge to have weight one. For size 2+2, the row and column sums yield the displayed parameterization. If any of the four potential edges is missing, its prescribed zero forces t to an endpoint. Otherwise all t∈[0,1] are allowed by these constraints. This full component consumes both indices of both cells; two such components cannot share a cell. Since there are 21 cells, s≤floor(21/2)=10. ∎

This argument also shows why the completion variables are not an arbitrary fractional matching on 42 vertices.

## 5. The remaining equations have only pins and equalities/complementations

### Lemma 5.1 · Classification of real entry equations

After the component parameterization, BD+DB+D=E is equivalent, over 0≤t_i≤1, to constant equations, endpoint pins t_i=0 or 1, and equations

\[
t_i=t_j\quad\text{or}\quad t_i=1-t_j.
\]

**Proof for different components.** The entry (BD)_uv depends only on the parameter of the component containing v. Its value is one of 0,1,t_j,1−t_j, because column v has either one unit entry or two entries t_j,1−t_j and B is binary. Similarly (DB)_uv is one of 0,1,t_i,1−t_i. Also D_uv=0 if the two indices lie in different components. Thus the equation is f(t_i)+g(t_j)=e, where e=E_uv is an integer.

If a function is constant, this is a constant check or a pin to 0 or 1. If both vary, the only possible integer right sides are 0,1,2. At 0 both summands must be 0; at 2 both must be 1. At 1 the equation is equality or complementation of the two parameters. No reduction modulo two has been used here.

**Proof for the same ambiguous component.** B has no entries between its two cells, since all four edges are eligible for D. Let a,b∈{0,1} be the B edges INSIDE the two cells. For an entry crossing the two cells, direct multiplication gives

\[
t+(a+b)(1-t)
\]

or the same expression with t replaced by 1−t. Its variable coefficient is 1−a−b∈{−1,0,1}, so equality to an integer is automatic, inconsistent, or an endpoint pin. Entries inside either cell and diagonal entries have constant value, since the intervening cross-cell B block is zero. Components already forced integral contribute only constants. This exhausts all entries. ∎

### Lemma 5.2 · A canonical half-integral feasible point

If the real system is feasible, there is a feasible point with each parameter in {0,1/2,1}. Moreover, if its feasible set contains a fractional or undetermined parameter, such a point can be chosen with at least one 1/2.

**Proof.** Make a relation graph whose edges are equalities or complementations and whose marked vertices have endpoint pins. In a connected component, every variable equals x or 1−x after choosing a root. A parity-consistent component with an endpoint pin has a unique 0/1 assignment. Incompatible endpoint pins make the whole system infeasible. An unpinned parity-consistent component has a free x∈[0,1]. An unpinned parity-inconsistent cycle imposes x=1−x and hence x=1/2. A parity-inconsistent component with an endpoint pin is infeasible.

In every free component choose x=1/2. All fixed endpoint components remain integral and all remaining components have parameter 1/2. If all components were fixed endpoint components, the feasible solution was already a unique binary point. ∎

**Important distinction.** An odd XOR cycle has no binary solution but does have the real solution 1/2 until the graph-origin lemma is used. The integrality proof must not assume it away.

## 6. A half-valued component creates an exact projector defect

Let D̄ be the canonical point from Lemma 5.2. Suppose it contains at least one half-parameter. Let S contain both cells of every half-parameter block, and define

\[
L=\operatorname{span}\{g_c:c\in S\},\qquad
P_L=\frac12\sum_{c\in S}g_cg_c^T.
\]

### Lemma 6.1 · Defect identities

\[
\bar D^2=I-P_L,\qquad\bar D P_L=P_L\bar D=0.
\]

**Proof.** A half block has off-diagonal block (1/2)J_2. It kills each of its two cell-difference vectors. On the two cell-sum vectors it swaps the cells and its square is identity. Equivalently, the square of the full 4×4 half block is diag(J_2/2,J_2/2), which is the orthogonal projector onto the two cell-sum directions. Its complement is exactly the sum of the two cell-difference projectors. All other components are integral matching edges with square identity. The components are disjoint, proving the global formulas. ∎

Set Q̄=B+2D̄. Then

\[
\bar Q M=4J_{42,7}-2M,
\]
\[
\bar Q^2+\bar Q=12I+4J-MM^T-4P_L. \tag{6.1}
\]

**Derivation.** The first equation follows from BM+2T=4J−2M. For the second,

\[
\bar Q^2+\bar Q
=B^2+B+2(B\bar D+\bar D B+\bar D)+4\bar D^2
=8I+4J-MM^T+4(I-P_L).
\]

### Lemma 6.2 · The defect space is B-invariant

**Proof.** B1=10·1 and D̄1=1 imply Q̄1=12·1. Since Q̄ is symmetric, it commutes with J_42. Also

\[
\bar Q MM^T=(4J_{42,7}-2M)M^T=8J_{42}-2MM^T.
\]

This expression is symmetric. Transposing therefore gives MM^TQ̄ equal to the same expression: Q̄ commutes with MM^T.

Every matrix commutes with its own polynomial. Take the commutator with Q̄ on both sides of (6.1). All terms except P_L already commute, hence [Q̄,P_L]=0. Lemma 6.1 gives [D̄,P_L]=0, so [B,P_L]=0. Therefore L is B-invariant. ∎

Each cell has two identical rows in M, so M^Tg_c=0, and 1^Tg_c=0 as well. Thus J and MM^T vanish on L. On L, D̄=0, hence Q̄=B. Restricting (6.1) yields

\[
(B|_L)^2+(B|_L)=8I_L.
\]

But L is a nonempty span of whole-cell differences, and Bχ is even by Lemma 2.2. Lemma 3.1 gives a contradiction. Therefore the canonical point has no half-parameter.

## 7. Conclude integrality and uniqueness

A free component could have been set to 1/2; an unpinned odd parity cycle would force 1/2. Both have been ruled out. Every component in the relation graph of a feasible system is therefore fixed to endpoints. There is exactly one solution in the parameter domain, with all parameters 0 or 1.

The forced components are integral too. Thus D is a symmetric binary row-stochastic matrix with zero diagonal. Every row has exactly one 1. Symmetry gives the same for columns and pairs its nonzero entries reciprocally; consequently D is a fixed-point-free involutory permutation matrix and D²=I. This proves Theorem T4. ∎

## 8. Consequence for the graph

If the feasible set is nonempty, use its D to set Q=B+2D. The calculation in §6 now has P_L=0, so Q satisfies the exact ordinary-sector equations. Define

\[
a=(Q-N)/2,\quad b=(Q+N)/2.
\]

On a B edge, Q=1 and N=±1, so a,b are 0 and 1 in one order. On a D edge, N=B=0 and Q=2, so a=b=1. Elsewhere both vanish. Therefore they are binary symmetric matrices with zero diagonal. Together with the fixed incidence labels they give the explicit graph in [GRAPH_RECONSTRUCTION.md](GRAPH_RECONSTRUCTION.md).

Conversely an integral valid completion satisfies (L) by expansion with D²=I. Thus real feasibility is exactly graph-completion feasibility for the normalized model.

## 9. Where this argument stops

The proof excludes a nonempty HALF-VALUED defect L. For a genuine integral matching D, that defect is zero. Lemma 3.1 then has no nonzero space to which it can be applied. Nothing above creates a contradictory nonzero space from a unique integral completion.

The existence statement remains

\[
\exists N\in\mathcal N:\ L_N\ne\varnothing.
\]

Its negation is the universal infeasibility target. This dossier does not supply it. The theorem also does not generate N or make the constraints quadratic in N become linear: B=|N| and B² occur in the coefficients.

## 10. Audit checkpoints

Every significant step can be reviewed independently in order:

1. Fixed canonical labels give R1=2χ; arbitrary representative switches cannot leave R frozen.
2. Signed equations make Bχ and BM even and T,E integral.
3. Invariance of L gives an integral symmetric restriction X with diagonal 0 or −1.
4. The parity/trace lemma really needs WHOLE cells and Bχ even.
5. Fractional support is forced by endpoints of convex combinations, not an integrality assumption.
6. All entry equations, including within an ambiguity block, have only the listed forms.
7. Real odd-parity cycles are retained as half-solutions before they are contradicted.
8. D̄²=I−P_L is exact and depends on choosing the canonical 0,1/2,1 point.
9. J_(42,7)M^T=2J_42 gives the coefficient 8 in the commutator calculation.
10. The final contradiction eliminates half-values, not the unique integral case.
11. The reconstruction must check every block of the 99×99 SRG identity.
12. The all-involutions reverse reduction separately needs the fixed-point input F0.



---

# Part 5: Full graph reconstruction

Source file within this handoff: `GRAPH_RECONSTRUCTION.md`.

# From (N,D) to the full 99-vertex graph, and back

**Status:** detailed editorial expansion of the reconstruction in the original parity note §1 and linear note §7, for independent review. The original sources gave the action matrices and stated the blockwise verification. Here the block calculations and graph vertex order are explicit. This is not a record of an independent review.

The positive construction is self-contained. The reverse implication for ALL C2 objects has one external project dependency: the one-fixed-point theorem F0.

## 1. Original target

A C2 object is a pair (Γ,σ) where Γ is a simple strongly regular graph with parameters (99,14,1,2) and σ is a nonidentity involutory automorphism.

For its adjacency A_Γ and permutation P_σ, the target conditions are

\[
A_\Gamma=A_\Gamma^T\in\{0,1\}^{99\times99},\quad
\operatorname{diag}A_\Gamma=0,\quad A_\Gamma\mathbf1=14\mathbf1,
\]
\[
A_\Gamma^2+A_\Gamma=12I_{99}+2J_{99},
\]
\[
P_\sigma^2=I,\quad P_\sigma\ne I,\quad A_\Gamma P_\sigma=P_\sigma A_\Gamma.
\]

For distinct vertices, the SRG matrix identity says there is one common neighbour for an edge and two for a nonedge. On the diagonal it says the degree is 14.

## 2. Normalization used in the reverse reduction

### F0 · External input

> Every involution of an srg(99,14,1,2) fixes exactly one vertex.

The supplied project notes use this as an established, externally sourced result. The three completion archives do not contain its full proof. The matrix theorem T4 is independent of it. A universal exclusion of the normalized matrices becomes an exclusion of ALL involutions only after F0 is separately secured.

### Consequences of F0, written out

Assume a graph Γ and involution σ, with Fix(σ)={x}.

For each y∈N(x), the number of neighbours of y inside N(x) is λ=1. Hence the graph induced on N(x) is a 1-regular graph on 14 vertices: seven disjoint edges. Label them {i^+,i^-}, i=1,…,7.

There are 84 other vertices. Each has exactly two neighbours in N(x), by μ=2 applied to it and x. These neighbours cannot be in the same interior edge, because that adjacent pair already has x as its unique common neighbour. Conversely, two vertices a,b in different interior blocks are nonadjacent and have exactly two common neighbours, one being x. Their other common neighbour is outside N(x): inside N(x), every vertex has only its one matched neighbour. Thus exterior vertices are in bijection with cross-block signed pairs {i^α,j^β}. There are 4·binom(7,2)=84 such pairs.

Now σ preserves N(x). If it exchanged two interior vertices a,b in different blocks, it would preserve the unordered pair {a,b}, and hence fix their unique exterior common neighbour. That contradicts Fix(σ)={x}. It has no fixed interior vertex, so it must swap the two endpoints of every interior edge. Thus σ(i^+)=i^- and, by uniqueness of exterior labels, σ changes BOTH signs of every exterior label.

For each cell c={i,j}, i<j, choose representatives p_(c,+) labelled {i^+,j^+} and p_(c,−) labelled {i^+,j^-}. Their images have both signs reversed. These are the canonical R rows.

No exterior vertex p is adjacent to σp. Otherwise their edge's unique common neighbour is σ-fixed, hence x; but x is not adjacent to an exterior vertex. Thus a_pp=b_pp=0.

For exterior p, the two common neighbours of p and σp form a σ-invariant set of size two. It contains no fixed vertex and no interior vertex, since the interior labels of p and σp are disjoint. It is consequently one exterior orbit {q,σq}. By symmetry and μ=2, q and σq in turn have exactly {p,σp} as their common neighbours. This supplies a perfect matching D on the 42 exterior orbits, recording their double adjacencies.

Each exterior vertex has degree 14, two interior neighbours, and hence 12 exterior neighbours. One orbit supplies two neighbours; all other adjacent orbits supply one. There are ten such single adjacencies, so B has row sum ten.

## 3. Extract N and D from a normalized graph

For representatives p_u and p_v put

\[
a_{uv}=A_\Gamma(p_u,p_v),\quad b_{uv}=A_\Gamma(p_u,\sigma p_v),
\]
\[
N=b-a,\quad B=|N|,\quad D_{uv}=a_{uv}b_{uv},\quad Q=a+b=B+2D.
\]

All products a_uv b_uv in this paragraph are scalar entrywise products. The ordinary matrix product ab is not meant.

The automorphism and undirected graph imply a,b symmetric. The diagonal is zero by the previous argument. With the fixed R,M labels, the action of the adjacency on σ-odd functions is

\[
S_-=\begin{pmatrix}-I_7&R^T\\R&-N\end{pmatrix}.
\]

The all-ones matrix acts as zero on these functions. Hence the full SRG identity gives S_-²+S_-=12I_49. Its off-diagonal and lower-right blocks yield exactly

\[
NR=0,\quad N^2=N+12I_{42}-RR^T.
\]

On σ-even functions, the action matrix is the A_+ displayed in §6. Its lower-right and lower-middle block identities yield (O). This proves the graph-to-matrix implication for the normalized class.

## 4. Construct the graph from a matrix pair

Conversely, assume N satisfies (S) and D is an integral completion satisfying (O). The real-linear theorem T4 supplies such an integral D whenever L_N is feasible, but the construction in this section only uses its explicitly checkable integral properties.

Order the 99 vertices as follows:

\[
x;\quad 1^+,\ldots,7^+;\quad1^-,\ldots,7^-;
\quad p_1,\ldots,p_{42};\quad \sigma p_1,\ldots,\sigma p_{42}.
\]

Define the 42×7 binary matrices

\[
R_+=(M+R)/2,\qquad R_-=(M-R)/2,
\]

and the 42×42 matrices

\[
a=(Q-N)/2,\qquad b=(Q+N)/2,\qquad Q=B+2D.
\]

The interior adjacency and interior–exterior incidence are

\[
F=\begin{pmatrix}0&I_7\\I_7&0\end{pmatrix},\qquad
K=\begin{pmatrix}R_+^T&R_-^T\\R_-^T&R_+^T\end{pmatrix}.
\]

The exterior adjacency is

\[
H=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]

Finally set

\[
A_\Gamma=
\begin{pmatrix}
0&\mathbf1_{14}^T&0\\
\mathbf1_{14}&F&K\\
0&K^T&H
\end{pmatrix}. \tag{4.1}
\]

### Binary entries and simplicity

If B_uv=1, N_uv=±1 and D_uv=0, so (a_uv,b_uv) is (0,1) or (1,0). If D_uv=1, B_uv=N_uv=0, so a_uv=b_uv=1. Otherwise both vanish. Their diagonals are zero. R_+,R_- are binary by the explicit signed row definitions. Therefore (4.1) is binary symmetric with zero diagonal.

### Degrees

The fixed vertex sees 14 interior vertices. Each interior vertex sees x, its mate, and 12 exterior vertices, by M^T1_42=12·1_7. Each exterior vertex sees two interior vertices and (a+b)1=Q1=(10+2)1=12 exterior vertices. Every degree is 14.

### Automorphism

Let P_σ fix x and swap the two interior layers and the two exterior layers. The displayed block forms give P_σ²=I, P_σ≠I, and A_ΓP_σ=P_σA_Γ. Its only fixed vertex is x.

## 5. Verify every σ-odd block of the SRG identity

Use the subspace of functions with value zero at x, opposite values on i^+,i^-, and opposite values on p_u,σp_u. The action matrix is S_- as in §3. Compute:

\[
(S_-^2+S_-)_{\mathrm{inner,inner}}
=I_7+R^TR-I_7=12I_7,
\]
\[
(S_-^2+S_-)_{\mathrm{inner,outer}}
=-R^T-R^TN+R^T=-R^TN=0,
\]
\[
(S_-^2+S_-)_{\mathrm{outer,inner}}=-NR=0,
\]
\[
(S_-^2+S_-)_{\mathrm{outer,outer}}
=RR^T+N^2-N=12I_{42}.
\]

Hence A_Γ²+A_Γ=12I on the 49-dimensional odd space. This is the full target identity there because J_99 kills every odd function.

## 6. Verify every σ-even block

Represent an even function by its value at x, its seven common interior-orbit values, and its 42 common exterior-orbit values. The action matrix is

\[
A_+=
\begin{pmatrix}
0&2\mathbf1_7^T&0\\
\mathbf1_7&I_7&M^T\\
0&M&Q
\end{pmatrix}.
\]

This basis is not orthonormal; A_+ need not be symmetric. The restriction of J_99 is

\[
J_+=\mathbf1_{50}(1,2\mathbf1_7^T,2\mathbf1_{42}^T),
\]

because an orbit-constant function's sum is its value at x plus twice every other orbit value. The target identity is A_+²+A_+=12I_50+2J_+.

All nine blocks are as follows; J in a block denotes the all-ones matrix of that block's size.

| Block | Computation of A_+²+A_+ | Target |
|---|---|---|
| x,x | 2·7 | 14 |
| x,inner | 2·1_7^T+2·1_7^T | 4·1_7^T |
| x,outer | 2·1_7^TM^T=2(M1_7)^T | 4·1_42^T |
| inner,x | 1_7+1_7 | 2·1_7 |
| inner,inner | 2J_7+2I_7+M^TM | 12I_7+4J_7 |
| inner,outer | 2M^T+M^TQ | 4J_(7,42) |
| outer,x | M1_7 | 2·1_42 |
| outer,inner | 2M+QM | 4J_(42,7) |
| outer,outer | MM^T+Q²+Q | 12I_42+4J_42 |

The inner–outer calculation uses the transpose of QM=4J−2M. These blocks are precisely 12I_50+2J_+.

The even and odd spaces are complementary and have dimensions 50 and 49. The target operator vanishes on each, hence on all of R^99. Thus the constructed A_Γ satisfies the complete SRG identity.

## 7. What a positive witness must include

An explicit N with a feasible completion is enough mathematically after the theorem is verified. For an independently checkable computational witness, publish N and either D or the final A_Γ; ideally publish all three with the index convention.

A direct verifier should check finite integer equalities, not a numerical spectrum:

1. A_Γ is 99×99, binary, symmetric, and has zero diagonal.
2. All row sums are 14.
3. A_Γ²+A_Γ=12I+2J exactly.
4. The displayed P_σ is a permutation, involutory, nonidentity, and commutes with A_Γ.
5. When supplied, N,D satisfy the signed and ordinary equations and agree with the reconstruction.

The code in this package implements these checks. There is no claimed m=7 witness in the package. The m=2 and m=11 test graphs are positive controls of related formulas, not examples of Conway 99.

## 8. Logical consequences

A positive verified A_Γ settles the entire Conway existence problem positively, and also establishes existence in C2. It does not need C3 or the rank-17/24 reductions.

A proof that NO normalized pair N,D exists excludes one-fixed-point involutions. Together with F0 this excludes every involution. It does not exclude graphs with no involution; in particular it does not eliminate the asymmetric branch.

If T4 failed, an explicit integral N,D could still be verified by this construction directly. Failure of the real-linear theorem is not, by itself, evidence either for or against graph existence.



---

# Part 6: Dependency graph

Source file within this handoff: `DEPENDENCIES.md`.

# Dependency graph and missing implications

Arrows mean “is used to prove,” not “is equivalent to.” All newly derived nodes retain review-required status.

## A. Latest proof: shortest dependency path

```text
Fixed canonical R,M,χ + COMPLETE signed equations (S)
   │
   ├── row count B1=10; BM even; T,E integral
   │       │
   │       └── feasible DM=T, D≥0, D1=1
   │               └── targets are actual cells
   │                       └── disjoint tiny matching components
   │                               └── at most 10 parameters t∈[0,1]
   │                                       └── entry equations = pins/equality/complementation
   │                                               └── canonical 0,1/2,1 feasible point
   │                                                       │
   │                                                       └── a half component would give
   │                                                           D̄²=I−P_L, D̄P_L=0
   │                                                               └── ordinary equation with defect −4P_L
   │                                                                   └── commutators force B-invariance of L
   │                                                                       └── X²+X=8I on whole-cell differences
   │                                                                                           │
   └── NR1=2Nχ=0 ⇒ Bχ even                                                                     │
           └── restriction X has even row sums                                                 │
                   └── X²+X=8I, diag X∈{0,−1} ⇒ tr X=0                                        │
                           └── irreducibility of t²+t−8 ⇒ tr X<0                                │
                                   └────────────────────────────── CONTRADICTION ◀──────────────┘

No half components ⇒ no free components ⇒ every feasible D is unique and integral  [T4]
   └── binary a,b + explicit interior incidence
           └── odd and even block verification
                   └── genuine 99-vertex graph with the prescribed involution [T0 positive]
```

Neither the 156-lattice classification nor the rank-17 classification is a node in this proof.

## B. Older branch, preserved but not needed by T4

```text
TWO integral completions of the same unsigned B,M
  └── difference supported on r ambiguity blocks, 1≤r≤10
      └── B-invariant cell-difference space, dim=2r
          └── X²+X=8I, XJ_0+J_0X=−J_0
              ├── entry counts ⇒ r≥5
              └── ZZᵀ=33I_r ⇒ 4|r
                      └── r=8
                          ├── Hamming distance ⇒ at most two completions [historical T2]
                          └── support classification ⇒ |A_0|=K_(4,4)
                              └── original block incidence ⇒ at most four cells through a block
                                  └── 32 required incidences > 28 available
                                      └── unsigned integral uniqueness [T3]
```

T3 has no signed hypothesis. T4 has the signed hypothesis and additionally proves real integrality. This distinction prevents an invalid inference of real integrality for arbitrary unsigned B.

## C. Link to C2 and exact missing arrow

```text
A graph with an involution                         [original C2 existence]
   │
   └── F0: unique fixed vertex                     [external project input]
           └── normalized graph labels and exact matrices
                   └── N∈𝒩 and D∈L_N             [necessity]

N∈𝒩 and D∈L_N
   └── T4                                         [written proof, review needed]
           └── D integral
                   └── explicit graph             [constructive sufficiency]

UNPROVED:
   (S) for an arbitrary N ── ? ──> L_N is always infeasible

If that missing implication is proved:
   normalized C2 does not exist
       + F0 ⇒ no Conway graph admits an involution
```

## D. What is NOT a missing implication

The following implications are not valid goals to assume silently:

- “there is at most one completion” ⇒ “there is none”;
- “the theorem is correct” ⇒ “there exists a valid N”;
- “the theorem is incorrect” ⇒ “there is no graph”;
- “a partial skeleton is feasible” ⇒ “a complete N exists”;
- “all sampled N/prefixes fail” ⇒ “all N fail”;
- “completion is linear for fixed N” ⇒ “the joint N,D problem is linear”;
- “no involution” ⇒ “no Conway graph.”

## E. Review priority

The shortest path to validating the current result is T4 → explicit reconstruction. Review F0 separately for the global reverse implication. The longer unsigned branch can be checked independently and must not be used to conceal an unverified step in the shorter signed proof.



---

# Part 7: Mathematical development record

Source file within this handoff: `DISCOVERY_RECORD.md`.

# Mathematical development record

This is a mathematical account of how the argument developed, grounded in the three supplied proof notes, the original research journal, and the conclusions stated in the conversation. It records the definitions, intermediate deductions, failed extensions, and scope corrections. It is not an assertion that every undocumented exploratory thought has been archived.

Full older proofs are retained, not replaced by this summary. The newest theorem's complete derivation is in [PROOF_CURRENT.md](PROOF_CURRENT.md).

## Stage 0 · Separate the signed core from its completion

The initial question was whether a complete signed core N might still leave a prohibitively large lifting problem. The known exact model splits exterior adjacencies into a,b, with N=b−a and Q=a+b. The missing doubles are encoded by D through Q=|N|+2D.

A key distinction was maintained: a COMPLETE N satisfying its quadratic equations is not a partial frame, a few stars, a choice of binary skeleton ρ, or a lattice selected from a finite list. The difficulty of generating the complete N is upstream of this investigation.

The original project script `extend_s_to_q.py` already determined the partner cell from block sums and then enumerated matchings. That observation is credited to the earlier project, not presented as a discovery of the subsequent notes. The exact historical repository/path/commit is listed in [PROVENANCE.md](PROVENANCE.md).

## Stage 1 · Determine the domain of D before solving for it

The block equation gives

\[
DM=2J-M-\frac12BM.
\]

Every right-side row fixes a partner CELL. Reciprocity confines matching edges to subgraphs of K_(2,2) between two cells, or to the one edge inside a cell. Each fully ambiguous component consumes two whole cells; there can be at most ten.

This changed the description from “a matching on 42 points” to “at most ten binary choices after local target tests.” The number of complete signed candidates was not reduced by this observation.

**Full proof:** original parity note §2; current proof §4.

## Stage 2 · Turn the ordinary quadratic equation into a linear matching equation

For an integral matching D²=I. Expanding Q²+Q then gives

\[
BD+DB+D=\frac12(8I+4J-MM^T-B^2-B).
\]

At a matrix entry only the components containing its two indices appear. The Boolean solutions are unary pins and XOR relations. The result is an exact small affine binary system, not a generic quadratic matching search.

**Critical qualification:** D²=I justified the expansion for integral matchings at this stage. It was not legitimate to assume D²=I for fractional matrices. The later proof addresses that distinction explicitly.

**Full proof:** original parity note §§3–4; current proof §5 distinguishes real from binary relations.

## Stage 3 · Compare two possible completions

Suppose D_1≠D_2 complete the same support. Their difference is supported on whole-cell differences. If r ambiguity blocks change, the difference space has dimension 2r, with 1≤r≤10.

The difference of the linear equations forces invariance under B, with restricted operators X and J_0 satisfying

\[
XJ_0+J_0X=-J_0,\qquad X^2+X=8I.
\]

The entry restrictions imply r≥5 and permit the block form

\[
X=\begin{pmatrix}A_0&C_0\\-C_0&-I-A_0\end{pmatrix},
\]

where A_0 is symmetric, C_0 antisymmetric, both with zero diagonal. Therefore

\[
A_0^2+A_0-C_0^2=8I,\quad A_0C_0=C_0A_0,
\]
\[
Z=I+2A_0+2C_0\quad\Longrightarrow\quad ZZ^T=33I_r.
\]

The determinant and mod-3 isotropic-subspace argument force 4|r; hence r=8. Three binary solutions would have pairwise Hamming distance eight among at most ten coordinates, which is impossible. This produced the first at-most-two theorem.

**Logical origin of 33:** it is 1+4·8, from completing the square in the restricted operator. It is not an independently imposed number-theoretic hypothesis.

**Full proof:** original parity note §§5–7.

## Stage 4 · Check the arithmetic intermediate object instead of declaring it impossible

The equation ZZ^T=33I_8, even with the relevant A_0,C_0 entry conditions, has an explicit solution. That solution is archived in the structural check output and source.

Thus a claimed contradiction from the 33-similitude ALONE would be false. The admissible arithmetic object was retained as a negative control, so any stronger obstruction had to use additional hypotheses genuinely inherited from the graph.

This is an example of an auxiliary construction that EXISTS, not a Conway witness. Its role is to prevent overextending a lemma.

## Stage 5 · Restore the original seven-block incidence

The next proof used the entry pattern of Z to classify its support. Every row has one magnitude-four entry and four magnitude-two entries. The magnitude-four positions form directed cycles; together with the symmetric magnitude-two support and mutual zeros they partition K_8 into a 2-factor P, a 4-regular graph F, and a perfect matching H.

Parity of the matrix equations forces every P edge to lie in exactly one triangle of G=P∪H and every H edge to lie in zero or two. This yields P=2C_4 and then |A_0|=K_(4,4).

The sixteen difference coordinates are still sixteen actual two-element subsets of SEVEN blocks. For a block, its incidence indicator t on those cells satisfies

\[
(|X|+2I+2J_0)t\le4\mathbf1.
\]

The structure forces |t|≤4. Summing over seven blocks permits at most 28 incidences; sixteen two-element cells require 32. Thus two completions are impossible.

**What changed:** arithmetic consistency did not guarantee compatibility with the original cell-incidence interpretation.

**What did not change:** this contradiction still starts with TWO completions. It cannot be applied to a graph merely because it has one completion.

**Full proof:** original unsigned uniqueness note §§3–7, including the hand support classification and capacity lemma.

## Stage 6 · Recover a simpler signed parity

For the canonical R,

\[
R\mathbf1=2\chi,\quad NR=0\Longrightarrow N\chi=0\Longrightarrow B\chi\equiv0\pmod2.
\]

On a B-invariant space of whole-cell differences, this parity makes the restriction X have even row sums. If X²+X=8I, its diagonal must then be zero. But the irreducible polynomial t²+t−8 forces equal multiplicities of the conjugate eigenvalues and a strictly negative trace. Contradiction.

This is a shorter mechanism under STRONGER hypotheses: it uses the signed N. It does not independently prove the arbitrary-unsigned theorem, which is why both arguments remain in the dossier.

**Full proof:** current proof §§2–3; original linear note §§2–3.

## Stage 7 · Attack fractional completions of one signed candidate

To move beyond comparison of two graphs, the equation was studied with real nonnegative D, symmetry, row sums one, support constraints, DM=T, and the linear matching equation—but WITHOUT D²=I.

Integrality of T forces the same tiny matching components by convexity. Every entry equation is a pin, equality, or complementation. Thus a nonempty real feasible set has a canonical point with parameters 0,1/2,1.

An odd parity cycle is not prematurely rejected: over the reals it supplies the half-solution. Free components can also be assigned 1/2.

This moved the question from “could two integral completions exist?” to “could ONE signed candidate have a fractional solution without a graph?”

## Stage 8 · Fractionality has a precisely located defect

For the canonical half-point D̄,

\[
\bar D^2=I-P_L,
\]

where L is the nonzero span of exactly the whole-cell differences in half-components. Expanding with this ACTUAL square, rather than substituting I, gives

\[
\bar Q^2+\bar Q=12I+4J-MM^T-4P_L.
\]

Commutation with J and MM^T forces Q̄, then B, to preserve L. On L the equation becomes X²+X=8I. Stage 6 rules it out. Therefore there is no half-component, free component, or fractional solution. Every feasible completion is unique and integral.

**Full proof:** current proof §§4–7.

## Stage 9 · Reconstruct all 99 vertices, not merely a quotient

A feasible completion gives binary a=(Q−N)/2 and b=(Q+N)/2. The fixed R rows specify the interior incidences. The even and odd action equations then recover the full SRG identity.

The supplied originals state this step. This handoff expands every block calculation, supplies a fixed vertex order, and includes a direct verifier. These additions are review aids; they do not establish a new C2 witness.

## Stage 10 · Locate the remaining gap without changing quantifiers

The theorem is

\[
\forall N\in\mathcal N:\quad L_N\text{ is empty or a singleton integral point}.
\]

The still-open nonexistence target is

\[
\forall N\in\mathcal N:\quad L_N=\varnothing.
\]

The former does not imply the latter. A real graph would supply exactly the integral solution the theorem still allows. No residual half-defect exists in that case.

The proposed “uniqueness forces extra symmetry” shortcut also stops: uniqueness implies equivariance under symmetries already present, not existence of a nontrivial symmetry.

## What the work did NOT establish

No complete m=7 signed core was constructed. No open lattice envelope or rank-17 pair was newly excluded by these completion notes. No universal family of linear infeasibility certificates was produced. No result says that infinite creativity guarantees a short proof, or that a large computation is mathematically necessary.

The recorded progression is: **domain compression → affine completion → uniqueness → real exactness → explicit reconstruction**. It is not a completed nonexistence argument.



---

# Part 8: Open obligations and implications

Source file within this handoff: `OPEN_OBLIGATIONS_AND_IMPLICATIONS.md`.

# What remains to be done, and what each outcome would mean

## 1. Two tasks, not one

**Task A: validate the reconstruction theorem.** Verify T4 and the exact graph reconstruction without relying on the author's confidence, the labels in the notes, or the absence of search survivors.

**Task B: decide the existence statement**

\[
\mathsf P:\quad\exists N\in\mathcal N\text{ with }L_N\ne\varnothing.
\]

Task A supplies a correct characterization. It does not answer Task B.

## 2. Exact review obligations

### A1. Check the matrix theorem under its actual assumptions

The reviewer should either establish every lemma of `PROOF_CURRENT.md` or identify the first failure with a counterexample or a missing hypothesis. The delicate steps are target convexity, the classification of ALL within-component entry equations, the canonical half-point, the defect commutator, and the rational trace argument.

The theorem is not about a fractional relaxation with an arbitrary guessed support. It requires the complete signed equations for N, with canonical labels R. Treating it as a statement for partial N or arbitrary B would change its hypotheses.

### A2. Check graph reconstruction block by block

Verify that the output adjacency is binary, symmetric, diagonal-zero, degree 14, and satisfies A²+A=12I+2J on both invariant subspaces. The even quotient has a weighted all-ones operator, not the unweighted 50×50 all-ones matrix.

### A3. Check the all-involutions normalization separately

The backward implication from any C2 graph to this normalized model uses F0: the involution has exactly one fixed vertex. The complete external proof is not included in these archives. The sources' attribution is not a substitute for checking that input. This does not affect verification of an explicit positive graph witness.

### A4. Separate evidence levels

The scripts test examples and algebra, not the universal proof. Re-running them with the same code is not independent mathematical verification. The original positive controls have no ambiguous matching blocks. Synthetic half-solutions test the algorithm's behavior precisely because they are not complete C2 candidates.

### A5. Establish novelty separately from truth

The partner-cell observation is already in the project script cited by the originals. The affine and integrality claims were not identified by the earlier targeted searches, but that does not establish literature novelty. A correct theorem and a new theorem are separate determinations.

## 3. What would prove C2 nonexistence via this route?

It is sufficient to prove

\[
\forall N\in\mathcal N:\quad L_N=\varnothing. \tag{U}
\]

Then a normalized C2 graph would supply a particular N∈𝒩 and an actual D∈L_N, contradicting (U). With F0 this excludes all involutions.

A stronger sufficient statement is 𝒩=∅. It would eliminate the signed cores before completion. The current materials prove neither statement.

A case split is also sufficient, but its union must be exhaustive over every N under consideration, and every case must be closed. Closing a finite selection of supports or additional-symmetry constructions is not (U).

## 4. What a linear certificate could look like

For a FIXED N, list the allowed unordered matching edges and make their nonnegative entries the vector d. All symmetry, row-sum, target-cell, and linear matching equations can be written

\[
C_Nd=b_N,\qquad d\ge0.
\]

A rational vector y satisfying

\[
C_N^Ty\ge0,\qquad b_N^Ty<0
\]

is a directly checkable infeasibility certificate: any d≥0 would give

\[
0\le d^TC_N^Ty=b_N^Ty<0.
\]

This calculation is the validity check for a certificate, not a construction of one. No universal coefficients y(N) are supplied in this package.

A uniform symbolic proof could construct suitable y(N) from the complete signed equations for every N. Alternatively a justified exhaustive computation could supply certificates across an exhaustive candidate partition. Both are possible forms of completing (U); neither has been executed here.

The dependence on N matters. B=|N| and B² appear in the right side, and BD couples unknown B and D. There is no single linear program in all unknowns whose integrality theorem has solved the whole problem.

## 5. What would prove existence?

One explicit complete N satisfying (S), with one D∈L_N, is enough after T4 and reconstruction are verified. More directly, an integral pair N,D can be reconstructed and checked without relying on the full real-integrality theorem.

The strongest positive deliverable is an explicit 99×99 binary adjacency with the exact finite identities verified. It establishes an srg(99,14,1,2) and an involution. Therefore it proves Conway existence, not just a promising quotient or relaxed frame.

An abstract nonconstructive proof of P would establish existence as a mathematical statement, but an explicit adjacency requires obtaining the witness N,D. “P is true” should not be described as an adjacency file already in hand unless those data have actually been supplied.

## 6. Outcome table

| Event | Legitimate conclusion | Illegitimate conclusion |
|---|---|---|
| T4 is independently verified | The stated completion relaxation is exact for every complete N satisfying (S). | “A suitable N exists.” |
| T4 is refuted | This proof/reformulation must be repaired or restricted. | “C2 is false” or “C2 is true.” |
| An admissible N has infeasible L_N | That particular signed core cannot produce a graph. | “All signed cores fail.” |
| A complete N has feasible L_N | Under T4 it yields an integral D; reconstruction yields a graph. | “A partial skeleton with similar invariants is enough.” |
| A candidate A passes exact 99-vertex verification | Conway existence is established positively by that witness. | “The uniqueness theorem alone constructed it.” |
| All N in an exhaustive class have infeasible L_N | That class is eliminated. | “The unclassified remainder is eliminated too.” |
| (U) is proved and F0 secured | No Conway graph has an involution. | “No Conway graph exists.” |
| A solver times out or a script crashes | No conclusion from that attempt. | “Infeasible.” |
| A run is complete on its input | Its precise stated input domain was processed. | “The input domain necessarily covers all C2.” |

## 7. Where the present proof mechanism stops

The contradiction tr X=0 and tr X<0 is produced by a HALF-VALUED component. If the completion is a unique integral matching, D²=I and the defect projector vanishes. There is no nonzero L to which that argument automatically applies.

Likewise the earlier contradiction 32>28 starts with TWO completions. A genuine graph only needs one. These conditional contradictions are useful rigidity results but cannot have their antecedents deleted.

The next genuinely nonexistence-directed lemma must derive a contradiction from a SINGLE pair N,D satisfying all exact conditions, or from a rigorously exhaustive class of such pairs. Another uniqueness lemma alone would not establish (U).

## 8. What can proceed without heavy compute?

Independent proof review, completing an omitted matrix calculation, checking a proposed universal identity, and seeking a symbolic infeasibility certificate can be mathematical tasks with no exhaustive search. Small exact computation can serve as falsification or implementation checking.

This dossier neither proves that a short non-computational obstruction exists nor that heavy computation is necessary. The unresolved issue is a missing universal implication, not a completed logical proof waiting only for processing time.

Existing Route C and rank-17 campaigns remain alternative sufficient routes if their reductions and exhaustive exclusions are fully validated. No runtime estimate, current exclusion count, or cloud-availability claim from those campaigns is established by this package.

## 9. Scope of a negative answer for Conway as a whole

C2 is the class of Conway graphs WITH an involution. A positive C2 witness is automatically a Conway graph. A negative C2 result says only that any Conway graph must lack involutions.

To infer that an eventual graph is asymmetric, one would additionally use independently established restrictions excluding every other nontrivial automorphism. To prove that no Conway graph exists, one still has to exclude the symmetry-free possibility. Neither extra conclusion follows from T4 by itself.



---

# Part 9: Independent reviewer brief

Source file within this handoff: `REVIEWER_BRIEF.md`.

# Independent review brief — start here in a fresh session

## Assignment

Independently audit the exact real-linear completion theorem T4 in this folder. Do not attempt to prove C2 nonexistence before deciding whether this theorem and its graph reconstruction are valid. Do not treat the author's “derived” labels or the supplied tests as independent verification.

No cloud launch, email, account operation, repository push, large SAT run, or paid tool is requested. Read the local files and reason from their precise assumptions. Small exact checks are permitted when they test a specified step. An exception is never an exclusion.

## Statement to audit

For c={i,j}, i<j, take two rows r_(c,+)=e_i+e_j and r_(c,−)=e_i−e_j, giving R∈Z^(42×7); M=|R|. Let N be a COMPLETE symmetric 42×42 integer matrix, diagonal zero, entries 0,±1, with

    NR=0,
    N²=N+12I−RRᵀ.

Set

    B=|N|,
    T=2J_(42,7)−M−BM/2,
    E=(8I+4J−MMᵀ−B²−B)/2.

The unknown D is REAL and must satisfy

    D=Dᵀ, D≥0, diagonal D=0, D1=1,
    D_uv=0 wherever B_uv=1,
    DM=T,
    BD+DB+D=E.

Claim: its feasible set is empty or is a singleton integral perfect matching.

A feasible D then gives Q=B+2D, a=(Q−N)/2, b=(Q+N)/2 and a reconstructed 99-vertex SRG with involution.

## Primary reading

1. `THEOREMS.md` for scope and distinction between T0–T5.
2. `PROOF_CURRENT.md` for the short signed proof.
3. `GRAPH_RECONSTRUCTION.md` for the full adjacency construction and weighted even-sector verification.
4. `AUDIT_STATUS_AND_LIMITS.md` and `checks/packaging_run.json` for what was and was not checked.

The original source proof is preserved at `originals/c2_linear_completion_2026_09_30/LINEAR_COMPLETION.md`. Compare it with the consolidated exposition rather than assuming the latter is an independently validated replacement.

The longer unsigned uniqueness proof is in its original directory. It is not needed for T4 and should not be imported to patch a gap without making the added dependency explicit.

## Required checks

A. Prove from the signed equations that B1=10·1, Bχ≡0 mod 2, T and E are integral, and T has row sum 2. χ must select the correct canonical row in every cell.

B. Prove the fractional target support claim using convex combinations. Do not presuppose D is integral. Check all allowed components, including imbalanced components and missing edges.

C. Check EVERY type of entry of BD+DB+D=E after component parameterization: distinct components, same ambiguous component, same cell, forced pairs, and diagonal. Verify that no coefficient type allowing a different interior rational value was omitted.

D. Prove the half-integral representative exists. In particular an odd parity cycle has a real half-solution and must not be rejected as though D were already binary.

E. Verify D̄²=I−P_L, commutation with MMᵀ and J, and the restriction X²+X=8I. Check the precise full-cell support of L.

F. Audit the integral restriction matrix, its diagonal 0 or −1, the even-row-sum argument, and the rational characteristic-polynomial multiplicities. The trace contradiction needs all these hypotheses.

G. Verify uniqueness of the FULL REAL feasible set, not merely integrality of one special feasible point.

H. Reconstruct the full 99×99 adjacency and verify both invariant sectors. Pay particular attention to the orbit weights in the action of J_99 on even functions.

I. Separate the external input F0 (every involution fixes exactly one vertex) from the matrix theorem. The positive reconstruction does not need the classification of all involutions; the reverse all-C2 reduction does.

J. Check that no assumption min K≥2, N_(c,+;c,−)=0, extra symmetry, or existence of a second completion entered unnoticed.

## Deliverable

Produce one of:

- **VALID AS STATED:** a stepwise verification with exact references to the hypotheses, including a separate status for F0;
- **VALID AFTER REPAIR:** the precise corrected statement and the proof of every added or changed step;
- **GAP IDENTIFIED:** the first unsupported inference, why it is unsupported, and what would repair it;
- **FALSE:** an explicit counterexample satisfying ALL stated assumptions and violating the conclusion, independently checked.

Do not label the theorem false merely because an example omitting NR=0 or the canonical cell structure violates it. Do not label it true merely because the positive controls pass.

## What a successful review would NOT prove

It would not establish that a suitable N exists, nor that all N fail. After validation the actual decision problem remains

    exists N satisfying the complete signed equations with L_N nonempty?

A positive explicit witness yields a Conway graph. A universal negative proof, with F0, excludes C2 but does not by itself exclude the asymmetric Conway case.



---

# Part 10: Audit status and limitations

Source file within this handoff: `AUDIT_STATUS_AND_LIMITS.md`.

# Audit status, source limitations, and evidence levels

## 1. The mathematical status has not been upgraded by packaging

The three notes contain written arguments. They do not report independent mathematical review or Lean verification. This handoff consolidates them, expands the graph-reconstruction calculations, and re-runs bounded checks. Those activities are not an independent referee report or a machine formalization.

No universal nonexistence certificate, complete m=7 signed core, or 99-vertex positive witness is present.

## 2. Files preserved versus exposition added

All files under `originals/` are extracted unmodified from the three supplied ZIP files. Source hashes are recorded in `source_archives.json`; package hashes are in `MANIFEST.json` and `SHA256SUMS`.

New Markdown files organize the assertions, proof dependencies, and consequences. `PROOF_CURRENT.md` follows the latest original proof with elementary expansions. `GRAPH_RECONSTRUCTION.md` expands the original action-matrix argument and labels the external F0 dependency. These are editorial mathematical derivations for review, not new external evidence.

The older `reconstruction.py` still contains its historical at-most-two assertion. It is retained as source history, not silently edited to look contemporaneous with T4. The supplied CLI wrapper treats any contradiction of the newer uniqueness claim as an AUDIT DISCREPANCY, never as an exclusion.

## 3. Fixed-point input is not proved by these archives

The supplied project audit states that a Conway involution fixes exactly one vertex and attributes this to Makhnev–Minakova. The completion archives do not include the original external proof. This handoff does not independently validate that attribution.

A reviewer can validate T4 without F0. The reduction from every possible involution to the normalized 42-orbit model additionally requires F0. Construction and direct verification of a positive 99-vertex witness do not require F0.

## 4. What the existing checks actually test

### Original reconstruction controls

The original suite constructs graphs of orders 9 and 243, checks their exact SRG identities, extracts their signed cores, and recovers their original double matchings. Both controls have zero ambiguous blocks. Thus they check conventions and reconstruction behavior, not nontrivial ambiguity in an m=7 graph.

It also compares the parity solver with every binary assignment in 500 bounded synthetic systems. These inputs do not satisfy all C2 hypotheses. Some intentionally have multiple solutions, demonstrating that the algorithm itself is not hardcoded to reject ambiguity.

### Original unsigned structural controls

The suite verifies one explicit 8×8 Z with ZZᵀ=33I, its induced A_0,C_0,X, the K_(4,4) support, the capacity bound for that example over 2^16 indicator vectors, and tiny support-matching cases. The universal support and capacity claims are proved in the note, not by that one example.

### Original linear controls

These verify signed parity on the positive controls; an abstract resonant X and binary cell lift that FAIL the required graph-origin parity; synthetic equality/complementation systems with a free interval or a forced half-point; and the half-matching defect identity.

Those synthetic countercontrols are essential scope tests, not Conway examples.

## 5. What the new packaging checks add

The check runner records its actual environment and compares reproduced original JSON outputs to the archived results. It also reconstructs whole graphs using the new explicit matrix code on the 9- and 243-vertex controls, checks permutation commutation and orbit coverage, and rejects deliberately corrupted inputs.

It does not enumerate signed 42×42 matrices, search any of the 156 lattices, access cloud resources, certify the original Route C searches, or independently prove T4. Its exact recorded result is in `checks/packaging_run.json`, not inferred from a README claim.

## 6. Original proof-status language

The originals use “PROUVÉ,” “DERIVED HERE,” and “complete mathematical proof.” These describe the author's proof claims. They are retained verbatim for provenance. The new dossier consistently distinguishes those claims from independent checking.

## 7. Mathematical caution points

- All labels must use the stated R. Orbit representative switches must transform R and N together.
- J_(42,7)Mᵀ=2J_42; the commutator calculation therefore uses 8J_42−2MMᵀ.
- The even quotient is in an unnormalized orbit-constant basis, so its J operator is weighted by orbit sizes.
- Only the real completion in D is linear. The unknown complete signed core still obeys a quadratic equation with discrete entries.
- The projector defect exists for the canonical half-solution. It vanishes for a genuine integral matching.
- The unsigned at-most-one theorem is stronger in its input generality, weaker in its conclusion about real relaxations. Do not merge their hypotheses.
- Any automated rejection must be justified by the relevant exact input equations. A timeout, failed assertion, parsing error, or discrepancy is not a mathematical no-instance.

## 8. Current nonclaims

No theorem here proves C2 empty, the existence of a graph, uniqueness of a graph over all signed cores, forced extra symmetry, a new current count of lattice exclusions, a known dollar cost to finish C2, or guaranteed termination within a practical compute budget.

No evidence in the package rules out a new uniform hand obstruction. No evidence proves that such an obstruction must be short or that the final proof must be computational.



---

# Part 11: Source provenance

Source file within this handoff: `PROVENANCE.md`.

# Provenance and source boundaries

## Source archives supplied in the conversation

| ID | Original archive | Role |
|---|---|---|
| S1 | `c2_reconstruction_2026_09_30.zip` | Affine parity completion, initial at-most-two result, reconstruction code and controls, research journal. |
| S2 | `c2_unique_completion_2026_09_30.zip` | Unsigned matching uniqueness, detailed 33-similitude and 32>28 proof, structural checks. |
| S3 | `c2_linear_completion_2026_09_30.zip` | Latest signed real-linear integrality/uniqueness proof and small checks. |

The complete extracted content of each is under `originals/`. Its bytes are unchanged. `source_archives.json` records the SHA-256 hashes of the source ZIPs, all members, and their correspondence to the extracted files. It also records the mounted standalone-note comparisons.

The three ZIPs themselves are not nested again: their full extracted contents are included. This makes the handoff directly readable without repeated unpacking.

## Conversation attachment identifiers

These identifiers document the provided source versions; they are not mathematical proof references by themselves.

- S1 proof: `file_00000000356482439651b3dbc010df69`, `PREUVE_RELEVEMENT_FR.md`.
- S1 archive: `file_000000009cb08243aed5bc12255ab63b`.
- S1 code: `file_00000000e3dc8243b611023a8b837c11`.
- S1 controls: `file_000000000fe881f4ae7350227c3a61f8`.
- S2 proof: `file_000000000e1c8210a0d38783c5adf3ca`, `UNIQUE_DOUBLE_MATCHING.md`.
- S2 archive: `file_00000000ae7481f48ecefd422dd06b81`.
- S3 proof: `file_0000000095a481f4b33cfd5c8f21e623`, `LINEAR_COMPLETION.md`.
- S3 archive: `file_00000000ba1482439d83902c526ab941`.
- S3 checks: `file_000000000f28820aa83ba49e9a0e13fb`.

## Claim-to-source map

| Material in this handoff | Source / derivation |
|---|---|
| Exact normalized matrices N,R,M,Q,D | S1 proof §1; S3 proof §1 and §7. |
| Forced partner cell; tiny components | S1 proof §2; S3 proof §4. |
| Affine binary completion | S1 proof §§3–4. |
| Real pins/equalities/complementations | S3 proof §5. |
| At most two completions; r=8 | S1 proof §§5–7. |
| Arbitrary-unsigned integral uniqueness | S2 proof §§1–7. |
| Canonical signed parity Bχ≡0 | S3 proof §2. |
| Trace obstruction on whole-cell differences | S3 proof §3. |
| Fractional defect and exact real completion | S3 proof §§5–7. |
| Explicit reconstruction formulas | S1 proof §1; S3 proof §7. All even/odd block products are expanded editorially in `GRAPH_RECONSTRUCTION.md`. |
| Mathematical development sequence | S1 `JOURNAL.md`, the three proof notes, and their stated scope transitions. |
| What remains unproved | S3 proof §§7–9 and the subsequent clarification in the conversation. |
| Historical controls | Each source archive's code and JSON output. |
| Reproduced check results and new CLI | Generated while assembling this package; recorded in `checks/packaging_run.json`. They are not independent theorem verification. |

## Known project precursor

The original notes credit the target-cell observation to:

- repository: `amazing-source/conway99-c2-experimental`;
- path: `scripts/extend_s_to_q.py`;
- commit: `609cc3bf25b11c1c7be187071d4462529ab9e384`.

Its described method computes the target cell from block sums, enumerates reciprocal matchings, and tests the ordinary equation. This handoff preserves that attribution. No fresh repository inspection or new literature-priority search was performed for the packaging task.

## Fixed-point source boundary

The earlier supplied audit `AUDIT_C2_FR.md`, §2.2, states that the unique-fixed-point input is attributed to Makhnev–Minakova and explicitly says the audit did not re-prove the external article. Its mounted source is identified in `context/F0_SOURCE_EXCERPT.md`.

That attribution is a project-source statement, not independent validation of the external theorem. The all-involutions equivalence must retain F0 as a separate dependency.

## Editorial additions, not silently inserted premises

The handoff introduces notation disambiguation, theorem IDs, a dependency diagram, a review checklist, an implications table, and a fully expanded graph-construction calculation. These are derivations and presentation additions based on the originals. No unknown N, positive Conway graph, universal infeasibility certificate, or extra symmetry is inserted.

No external web research was needed to assemble these supplied mathematical materials. The package does not establish novelty, formal certification, or the current state of all project repositories.

## Integrity versus truth

A matching SHA-256 proves that the bytes match the recorded bytes. It does not prove that the mathematical arguments are correct or that a search is exhaustive. Likewise, identical program output is reproducibility evidence, not an independent proof of the theorem.



---

# Part 12: Original first proof, preserved in French

Source file within this handoff: `originals/c2_reconstruction_2026_09_30/PREUVE_RELEVEMENT_FR.md`.

# C2 — relèvement affine et rigidité à deux complétions

**30 septembre 2026. Recherche issue du retour aux axiomes du graphe.**

## Statut et portée

Les résultats ci-dessous ont une preuve mathématique complète dans cette note. Ils n'ont pas encore fait l'objet d'une relecture indépendante ou d'une formalisation Lean. Les contrôles programmatiques joints sont des contrôles, pas le fondement de la preuve.

**Résultat principal.** Fixer tous les labels et une matrice signée complète N satisfaisant les équations impaires de C2. Les complétions de N en un graphe de paramètres (99,14,1,2) avec l'involution prescrite sont décrites exactement par un système affine de parités sur au plus dix bits. Il y en a zéro, une ou deux. S'il y en a deux, leurs couplages de doubles diffèrent sur exactement huit blocs ambigus de quatre orbites, donc seize cellules et trente-deux orbites extérieures.

Il s'agit de complétions **étiquetées, avec le même N**, pas d'une borne sur le nombre de graphes à isomorphisme près ni sur l'ensemble des N possibles. Aucune nouvelle enveloppe ou classe rang-17 n'a été exclue par ce travail.

La détermination de la cellule du partenaire par les sommes de blocs existe déjà dans `scripts/extend_s_to_q.py`, dépôt `conway99-c2-experimental`, commit `609cc3bf25b11c1c7be187071d4462529ab9e384`. Le script énumère ensuite les couplages et teste l'équation quadratique de Q. Cette note ne revendique pas cette première observation. La formulation affine et la rigidité arithmétique à deux complétions n'ont pas été identifiées dans les recherches ciblées effectuées ; cela ne certifie pas leur nouveauté dans tout le corpus ou dans la littérature.

## 1. Objet exact et conventions

Les 21 cellules sont les paires non ordonnées c={i,j} de {1,...,7}. Chacune porte deux labels extérieurs c+ et c−, de vecteurs e_i+e_j et e_i−e_j, i<j. La matrice R a ces 42 vecteurs comme lignes, et M=|R|. Ainsi

- R^T R=12 I_7 ;
- chaque ligne de M contient deux 1 ;
- les deux lignes d'une cellule dans M sont identiques, et deux cellules distinctes donnent des lignes distinctes.

La matrice N est symétrique entière, de diagonale nulle, avec N_ij dans {−1,0,1}, et

    N R=0,
    N²=N+12 I_42−R R^T.                         (1)

Posons B=|N|, valeur absolue entrée par entrée. La diagonale de (1) donne B1=10 1.

Un couplage de doubles est une matrice de permutation symétrique D sans point fixe, disjointe du support de B. Le quotient ordinaire est

    Q=B+2D.

Il doit vérifier

    Q M=4 J_(42,7)−2M,                          (2)
    Q²+Q=12 I_42+4 J_42−M M^T.                  (3)

Sa somme de ligne 12 est automatique à partir de B1=10 et D1=1.

Avec (1), ces conditions sont équivalentes à la reconstruction du graphe enraciné avec l'involution prescrite. En effet, les adjacences entre représentants et leurs images sont

    a=(Q−N)/2,   b=(Q+N)/2.

Elles sont booléennes grâce aux conditions d'entrées et de disjonction. Les incidences avec le sommet fixé et les sept blocs intérieurs sont imposées par R. Sur l'espace impair, la matrice est

    S = [[−I_7, R^T], [R, −N]],

et (1) implique S²+S=12I. Sur l'espace invariant, dans la base des valeurs constantes sur chaque orbite, la matrice est

    Q_full = [[0, 2·1^T, 0],
              [1, I_7, M^T],
              [0, M, Q]].

Les identités M^T M=10I_7+2J_7 et M1=2·1, combinées à (2)–(3), donnent l'équation SRG sur tous ses blocs. Les deux espaces sont complémentaires sur R. Ainsi la matrice booléenne complète A vérifie A²+A=12I+2J, et son degré est 14. La permutation prescrite commute avec A et est une involution non triviale.

Cette preuve ne suppose ni min K≥2 ni la nullité des produits entre les deux vecteurs d'une cellule.

## 2. PROUVÉ — le graphe des partenaires possibles

De (2),

    D M=T,   T=2J_(42,7)−M−(B M)/2.             (4)

Pour chaque orbite u, T_u doit être la ligne de M de la cellule de d(u). Si T_u n'est pas une ligne de M, il n'y a aucune complétion. La ligne, lorsqu'elle existe, détermine une unique cellule cible t(u).

Construire le graphe C_N sur les 42 orbites : u et v sont reliés si et seulement si

    u≠v, B_uv=0, cell(v)=t(u), cell(u)=t(v).

Les couplages parfaits de C_N sont exactement les D satisfaisant (2), la condition de couplage et la disjonction de support.

**Structure des composantes.** Une arête reliant les cellules c,d reste dans le groupe des orbites de c ciblant d et des orbites de d ciblant c. Si c≠d, ce groupe est un sous-graphe de K_(2,2). Si c=d, il est contenu dans l'arête joignant les deux orbites de c. Des groupes de cellules différents ne partagent pas une orbite : sa cellule cible est unique.

Chaque groupe a zéro, un ou deux couplages parfaits. Deux couplages sont possibles uniquement pour le K_(2,2) complet. Après rejet des groupes sans couplage et fixation des couplages uniques, chaque K_(2,2) complet fournit un bit indépendant.

Chaque bloc ambigu utilise les deux orbites de deux cellules. Les blocs ambigus sont disjoints. Leur nombre s vérifie donc

    s ≤ floor(21/2)=10.

La condition (2) ne laisse pas un couplage arbitraire sur 42 objets.

## 3. PROUVÉ — l'équation ordinaire est linéaire en D

Comme D²=I, développer (3) donne

    B D + D B + D = E,
    E=(8I+4J−M M^T−B²−B)/2.                     (5)

L'intégralité de E découle aussi de (1) modulo 2 : N≡B et R≡M, donc B²+B≡M M^T.

À l'entrée (u,v), (5) s'écrit

    B_(u,d(v)) + B_(d(u),v) + [d(u)=v] = E_uv. (6)

Les choix de d(u) et d(v) dépendent chacun d'au plus un des s bits.

## 4. PROUVÉ — toutes les contraintes restantes sont des parités

Si u,v appartiennent au même bloc ambigu, (6) dépend d'un seul bit ; elle l'autorise, l'interdit, le fixe, ou ne le contraint pas.

S'ils appartiennent à des blocs différents, [d(u)=v]=0. L'équation est

    f(t_u)+g(t_v)=e,                            (7)

avec f et g des fonctions booléennes d'un bit, ou des constantes. Toute fonction booléenne d'un bit est 0,1,t ou 1−t.

- Si e=0, il faut f=0 et g=0 : seulement des contraintes unaires.
- Si e=2, il faut f=1 et g=1 : seulement des contraintes unaires.
- Si e=1, il faut f XOR g=1 : une parité binaire, éventuellement unaire ou constante.
- Une autre valeur de e est impossible.

On ne remplace pas arbitrairement une égalité entière par sa réduction modulo 2 : les cas e=0 et e=2 sont traités séparément. C'est essentiel pour la suffisance.

Il reste donc uniquement

    t_i=epsilon,    t_i XOR t_j=epsilon,

plus des tests constants. Les solutions forment un espace affine sur F_2. Elles peuvent être trouvées par propagation sur un graphe signé : ajouter un sommet constant 0 et traduire chaque équation en une arête de parité prescrite. Le système est réalisable si et seulement si chaque cycle a somme des étiquettes égale à zéro.

**Complétude.** Tout graphe donne une solution de ce système. Inversement, toute solution fournit un D vérifiant (2) et (5), donc (3), et la reconstruction du §1 donne le graphe. Il ne s'agit donc pas d'un filtre seulement nécessaire à cet étage : il décide exactement le relèvement de N.

Le graphe de parités n'est pas un cocycle deviné par analogie : ses variables et chaque étiquette viennent explicitement de (4)–(6). Pour exclure tout C2 par cet objet, il resterait à prouver que chaque N satisfaisant (1) échoue à un test préliminaire ou donne un système de parités contradictoire. Cette quantification universelle n'est pas démontrée ici.

## 5. PROUVÉ — deux complétions distinctes imposent une similitude entière de facteur 33

Supposer D_1≠D_2, tous deux valides pour le même N. Ils diffèrent sur r blocs ambigus, avec 1≤r≤10. Pour chacune des 2r cellules touchées, prendre

    f_c=(e_(c+)−e_(c−))/sqrt(2).

Ces vecteurs sont une base orthonormée d'un espace L de dimension 2r. Sur L, D_2=−D_1, et sur L^perp leurs actions coïncident. Autrement dit D_1−D_2 a image L et noyau L^perp. Posons J=D_1|_L, une involution orthogonale qui échange deux à deux les cellules de chaque bloc ambigu, avec des signes éventuels.

Soustraire (5) pour D_1 et D_2 donne

    B(D_1−D_2)+(D_1−D_2)B+(D_1−D_2)=0.

Pour x dans le noyau de D_1−D_2, cette égalité impose Bx dans le même noyau. B étant symétrique, L est également invariant. En notant B_L sa restriction,

    B_L J + J B_L = −J.                         (8)

L est orthogonal aux colonnes de M, puisque les deux lignes de chaque cellule sont identiques. Il est aussi orthogonal au vecteur constant. En restreignant (3) pour Q_1=B+2D_1 à L et en utilisant (8), on obtient

    B_L²+B_L=8I_(2r).                            (9)

### 5.1 Les entrées de B_L

Dans la base f_c,

    (B_L)_cc=−B_(c+,c−) ∈ {0,−1}.

Pour c≠d, l'invariance de L permet d'écrire

    (B_L)_cd=B_(c+,d+)−B_(c+,d−) ∈ {0,±1}.

Les changements de signe de base ne modifient pas ces ensembles d'entrées. Entre les deux cellules d'un même bloc ambigu, cette entrée est nulle : les quatre partenaires possibles ont B_uv=0 par définition de C_N.

La diagonale de (9) donne exactement huit entrées hors diagonale non nulles par ligne, puisque d²+d=0 pour d∈{0,−1}. Une ligne a au plus 2r−2 places autorisées, donc

    r≥5.                                        (10)

### 5.2 Forme par blocs

L'entrée de (8) entre les cellules appariées force la somme de leurs deux diagonales à être −1. Dans chaque paire, l'une vaut donc 0 et l'autre −1. Ordonner d'abord les r cellules de diagonale 0, puis leurs partenaires, et choisir les signes pour avoir

    J = [[0,I],[I,0]].

L'équation (8) et la symétrie de B_L imposent alors

    B_L = [[A,C], [−C,−I−A]],

avec A entier symétrique de diagonale nulle et C entier antisymétrique. L'équation (9) donne

    A²+A−C²=8I_r,    AC=CA.                     (11)

Définir l'entier

    Z=I_r+2A+2C.

Alors, par (11),

    Z Z^T=(I+2A+2C)(I+2A−2C)=33I_r.             (12)

C'est une conséquence de l'existence de **deux** complétions, et non une conséquence nécessaire d'une complétion unique. Ne pas déplacer ce quantificateur.

## 6. PROUVÉ — r est divisible par 4, donc r=8

D'abord det(Z)²=33^r. Comme det(Z) est entier et 33 n'est pas un carré, r est pair.

Sur Z_3, (12) implique que tous les exposants 3-adiques des facteurs de Smith de Z valent 0 ou 1 : en effet 3Z^−1=Z^T/11 est 3-intégrale. Comme v_3(det Z)=r/2, exactement r/2 de ces facteurs sont divisibles par 3. Ainsi

    rank_F3(Z mod 3)=r/2.

Par (12), les lignes de Z modulo 3 engendrent un sous-espace totalement isotrope de dimension r/2 pour le produit scalaire standard de F_3^r. Cette forme de dimension r=2h doit être scindée.

Voici le test de discriminant, sans hypothèse cachée : choisir une base de ce sous-espace isotrope et une base duale complémentaire. La matrice de la forme devient [[0,I_h],[I_h,T]]. Son déterminant vaut (−1)^h. Le déterminant initial vaut 1, et un changement de base ne le modifie que par un carré. Donc (−1)^h doit être un carré de F_3. Comme −1 n'y est pas un carré, h est pair.

Il s'ensuit 4|r. Avec 5≤r≤10,

    r=8.

Deux complétions distinctes diffèrent donc sur huit blocs, seize cellules, trente-deux orbites, soit soixante-quatre sommets extérieurs. Elles coïncident sur les dix autres orbites extérieures.

## 7. PROUVÉ — il existe au plus deux complétions

Représenter les complétions par leurs s≤10 bits. Le §6 montre que deux complétions distinctes ont toujours distance de Hamming 8.

Supposer qu'il y en ait trois t_0,t_1,t_2. Les supports de t_1 XOR t_0 et t_2 XOR t_0 ont chacun taille 8 dans un ensemble de taille au plus 10. Leur intersection a taille au moins 6, donc leur différence symétrique a taille au plus 4. Mais cette différence symétrique est le support de t_1 XOR t_2, qui doit avoir taille 8. Contradiction.

Le nombre de complétions est donc 0,1 ou 2. En présence de deux solutions, le système affine du §4 a dimension exactement un.

**Ce n'est pas une preuve que la borne 2 est atteinte.** Aucune réalisation de C2 n'est produite dans cette note.

## 8. Conséquence auxiliaire contrôlable : symétrie forcée du défaut E

De E=BD+DB+D et D²=I,

    DED=E.

Donc le couplage D est une involution sans point fixe de la matrice pondérée E. De plus E_uv∈{0,1,2}, E_uu=0, E1=21·1, et E_(u,d(u))=1. Toute fonction de sommet préservée par les automorphismes de E prend ses valeurs avec des multiplicités paires : chaque fibre est stable sous D et D y est sans point fixe.

Ceci fournit des tests nécessaires sur B et M. Cela ne démontre pas que E est toujours asymétrique ni qu'un de ces tests exclut les cas restants. La caractérisation affine précédente est plus précise que le seul test d'automorphismes de E.

## 9. Contrôles exécutés

`reconstruction.py` utilise des entiers ; il ne lance aucun solveur.

### Graphes réellement existants

- Graphe sur F_3², connexion ±e_1,±e_2 : 9 sommets, degré 4.
- Graphe sur F_3[x]/(x^5−x^3+x²−x−1), connexion ±x^i, 0≤i<11 : 243 sommets, degré 22.

Dans les deux cas, le programme vérifie exactement l'identité SRG sur la matrice complète, extrait les orbites sous v↦−v, puis reconstruit le couplage initial. Le résultat est une unique complétion, sans bloc ambigu. Le contrôle à 243 sommets relève de la construction de Berlekamp–van Lint–Seidel par le code ternaire de Golay ; ici ses propriétés nécessaires sont recalculées directement.

Ces témoins contrôlent les normalisations et le relèvement général. Comme ils n'ont pas de bloc ambigu, ils ne constituent pas une validation expérimentale non vacue du théorème spécifique « r=8 ».

### Systèmes synthétiques de relèvement

500 systèmes avec jusqu'à six blocs ambigus ont été générés. Les solutions prédites par les parités ont été comparées à toutes les affectations binaires de ces petits systèmes : égalité exacte à chaque fois. 72 cas ont plusieurs solutions.

Ces objets synthétiques ne prétendent PAS satisfaire (1) ou être des graphes fortement réguliers. Ils contrôlent uniquement le passage des tables booléennes au système affine, y compris les cas avec plusieurs solutions.

`controls.json` enregistre explicitement : 0 candidat C2 complet examiné, 0 nouvelle exclusion C2.

## 10. Où ce résultat se raccorde au problème principal

Chaîne exacte :

    C2 existe
       ⇒ il existe N satisfaisant (1)
       ⇒ les cellules cibles T sont admissibles
       ⇒ C_N admet un couplage parfait
       ⇒ son graphe de parités est cohérent.

Réciproquement, un N complet satisfaisant (1) et passant ces trois tests reconstruit C2. La liberté résiduelle n'est donc pas un nouveau grand problème d'énumération : elle est décidée par des parités et donne au plus deux graphes étiquetés.

Cela corrige une localisation antérieure trop vague : présenter « le couplage des deux secteurs » comme nécessairement une seconde explosion combinatoire après un N complet n'est pas justifié. Le problème coûteux observé dans les routes de frames est en grande partie **en amont** : construire ou exclure N lui-même.

Le théorème élimine exactement les N dont la reconstruction échoue. Il ne prouve pas que tout N échoue. Il ne donne pas non plus un test de parité directement sur une injection rho partielle ou sur trois h : B entier et complet doit être connu pour former (4) et (5).

## 11. Provenance minimale

- `conway99-c2-experimental`, `609cc3bf25b11c1c7be187071d4462529ab9e384`, `scripts/extend_s_to_q.py` : cellule cible forcée, énumération historique de D, équation de Q.
- `conway99-rank17`, `d9fdc855f3a46baf0d8c230f1e257012858f18a7`, `TARGETS_AB_STRUCTURES.md`, §1 : séparation exacte des secteurs N et Q, nécessité du couplage.
- `conway99-involution`, `e3f14c2ec556535b2cd6effb2c88d0f5e6fcd1d5`, `notes/NOTE_involution_case.md`, §2 : normalisation du graphe et modèle d'orbites.
- E. R. Berlekamp, J. H. van Lint, J. J. Seidel, *A strongly regular graph derived from the perfect ternary Golay code* (1973 ; repris dans *Geometry and Combinatorics*, 1991), DOI 10.1016/B978-0-12-189420-7.50012-8 : origine du contrôle à 243 sommets.

Les résultats §§2–8 sont déduits ici des équations écrites, indépendamment de la complétude d'une campagne Route C ou d'un compteur d'exclusions.



---

# Part 13: Original unsigned uniqueness proof

Source file within this handoff: `originals/c2_unique_completion_2026_09_30/UNIQUE_DOUBLE_MATCHING.md`.

# Conway-99: the unsigned support determines the double matching uniquely

Research note, 30 September 2026.

## Status and exact scope

**DERIVED HERE: a complete mathematical argument is provided below. It has not yet had an independent reader or a Lean formalization. No priority in the literature is asserted.**

The argument strengthens the preceding conversation note, `PREUVE_RELEVEMENT_FR.md`, which bounded the number of completions of a fixed signed quotient by two. In fact the double matching is unique when it exists, and the uniqueness already holds with the unsigned support fixed; the signed quotient equations are not needed in the uniqueness proof.

This is **not** a proof that C2 is empty. It rules out two different ordinary-sector completions of the same support. It does not rule out a unique completion, and it does not provide an exhaustive exclusion of any further rank-24 envelope or rank-17 pair class.

All matrices and all counts below have explicit finite definitions. The proof does not use the 156-lattice classification, the rank-17 classification, a minimum assumption on K, an extra graph automorphism, or zero same-cell inner products.

## 1. The theorem

Let the 42 indices be arranged into 21 cells, two indices per cell. Identify the cells with the two-element subsets of a seven-element set. Let M be the 42 by 7 binary matrix whose row at either index in cell c is the incidence vector of c.

Let B be a symmetric binary 42 by 42 matrix with zero diagonal and row sum ten.

Call D a valid completion when:

1. D is the permutation matrix of a fixed-point-free involution on the 42 indices;
2. D and B have disjoint supports;
3. Q = B + 2D satisfies

   QM = 4 J_(42,7) - 2M,

   Q^2 + Q = 12 I_42 + 4 J_42 - MM^T.

**Theorem. There is at most one valid D.**

In the C2 graph model B is the graph of single adjacencies between the 42 exterior involution-orbits and D records their double-adjacency partners. For a fixed complete signed quotient N, B=|N|. The theorem therefore implies at most one labelled graph completion for that N and the fixed root labels. It is not a bound on the total number of N or the total number of C2 graphs.

The model and target-cell observation were already present in the project's `scripts/extend_s_to_q.py`, `conway99-c2-experimental`, commit `609cc3bf25b11c1c7be187071d4462529ab9e384`. The new part of this note is the elimination of the two-completion case using the original seven-block incidence.

## 2. Two completions would differ on at most ten four-index blocks

The first equation gives

   DM = T,   T = 2J_(42,7) - M - BM/2.

For each index u, T_u must be the incidence vector of the cell containing its partner d(u). All 21 possible rows are distinct, so this target cell is fixed by B and M.

A possible matching edge u--v must satisfy all of:

   u != v,  B_uv = 0,
   cell(v) = target(u),  cell(u) = target(v).

For two distinct cells c,d, such edges lie in a bipartite graph on the indices of c targeting d and the indices of d targeting c. Each side has at most two elements. Different unordered cell-pairs use disjoint sets of indices, since the target of an index is unique. Edges within a cell lie in its single possible two-index matching.

Consequently a component has two perfect matchings only when it is the entire K_(2,2) between two cells. Such an ambiguous component consumes both indices of both cells; different ambiguous components cannot share a cell. There are at most floor(21/2)=10 ambiguous components.

Suppose D_1 and D_2 are distinct valid completions. They differ on r of these components, where

   1 <= r <= 10.

For each of the 2r affected cells c define

   f_c = (e_(c,+) - e_(c,-))/sqrt(2),

and let L be their real span. The difference D_1-D_2 has image L and kernel L^perp. The two matchings act oppositely on L and identically on L^perp.

## 3. The difference space carries a constrained integral operator

Expanding the second equation for Q and using D^2=I gives

   BD + DB + D = E,

   E = (8I + 4J - MM^T - B^2 - B)/2.

Subtract the equations for D_1 and D_2. Since B is symmetric, both the kernel and the image of D_1-D_2 are B-invariant. Set

   X = B restricted to L,   J_0 = D_1 restricted to L.

Then

   X J_0 + J_0 X = -J_0.                         (3.1)

Both M^T and the all-ones functional vanish on L. Restricting the Q_1 equation to L, with Q_1|L=X+2J_0, therefore gives

   X^2 + X = 8I_(2r).                            (3.2)

In the orthonormal cell-difference basis:

* X_cc = -B_(c,+;c,-) lies in {0,-1};
* X_cd lies in {0,+1,-1} for c != d;
* X_cd = 0 when c,d form one of the ambiguous matching components.

Here is the entry argument, including the information needed later. For two affected cells, write the binary block of B as [[a,b],[c,d]]. Invariance of the difference space, and orthogonality to the sum space, imply a+b=c+d and a+c=b+d. Thus a=d and b=c. If X_cd != 0, this block is a perfect matching, so each index in c has exactly one B-neighbour in d. If X_cd=0, the block is either zero or all ones. Sign changes in the f_c basis do not change these absolute-value statements.

The diagonal of (3.2) says that X has exactly eight nonzero off-diagonal entries per row. Since its matching-partner entry is zero, 8 <= 2r-2, and

   r >= 5.                                      (3.3)

Equation (3.1) says that the two diagonals in each paired cell-block add to -1. In each pair one cell has diagonal zero and the other diagonal -1. Order the zero-diagonal cells first, then their partners, and choose basis signs so that

   J_0 = [[0,I_r],[I_r,0]].

There are integral matrices A,C such that

   X = [[A,C],[-C,-I_r-A]],

   A^T=A,  C^T=-C,  A_ii=C_ii=0,
   A_ij,C_ij in {0,+1,-1}.

Equations (3.1)--(3.2) give

   A^2 + A - C^2 = 8I_r,   AC=CA.

It follows that the integral matrix

   Z = I_r + 2A + 2C

satisfies

   ZZ^T = 33I_r.                                (3.4)

This is the same difference-space reduction as in the preceding note, rederived here without assuming N.

## 4. Arithmetic forces r=8

Taking determinants of (3.4) shows that r is even. At the prime 3,

   3 Z^(-1) = Z^T / 11

is integral. Hence every 3-adic Smith exponent of Z is at most one. Their sum is v_3(det Z)=r/2, so exactly r/2 exponents are one and

   rank_(F_3)(Z mod 3) = r/2.

The rows of Z mod 3 are mutually orthogonal by (3.4), so they give a totally isotropic half-dimensional subspace of the standard form on F_3^r. Write r=2h. A nondegenerate form with such a subspace has determinant class (-1)^h: extend an isotropic basis to a dual basis, obtaining Gram [[0,I],[I,T]]. Its determinant is (-1)^h.

The standard form has determinant one. Since -1 is not a square in F_3, h is even. Therefore 4 divides r. Together with 5 <= r <= 10,

   r = 8.                                       (4.1)

There would be sixteen affected cells.

## 5. New structural lemma: |A| must be K_(4,4)

We now use the entry restrictions of Z, not just its determinant. Throughout this section r=8.

### 5.1 Every row has one entry of magnitude four and four of magnitude two

Z has diagonal one and off-diagonal entries in {0,+2,-2,+4,-4}. For i != j:

* if |Z_ij|=4, then Z_ji=0;
* if |Z_ij|=2, then |Z_ji|=2;
* if Z_ij=Z_ji=0, then A_ij=C_ij=0.

These follow directly from Z_ij=2(A_ij+C_ij), Z_ji=2(A_ij-C_ij).

If a row has p off-diagonal entries of magnitude four and q of magnitude two, its norm is

   1+16p+4q=33,  p+q <= 7.

Its only possibilities are (p,q)=(1,4) or (2,0).

The latter is impossible. Choose a magnitude-four entry Z_ij in such a row. Z_ji=0. The inner product of rows i and j is the term Z_ij Z_jj=+/-4 plus multiples of eight, since the only other off-diagonal nonzero in row i has magnitude four and multiplies an even off-diagonal entry of row j. This cannot vanish modulo eight.

Thus every row has exactly one magnitude-four and four magnitude-two entries. The magnitude-two support is symmetric, so every column also has four such entries. Since Z^TZ=33I, every column has exactly one magnitude-four entry.

### 5.2 Three support graphs on eight vertices

The magnitude-four positions therefore form a permutation, with no fixed points or two-cycles. Let P be the undirected union of its cycles. P is a simple 2-factor with cycles of length at least three.

Let F be the graph of magnitude-two positions. It is 4-regular. Each vertex has one outgoing magnitude-four entry and one incoming one (whose transpose entry is zero), four neighbours in F, and one remaining mutual-zero partner. The mutual-zero pairs form a perfect matching H. Therefore

   K_8 = P disjoint-union F disjoint-union H.

Let G=P union H, a simple cubic graph, so F is the complement of G.

### 5.3 Parity specifies the triangles in G

Set K=A+C=(Z-I)/2. Expanding ZZ^T=33I gives

   KK^T = 8I-A.

Modulo two, K is exactly the adjacency matrix of F. Hence

   F^2 = A   modulo two.

Since F is the complement of a cubic graph G on eight vertices, an exact expansion gives

   F^2 = I + G^2 + 2G.

For distinct i,j, therefore A_ij is nonzero exactly when G^2_ij is odd. Recall A_ij is in {0,+1,-1}.

On an edge of P, A_ij is necessarily +/-1, since exactly one of Z_ij,Z_ji has magnitude four. Thus each P-edge has an odd number of common G-neighbours. A cubic graph allows at most two common neighbours for adjacent vertices, so every P-edge is in exactly one triangle.

On an edge of H, A_ij=0, so the edge is in zero or two triangles.

### 5.4 The 2-factor P consists of two four-cycles

If an H-edge uv is in two triangles, u and v have the same other two neighbours a,b. All four edges ua,ub,va,vb belong to P, and the degree-two condition forces them to be an entire four-cycle of P.

If a vertex v belongs to a P-cycle of length at least five, its H-edge cannot be in two triangles, by the preceding observation. It is therefore in no triangle. The two P-edges incident with v each lie in exactly one triangle, so the two P-neighbours of v must be adjacent. Their edge is not in P in a cycle of length at least five, hence belongs to H. This H-edge has a common neighbour v; its number of common neighbours must be two, forcing v onto a four-cycle of P, a contradiction.

Thus every P-cycle has length three or four. Eight vertices cannot be partitioned into such cycles except as 4+4. Therefore

   P = C_4 disjoint-union C_4.

Each four-cycle has exactly one H-diagonal. An edge of the four-cycle cannot lie in a triangle through an outside vertex: that would require two H-edges to the same outside vertex. With no H-diagonal a P-edge has no triangle; with both diagonals it has two. Both violate the exactly-one condition. The remaining two H-edges join the remaining vertices across the two four-cycles.

### 5.5 Recovering |A|

Let U consist of the endpoints of the two internal H-diagonals (four vertices), and V consist of the other four vertices.

* Every P-edge joins U to V and has A_ij != 0.
* A cross-cycle U--V pair is an F-edge. It has exactly one common G-neighbour, namely the H-partner of its V endpoint. Thus A_ij != 0.
* A U--U pair is either an H-edge, where A_ij=0, or a cross-cycle pair with no common G-neighbour.
* A V--V pair is an H-edge, or has zero or two common G-neighbours. In every case A_ij=0.

Consequently

   |A| = adjacency matrix of K_(4,4).           (5.1)

We also retain:

   W := |A|+|C| is symmetric, has zero diagonal and row sum eight;
   W_ij is 2 on P, 1 on F, and 0 on H.          (5.2)

In particular the only zero off-diagonal pairs of W form a perfect matching.

No enumeration of signings or matrices is used in this lemma.

## 6. Restore the seven-block incidence: a capacity lemma

Recall the sixteen affected cells are still actual two-element subsets of the seven original blocks. They cannot be treated as arbitrary sixteen coordinates.

Let delta be the diagonal of |X|: it is zero on the first eight cells and one on their partners. For a fixed original block j define t in {0,1}^16 by

   t_c=1 if affected cell c contains j, and 0 otherwise.

For an index u in cell c, its D-partner lies in the paired cell c*. The exact block equation says

   (BM)_(u,j) = 4 - 2 t_c - 2 t_(c*).

On the other hand the affected cells alone contribute at least (|X|t)_c B-neighbours incident with block j: every nonzero off-diagonal entry of X supplies one neighbour per orbit, and its diagonal magnitude supplies the cellmate. Other neighbours only increase the total. Hence

   (|X|+2I+2J_0)t <= 4*1_(16)                  (6.1)

entrywise.

**Capacity lemma. Every binary t satisfying (6.1) has at most four ones.**

### 6.1 At most one cell from each pair; at most five in total

If both paired cells are selected, consider the one with delta=1. Its diagonal contribution to the left side of (6.1) is at least 1+2+2=5. This is impossible. So t selects at most one cell per pair.

Write q=|t| and s for the number of selected delta=1 cells. Column sums of |X|+2I+2J_0 are 12+delta. Summing (6.1) gives

   12q+s <= 64.

Thus q<=5.

### 6.2 Five selected cells would all have delta=0

Suppose q=5. Let S be the corresponding five pair indices among eight, and let T be the other three. Let b be the indicator of S. Adding the two inequalities (6.1) in a selected pair i gives

   (Wb)_i <= 4-epsilon_i,

where epsilon_i is one if the selected cell of pair i has delta=1, and zero otherwise. Thus

   sum_(i in S)(Wb)_i <= 20-s.

Since W has row sum eight, the total W-weight between S and T is at least 40-(20-s)=20+s. The total degree in T is 24, so the weight of edges internal to T satisfies

   2 e_W(T) <= 4-s.

Among three vertices at most one of the three pairs belongs to the zero matching H of (5.2). Each of the other pairs has weight at least one. Therefore e_W(T)>=2. It follows that s=0.

### 6.3 K_(4,4) forbids those five cells

All five selected cells would therefore lie in the delta=0 half. On these coordinates (6.1) requires every selected vertex to have at most two neighbours in the subgraph of |A| induced by the selected indices.

But |A|=K_(4,4). Any set of five vertices meets both parts, with at least three in one part. A selected vertex in the other part has at least three selected neighbours. Contradiction.

This proves the capacity lemma.

## 7. The contradiction: thirty-two incidences cannot fit into twenty-eight slots

Apply the capacity lemma to each of the seven original blocks. Each belongs to at most four of the sixteen affected cells. Thus the number of block--affected-cell incidences is at most

   7*4 = 28.

But every affected cell is a two-element subset of the blocks, so that same number is exactly

   16*2 = 32.

This is impossible. Therefore the assumed D_1 != D_2 do not exist. The theorem follows.

## 8. Exact connection to the main C2 problem

The preceding reconstruction note converts the possible D into an affine system of unary and binary parity constraints once B is complete and target cells are checked. A valid complete signed matrix N still must satisfy

   NR=0,  N^2=N+12I-RR^T,
   N symmetric, diagonal zero, entries in {0,+1,-1}.

For N fixed and B=|N|, any solution of the exact completion system reconstructs a graph. The theorem here says that system has either zero solutions or exactly one.

Equivalently, in a consistent parity graph, every ambiguity bit is connected to a fixed bit; there is no free parity component. Otherwise flipping that component would provide two valid D, which the theorem forbids.

The open nonexistence obligation is still:

   For every complete signed N satisfying the odd equations,
   its target-cell/matching/parity completion tests reject.

This note does not prove that statement. The argument 32>28 begins with TWO completions and cannot be reused under the assumption of only one. In particular it does not by itself eliminate an existing open rank-17 class or rank-24 envelope.

The informational lesson is concrete rather than speculative: the abstract difference-space equations permit matrices Z with ZZ^T=33I, but the original seven-block incidence prevents those difference spaces from occurring between two completions. The restored incidence information, not the bare determinant, supplies the contradiction.

## 9. Checks, nonclaims, and negative control

The mathematical proof above is independent of the computational checks.

`verify_structure.py` uses Python's standard library and integer arithmetic. It checks an explicit 8 by 8 Z satisfying all the difference-space matrix identities; derives A,C,X; verifies that |A| is K_(4,4); checks the capacity inequality on all 2^16 binary vectors for this explicit example; and checks the eight permitted zero matchings for a fixed pair of four-cycles.

The explicit Z is important as a negative control: ZZ^T=33I together with the stated A,C entry restrictions is NOT itself impossible. Its existence prevents mistakenly presenting the arithmetic intermediate object as a C2 contradiction.

The check of one explicit Z is not a classification or a computer proof of the theorem; the universal structure and capacity lemmas are proved in Sections 5 and 6.

No C2 signed quotient was constructed or exhaustively searched. No cloud resources were used. No repository was modified. A human/independent mathematical review is still needed, especially of the difference-space reduction, the support-parity argument, and the transfer of the cell-incidence inequality (6.1).



---

# Part 14: Original real-linear completion proof

Source file within this handoff: `originals/c2_linear_completion_2026_09_30/LINEAR_COMPLETION.md`.

# Conway-99: exact real-linear completion of a complete signed quotient

Research continuation, 30 September 2026.

## Status

**DERIVED HERE — a complete mathematical proof follows.** No independent mathematical review or Lean verification has yet been performed. No priority claim is made. The tests accompanying this note are sanity checks, not an exhaustive C2 computation.

This note pursues the preceding completion-uniqueness lead into an assertion about **one** candidate. It does not assume two graphs exist. It proves that, for a complete signed quotient satisfying the stated equations, a particular real-linear relaxation of the double matching is exact: its feasible set is either empty or a singleton integral perfect matching.

This is not an exclusion of every signed quotient, every envelope, or any newly named rank-17 class. The construction or exclusion of the complete signed quotient remains an unresolved proof obligation in this investigation.

## 1. Exact hypotheses and theorem

Index 42 rows by pairs `(c,+),(c,-)`, where the 21 cells are the two-element subsets `c={i,j}` of `{1,...,7}`, with `i<j`. Let R be the 42 by 7 matrix with rows

    r_(c,+)=e_i+e_j,     r_(c,-)=e_i-e_j.

Put M=|R|. Thus M repeats each cell-incidence vector twice. In particular

    R^T R = 12I_7,      M 1_7 = 2 1_42,
    M^T 1_42 = 12 1_7,  M^T M=10I_7+2J_7.

Assume a **complete** symmetric integer matrix N satisfies

    diag N=0,  N_uv in {0,+1,-1},
    NR=0,      N^2=N+12I_42-RR^T.                 (1)

Define

    B=|N|,
    T=2J_(42,7)-M-(BM)/2,
    E=(8I_42+4J_42-MM^T-B^2-B)/2.                (2)

Consider the following system, with D an arbitrary REAL matrix:

    D=D^T,  D>=0 entrywise,  diag D=0,
    D 1_42=1_42,
    D_uv=0 whenever B_uv=1,
    DM=T,
    BD+DB+D=E.                                   (LP)

Every condition is affine-linear or a linear inequality in D. **Do not impose D^2=I or D_uv in {0,1}.**

### Theorem

Under (1), the feasible set of (LP) is either empty or consists of one matrix. In the latter case this matrix is the permutation matrix of a fixed-point-free involution, disjoint from B.

Consequently, for a fixed N satisfying (1), real feasibility of (LP) is equivalent to graph completion in the exact C2 model. It does not merely test a necessary fractional relaxation.

The proof below does not assume the preceding long theorem for arbitrary unsigned B. It uses an additional parity property forced by the **signed** equations (1).

## 2. The graph-origin parity retained from NR=0

Let chi in {0,1}^42 be 1 at `(c,+)` and 0 at `(c,-)`. It selects exactly one index in every cell. The choice is fixed by the displayed rows of R, not by a new hypothesis on a graph.

    R 1_7=2 chi.

Thus (1) implies the exact integer equality N chi=0. Since N and |N| agree modulo 2,

    B chi = 0  modulo 2.                         (3)

Equivalently, each orbit has an even number of B-neighbours among the 21 plus-labelled indices. This elementary consequence is used as an ingredient; no claim that it was previously unknown is needed.

The diagonal of (1) gives ten nonzeros in each row of N, hence

    B 1_42=10 1_42.                               (4)

Also BM is even, since N R=0 modulo 2 and R=M modulo 2. The second equation in (1) modulo 2 gives

    B^2+B=MM^T  modulo 2.

Therefore both T and E in (2) are integer matrices. Moreover T 1_7=2 1_42.

## 3. The invariant-difference-space obstruction

### Lemma

Let B be symmetric binary with zero diagonal and let chi select one index from each of a collection of two-index cells, with B chi even. There is no nonzero B-invariant subspace L of the following form:

    L=span_R { g_c : c in S },
    g_c=e_(c,+)-e_(c,-),

where S is a nonempty collection of whole cells, such that the restriction X=B|L satisfies

    X^2+X=8I.                                    (5)

Here X is represented in the basis g_c; its Gram matrix is 2I, so X is symmetric.

### Proof

Let G have columns g_c, for c in S. Invariance means BG=GX. The coefficient of g_c in Bg_d is `(Bg_d)_(c,+)`, an integer, so X is integral. Its diagonal is

    X_cc=-B_(c,+;c,-) in {0,-1}.                  (6)

Since chi^T G is the all-ones row, (3) gives

    1^T X=chi^T BG=(B chi)^T G=0 modulo 2.

As X is symmetric, every row sum of X is even. Reduce the diagonal of (5) modulo 2:

    0=(X^2+X)_cc
      =sum_d X_cd^2 + X_cc
      =sum_d X_cd + X_cc
      =X_cc  modulo 2.

Together with (6), this forces X_cc=0 for every c, hence tr X=0.

On the other hand f(t)=t^2+t-8 has irrational roots

    alpha=(-1+sqrt(33))/2,
    beta =(-1-sqrt(33))/2.

It is irreducible over Q. Since X is an integer matrix annihilated by f, its rational characteristic polynomial is f^a for some integer a>=1. Thus dim L=2a and

    tr X=a(alpha+beta)=-a != 0.

This contradicts tr X=0. ∎

**Scope of this lemma.** It needs a subspace spanned by differences of entire designated cells, not just an arbitrary subspace of the same dimension. It also needs (3). A bare matrix X with X^2+X=8I is not impossible.

## 4. Feasible D is supported on disjoint tiny matching components

Assume (LP) is feasible, for now without integrality.

Each row of DM is a convex combination of the binary rows of M. Since T is integral, has row sum 2, and equals DM, every row of T must itself be a binary vector of weight 2: every entry is between 0 and 1.

If D_uv>0, every coordinate of M_v must equal the corresponding coordinate of T_u. Indeed a convex combination of 0/1 numbers can equal the endpoint 0 or 1 only if each positively weighted term has that value. Thus

    D_uv>0 => cell(v)=target(u).

Symmetry gives cell(u)=target(v); disjointness gives B_uv=0.

Each index has a unique target cell. The allowed edges consequently split into disjoint components on at most four indices. A component is bipartite between two cells (each of size at most 2), or is the unique edge within a cell. The row-sum equations exclude unequal bipartition sizes. A feasible two-by-two block is either forced integral or has all four edges available and takes the form

    [ t_i    1-t_i ]
    [ 1-t_i    t_i ],     0<=t_i<=1,             (7)

with its transpose in the opposite block.

The latter is an ambiguous K_(2,2); it consumes both indices of two distinct cells. Different ambiguous blocks use disjoint cells, so there are at most ten parameters t_i.

This component analysis follows solely from (LP); it is not an integrality assumption.

## 5. Every nonempty real feasible set has a canonical half-integral point

At an entry (u,v) of the last equation of (LP),

    (BD+DB+D)_uv=E_uv,                            (8)

there are at most two parameters, because column v of D belongs to the component of v and row u to the component of u.

For indices from different matching components, D_uv=0. The two summands are functions f(t_i),g(t_j), each belonging to

    0, 1, t, 1-t.

Because E_uv is integer, an equation f+g=E is either inconsistent, automatic, a pin to 0 or 1, or one of

    t_i=t_j,       t_i=1-t_j.

For example, if both functions vary, E=0 or E=2 forces both summands to an endpoint; E=1 gives equality or complementation. These endpoint reductions use the bounds 0<=t<=1 and are exact over R, not just over F_2.

For indices in the same ambiguous component, let a and b be the binary B-adjacencies inside its two cells. On a cross-cell position the expression is

    t+(a+b)(1-t)

or the expression with t replaced by 1-t. Its coefficient is 1-a-b in {-1,0,1}. Hence an integer right side again only gives an endpoint pin, an automatic equation, or inconsistency. Same-cell positions add no other kind of equation because B is zero between the two cells of the ambiguity block.

Thus the exact real solution set is represented by a graph of equality/complementation relations, with some variables fixed to endpoints.

In a connected component, transporting a value x along paths gives variables equal to x or 1-x:

* A consistent component with a fixed variable has all values in {0,1}.
* A component without a fixed variable and without an inconsistent parity cycle has one free x in [0,1].
* A component without a fixed variable but with an inconsistent parity cycle forces x=1-x, hence x=1/2 for all its variables.
* A component containing both an endpoint pin and an inconsistent parity cycle is infeasible.

Consequently, whenever (LP) is feasible, select x=1/2 in every free component. This produces a feasible Dbar for which

    every t_i is 0, 1/2, or 1.                   (9)

If any half-fixed or free component exists, this chosen Dbar has at least one t_i=1/2.

## 6. A half-integral solution creates exactly the forbidden subspace

Suppose Dbar has at least one half-parameter. Let S consist of both cells in every half-parameter block, and let

    L=span{ g_c : c in S },
    P_L=sum_(c in S) g_c g_c^T/2.

A block (7) with t=1/2 is the average of its two perfect matchings. It kills the two cell-difference directions and is an involution on the cell-sum directions. All other blocks of Dbar are integral matchings. Therefore, exactly,

    Dbar^2=I-P_L,       Dbar P_L=P_L Dbar=0.     (10)

Put Qbar=B+2Dbar. From (2) and (LP),

    Qbar M=4J-2M,
    Qbar^2+Qbar=12I+4J-MM^T-4P_L.              (11)

The second formula follows by expansion, retaining Dbar^2 rather than replacing it by I:

    Qbar^2+Qbar
      =B^2+B+2(BDbar+Dbar B+Dbar)+4Dbar^2
      =8I+4J-MM^T+4Dbar^2.

Next Qbar 1=12 1, so Qbar commutes with J. It also commutes with MM^T: multiplying the first equation in (11) by M^T gives

    Qbar MM^T=8J-2MM^T,

whose transpose is the same expression.

Every matrix commutes with its own polynomial. Taking the commutator of Qbar with the second equation in (11) therefore gives

    [Qbar,P_L]=0.

Since Dbar kills L and its orthogonal complement does not map into L, (10) implies

    [B,P_L]=0.

Thus L is B-invariant. Both M^T and the all-ones functional vanish on L. Restricting (11) to L, where Qbar=B, gives

    (B|L)^2+(B|L)=8I_L.

But L is a nonzero span of complete cell differences. Section 3 rules it out using the parity B chi even.

Therefore the canonical solution (9) contains no half-parameters. ∎

## 7. Integrality, uniqueness, and graph reconstruction

A free real component would have supplied a half-parameter in the canonical choice, and a half-fixed component would have done so necessarily. Both are impossible. Hence every variable is pinned to 0 or 1 and every component is determined.

It follows that the feasible set of (LP) is either empty or a singleton, and in the latter case D is an integral symmetric row-stochastic matrix with zero diagonal: a perfect matching.

Now D^2=I. Equation (11) reduces to the exact ordinary-sector equations without a defect. Together with (1), they reconstruct the 84 by 84 exterior adjacency matrix with blocks

    a=(Q-N)/2,    b=(Q+N)/2,
    H=[a b; b a].

On support B, Q=1 and N=+/-1, so a,b are 0/1; on support D, Q=2 and N=0, so a=b=1; elsewhere both are zero. The signed labels R specify the two inner neighbours of each exterior vertex. Add the fixed vertex and the seven inner edges. The signed and ordinary equations give, block by block, the full degree and common-neighbour equations.

The theorem therefore has the exact logical consequence

    C2 exists
      iff there exists a complete N satisfying (1)
          for which the real system (LP) is feasible.    (12)

No claim is made that the right side is always infeasible.

## 8. What this adds to the previous lead

1. The preceding unsigned uniqueness theorem compared two integral completions. This theorem works under a stronger graph-origin hypothesis, namely a signed N satisfying (1), but reaches a stronger conclusion: fractional solutions and continuous ambiguity are impossible as well.
2. The resonant arithmetic object X^2+X=8I is killed here by B chi=0 modulo 2. No 8-by-8 sign classification or 32-versus-28 incidence argument is needed in this signed setting.
3. A completed N has a linear-algebraic existence test for D. The already described parity solver is small; no large runtime improvement is claimed merely from replacing it by a linear formulation.
4. Because (LP) is rational and bounded, infeasibility can be exhibited by a rational linear certificate. This supplies a precise possible certificate language, not a universal certificate already found.
5. For partial N or partial B, the hypotheses of the theorem are not yet available. Applying the theorem to an arbitrary incomplete prefix without a sound relaxation would be invalid.

The exact remaining arrow is to exclude all N in (12), or to construct one for which (LP) is feasible. Producing a linear certificate for one completed N does not cover every possible N.

## 9. The proposed symmetry shortcut, checked

The earlier uniqueness theorem implies that an automorphism of (B,M), with block columns allowed to permute, must preserve D when D exists: conjugating D would otherwise give a second completion.

It does not prove that such a nonidentity automorphism exists. Nor does an automorphism of (B,M) automatically preserve the signed labels and N needed for a graph automorphism. No contradiction from 'uniqueness forces an extra symmetry' has been established.

## 10. Checks and limitations

The accompanying script performs small exact checks:

* the existing nine-vertex and 243-vertex positive controls satisfy N chi=0 and B chi even;
* the explicit previous 33-similitude generates X with X^2+X=8I, and its odd column sums occur exactly where its diagonal is -1;
* a binary lift of that X to pairs of indices is invariant on cell differences but violates B chi even, so it cannot come from (1);
* a synthetic odd parity cycle has a unique real half-solution and no binary solution: this shows why the signed hypotheses are essential, rather than assuming every parity relaxation is integral;
* a synthetic balanced cycle has a free real component and two binary endpoints;
* the block identity Dbar^2=I-P_L is checked exactly with matrices scaled by two.

These are not 99-vertex witnesses and not an exhaustive proof of C2. No lattice class has been newly excluded by this note. The universal claims rest on Sections 2-7. Targeted repository/public searches did not establish the literature priority of this formulation.



---

# Part 15: Original research journal

Source file within this handoff: `originals/c2_reconstruction_2026_09_30/JOURNAL.md`.

# Journal de recherche — 30 septembre 2026

Objectif : produire une conséquence des axiomes exacts, pas extrapoler les recherches infructueuses.

1. Relecture du modèle (N,D) et de l'audit transversal local. Distinction maintenue entre une matrice signée complète et un préfixe de frame.
2. Contrôle de pistes proches du corpus : les triplets de droites et les réflexions locales sont déjà étudiés. Pas de prétention de nouveauté sur ces objets.
3. Conséquence directe retrouvée : la cellule de D(u) est forcée par les comptes BM. Vérification de provenance : présente dans extend_s_to_q.py. Ne pas la présenter comme nouvelle.
4. Décomposition exacte du domaine de D : composantes contenues dans K2 ou K2,2 ; au plus dix choix binaires.
5. Après D²=I, l'équation ordinaire est linéaire en D. Chaque entrée ne dépend que de deux choix binaires. Ses solutions sont des contraintes unaires et XOR, et non un problème quadratique général.
6. Étude de deux complétions : différence supportée par des différences de cellules ; invariance forcée ; B_L²+B_L=8I ; production d'une similitude entière ZZ^T=33I de taille r. Argument mod 3 ⇒ 4|r ; capacité ⇒ 5≤r≤10 ; donc r=8. Distance de Hamming ⇒ au plus deux complétions.
7. Contrôles exacts : deux graphes positifs, 500 petits systèmes synthétiques. Les systèmes synthétiques ne sont pas des contre-exemples ou des modèles des axiomes de C2.
8. Limite : aucun N complet m=7 n'est disponible dans ce travail ; pas d'exclusion de classe revendiquée. Le résultat compresse le dernier relèvement, pas la génération préalable des N.
9. Pas de modification des dépôts distants, de lancement cloud, d'envoi de courriel ou de solveur massif.

## Correction de méthode

Exiger systématiquement une propriété « non impliquée par le modèle réduit complet » est trop fort : si ce modèle est impossible, il implique logiquement toute propriété. Une reformulation équivalente peut constituer un progrès si elle expose un mécanisme de décision ou de preuve beaucoup plus court. Ici, l'équation de Q est connue ; son espace de complétions affine et sa rigidité sont l'objet de l'étude.

## Nouveauté

Recherche ciblée dans les dépôts : extend_s_to_q, D-consistency, completions, Sylvester. Elle retrouve l'énumérateur historique, mais pas les propositions affines et de rigidité de cette note. Absence d'antériorité non certifiée : les recherches ciblées ne couvrent pas tous les fichiers, branches et publications.
