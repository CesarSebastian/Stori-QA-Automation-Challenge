from appium.webdriver.common.appiumby import AppiumBy

import time


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def enterUrl(self):
        url = "https://rahulshettyacademy.com/AutomationPractice"
        input = self.driver.find_element(AppiumBy.XPATH,
                                    "//android.widget.EditText[@resource-id='com.android.chrome:id/search_box_text']")
        input.clear()
        input.send_keys(url)
        time.sleep(5)
        self.driver.press_keycode(66)
        time.sleep(5)
