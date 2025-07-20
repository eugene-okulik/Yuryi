import pytest
import allure

# Импорты нужны для фикстур, используемых в тестах
from test_api_lopatin.conftest import create_obj_endpoint, update_obj_endpoint  # noqa: F401 - линтер игнорирует импорт
from test_api_lopatin.conftest import GetObj
from test_api_lopatin.conftest import DeleteObj


TEST_DATA = [
    {'name': "poco", 'data': {"color": "red", "size": "small"}},
    {'name': "honor", 'data': {"color": "green", "size": "medium"}},
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
def test_get_all_obj(get_obj_endpoint):
    print('Тест получения всех объектов')
    get_obj_endpoint.get_all_obj()
    get_obj_endpoint.check_response_status_is_200


@allure.feature('object')
@allure.story('Manipulate object')
@pytest.mark.parametrize('data', TEST_DATA)
def test_create_new_obj(create_obj_endpoint, data):
    print('Create new object with TEST_DATA')
    create_obj_endpoint.create_new_obj(body=data)  # инициализированный объект.его метод
    create_obj_endpoint.check_response_status_is_200()  # инициализированный объект.его метод
    create_obj_endpoint.check_response_name_is_correct(data['name'])  # инициализированный объект.его метод


@allure.feature('object')
@allure.story('Get object')
@allure.title('Получение одного объекта')
@pytest.mark.smoke
def test_get_one_obj(get_obj_endpoint, create_new_obj):
    print('Тест получения одного объекта')
    get_obj_endpoint.get_one_obj(create_new_obj)
    get_obj_endpoint.check_response_status_is_200()


@allure.feature('object')
@allure.story('Manipulate object')
@pytest.mark.parametrize('negative_data', NEGATIVE_DATA)
def test_create_new_obj_with_array_in_body(create_obj_endpoint, negative_data):
    print('Negative test create new object with NEGATIVE_DATA')
    create_obj_endpoint.create_new_obj(body=negative_data)  # инициализированный объект.его метод
    create_obj_endpoint.check_bad_request()  # инициализированный объект.его метод
    create_obj_endpoint.check_response_name_is_correct(negative_data['name'])


@allure.feature('object')
@allure.story('Manipulate object')
@allure.title('Обновление объекта PUT запрос')
@pytest.mark.medium
def test_put_object(create_new_obj, update_obj_endpoint):
    print('Тест частичного обновления объекта (PUT)')
    body = {
        "name": "blackberry",
        "data": {"color": "red", "size": "small"}
    }
    update_obj_endpoint.make_put_changes_in_obj(create_new_obj, body)
    update_obj_endpoint.check_response_status_is_200()


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


@allure.feature('object')
@allure.story('Manipulate object')
@allure.title('Тест удаления объекта (delete)')
@pytest.mark.medium
def test_delete_object(create_new_obj, delete_obj_endpoint):
    print('Тест удаления объекта (delete)')
    delete_obj_endpoint.obj_id = create_new_obj
    delete_obj_endpoint.delete_obj()
    delete_obj_endpoint.check_response_status_is_200()
