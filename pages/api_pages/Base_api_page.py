import requests

class BaseAPIPage:
    base_url = "https://reqres.in/"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _get(self, endpoint, params=None):
        try:
            response = self.session.get(self.base_url + endpoint, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Failed to GET {endpoint}: {e}")

class UsersAPIPage(BaseAPIPage):
    endpoint = "api/users/"

    def get_users(self, page=1, per_page=6):
        params = {"page": page, "per_page": per_page}
        return self._get(self.endpoint, params=params)

