import pytest
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


@pytest.mark.parametrize("user_id", [1, 2, 3, 5])
def test_get_user_by_id_parametrized(user_id: int):
    r = get(f"/users/{user_id}")
    assert r.status_code == 200

    data = r.json()
    assert data["id"] == user_id
    assert "email" in data and "@" in data["email"]


def test_get_user_by_id_from_fixture(valid_user_id: int):
    r = get(f"/users/{valid_user_id}")
    assert r.status_code == 200
    assert r.json()["id"] == valid_user_id


def test_get_user_not_found(invalid_user_id: int):
    r = get(f"/users/{invalid_user_id}")
    assert r.status_code == 404


def test_create_post_contract_check():
    payload = {"title": "qa test", "body": "hello", "userId": 1}
    r = post("/posts", json=payload)

    assert r.status_code == 201
    data = r.json()

    # jsonplaceholder returns id for created resource (fake but consistent)
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]