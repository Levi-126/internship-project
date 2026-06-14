from behave import given, when, then
from time import sleep


@when("Login to the Page")
def complete_signin(context):
        context.app.sign_in_page.login(
            'levi126@gmail.com',
            'test+levi+careerist'
        )
        sleep(2)
