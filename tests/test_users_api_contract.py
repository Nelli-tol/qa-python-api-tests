from utils.client import get

def test_users_schema_contract():
    r = get("/users")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list) and len(data) > 0

    u = data[0]
    # contract keys
    for k in ["id", "name", "username", "email"]:
        assert k in u

    # basic field rules
    assert isinstance(u["id"], int)
    assert "@" in u["email"]