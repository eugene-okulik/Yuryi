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


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def get_obj_endpoint():
    return GetObj()  # Подчеркивание GetObj означает, что Python не может найти этот класс из-за отсутствующего импорта


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def update_obj_endpoint():
    return UpdateObj()


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def delete_obj_endpoint():
    return DeleteObj()


@pytest.fixture()  # инициализация update_post_endpoint() исп в test_jsph.py
def create_new_obj(create_obj_endpoint):
    body = {"name": "test_object", "data": {"key": "value", "key2": "value2"}}
    response = create_obj_endpoint.create_new_obj(body)
    print(response)
    obj_id = response.json()['id']
    print(f'Created object with ID: {obj_id}')
    #creturn obj_id
    yield obj_id
    print('deleting obj')
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
