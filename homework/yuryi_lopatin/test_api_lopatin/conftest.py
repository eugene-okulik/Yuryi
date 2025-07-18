import pytest
from test_api_lopatin.endpoints.create_obj import CreateObj
from test_api_lopatin.endpoints.get_obj import GetObj
from test_api_lopatin.endpoints.update_obj import UpdateObj


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def get_obj_endpoint():
    return GetObj()  # Подчеркивание GetObj означает, что Python не может найти этот класс из-за отсутствующего импорта


@pytest.fixture()  # инициализация create_post_endpoint() исп в test_jsph.py
def update_obj_endpoint():
    return UpdateObj()


@pytest.fixture()  # инициализация update_post_endpoint() исп в test_jsph.py
def create_new_obj(create_obj_endpoint):
    body = {"name": "test_object", "data": {"key": "value", "key2": "value2"}}
    response = create_obj_endpoint.create_new_obj(body)
    obj_id = response.json()['id']
    print(obj_id)
    return obj_id
