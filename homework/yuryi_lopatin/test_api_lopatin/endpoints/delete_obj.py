import requests
import allure
from test_api_lopatin.endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):
    url = 'http://167.172.172.115:52353/object'
    response = None
    obj_id = None

    @allure.step('Delete_obj')
    def delete_obj(self):
        self.response = requests.delete(f'{self.url}/{self.obj_id}')
        print(f'DELETE response {self.response.status_code}')
        print(f'DELETE URL: {self.url}/{self.obj_id}')
        return self.response
    