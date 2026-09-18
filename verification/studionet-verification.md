# StudioNet verification

Contract: [`0x842cd47793b3A0dB2B72cf569DB7344071968fA1`](https://explorer-studio.genlayer.com/address/0x842cd47793b3A0dB2B72cf569DB7344071968fA1) on GenLayer StudioNet, chain ID `61999`.

## Source parity and clean start

- Deployed source SHA-256: `852eae81df1471cc052212ccd068c1b37a58abef0bfc625bab88f434d7d1a1c0`
- Repository source SHA-256: `852eae81df1471cc052212ccd068c1b37a58abef0bfc625bab88f434d7d1a1c0`
- Exact source parity: `true`.
- Initial counters: services `0`, versions `0`, incidents `0`.

## Immutable sources

All four runbooks are bound to repository `Azaria723/RunbookRouter`, full commit `f3107082d3c1e0ab2198338b6dc79f9a2efec22a`, exact paths and fetched-byte SHA-256 commitments. The final catalog readback contains four active version records with the expected commit, digest and bounded routing vocabulary.

## Live transactions

| Operation | Transaction | Verified effect |
|---|---|---|
| Create service | [`0xf915…af73`](https://explorer-studio.genlayer.com/tx/0xf9152648e3954031ffad7672af03783c03cd0129e63b443774cc1fc5ecffaf73) | Service 0 binds repository authority, responder and 600-second acknowledgement window |
| Publish bridge runbook | [`0x42ea…4c89`](https://explorer-studio.genlayer.com/tx/0x42ea01cc35d09819b42741a96c5af01d28ebbc7d01015530e8e38337c5f94c89) | Version 0, `WITHDRAWAL_DEGRADATION` |
| Publish RPC runbook | [`0xbdda…e95c`](https://explorer-studio.genlayer.com/tx/0xbdda554a064bcbf3e53c109fd0ff1eb2a449d311fe3bc83569d3976d803e95c1) | Version 1, `RPC_UNAVAILABLE` |
| Publish oracle runbook | [`0xf1a0…d42b`](https://explorer-studio.genlayer.com/tx/0xf1a07ba8654c05b8556618362e4596dbfdbd74ed0da8538052fd8eb45eb4d42b) | Version 2, `ORACLE_STALE` |
| Publish frontend runbook | [`0xea90…6d95`](https://explorer-studio.genlayer.com/tx/0xea909d8d7443dfa4655aaac58d81d5c96d203edde7dab2c4212a54af45fa6d95) | Version 3, `FRONTEND_DEGRADATION` |
| Open incident | [`0x1066…54f3`](https://explorer-studio.genlayer.com/tx/0x1066db92bb725f3f807e98e8c3089b0bf6c921a6e88d748d7a847a93259154f3) | Incident 0 records withdrawal-relayer symptoms |
| Route incident | [`0x4b2c…f70c`](https://explorer-studio.genlayer.com/tx/0x4b2cd91e77fb45ef84db4564509a255a3db88c07d5ba58f9497915b47bfbf70c) | Validators select version 0 with bounded output |
| Acknowledge | [`0x33ee…c692`](https://explorer-studio.genlayer.com/tx/0x33ee88927998cc5ca6120e2ca056725dc8daf5251b068555a92b47f9ad63c692) | Bound responder accepts the route before deadline |
| Record mitigation | [`0x621b…3aac`](https://explorer-studio.genlayer.com/tx/0x621bfac2ecb42572ee62263bb4ae759d68ecf27044c73b1fa9d088b774013aac) | Incident advances to `MITIGATING` with operational note |
| Resolve | [`0x92c1…17da`](https://explorer-studio.genlayer.com/tx/0x92c1353f6f9ddb09cc7a28f500ab8177bf831ef78049721245d0c796e97b17da) | Original reporter confirms recovery; final status `RESOLVED` |

## Semantic route readback

```json
{
  "status": "ROUTED",
  "selected_version_id": 0,
  "incident_class": "WITHDRAWAL_DEGRADATION",
  "severity": "HIGH",
  "confidence": "HIGH",
  "initial_action": "pause-outbound-queue"
}
```

## Final authoritative state

- Counters: services `1`, versions `4`, incidents `1`.
- Incident 0 status: `RESOLVED`.
- The selected runbook remains version 0 at the immutable fixture commit.
- Acknowledgement occurred before the stored deadline.
- Mitigation and resolution notes are preserved in contract state.

This proves the architectural boundary: validator consensus selected a verified response starting point; deterministic role checks controlled acknowledgement, mitigation and resolution. The deployment account received no implicit lifecycle authority.

## Adversarial coverage

Direct Mode `12/12` tests cover digest mismatch, unverified-candidate exclusion, malformed/out-of-vocabulary semantic output, wrong roles, invalid transition order, route replay, version-history preservation and permissionless overdue escalation. These failure paths preserve protected state and require no deployment-account participation.
