from playwright.sync_api import Page


def test_by_dz2(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_btn = page.get_by_role('link', name='Form Authentication')
    search_btn.click()

    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')

    page.get_by_role('button').click()


def test_by_dz8(page: Page):
    page.goto('https://demoqa.com')
    page.get_by_role('link', name='forms').click()
    page.wait_for_load_state('domcontentloaded')
    page.get_by_text('Practice Form').click()

    page.locator('#firstName').scroll_into_view_if_needed()
    page.locator('#firstName').fill('Tom')
    page.locator('#lastName').scroll_into_view_if_needed()
    page.locator('#lastName').fill('Smith')
    page.locator('#userEmail').scroll_into_view_if_needed()
    page.locator('#userEmail').fill('test@example.com')

    page.locator('label[for="gender-radio-1"]').click()

    page.locator('#userNumber').fill('1234567890')

    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__month-select').select_option('January')
    page.locator('.react-datepicker__year-select').select_option('1990')
    page.locator('.react-datepicker__day--001').first.click()

    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press('Enter')

    page.locator('label[for="hobbies-checkbox-1"]').first.click()

    page.locator('#currentAddress').fill('123 Test Street')

    page.locator('#submit').click()
