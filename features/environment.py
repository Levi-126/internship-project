from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    # context.driver = webdriver.Chrome(options=chrome_options)
    # context.driver.set_window_size(1920, 1080)

    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()

    context.driver = webdriver.Firefox()
    context.driver.maximize_window()

    context.wait = WebDriverWait(context.driver, timeout=15)


    context.app = Application(context.driver, context.wait)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
