# Native representation inventor

Treat `docs/NATIVE_MODEL.md` as trusted input.

For the invention phase, do **not** reconstruct the problem as a matrix, spectrum, lattice, code, Hodge complex, group action, SAT/ILP model, or modular-rank problem.

The task is not to prove EX/NOT-EX immediately.

The task is:

> Replace the primitives of the native four-state problem so that global extendability or global closure becomes simpler.

Develop at least three genuinely different primitive descriptions.

For each record:

- primitives;
- exact definition;
- legal local move;
- information forgotten;
- information made simple;
- exact laws;
- examples/counterexamples;
- how partial objects compose;
- what can go wrong under composition.

Focus especially on the empirical phenomenon that small exact pieces usually extend.

Try to define a boundary/defect object for a valid partial assignment `P`:

\[
\partial P
\]

such that extension depends only on `∂P`.

Test order of extension: if adding A then B versus B then A leaves a discrepancy, define the discrepancy before naming the theory it resembles.

If a representation repeatedly says “I need a larger neighborhood,” stop and mutate the representation instead.

Do not read the old repository until a new object has:
1. a precise definition;
2. at least two exact nontrivial laws;
3. a reason it may affect extension/closure.

Then perform a targeted duplication check.

The goal is not sophistication. It is to discover what the exact problem is actually made of.
