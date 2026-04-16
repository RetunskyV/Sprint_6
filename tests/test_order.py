import pytest
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data.order_data import OrderTestData
from utils.date_helper import DateHelper
from locators.main_page_locators import MainPageLocators


class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного флоу заказа с разными точками входа")
    @pytest.mark.parametrize("button_type", OrderTestData.BUTTON_TYPES)
    def test_order_flow(self, driver, button_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        delivery_date = DateHelper.get_delivery_date()
        user = OrderTestData.USER_DATA

        with allure.step(f"Нажать кнопку заказа ({button_type})"):
            if button_type == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Заполнить первую страницу формы"):
            order_page.fill_first_page(
                user['name'],
                user['surname'],
                user['address'],
                user['phone']
            )

        with allure.step("Заполнить вторую страницу формы"):
            order_page.fill_second_page(
                delivery_date,
                user['comment']
            )

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить появление окна об успешном создании заказа"):
            assert order_page.is_success_modal_visible(), "Окно успешного создания заказа не появилось"

    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.description("При клике на логотип Самоката происходит переход на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        main_page = MainPage(driver)

        with allure.step("Перейти к форме заказа через кнопку вверху"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить, что URL соответствует главной странице"):
            WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса открывается новая вкладка с Дзеном")
    def test_yandex_logo_redirect(self, driver):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPage(driver)

        with allure.step("Дождаться загрузки главной страницы"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, MainPageLocators.ORDER_BUTTON_TOP))
            )

        with allure.step("Запомнить текущую вкладку"):
            original_window = driver.current_window_handle

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия новой вкладки"):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        with allure.step("Переключиться на новую вкладку"):
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break

        with allure.step("Дождаться редиректа на Дзен"):
            WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))

        with allure.step("Проверить, что URL содержит dzen.ru"):
            assert "dzen.ru" in driver.current_url