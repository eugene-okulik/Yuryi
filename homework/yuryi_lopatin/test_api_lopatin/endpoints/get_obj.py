import requests
import allure

from test_api_lopatin.endpoints.endpoint import Endpoint


class GetObj(Endpoint):
    url = 'http://167.172.172.115:52353/object'
    response = None
    obj_id = None


    @allure.step('Get_all_obj')
    def get_all_obj(self):
        self.response = requests.get(self.url)
        print(f'GET response {self.response.status_code}')
        print(self.url)
        return self.response


    @allure.step('Get_a_obj')
    def get_one_obj(self, obj_id):
        self.response = requests.get(f'{self.url}/{obj_id}')
        print(f'GET response {self.response.status_code}')
        print(f'GET URL: {self.url}/{obj_id}')
        return self.response
