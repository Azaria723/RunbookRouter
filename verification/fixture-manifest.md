# Test resource manifest

All resources are synthetic operational examples maintained inside this repository. They do not describe a real incident.

| Resource | Canonical path | Bytes | SHA-256 | Expected route |
|---|---|---:|---|---|
| Bridge withdrawal | `/evidence/runbooks/bridge-withdrawal.md` | 292 | `bbb1f4fd5cc1d7e2d52f31abdc4b12c3dbbe1d0a9d57b8ee56c13ecffecfc96f` | `WITHDRAWAL_DEGRADATION` / `pause-outbound-queue` |
| RPC outage | `/evidence/runbooks/rpc-outage.md` | 278 | `6e1674c663401648c102098d753d8597511fa2fb242e7f2b4be92717cb5df9c0` | `RPC_UNAVAILABLE` / `shift-rpc-traffic` |
| Oracle stale price | `/evidence/runbooks/oracle-stale.md` | 315 | `dbac45d53679abc272ea4b26f37eb1f7902866b35d406372ab1c157f22b6e83f` | `ORACLE_STALE` / `freeze-price-dependent-actions` |
| Frontend degradation | `/evidence/runbooks/frontend-degradation.md` | 298 | `0fa305ca4645f7d4f15363e54d28c50d4f8b4c6def5b20ae11e0e3f277fd924f` | `FRONTEND_DEGRADATION` / `activate-static-status-page` |

The immutable Git commit is filled only after the repository is pushed. At runtime the contract independently verifies commit identity, complete tree, blob metadata, Git SHA-1 and fetched-byte SHA-256.
