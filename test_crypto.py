from keyring.backend import get_all_keyring
import pytest
import foo

@pytest.fixture(scope="module", autouse=True)
def ensure_keyring_backends() -> None:
    get_all_keyring()

def test_one():
    assert 1 + 1 == 2
