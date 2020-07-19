import string
from random import random

from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.browser.find_element_by_id('login_link').click()
     #   res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.browser.find_element_by_name('registration-email').send_keys(email)
        self.browser.find_element_by_name('registration-password1').send_keys(password)
        self.browser.find_element_by_name('registration-password2').send_keys(password)
        self.browser.find_element_by_name('registration_submit').click()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url in "login", 'ссылка не соответствует'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert len(self.browser.find_elements_by_id('login_form')) == 1, 'отсутсвует форма логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert len(self.browser.find_elements_by_id('register_form')) == 1, 'отсутсвует форма регистрации'