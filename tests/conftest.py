import pytest


@pytest.fixture
def valid_user_id() -> int:
    return 1


@pytest.fixture
def invalid_user_id() -> int:
    return 9999