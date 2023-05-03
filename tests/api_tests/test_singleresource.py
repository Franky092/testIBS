import pytest
import requests


@pytest.mark.parametrize('page, expected_status', [
    (6, 200),
    (3, 200),
    (1, 200),
    (2, 200),
    (10, 200),
])
def test_get_resource(base_url, page, expected_status):
    response = requests.get(f'{base_url}/unknown/{page}')
    assert response.status_code == expected_status


@pytest.mark.parametrize('page, expected_status', [
    (60, 404),
    (31, 404),
    (44, 404),
    (211, 404),
    (102, 404),
])
def test_get_notfound_resource(base_url, page, expected_status):
    response = requests.get(f'{base_url}/unknown/{page}')
    assert response.status_code == expected_status

