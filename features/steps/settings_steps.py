from behave import given, when, then
from time import sleep


@when("Click on Settings Option")
def choose_settings(context):
    context.app.settings_page.select_settings()
    sleep(1)

@when("Click on Edit Profile Option")
def choose_edit_profile(context):
    context.app.edit_profile_page.select_edit_profile()
    sleep(10)

