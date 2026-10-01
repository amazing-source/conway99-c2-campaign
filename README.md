# Conway 99 · C2 exact-decision research campaign

**Campaign snapshot:** 2026-10-01  
**Problem:** the involution (`C2`) branch of a putative `srg(99,14,1,2)`  
**Current verdict:** **OPEN** — no complete witness and no universal contradiction is known in this campaign.

This repository is a research handoff and campaign ledger. Its purpose is to keep the exact mathematical target, proved/reported reductions, failed mechanisms, computational backstops, and AI-research experiments in one place without silently promoting evidence into proof.

## The exact question

The current clean formulation is a 42-label problem.

Let `R` be the canonical 42×7 matrix of positive `D7` roots `e_i+e_j, e_i-e_j` for `1 <= i < j <= 7`, and set

\[
M=|R|,\qquad H=RR^T,\qquad K=MM^T.
\]

The coupled formulation seeks integer symmetric zero-diagonal 42×42 matrices `Q,N` satisfying

\[
NR=0,\qquad N^2=N+12I-H,
\]

\[
Q^2+Q+K=12I+4J,\qquad QM=4J_{42,7}-2M,
\]

and for every `x != y`

\[
(Q_{xy}-1)^2+N_{xy}^2=1.
\]

Thus every unordered pair is in exactly one of four states:

| state | `Q_xy` | `N_xy` | meaning |
|---|---:|---:|---|
| `n` | 0 | 0 | null |
| `d` | 2 | 0 | double-partner |
| `m` | 1 | -1 | signed edge |
| `p` | 1 | +1 | signed edge |

From a solution,

\[
B=[Q=1],\qquad D=[Q=2].
\]

The `d` relation is a perfect matching on the 42 exterior involution-orbits. Together with `N`, it reconstructs the exterior graph and then the full 99-vertex adjacency matrix.

See [`theorems/THEOREM_C.md`](theorems/THEOREM_C.md).

## Why this repo exists

The campaign moved through several layers:

1. an exact completion theorem (`T4`) for a fixed signed core `N`;
2. a ternary/capacity reformulation;
3. the coupled `(Q,N)` four-state formulation;
4. many representation experiments, most of which were killed or identified as rediscoveries;
5. a finite lattice-envelope route (`Route C`) kept as a computational safety net;
6. a proposed native exact solver for the four-state system;
7. an AI-research campaign designed to reduce repeated convergence into the same mathematical attractor basins.

The repository is intentionally conservative about status.

## Current major results

| ID | Result | Campaign status | What it does **not** prove |
|---|---|---|---|
| `T4` | For a complete valid `N`, the real completion system `L_N` is empty or a singleton integral perfect matching | written proof; campaign reports a blind independent audit | does not prove such an `N` exists or that all `L_N` are empty |
| `TC` | Exact coupled formulation in `(Q,N)` alone; `D=[Q=2]` | proved in-session; elementary; needs independent archival audit | does not shrink the solution set |
| `TRI` | Mod-3 signed equations + pointwise capacities force the exact integer signed equations | written proof; independently checked once in the campaign | does not prove any admissible projector exists or fails |
| `RC` | Response-card boundary quotient is exact but non-compressive | exact negative result; concrete C2 correction strengthens it | does not provide a smaller global state space |
| `C3` | Order-3 branch is recorded elsewhere as closed by the project | separate campaign result; not used in the C2 theorems here | does not decide C2 or asymmetric existence |

## What would settle C2

### Positive

One exact solution `(Q,N)` of the coupled system is enough.

Reconstruct `D`, then the full 99×99 adjacency matrix `A`, and independently verify

\[
A^2+A=12I+2J.
\]

That proves a Conway graph exists and has the prescribed involution.

### Negative

Prove no coupled solution exists.

Equivalently, in the older `T4` formulation prove

\[
\forall N\in\mathcal N,\qquad L_N=\varnothing.
\]

Extending the normalized one-fixed-point conclusion to all involutions uses the separate fixed-point input `F0`.

**C2 false does not imply Conway false.** A completely asymmetric graph could still exist.

## Active campaign lanes

### A · conceptual / representation discovery

Search for a genuinely global language for joint `(Q,N)` realizability. Large local-radius escalation is currently treated as a known failure mode.

### B · Route C finite computation

A separate odd-unimodular-envelope route reduces the involution branch to 156 rank-24 envelopes. The live campaign report currently says **91/156 excluded** and estimates roughly **6,600 CPU-hours** for the remaining finite work. These numbers are **campaign-reported and must be reconciled with the canonical Route-C tracker before publication**.

See [`compute/ROUTE_C.md`](compute/ROUTE_C.md).

### C · native four-state solver

Build an exact solver directly on the 861 four-valued pair variables instead of expanding the mathematics into a generic CNF first.

See [`compute/NATIVE_SOLVER.md`](compute/NATIVE_SOLVER.md).

## Reading order

1. [`STATUS.md`](STATUS.md)
2. [`docs/NATIVE_MODEL.md`](docs/NATIVE_MODEL.md)
3. [`theorems/T4_RECONSTRUCTION.md`](theorems/T4_RECONSTRUCTION.md)
4. [`theorems/THEOREM_C.md`](theorems/THEOREM_C.md)
5. [`theorems/TERNARY_CAPACITY.md`](theorems/TERNARY_CAPACITY.md)
6. [`research/FAILURE_MEMORY.md`](research/FAILURE_MEMORY.md)
7. [`research/REPRESENTATION_EXPERIMENTS.md`](research/REPRESENTATION_EXPERIMENTS.md)
8. [`ROADMAP.md`](ROADMAP.md)
9. [`provenance/STATUS_LABELS.md`](provenance/STATUS_LABELS.md)

## Archived source material

`archive/` contains preserved source documents from the campaign:

- `FULL_DOSSIER.md` — the consolidated T4/reconstruction handoff.
- `TERNARY_PROOF.md` — the ternary/capacity note.
- `RESPONSE_CARD_RAW.md` — the fresh-session response-card analysis before the concrete-D7 correction.

These files are preserved rather than silently rewritten.

## Research discipline

A timeout is not evidence.  
A symmetry-restricted failure is not a universal exclusion.  
A modular lift is not a graph.  
A reformulation is not a contradiction.  
A solver result is only as strong as the encoded domain and its certificate.  
A novelty claim is separate from a truth claim.
