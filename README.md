# RunbookRouter

RunbookRouter is a GenLayer intelligent-contract dApp for evidence-bound incident dispatch. Validators verify a bounded catalog of immutable operational runbooks and semantically route an incident to the best matching response procedure. Deterministic roles then govern acknowledgement, mitigation and resolution.

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

Current result: `10 passed`; production frontend build passed.

See [architecture](docs/ARCHITECTURE.md), [threat model](docs/THREAT_MODEL.md), [deployment plan](docs/DEPLOYMENT.md), and [fixture manifest](verification/fixture-manifest.md).
