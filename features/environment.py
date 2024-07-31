import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

from tests.main_page import MainPage


def before_all(context):
    pass


def after_all(context):
    pass


def before_scenario(context, scenario):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "12"
    options.device_name = "joyeuse"
    options.app_package = "com.android.chrome"
    options.app_activity = "com.google.android.apps.chrome.Main"

    # Inicializa el driver de Appium
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()