import allure


class Endpoint:  # родительский класс для всех endpoints
    url = 'http://167.172.172.115:52353/object'
    response = None  # для строки self.response = requests.post
    json = None  # для строки self.json = self.response.json()
    obj_id = None
    headers = {'Content-Type': 'application/json'}


    @allure.step('Check that title is the same sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name, 'name is not name'

    @allure.step('Check that response is 200')
    def check_response_status_is_200(self):
        assert self.response.status_code == 200, f"Ожидался код 200, получен {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, f"Ожидался код 400, получен {self.response.status_code}"
