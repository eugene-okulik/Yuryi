import requests
import pytest


@pytest.fixture(scope='session')
def start_testing():
    print('Start testing')
    yield
    print('Testing completed')


def test_get_all_obj(start_testing):
    print('Тест получения всех объектов')
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200


"""Создает новых объектов с разными данными"""
@pytest.mark.parametrize('name, data', [
    ("iphone", {"color": "white", "size": "big"}),
    ("samsung", {"color": "silver", "size": "medium"}),
    ("xiaomi", {"color": "black", "size": "smal"})
    ]
                         )
def test_create_new_obj_id(name, data):
    body = {"name": name, "data": data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    print(f'Created object: {name}')
    assert response.status_code == 200
    obj_id = response.json()['id']  # тут в self.post_id будет хранится ответ в виде id из json
    print(f'Created object with id: {obj_id}')

    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    print(f'Удаление объекта с id: {obj_id}')


"""Создает новый объект и возвращает его ID"""
@pytest.fixture()
def new_obj_id():
    body = {"name": "lox", "data": {"color": "white", "size": "big"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    print(response)
    obj_id = response.json()['id']  # тут в self.post_id будет хранится ответ в виде id из json
    print(f'Created object with ID: {obj_id}')
    yield obj_id
    print('deleting obj')
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


"""Тест получения объекта по ID"""
def test_get_one_obj(new_obj_id):
    obj_id = new_obj_id
    print('Тест получения объекта по ID')
    response = requests.get(f'http://167.172.172.115:52353/object/{obj_id}')
    assert response.status_code == 200
    assert response.json()['id'] == obj_id


"""Тест обновления объекта (PUT)"""
@pytest.mark.medium
def test_put_object(new_obj_id):
    obj_id = new_obj_id
    print('Тест обновления объекта (PUT)')
    body = {
        "name": "saks",
        "data": {"color": "red", "size": "small"}
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{obj_id}', json=body).json()
    assert response['name'] == 'saks'
    assert response['data'] == {"color": "red", "size": "small"}


"""Тест частичного обновления объекта (PATCH)"""
@pytest.mark.medium
def test_patch_object(new_obj_id):
    obj_id = new_obj_id
    print('Тест частичного обновления объекта (PATCH)')
    body = {
        "name": "ass",
        "data": {"color": "pink", "size": "very big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = (requests.patch(f'http://167.172.172.115:52353/object/{obj_id}', json=body, headers=headers)
                .json())
    assert response['name'] == 'ass'
    assert response['data'] == {"color": "pink", "size": "very big"}


"""Тест удаления объекта"""
@pytest.mark.critical
def test_delete_a_object(new_obj_id):
    obj_id = new_obj_id
    print('Тест удаления объекта')
    response = requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    assert response.status_code == 200, 'status code'
    print(response)
    print(response.status_code)
