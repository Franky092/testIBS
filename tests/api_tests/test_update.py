import pytest
import requests


@pytest.mark.parametrize('page, id, name, job,  expected_status', [
    (1, 21, 'name1', "job1",  200),
    (2, 22, 'name2', "job2",  200),
    (3, 23, 'name3', "job3",  200),
    (4, 24, 'name4', "job4",  200)
])
def test_update_user(base_url, page, id, name, job, expected_status):

    data = {
        "id": f"{id}",
        "name": f"{name}",
        "job": f"{job}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.put(f"{base_url}/users/{page}", json=data, headers=headers)
    assert response.status_code == expected_status
    assert response.json()['id'] == f'{id}'
    assert response.json()['name'] == f'{name}'
    assert response.json()['job'] == f'{job}'


@pytest.mark.parametrize('page, id, name, job,  expected_status', [
    (1, 21, 'name1', "job1",  200),
    (2, 22, 'name2', "job2",  200),
    (3, 23, 'name3', "job3",  200),
    (4, 24, 'name4', "job4",  200)
])
def test_get_update_user_with_patch(base_url, page, id, name, job, expected_status):

    data = {
        "id": f"{id}",
        "name": f"{name}",
        "job": f"{job}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.patch(f"{base_url}/users/{page}", json=data, headers=headers)
    assert response.status_code == expected_status
    assert response.json()['id'] == f'{id}'
    assert response.json()['name'] == f'{name}'
    assert response.json()['job'] == f'{job}'
