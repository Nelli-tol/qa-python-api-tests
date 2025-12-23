from utils.client import get, post


def test_get_users_returns_list():
    r = get("/users")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

    first = data[0]
    assert "id" in first
    assert "email" in first
    assert "username" in first


def test_get_user_by_id():
    r = get("/users/1")
    assert r.status_code == 200

    u = r.json()
    assert u["id"] == 1
    assert "email" in u and "@" in u["email"]


def test_create_post_contract_check():
    payload = {"title": "qa test", "body": "hello", "userId": 1}
    r = post("/posts", json=payload)

    assert r.status_code == 201

    created = r.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]
    assert "id" in created