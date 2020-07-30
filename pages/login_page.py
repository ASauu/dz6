import string
from random import random

from .base_page import BasePage
from pages.locators import MainPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def login(self, user, passv):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.LOGIN_FIELD).send_keys(user)
        self.browser.find_element(*BasePageLocators.PASS_FIELD).send_keys(passv)
        self.browser.find_element(*BasePageLocators.LOGIN_SUBMIT).click()

    def register_new_user(self, email, password):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.REG_PASS1).send_keys(password)
        self.browser.find_element(*BasePageLocators.REG_PASS2).send_keys(password)
        self.browser.find_element(*BasePageLocators.REG_SUBMIT).click()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url in "login", 'ссылка не соответствует'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert len(self.browser.find_elements(*BasePageLocators.LOGIN_FORM)) == 1, 'отсутсвует форма логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert len(self.browser.find_elements(*BasePageLocators.REG_FORM)) == 1, 'отсутсвует форма регистрации'