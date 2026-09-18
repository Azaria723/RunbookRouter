# Adversarial test matrix

The contract is exercised in GenLayer Direct Mode with strict web mocks and deterministic LLM outputs. The deployed StudioNet instance separately proves the complete successful lifecycle. Direct Mode is used for destructive and malformed-input branches so public verification does not pollute the canonical deployment state.

## Verified branches

| Boundary | Cases |
|---|---|
| GitHub availability | commit, tree and raw `404`; total web unavailability; malformed JSON; oversized commit, tree and raw bodies |
| Immutable Git identity | mismatched commit SHA; malformed tree SHA; truncated tree; missing and duplicate paths; wrong byte size; wrong Git blob SHA-1; wrong SHA-256 |
| Semantic output | nonexistent version; unregistered class; unregistered action; prompt-injection attempt; explicit no-match; replay after manual triage |
| Authorization | creator-only publishing; responder-only acknowledgement and mitigation; reporter-only resolution |
| Lifecycle | resolve before mitigation; expired acknowledgement; premature escalation; permissionless overdue escalation; replay after resolution |
| State integrity | append-only revision history; invalid inputs preserve counters; nonexistent IDs return bounded errors |
| Input boundaries | service key and acknowledgement window; taxonomy JSON, duplicates, cardinality and vocabulary; component, description and observation time |
| Architecture | comparative consensus is present; `strict_eq` and prior-project mechanisms are absent |

## Results

- Direct Mode: `44 passed`.
- StudioNet happy path: service creation, four immutable runbooks, incident opening, semantic route, acknowledgement, mitigation and reporter-confirmed resolution.
- Deployed/local contract source parity remains exact because this expansion adds tests and documentation only.

## Design limitation found during audit

`service.active` and `version.active` are stored and checked, but this deployed version exposes no public deactivation method. Consequently, inactive-service behavior cannot be reached through a valid transaction and was not fabricated by mutating Direct Mode storage. Version replacement is covered: publishing a valid next revision removes the prior version from the current catalog while preserving its readable history.

This is an adversarial regression suite, not a claim of independent third-party audit or formal verification.
