import logging

from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class SwitchAlert:

    def __init__(self, driver):
        self.driver = driver

    def found_input(self):
        self.driver.swipe(start_x=1000, start_y=500, end_x=500, end_y=500, duration=1000)

        for _ in range(2):
            try:
                inputText = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                "(//android.view.View[@text='Switch To Alert Example'])[1]/android.widget.EditText")
                if inputText:
                    logging.info("Element found")
            except:
                logging.info("Element not found")
                self.driver.swipe(start_x=1000, start_y=500, end_x=100, end_y=500, duration=1000)

    def enter_text(self,text):
        inputText = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                         "(//android.view.View[@text='Switch To Alert Example'])[1]/android.widget.EditText")
        inputText.clear()
        inputText.click()
        inputText.send_keys(text)
        self.driver.back()

    def click_button(self,button):
        self.wait_until_element_is_clickable(AppiumBy.XPATH, f"//android.widget.Button[@text='{button}']").click()

    def print_text(self):
        alertText = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                        "//android.widget.TextView[@resource-id='com.android.chrome:id/message_paragraph_1']")
        logging.info(alertText.get_attribute("text"))
        print(alertText.get_attribute("text"))

    def confirm(self):
        time.sleep(5)
        self.wait_until_element_is_clickable(AppiumBy.XPATH,
                            "//android.widget.Button[@resource-id='com.android.chrome:id/positive_button']").click()

    def validate_text(self):
        validText = "Hello Stori Card, Are you sure you want to confirm?"
        time.sleep(1)
        confirmText = (self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                          "//android.widget.TextView[@resource-id='com.android.chrome:id/message_paragraph_1']")
                                                 .get_attribute("text"))
        if validText == confirmText:
            logging.info("Is the same text")
            print("Is the same text")
        else:
            logging.info("No is the same text")
            print("No is the same text")

    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))