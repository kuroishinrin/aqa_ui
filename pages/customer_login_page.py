from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fild_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        pass_field = self.find(loc.pass_field_loc)
        button_sign_in = self.find(loc.button_sign_in_loc)
        email_field.send_keys(login)
        pass_field.send_keys(password)
        button_sign_in.click()
        WebDriverWait(self.driver, 5).until(ec.staleness_of(button_sign_in))

    def check_error_alert(self, test_data):
        error_message = self.find(loc.error_message_loc)
        assert error_message.text == test_data