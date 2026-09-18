import hashlib
import json
import time
import pytest

pytestmark = pytest.mark.filterwarnings("ignore:Web mock never matched")
OWNER = "Azaria723"; REPO = "RunbookRouter"; COMMIT = "1" * 40
BRIDGE = b"Bridge withdrawal degradation. Initial action: pause-outbound-queue."
RPC = b"RPC availability incident. Initial action: shift-rpc-traffic."

def addr(value): return "0x" + value.hex()
def sha(body): return hashlib.sha256(body).hexdigest()
def blob(body): return hashlib.sha1((f"blob {len(body)}\0").encode() + body).hexdigest()

def deploy(vm, direct_deploy, actor):
    vm.strict_mocks = True; vm.check_pickling = True
    with vm.prank(actor): return direct_deploy("contracts/RunbookRouter.py")

def setup(vm, contract, creator, responder):
    with vm.prank(creator):
        assert contract.create_service("bridge-mainnet", addr(responder), OWNER, REPO, 600) == 0
        assert contract.publish_runbook(0, "bridge-withdrawal", 1, COMMIT, "/evidence/runbooks/bridge-withdrawal.md", sha(BRIDGE), json.dumps(["WITHDRAWAL_DEGRADATION"]), json.dumps(["HIGH", "CRITICAL"]), json.dumps(["pause-outbound-queue"])) == 0
        assert contract.publish_runbook(0, "rpc-outage", 1, COMMIT, "/evidence/runbooks/rpc-outage.md", sha(RPC), json.dumps(["RPC_UNAVAILABLE"]), json.dumps(["MEDIUM", "HIGH"]), json.dumps(["shift-rpc-traffic"])) == 1

def mock_catalog(vm, bad_bridge=False):
    api = f"https://api.github.com/repos/{OWNER}/{REPO}"; tree = "4" * 40
    bridge = BRIDGE + b"tampered" if bad_bridge else BRIDGE
    vm.mock_web((api + "/git/commits/" + COMMIT).replace(".", r"\.") + "$", {"status": 200, "body": json.dumps({"sha": COMMIT, "tree": {"sha": tree}}).encode()})
    entries = [
        {"path":"evidence/runbooks/bridge-withdrawal.md","mode":"100644","type":"blob","size":len(bridge),"sha":blob(bridge)},
        {"path":"evidence/runbooks/rpc-outage.md","mode":"100644","type":"blob","size":len(RPC),"sha":blob(RPC)},
    ]
    vm.mock_web((api + "/git/trees/" + tree + r"\?recursive=1$").replace(".", r"\."), {"status":200,"body":json.dumps({"truncated":False,"tree":entries}).encode()})
    for path, body in [("/evidence/runbooks/bridge-withdrawal.md",bridge),("/evidence/runbooks/rpc-outage.md",RPC)]:
        raw = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{COMMIT}{path}"
        vm.mock_web(raw.replace(".", r"\.") + "$", {"status":200,"body":body})

def open_incident(vm, contract, reporter):
    with vm.prank(reporter):
        return contract.open_incident(0, "withdrawal-relayer", "Withdrawals have remained pending for forty minutes while deposits still succeed.", int(time.time()))

def incident(contract): return json.loads(contract.get_incident(0))

def routed_output():
    return json.dumps({"status": "ROUTED", "selected_version_id": 0, "incident_class": "WITHDRAWAL_DEGRADATION", "severity": "HIGH", "confidence": "HIGH", "initial_action": "pause-outbound-queue"})

