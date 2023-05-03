import pytest
import requests


@pytest.mark.parametrize('email, password, expected_status', [
    ("eve.holt@reqres.in", "mypass", 400),
    ("eve@reqres.in", "mypass", 400),
])
def test_successful_register(base_url, email, password, expected_status):
    data = {
        "email": f"{email}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/register", json=data, headers=headers)

    assert response.status_code == expected_status
    assert response.json()['error'] == "Missing password"
