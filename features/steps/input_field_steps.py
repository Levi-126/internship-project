from behave import given, when, then
from time import sleep


@then("Enter test information")
def input_field_info(context):
    context.app.input_field_page.languages_field("English")
    sleep(1)


@then("Check the right information is present")
def validate_input_info(context):
    context.app.input_field_page.verify_info("English")

@then("Check the Close and Save Changes buttons are Available")
def validate_input_info_entered(context):
    context.app.input_field_page.save_button_clickable()
    sleep(1)
    context.app.input_field_page.close_button_clickable()
    sleep(1)

