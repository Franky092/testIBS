import pytest
import requests
from pages.api_pages.Base_api_page import UsersAPIPage

@pytest.mark.get_users
@pytest.mark.parametrize('page, per_page, expected_status', [
    (1, 6, 200),
    (1, 6, 200),
    (1, 10, 200)
])
def test_get_users(page, per_page, expected_status):
    api_page = UsersAPIPage()
    response = api_page.get_users(page=page, per_page=per_page)
    assert response.status_code == expected_status
    assert len(response.json()['data']) == per_page
    return response.status_code, response.text
