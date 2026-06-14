from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class EditProfile(Page):

    EDIT_PROFILE_BUTTON = (By.XPATH, "//a[@href='/profile-edit' and @class='page-setting-block w-inline-block']")

    def select_edit_profile(self):
        self.driver.find_element(*self.EDIT_PROFILE_BUTTON).click()
        sleep(1)
