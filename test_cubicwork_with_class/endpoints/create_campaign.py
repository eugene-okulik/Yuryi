import requests
import allure
from test_cubicwork_with_class.endpoints.endpoint import Endpoint


class CreateCamp:
    url = 'https://aooh-test.cubicservice.ru/v1/campaigns/new?counterpartyId=7'
    response = None
    json=None

    def create_new_camp(self, create_body, headers):
        self.response = requests.post(self.url, json=create_body, headers=headers)
        self.json = self.response.json()
        return self.response  # если потребуется вернуть данные json

# class CreateCamp(Endpoint):
#     #url = 'https://aooh-test.cubicservice.ru/v1/campaigns/new?counterpartyId=7'
#     response = None
#     json=None
#
#     @allure.step('Creating campaign')
#     def create_new_campaign(self, create_body, headers):
#         self.response = requests.post(
#             f'{self.url}/v1/campaigns/new?counterpartyId=7', json=create_body, headers=headers
#         )
#         print(self.response, self.url)
#         self.json = self.response.json()
#         return self.response  # если потребуется вернуть данные json

    # def get_list_adverts_campaigns(self, body, headers):
    #     self.response = requests.post(self.url, json=body, headers=headers)
    #     self.json = self.response.json()
    #     return self.response  # если потребуется вернуть данные json

    # get_list_adverts_camp = CreateCamp()
    # get_list_adverts_camp.get_list_adverts_campaigns(body=body, headers=headers)