from utils.client import get

def test_get_user_invalid_id_returns_404(invalid_user_id):
    r = get(f"/users/{invalid_user_id}")
    assert r.status_code == 404
