import pytest
import requests
@pytest.mark.get_users
@pytest.mark.parametrize('delay, per_page, expected_status', [
    (1, 6, 200),
    (2, 6, 200),
    (1, 10, 200)
])
def test_get_users(base_url, delay, per_page, expected_status):
    response = requests.get(f'{base_url}/users', params={'delay': delay, 'per_page': per_page})
    assert response.status_code == expected_status
    assert len(response.json()['data']) == per_page
