import requests

class CreateCamp:
    url = 'https://aooh-test.cubicservice.ru/v1/campaigns/new?counterpartyId=7'
    response = None
    json=None

    def create_new_camp(self, create_body, headers):
        self.response = requests.post('https://aooh-test.cubicservice.ru/v1/campaigns/new?counterpartyId=7',
                                        json=create_body, headers=headers)
        self.json = self.response.json()
        return self.response  # если потребуется вернуть данные json
