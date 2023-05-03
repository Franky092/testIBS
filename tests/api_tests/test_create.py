import pytest
import requests


@pytest.mark.parametrize('id, name, job,  expected_status', [
    (21, 'name1', "job1",  201),
    (22, 'name2', "job2",  201),
    (23, 'name3', "job3",  201),
    (24, 'name4', "job4",  201)
])
def test_create_user(base_url, id, name, job, expected_status):

    data = {
        "id": f"{id}",
        "name": f"{name}",
        "job": f"{job}"
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{base_url}/users", json=data, headers=headers)
    assert response.status_code == expected_status
    assert response.json()['id'] == f'{id}'
    assert response.json()['name'] == f'{name}'
    assert response.json()['job'] == f'{job}'
