import pytest
import requests
from test_api_lopatin.endpoints.create_obj import CreateObj
from test_api_lopatin.endpoints.delete_obj import DeleteObj
from test_api_lopatin.endpoints.get_obj import GetObj
from test_api_lopatin.endpoints.update_obj import UpdateObj


@pytest.fixture(scope='session')
def start_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()  # инициализация create_post_endpoint() исп в test
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture()  # инициализация create_post_endpoint() исп в test
def get_obj_endpoint():
    return GetObj()  # Подчеркивание GetObj означает, что Python не может найти этот класс из-за отсутствующего импорта


@pytest.fixture()  # инициализация create_post_endpoint() исп в testpy
def update_obj_endpoint():
    return UpdateObj()


@pytest.fixture()  # инициализация create_post_endpoint() исп в test
def delete_obj_endpoint():
    return DeleteObj()


@pytest.fixture()  # инициализация update_post_endpoint() исп в test
def create_new_obj(create_obj_endpoint):
    body = {"name": "test_object", "data": {"key": "value", "key2": "value2"}}
    response = create_obj_endpoint.create_new_obj(body)
    print(response)
    obj_id = response.json()['id']
    print(f'Created object with ID: {obj_id}')
    yield obj_id
    print('Object obj')   # Удаления не делаем - объект уже удален в тесте
    delete_endpoint = DeleteObj()
    delete_endpoint.obj_id = obj_id
    delete_response = delete_endpoint.delete_obj()
    if delete_response.status_code == 200:
        print(f'Object {obj_id} successfully deleted')
    elif delete_response.status_code == 404:
        print(f'Object {obj_id} deleted in test')
    else:
        print(f'Unexpected status code deletion {delete_response.status_code}')


@pytest.fixture()  # создание объекта БЕЗ cleanup для теста удаления
def create_obj_for_delete(create_obj_endpoint):
    body = {"name": "test_object_for_delete", "data": {"key": "value", "key2": "value2"}}
    response = create_obj_endpoint.create_new_obj(body)
    print(response)
    obj_id = response.json()['id']
    print(f'Created object for delete test with ID: {obj_id}')
    yield obj_id
    print('No cleanup needed - object was deleted in test')



