import pytest
import allure

from test_api_lopatin.conftest import create_obj_endpoint
from test_api_lopatin.conftest import update_obj_endpoint
from test_api_lopatin.endpoints.get_obj import GetObj


@pytest.fixture(scope='session')
def start_testing():
    print('Start testing')
    yield
    print('Testing completed')


TEST_DATA = [
    {'name': "poco", 'data': {"color": "red", "size": "small"}},
    {'name': "honor", 'data': {"color": "green", "size": "medium"}}
]

TEST_DATA2 = [
    {'name': "iphone", 'data': {"color": "white", "size": "big"}},
    {'name': "samsung", 'data': {"color": "silver", "size": "medium"}},
    {'name': "xiaomi", 'data': {"color": "black", "size": "small"}}
]


NEGATIVE_DATA = [
    {"name": ['array'], "data": {"color": "blue", "size": "small"}},
    {"name": "huawei", "data": [{"color": "purple", "size": "medium"}]}
]


@allure.feature('object')
@allure.story('Get object')
@allure.title('Получение всех объектов')
@pytest.mark.smoke
def test_get_all_obj():
    print('Тест получения всех объектов')
    print('get all object')
    get_all_obj_endpoint = GetObj()
    response = get_all_obj_endpoint.get_all_obj()
    assert response.status_code == 200
    print(response)


"""Create new object with TEST_DATA"""
@allure.feature('object')
@allure.story('Manipulate object')
@pytest.mark.parametrize('data', TEST_DATA)
def test_create_new_obj(create_obj_endpoint, data):
    print('Create new object with TEST_DATA')
    create_obj_endpoint.create_new_obj(body=data)  # инициализированный объект.его метод
    create_obj_endpoint.check_response_status_is_200()  # инициализированный объект.его метод
    create_obj_endpoint.check_response_name_is_correct(data['name'])  # инициализированный объект.его метод


"""Тест получения одного объекта по ID который создан в create_new_obj файла create_obj.py"""
@allure.feature('object')
@allure.story('Get object')
@allure.title('Получение одного объекта')
@pytest.mark.smoke
def test_get_one_obj(create_new_obj):
    print('Тест получения одного объекта')
    get_one_obj_endpoint = GetObj()
    response = get_one_obj_endpoint.get_one_obj(create_new_obj)
    assert response.status_code == 200


"""Create new object with TEST_DATA2"""
@allure.feature('object')
@allure.story('Manipulate object')
@pytest.mark.parametrize('data', TEST_DATA2)
def test_create_new_obj2(create_obj_endpoint, data):
    print('Create new object with TEST_DATA2')
    create_obj_endpoint.create_new_obj(body=data)  # инициализированный объект.его метод
    create_obj_endpoint.check_response_status_is_200()  # инициализированный объект.его метод
    create_obj_endpoint.check_response_name_is_correct(data['name'])


"""Negative test create new object with TEST_DATA"""
@allure.feature('object')
@allure.story('Manipulate object')
@pytest.mark.parametrize('negative_data', NEGATIVE_DATA)
def test_create_new_obj_with_array_in_body(create_obj_endpoint, negative_data):
    print('Negative test create new object with TEST_DATA')
    create_obj_endpoint.create_new_obj(body=negative_data)  # инициализированный объект.его метод
    create_obj_endpoint.check_bad_request()  # инициализированный объект.его метод
    create_obj_endpoint.check_response_name_is_correct(negative_data['name'])


"""By PUT request for 1 object with TEST_DATA"""
@allure.feature('object')
@allure.story('Manipulate object')
@allure.title('Обновление объекта PUT запрос')
@pytest.mark.medium
def test_put_object(create_new_obj, update_obj_endpoint):
    body = {
        "name": "blackberry",
        "data": {"color": "red", "size": "small"}
    }
    update_obj_endpoint.make_put_changes_in_obj(create_new_obj, body)
    update_obj_endpoint.check_response_status_is_200()


"""Тест частичного обновления объекта (PATCH)"""
@allure.feature('object')
@allure.story('Manipulate object')
@allure.title('Обновление объекта PATCH запросом')
@pytest.mark.medium
def test_patch_object(create_new_obj, update_obj_endpoint):
    print('Тест частичного обновления объекта (PATCH)')
    body = {
        "name": "oppo",
        "data": {"color": "pink", "size": "very big"}
    }
    update_obj_endpoint.patch_changes_in_obj(create_new_obj, body)
    update_obj_endpoint.check_response_status_is_200()


"""Тест удаления объекта (delete)"""
@allure.feature('object')
@allure.story('Manipulate object')
@allure.title('Тест удаления объекта (delete)')
@pytest.mark.medium
def test_delete_object(create_new_obj, update_obj_endpoint):
    print('Тест удаления объекта (delete)')
    update_obj_endpoint.delete_obj(create_new_obj)
