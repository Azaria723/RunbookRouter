from pathlib import Path

SOURCE = Path("contracts/RunbookRouter.py").read_text()

def test_uses_comparative_semantics_and_verified_sources():
    for token in ["gl.eq_principle.prompt_comparative", "gl.nondet.web.get", "gl.nondet.exec_prompt", "_blob_sha1", "hashlib.sha256(response.body)"]:
        assert token in SOURCE
    assert "strict_eq" not in SOURCE

def test_architecture_is_routing_lifecycle_not_prior_projects():
    for token in ["def publish_runbook", "def route_incident", "def acknowledge", "def record_mitigation", "def resolve", "def escalate_overdue"]:
        assert token in SOURCE
    for forbidden in ["def vote", "quorum", "ballots", "escrow", "compare two repository license"]:
        assert forbidden not in SOURCE.lower()
