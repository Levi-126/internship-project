from behave import given, when, then
from time import sleep


@given("Open Reely main page")
def open_target_main(context):
    context.app.main_page.open_main()
    sleep(4)

