import pytest
import requests


@pytest.mark.parametrize('sumpeople, expected_status', [
    (6, 200)
])
def test_get_list_resource(base_url, sumpeople, expected_status):
    response = requests.get(f'{base_url}/unknown')
    assert response.status_code == expected_status
    assert len([user["id"] for user in response.json()['data']]) == sumpeople
