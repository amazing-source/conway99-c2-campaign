# Status labels

Use these labels literally.

- `PROVED-HERE` — a written mathematical proof exists in this campaign.
- `AUDITED-IN-CAMPAIGN` — a separate blind agent reportedly rederived/checked the argument.
- `FORMALLY-VERIFIED` — proof assistant or independently checkable formal certificate. Do not use unless actually available.
- `COMPUTED` — exact computation completed on its stated domain.
- `CERTIFIED-UNSAT` — exact unsatisfiability result with a preserved independently checkable proof/certificate.
- `SOLVER-UNSAT` — solver reported UNSAT but a proof certificate has not been archived.
- `UNKNOWN` — timeout or undecided.
- `REPORTED` — described in campaign logs but underlying proof/code artifacts are not present in this repository.
- `DUPLICATE` — targeted check found the mechanism/results already in project notes.
- `REFORMULATION` — exact equivalent language; does not shrink the solution set by itself.
- `SUPERSEDED` — stronger later result exists.
- `REFUTED` — explicit counterexample/error invalidates the claim.
- `OPEN` — unresolved.
- `HEURISTIC` — evidence only.

## Non-negotiable implications

`UNKNOWN != SAT` and `UNKNOWN != UNSAT`.

`SOLVER-UNSAT != CERTIFIED-UNSAT`.

A branch exclusion is not a universal exclusion.

A symmetry-restricted exclusion is not a generic exclusion.

A feasible relaxation is not a graph.

A modular model is not an integer graph.

A beautiful representation is not a contradiction.
