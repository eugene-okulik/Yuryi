import requests
import allure
from test_api_lopatin.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):

    def create_new_obj(self, body, headers=None):
        headers = headers if headers else self.headers
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
