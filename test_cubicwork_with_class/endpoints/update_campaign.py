import requests
import allure
from requests import JSONDecodeError
#from test_cubicwork_with_class.endpoints.endpoint import Endpoint  # Измените путь под ваш проект


class UpdateCamp():
    """Класс для обновления рекламных кампаний - адаптирован из вашего UpdateMeme"""
    url = 'https://aooh-test.cubicservice.ru/v1/campaigns/new?counterpartyId=7'
    response = None
    json = None

    @allure.step('Update campaign')
    def update_new_camp(self, campaign_id, update_body, headers):  #, counterparty_id=7):  # Получение кампании
        self.response = requests.post(
            f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/update?counterpartyId=7',
            json=update_body, headers=headers)
        self.json = self.response.json()
        return self.response  # если потребуется вернуть данные json
