from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage(Page):

    # SETTINGS_BUTTON = (By.XPATH, "//a[@href='https://soft.reelly.io/settings']")
    ALTERNATE_SETTINGS_ROUTE = (By.XPATH, "//a[@href='https://soft.reelly.io/profile-edit']")
    MOBILE_SETTINGS_LOCATOR = (By.XPATH, "//a[@href='/settings']")

    def select_settings(self):
        self.click(*self.ALTERNATE_SETTINGS_ROUTE)

        elements = self.find_elements(self.MOBILE_SETTINGS_LOCATOR)
        visible = [e for e in elements if e.is_displayed()]
        visible[-1].click()
