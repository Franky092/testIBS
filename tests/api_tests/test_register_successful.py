import pytest
import requests

#Кейс с неверными данными
@pytest.mark.parametrize('email, password, expected_status', [
    ("eve.holt@reqres.in", "mypass", 200),
    ("eve@reqres.in", "mypass", 200),
])
def test_successful_register(base_url, email, password, expected_status):
    data = {
        "email": f"{email}",
        "password": f"{password}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/register", json=data, headers=headers)

    assert response.status_code == expected_status
    assert response.json()['id'] == 4
