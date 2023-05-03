import pytest
import requests


@pytest.mark.parametrize('email, password, token, expected_status', [
    ("eve.holt@reqres.in", "cityslicka", 'QpwL5tke4Pnpja7X4', 200)
])
def test_login_successfull(base_url, email, password, token, expected_status):
    data = {
        "email": f"{email}",
        "password": f"{password}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/login", json=data, headers=headers)

    assert response.status_code == expected_status
    assert response.json()['token'] == f'{token}'

@pytest.mark.parametrize('email, password, token, expected_status', [
    ("eve.holt@reqres.in", "cityslicka", 'QpwL5tke4Pnpja7X4', 400)
])
def test_login_unsuccessfull(base_url, email, password, token, expected_status):
    data = {
        "email": f"{email}",
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/login", json=data, headers=headers)

    assert response.status_code == expected_status
    assert response.json()['error'] == "Missing password"
