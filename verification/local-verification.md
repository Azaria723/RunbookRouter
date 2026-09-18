# Local verification

- Direct Mode contract suite: `12 passed`.
- Frontend production build: passed.
- Contract source SHA-256: `852eae81df1471cc052212ccd068c1b37a58abef0bfc625bab88f434d7d1a1c0`.
- Strict web mocks and contract serialization checks are enabled.
- Positive coverage: verified multi-candidate routing and the full route → acknowledge → mitigate → resolve lifecycle.
- Adversarial coverage: fetched-byte digest mismatch, unverified candidate exclusion, nonexistent selection, out-of-vocabulary action/class, wrong roles, invalid order, invalid service configuration, terminal route replay and protected-state preservation.
- Liveness coverage: a missed acknowledgement deadline enables permissionless escalation and prevents late acknowledgement.
- Revision coverage: successor publication deactivates the former routing candidate while preserving historical state.
- Originality check: no ballot, quorum, council, escrow, two-document comparison, registry-consumption or snapshot-journal architecture.
