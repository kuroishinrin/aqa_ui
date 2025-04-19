from pages.base_page import BasePage
from pages.locators import sale_locators as loc

class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_title(self, text):
        page = self.find(loc.title_loc).text
        assert page == text