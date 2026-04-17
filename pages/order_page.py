from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from test_data.order_data import OrderTestData


class OrderPage(BasePage):

    def fill_first_page(self, name, surname, address, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_element(OrderPageLocators.METRO_INPUT)
        metro_locator = OrderPageLocators.METRO_OPTION_TEMPLATE.format(station=OrderTestData.METRO_STATION)
        self.click_element(metro_locator)
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_page(self, date, comment=""):
        self.input_text(OrderPageLocators.DATE_INPUT, date)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_locator = OrderPageLocators.RENTAL_PERIOD_OPTION_TEMPLATE.format(period=OrderTestData.RENTAL_PERIOD)
        self.click_element(rental_locator)
        color_locator = OrderPageLocators.COLOR_TEMPLATE.format(color_text=OrderTestData.COLOR_TEXT)
        self.click_element(color_locator)
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def is_success_modal_visible(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)