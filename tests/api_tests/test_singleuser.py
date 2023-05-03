import pytest
import requests


@pytest.mark.parametrize('page, email, expected_status', [
    (2, "janet.weaver@reqres.in", 200),
    (3, "emma.wong@reqres.in", 200),
    (4, "eve.holt@reqres.in", 200),
])
def test_get_user(base_url, page, email, expected_status):
    response = requests.get(f'{base_url}/users/{page}')
    assert response.status_code == expected_status
    assert response.json()['data']["email"] == email


@pytest.mark.parametrize('page, expected_status', [
    (50, 404),
    (52, 404),
    (99, 404),
])
def test_get_nonexistent_user(base_url, page, expected_status):
    response = requests.get(f'{base_url}/users/{page}')
    assert response.status_code == expected_status


