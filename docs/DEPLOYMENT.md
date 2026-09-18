# Deployment plan

1. Run all Direct Mode tests and the frontend production build.
2. Push the complete repository, including the synthetic runbook fixtures.
3. Record the immutable full commit containing the fixtures and recompute their exact byte SHA-256 values.
4. Deploy the exact `contracts/RunbookRouter.py` source to StudioNet without constructor arguments.
5. Verify deployed/local source byte parity before any writes.
6. Create one service with a dedicated responder and the repository coordinates.
7. Publish the four runbooks from the immutable commit with their exact digests and bounded taxonomies.
8. Exercise a matched route, manual-triage route, wrong-role transitions, successful response lifecycle and overdue escalation.
9. Retain transaction links and authoritative post-state reads.

Never publish credentials or describe private account orchestration in public evidence.
