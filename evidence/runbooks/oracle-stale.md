# Oracle stale price incident

Use when an oracle price timestamp exceeds the permitted freshness window or diverges materially from reference markets.

Initial action: freeze-price-dependent-actions

Inspect the last successful update, feeder availability and deviation guard before resuming dependent operations.
