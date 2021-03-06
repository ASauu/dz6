import pytest
from .pages.locators import ProductPageLocator
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*ProductPageLocator.ITEM_ICON)
    assert page.is_element_present(*ProductPageLocator.ITEM_CONTENT)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    assert page.is_not_element_present(*ProductPageLocator.ITEM_ICON)
    assert page.is_element_present(*ProductPageLocator.ITEM_CONTENT)

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()