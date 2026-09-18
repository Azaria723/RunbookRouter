# Local verification

- Direct Mode contract suite: `44 passed`.
- Frontend production build: passed.
- Cloudflare Pages production: [`https://runbook-router.pages.dev`](https://runbook-router.pages.dev), HTTP `200`; deployed bundle contains the verified contract address and adversarial-evidence link.
- Contract source SHA-256: `852eae81df1471cc052212ccd068c1b37a58abef0bfc625bab88f434d7d1a1c0`.
- Strict web mocks and contract serialization checks are enabled.
- Positive coverage: verified multi-candidate routing and the full route → acknowledge → mitigate → resolve lifecycle.
- Adversarial coverage: unavailable/malformed/oversized GitHub responses; commit, tree, blob, size and digest mismatches; prompt injection; nonexistent selection; out-of-vocabulary action/class; wrong roles; invalid order; boundary inputs; terminal replay and protected-state preservation.
- Liveness coverage: a missed acknowledgement deadline enables permissionless escalation and prevents late acknowledgement.
- Revision coverage: successor publication deactivates the former routing candidate while preserving historical state.
- Originality check: no ballot, quorum, council, escrow, two-document comparison, registry-consumption or snapshot-journal architecture.
- Immutable-source preflight: commit `f3107082d3c1e0ab2198338b6dc79f9a2efec22a`; all four GitHub raw fixtures returned HTTP `200` with exact byte-length and SHA-256 parity.
