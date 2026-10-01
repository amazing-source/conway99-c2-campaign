# Route C · finite lattice-envelope backstop

## Role

Route C is the campaign's finite NOT-EX safety net.

The established route reduces the normalized involution problem to a finite list of **156** odd unimodular rank-24 lattice envelopes, followed by exact frame/admissibility checks.

## Reported status

Current conversation-level report:

\[
91/156
\]

excluded.

Reported remaining computational cost:

\[
\approx 6600\text{ CPU-hours}.
\]

**Important:** these numbers were supplied during the live campaign and are not automatically synchronized with the canonical Route-C tracker. Before launching a farm, reconcile every envelope ID and status against the authoritative repository.

## Why keep Route C alive

Conceptual research can stall or rediscover old ideas.

Finite exact computation has monotone value:

\[
91\to92\to\cdots\to156.
\]

If every envelope is rigorously excluded under an exhaustive and correct reduction, C2 is excluded.

A surviving envelope is **not** by itself a Conway graph.

## Execution principles

For every envelope, track only:

- `CERTIFIED_EXCLUDED`
- `OPEN`
- `PARTIAL`
- `ERROR`

Never convert timeout/UNKNOWN into exclusion.

Preserve:

- lattice identifier;
- exact basis/hash;
- code commit;
- parameters;
- certificate or independently checkable witness of infeasibility;
- verifier;
- runtime / memory;
- controls.

## Workload strategy

Separate the remaining cases into:

1. cheap throughput;
2. medium exact jobs;
3. hard-tail research cases.

Do not allow one Golay/O24-like hard family to monopolize all resources.

Whenever many envelopes fail for the same reason, stop and attempt to promote that repeated computational reason into a family-level mathematical lemma.

## Local-machine sanity estimate

At 6,600 CPU-hours and 18 perfectly utilized hardware threads, the idealized wall time is roughly 367 hours (~15 days). Real wall time will be higher because scaling, thermal limits, verification, and case imbalance are not perfect.

Cloud compute can reduce wall time if the workload is embarrassingly parallel.

## Publication standard

A final `156/156` statement must be backed by an auditable manifest, not by a folder of successful terminal logs.
