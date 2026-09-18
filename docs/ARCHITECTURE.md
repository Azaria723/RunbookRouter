# Architecture

## Persistent objects

RunbookRouter stores three different object families:

1. **Services** bind an operator, responder, repository authority and acknowledgement window.
2. **Runbook versions** are append-only source commitments. Publishing a successor deactivates the previous routing candidate but preserves its readable history.
3. **Incidents** are workflow records with a reporter, frozen semantic route, deadlines and response notes.

This is not a two-document comparison, evidence registry, council, ballot system, escrow or one-shot authorization gate.

## Routing boundary

For each active candidate, validators independently derive GitHub URLs from service configuration, verify the full commit, complete tree, exact path, regular-blob mode, Git blob identity, length and SHA-256 of fetched bytes. Unverified candidates are excluded.

`prompt_comparative` selects at most one candidate. The contract accepts `ROUTED` only when the version exists in the verified candidate set and the class, severity and initial action are members of that version's registered vocabulary. All other results become `MANUAL_TRIAGE`.

## Authority boundary

- Service creator: publishes runbook revisions.
- Any account: opens and routes an incident.
- Bound responder: acknowledges and records mitigation.
- Original reporter: confirms resolution.
- Any account: escalates a routed incident after its acknowledgement deadline.

The semantic outcome supplies a response starting point; deterministic state and roles control execution.
