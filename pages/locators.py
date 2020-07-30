from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocator():
    ADD_BOOK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GET_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ". alertinner")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    BASKET_EMPTY_LABEL =(By.CSS_SELECTOR, "#content_inner p")
    ITEM_ICON = (By.CSS_SELECTOR, '.basket-items')
    ITEM_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    ITEM_ALERT = (By.CSS_SELECTOR, '.alertinner ')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '[href*="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    LOGIN_SUBMIT = (By.NAME, 'login_submit')
    REG_SUBMIT = (By.NAME, 'registration_submit')

    LOGIN_FIELD = (By.ID, 'id_login-username')
    PASS_FIELD = (By.ID, 'id_login-password')
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PASS1 = (By.NAME, 'registration-password1')
    REG_PASS2 = (By.NAME, 'registration-password2')
