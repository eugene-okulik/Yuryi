class BasePage:
    base_url = 'http://testshop.qa-practice.com'


    def __init__(self, page):
        self.page = page


    def open(self, url=None):
        if url:
            self.page.goto(url)
        else:
            page_url = getattr(self, 'page_url', '')
            self.page.goto(f'{self.base_url}{page_url}')
