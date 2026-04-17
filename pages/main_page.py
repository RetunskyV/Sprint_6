from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_question(self, index):
        question_locator = MainPageLocators.QUESTIONS[index]["question"]
        self.scroll_to_element(question_locator)
        element = self.find_element(question_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, index):
        answer_locator = MainPageLocators.QUESTIONS[index]["answer"]
        return self.get_text(answer_locator)

    def is_answer_visible(self, index):
        answer_locator = MainPageLocators.QUESTIONS[index]["answer"]
        return self.is_element_visible(answer_locator)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)