from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.service import Service ### USED FOR FIREFOX BROWSER
# from webdriver_manager.firefox import GeckoDriverManager ### USED FOR FIREFOX BROWSER
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### HEADLESS MODE SYNTAX ###
    # chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    # context.driver = webdriver.Chrome(options=chrome_options)
    # context.driver.set_window_size(1920, 1080)

    ### MOBILE EMULATION ###
    mobile_emulation = {"deviceName": "iPhone X"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    context.driver = webdriver.Chrome(options=chrome_options)


    # context.driver = webdriver.Firefox()
    # context.driver.maximize_window()

    ### BROWSERSTACK INFO ###
    # bs_user = 'leviwilkerson_HEvT1s'
    # bs_key = 'siHyucCHPaT5YXMNrFAz'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #         "osVersion" : "16",
    #         "deviceName" : "iPhone 14 Plus",
    #         'browserName': "safari",
    #         'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.wait = WebDriverWait(context.driver, timeout=15)


    context.app = Application(context.driver, context.wait)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
