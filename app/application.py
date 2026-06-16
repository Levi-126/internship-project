from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.edit_profile_page import EditProfile
from pages.input_field_page import InputFields


class Application:

    def __init__(self, driver, wait):
        self.page = Page(driver, wait)
        self.sign_in_page = SignInPage(driver, wait)
        self.main_page = MainPage(driver, wait)
        self.settings_page = SettingsPage(driver, wait)
        self.edit_profile_page = EditProfile(driver, wait)
        self.input_field_page = InputFields(driver, wait)
