import logging
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class DropSelect:
    def __init__(self, driver):
        self.driver = driver

    def drop_select(self):
        self.driver.swipe(1000, 800, 100, 800, 1000)
        self.driver.swipe(1000, 800, 700, 800, 1000)
        time.sleep(2)

        button = self.wait_until_element_is_clickable(AppiumBy.XPATH, "//android.view.View[@resource-id='dropdown-class-example']")
        button.click()
        self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Option2']").click()
        time.sleep(5)
        button.click()
        self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Option3']").click()
        time.sleep(5)

    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))