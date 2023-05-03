import pytest
import requests

@pytest.mark.parametrize('page, expected_status', [
    (1, 204),
    (2, 204),
    (3, 204),
    (4, 204)
])
def test_delete_user(base_url, page, expected_status):

    response = requests.delete(f"{base_url}/users/{page}")
    assert response.status_code == expected_status
