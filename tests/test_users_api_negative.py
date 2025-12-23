from utils.client import get

def test_get_unknown_endpoint_returns_404():
    r = get("/this-endpoint-does-not-exist")
    assert r.status_code == 404


def test_get_user_invalid_id_returns_404(invalid_user_id):
    r = get(f"/users/{invalid_user_id}")
    assert r.status_code == 404