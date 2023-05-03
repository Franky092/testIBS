from pages.api_pages.Base_api_page import UsersAPIPage


def test_get_users():
    page = 1
    per_page = 6
    api_page = UsersAPIPage()
    response = api_page.get_users(page=page)
    assert response.status_code == 200
    assert len(response.json()["data"]) == per_page
