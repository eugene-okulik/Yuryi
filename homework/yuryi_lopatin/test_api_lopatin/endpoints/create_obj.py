import requests
import allure
from test_api_lopatin.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):

    def create_new_obj(self, body, headers=None):
        # if len(body['name']) > 1000:  # if добавим если есть логика. Например, если длинное имя, то отдельный endpoint
        #     self.url = f'{self.url}/long_name'  # если нет отдельной логики, то эти строки можно убрать
        headers = headers if headers else self.headers  # если headers не application/json, то None
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        print(self.response, self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400
