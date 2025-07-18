import requests
import allure

from test_api_lopatin.endpoints.endpoint import Endpoint


class UpdateObj(Endpoint):
    obj_id = None

    @allure.step('PUT_request')
    def make_put_changes_in_obj(self, obj_id, body, headers=None):
        # if len(body['name']) > 1000:  # if добавим если есть логика. Например, если длинное имя, то отдельный endpoint
        #     self.url = f'{self.url}/long_name'  # если нет отдельной логики, то эти строки можно убрать
        headers = headers if headers else self.headers  # если headers не application/json, то None
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=body,
            headers=headers
        )
        print(f'PUT response{self.response.status_code}')
        print(f'PUT URL:{self.url}/{obj_id}')
        self.json = self.response.json()#['id'] # тут в self.post_id будет хранится ответ в виде id из json
        return self.response  # на случай работы на прямую с response в def put_a_post файла test_jsph.py

    @allure.step('PATCH_request')
    def patch_changes_in_obj(self, obj_id, body, headers=None):
        # if len(body['name']) > 1000:  # if добавим если есть логика. Например, если длинное имя, то отдельный endpoint
        #     self.url = f'{self.url}/long_name'  # если нет отдельной логики, то эти строки можно убрать
        headers = headers if headers else self.headers  # если headers не application/json, то None
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=body,
            headers=headers
        )
        print(f'PATCH response{self.response.status_code}')
        print(f'PATCH URL:{self.url}/{obj_id}')
        self.json = self.response.json()  # ['id'] # тут в self.post_id будет хранится ответ в виде id из json
        return self.response  # на случай работы на прямую с response в def put_a_post файла test_jsph.py

    @allure.step('DELETE_request')
    def delete_obj(self, obj_id):
        self.response = requests.delete(f'{self.url}/{obj_id}')
        print(f'DELETE URL:{self.url}/{obj_id}')
