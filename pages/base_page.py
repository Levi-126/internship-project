from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait =  WebDriverWait(driver, 15)

    def open_url(self, end_url=''):
        self.driver.get(f'https://soft.reelly.io/{end_url}')

    def find_element(self, *locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_elements(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.find_elements(*locator)

    def click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def clear_field(self, *locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

    def input_text(self, text, *locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def validate_input_field(self, *locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")

    def save_button_enabled(self, *locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()

    def close_button_enabled(self, *locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()


