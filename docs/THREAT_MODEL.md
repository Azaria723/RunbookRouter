# Threat model

| Threat | Control |
|---|---|
| Attacker-shaped source URL | Users never submit a URL; the contract derives GitHub API and raw URLs from service-bound owner/repository, full commit and validated path. |
| Mutable or substituted content | Full commit, tree identity, Git blob identity, byte length and recomputed SHA-256 must all agree. |
| Truncated repository tree | `truncated` must be exactly `false`; oversized responses fail closed. |
| Prompt injection inside runbook or incident | Prompt marks all bodies as untrusted quoted data; output is schema- and vocabulary-bound. |
| Hallucinated route/action | Selected version must be in the verified candidate set; class, severity and action must exist in its metadata. |
| Unavailable source | Candidate is excluded; zero verified candidates produces `MANUAL_TRIAGE`. |
| Model disagreement or malformed output | Comparative consensus plus deterministic validation falls back to `MANUAL_TRIAGE`. |
| Unauthorized workflow mutation | Responder and reporter roles are checked independently for each transition. |
| Skipped workflow stage | Each write accepts only its exact predecessor state. |
| Silent responder | A routed incident can be permissionlessly moved to `ESCALATED` after the bound deadline. |
| Runbook rewrite | Revisions are append-only and old versions remain readable. |

RunbookRouter does not execute emergency actions itself. It records a verified route and accountable response lifecycle.
