import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data.order_data import OrderTestData
from utils.date_helper import DateHelper
from config.urls import Urls
from locators.main_page_locators import MainPageLocators   # ← добавить


class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката через верхнюю кнопку")
    @allure.description("Проверка полного флоу заказа с верхней кнопки")
    def test_order_flow_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        delivery_date = DateHelper.get_delivery_date()
        user = OrderTestData.USER_DATA

        with allure.step("Нажать верхнюю кнопку заказа"):
            main_page.click_order_button_top()

        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(
                user['name'],
                user['surname'],
                user['address'],
                user['phone']
            )

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(delivery_date, user['comment'])

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить появление окна об успешном создании заказа"):
            assert order_page.is_success_modal_visible()

    @allure.title("Позитивный сценарий заказа самоката через нижнюю кнопку")
    @allure.description("Проверка полного флоу заказа с нижней кнопки")
    def test_order_flow_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        delivery_date = DateHelper.get_delivery_date()
        user = OrderTestData.USER_DATA

        with allure.step("Нажать нижнюю кнопку заказа"):
            main_page.click_order_button_bottom()

        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(
                user['name'],
                user['surname'],
                user['address'],
                user['phone']
            )

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(delivery_date, user['comment'])

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить появление окна об успешном создании заказа"):
            assert order_page.is_success_modal_visible()

    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.description("При клике на логотип Самоката происходит переход на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Перейти к форме заказа через кнопку вверху"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить, что URL соответствует главной странице"):
            main_page.wait_for_url(Urls.BASE_URL)
            assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса открывается новая вкладка с Дзеном")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_url()

        with allure.step("Дождаться загрузки главной страницы"):
            main_page.wait_for_element_present(MainPageLocators.ORDER_BUTTON_TOP)

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_new_window()

        with allure.step("Дождаться редиректа на Дзен"):
            main_page.wait_for_url_contains("dzen.ru")

        with allure.step("Проверить, что URL содержит dzen.ru"):
            assert "dzen.ru" in main_page.get_current_url()