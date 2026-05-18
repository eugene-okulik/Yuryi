from page.contactus_page import  ContactusPage
from playwright.sync_api import Page
import time


"""Проверка заполнение формы → отправка → проверка"""
def test_prnt_form_about_user(page: Page):
    contactus_form = ContactusPage(page)
    contactus_form.open()
    time.sleep(3)
    contactus_form.print_in_form_with_chain_qa()
    time.sleep(3)
