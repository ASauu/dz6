from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocator():
    ADD_BOOK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GET_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ". alertinner")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    BASKET_EMPTY_LABEL =(By.CSS_SELECTOR, "#content_inner p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '[href*="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")