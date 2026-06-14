class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, end_url=''):
        self.driver.get(f'https://soft.reelly.io/{end_url}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def clear_field(self, *locator):
        self.driver.find_element(*locator).clear()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def validate_input_field(self, *locator):
        return self.driver.find_element(*locator).get_attribute("value")

    def save_button_enabled(self, *locator):
        return self.driver.find_element(*locator).is_enabled()

    def close_button_enabled(self, *locator):
        return self.driver.find_element(*locator).is_enabled()

