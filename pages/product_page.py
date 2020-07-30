import math
from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):

    def add_product(self):
        batton = self.browser.find_element(*ProductPageLocator.ADD_BOOK)
        batton.click()

    def is_backet_empty(self):
        return len(self.browser.find_elements(*ProductPageLocator.BASKET_EMPTY_LABEL)) == 1

    def text_backet_empty(self):
        text = self.browser.find_element(*ProductPageLocator.BASKET_EMPTY_LABEL).text
        return text

    def go_to_basket(self):
        batton = self.browser.find_element(*ProductPageLocator.BASKET_BUTTON)
        batton.click()

    def get_book(self):
        res = self.browser.find_element(*ProductPageLocator.GET_BOOK)
        return res.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            w=0
            print('sss')


        except NoAlertPresentException:
            print("No second alert presented")