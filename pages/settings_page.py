from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):

    SETTINGS_BUTTON = (By.XPATH, "//a[@href='https://soft.reelly.io/settings']")

    def select_settings(self):
        self.click(*self.SETTINGS_BUTTON)

