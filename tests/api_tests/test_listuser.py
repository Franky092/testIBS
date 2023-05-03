import pytest
import requests
from pages.api_pages.Base_api_page import UsersAPIPage

@pytest.mark.get_users
@pytest.mark.parametrize('page, per_page, expected_status', [
    (1, 6, 200),
    (1, 6, 200),
    (1, 10, 200)
])
def test_get_users(base_url, page, per_page, expected_status):
    response = requests.get(f'{base_url}/users', params={'page': page, 'per_page': per_page})
    assert response.status_code == expected_status
    assert len(response.json()['data']) == per_page
    return response.status_code, response.text