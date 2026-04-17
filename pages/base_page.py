from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from config.urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.find_element(locator).text

    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_url_contains(self, url_part):
        self.wait.until(EC.url_contains(url_part))

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url=Urls.BASE_URL):
        self.driver.get(url)

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def wait_for_element_present(self, locator):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))