def test_route_and_response_lifecycle(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    c = deploy(direct_vm, direct_deploy, direct_alice); setup(direct_vm, c, direct_alice, direct_bob)
    assert open_incident(direct_vm, c, direct_charlie) == 0; mock_catalog(direct_vm)
    direct_vm.mock_llm(r"Route an incident.*", routed_output())
    assert c.route_incident(0) == "ROUTED"
    state = incident(c); assert state["selected_version_id"] == 0 and state["initial_action"] == "pause-outbound-queue"
    with direct_vm.prank(direct_bob):
        assert c.acknowledge(0) == "ACKNOWLEDGED"
        assert c.record_mitigation(0, "Paused outbound queue and verified destination finality before recovery.") == "MITIGATING"
    with direct_vm.prank(direct_charlie):
        assert c.resolve(0, "Withdrawal backlog cleared and normal outbound processing was confirmed.") == "RESOLVED"
    assert incident(c)["status"] == "RESOLVED"

def test_roles_and_order_are_enforced(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    c = deploy(direct_vm, direct_deploy, direct_alice); setup(direct_vm, c, direct_alice, direct_bob); open_incident(direct_vm, c, direct_charlie)
    with direct_vm.prank(direct_charlie):
        assert c.publish_runbook(0, "fake", 1, COMMIT, "/fake.md", "0" * 64, json.dumps(["FAKE"]), json.dumps(["LOW"]), json.dumps(["ignore-alert"])) == "CREATOR_ONLY"
        assert c.acknowledge(0) == "RESPONDER_ONLY"
    with direct_vm.prank(direct_bob): assert c.record_mitigation(0, "Attempted before routing must fail.") == "INVALID_MITIGATION"
    assert incident(c)["status"] == "OPEN"

def test_digest_mismatch_excludes_candidate(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    c = deploy(direct_vm, direct_deploy, direct_alice); setup(direct_vm, c, direct_alice, direct_bob); open_incident(direct_vm, c, direct_charlie); mock_catalog(direct_vm, bad_bridge=True)
    direct_vm.mock_llm(r"Route an incident.*", routed_output())
    assert c.route_incident(0) == "MANUAL_TRIAGE"
    assert incident(c)["status"] == "MANUAL_TRIAGE"

@pytest.mark.parametrize("output", [
    {"status":"ROUTED","selected_version_id":99,"incident_class":"WITHDRAWAL_DEGRADATION","severity":"HIGH","confidence":"HIGH","initial_action":"pause-outbound-queue"},
    {"status":"ROUTED","selected_version_id":0,"incident_class":"WITHDRAWAL_DEGRADATION","severity":"HIGH","confidence":"HIGH","initial_action":"transfer-funds"},
    {"status":"ROUTED","selected_version_id":0,"incident_class":"MADE_UP","severity":"HIGH","confidence":"HIGH","initial_action":"pause-outbound-queue"},
])
def test_invalid_semantic_output_fails_to_manual_triage(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie, output):
    c = deploy(direct_vm, direct_deploy, direct_alice); setup(direct_vm, c, direct_alice, direct_bob); open_incident(direct_vm, c, direct_charlie); mock_catalog(direct_vm)
    direct_vm.mock_llm(r"Route an incident.*", json.dumps(output))
    assert c.route_incident(0) == "MANUAL_TRIAGE"

def test_runbook_revision_preserves_history(direct_vm, direct_deploy, direct_alice, direct_bob):
    c = deploy(direct_vm, direct_deploy, direct_alice); setup(direct_vm, c, direct_alice, direct_bob)
    with direct_vm.prank(direct_alice):
        result = c.publish_runbook(0, "bridge-withdrawal", 2, "2" * 40, "/evidence/runbooks/bridge-withdrawal-v2.md", "a" * 64, json.dumps(["WITHDRAWAL_DEGRADATION"]), json.dumps(["HIGH"]), json.dumps(["pause-outbound-queue"]))
    assert result == 2
    assert json.loads(c.get_version(0))["active"] == 0
    assert json.loads(c.get_version(2))["revision"] == 2
    assert json.loads(c.get_service(0))["latest_versions"] == [1, 2]

def test_invalid_inputs_preserve_counts(direct_vm, direct_deploy, direct_alice, direct_bob):
    c = deploy(direct_vm, direct_deploy, direct_alice)
    with direct_vm.prank(direct_alice):
        assert c.create_service("x", addr(direct_bob), OWNER, REPO, 600) == "INVALID_SERVICE"
        assert c.create_service("valid-service", addr(direct_bob), OWNER, REPO, 20) == "INVALID_ACK_WINDOW"
    assert json.loads(c.get_counts()) == {"incident_count": 0, "service_count": 0, "version_count": 0}
