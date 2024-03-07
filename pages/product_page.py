from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Add busket button is not presented"

    def add_product_in_busket(self):
        add_busket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_busket_button.click()

    def checking_message_about_successful_addition_of_the_product_to_the_store(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_AADDITION_ADD_BASKET_MESSAGE).text
        assert title in message

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
        except NoAlertPresentException:
            print("No second alert presented")
