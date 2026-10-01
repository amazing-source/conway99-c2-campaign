# Contributing research results

This is a mathematical research repository. The primary contribution standard is **scope discipline**.

For every result, record:

1. exact hypotheses;
2. exact conclusion;
3. proof or computation;
4. domain processed;
5. evidence level;
6. duplication check;
7. consequence for EX / NOT-EX.

## Computational contributions

Never commit only a terminal screenshot.

Include:

- input identifier/hash;
- exact program/version;
- parameters;
- output;
- verifier;
- certificate where possible;
- controls.

## New representations

A representation is worth archiving even if it does not solve C2, provided it has:

- an exact definition;
- at least one nontrivial derived law;
- a clear account of what information it forgets;
- a falsification/compression test.

If it collapses to a known route, record the duplication and close it.

## Failed attempts

Do not delete them. Add the failure mechanism to `research/FAILURE_MEMORY.md`.

A clean counterexample to an attractive lemma is a research result.
