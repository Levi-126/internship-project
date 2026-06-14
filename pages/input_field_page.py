from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class InputFields(Page):

    LANGUAGES_INPUT = (By.ID, 'Languages')
    SAVE_BUTTON = (By.XPATH, "//div[@class='save-changes-button']")
    CLOSE_BUTTON = (By.XPATH, "//a[@class='close-button w-button']")

    def languages_field(self, language):
        self.clear_field(*self.LANGUAGES_INPUT)
        sleep(1)
        self.input_text(language, *self.LANGUAGES_INPUT)
        sleep(2)

    def verify_info(self, expected_language):
        actual_value = self.validate_input_field(*self.LANGUAGES_INPUT)
        assert actual_value == expected_language, \
            f"Expected '{expected_language}', but got '{actual_value}'"

    def save_button_clickable(self):
        return self.save_button_enabled(*self.SAVE_BUTTON)

    def close_button_clickable(self):
        return self.close_button_enabled(*self.CLOSE_BUTTON)








