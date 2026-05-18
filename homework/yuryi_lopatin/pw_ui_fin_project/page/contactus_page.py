from page.locators.contactus_locators import ContactLocators as loc
from page.base_page import BasePage
from playwright.sync_api import expect
import time


# Константы URL-путей
THANKYOU = "/contactus-thank-you"


class ContactusPage(BasePage):
    page_url = '/contactus'


    def print_in_form_with_chain_qa(self):
        # Цепочка заполнения формы
        form = self.page.locator(loc.FORM)
        form.locator('#contact1').fill('Иван Иванов')
        form.locator('#contact2').fill('21234567')
        form.locator('#contact3').fill('ivan@example.com')
        form.locator('#contact4').fill('Тест "ООО «Рога и Копыта»"')
        form.locator('#contact5').fill('ivan example')
        form.locator('#contact6').fill('Тест овощи')
        submit_button = form.locator(loc.SUBMIT)  # Наводим на кнопку (для эффекта)
        submit_button.hover()
        self.page.wait_for_timeout(200)
        submit_button.click()  # Отправляем
        time.sleep(3)
        time.sleep(3)
        expect(self.page).to_have_url(f"{self.base_url}{THANKYOU}")
