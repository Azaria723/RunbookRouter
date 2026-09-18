# RunbookRouter

RunbookRouter is a GenLayer intelligent-contract dApp for evidence-bound incident dispatch. Validators verify a bounded catalog of immutable operational runbooks and semantically route an incident to the best matching response procedure. Deterministic roles then govern acknowledgement, mitigation and resolution.

Live application: [runbook-router.pages.dev](https://runbook-router.pages.dev)

## Why GenLayer

Symptom reports rarely match runbook titles word-for-word. `route_incident` uses comparative validator consensus to select among verified candidates, while the contract constrains every selected class, severity and action to the chosen runbook's registered vocabulary. If no source is verifiable, no candidate materially matches, or model output leaves the vocabulary, the incident fails safely to `MANUAL_TRIAGE`.

## Architecture

```text
Versioned runbook catalog
       ↓ immutable Git source + fetched-byte digest verification
Open incident
       ↓ bounded multi-candidate semantic routing
ROUTED or MANUAL_TRIAGE
       ↓ responder-only acknowledgement and mitigation
Reporter-confirmed RESOLVED / permissionless overdue ESCALATED
```

The deployer receives no implicit operational authority. Each service stores its creator and responder explicitly. AI routing cannot acknowledge, mitigate, resolve or escalate an incident.

## Local verification

```bash
python -m pip install -r requirements.txt
python -m pytest -q
cd frontend
npm install
npm run build
```

Current result: `44 passed`; production frontend build passed.

See [architecture](docs/ARCHITECTURE.md), [threat model](docs/THREAT_MODEL.md), [deployment plan](docs/DEPLOYMENT.md), and [fixture manifest](verification/fixture-manifest.md).

## Immutable test source

The four synthetic runbooks are pinned to commit `f3107082d3c1e0ab2198338b6dc79f9a2efec22a`. Their public raw responses were fetched after push and independently matched the recorded byte lengths and SHA-256 commitments.

## Verified StudioNet deployment

- Frontend: [https://runbook-router.pages.dev](https://runbook-router.pages.dev)
- Contract: [`0x842cd47793b3A0dB2B72cf569DB7344071968fA1`](https://explorer-studio.genlayer.com/address/0x842cd47793b3A0dB2B72cf569DB7344071968fA1)
- Chain ID: `61999`
- Deployed/local source SHA-256: `852eae81df1471cc052212ccd068c1b37a58abef0bfc625bab88f434d7d1a1c0`
- Live lifecycle: four verified runbooks → matched incident route → responder acknowledgement → mitigation → reporter-confirmed resolution.

See [StudioNet verification](verification/studionet-verification.md) for transaction links and final authoritative state, and the [adversarial test matrix](verification/adversarial-test-matrix.md) for failure-path coverage and its explicit limitation.
