import time

from selenium.webdriver.common.by import By

from pages.locators import ProductPageLocator
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest



@pytest.mark.need_review_custom_scenarios
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product = ProductPage(browser, link)
    product.open()
    product.add_product()
    product.solve_quiz_and_get_code()
    product.is_not_element_present(*ProductPageLocator.ITEM_ALERT)

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product = ProductPage(browser, link)
    product.open()
    assert product.get_book() == 'Coders at Work'
    product.add_product()
    product.solve_quiz_and_get_code()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_backet_empty(), 'Корзина не пуста'
    assert 'Your basket is empty' in page.text_backet_empty(), 'Текст не соответсвует'

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    login = LoginPage(browser, link)
    login.open()
    login.login(user='1596129727.7071972@fakemail.org',passv='1596129727.7071972@fakemail.org')
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE)

