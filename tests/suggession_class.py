from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class Suggession_Class:
    def __init__(self, driver):
        self.driver = driver

    def enter_ini(self, ini):
        sugg = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                    "//android.widget.EditText[@resource-id='autocomplete']")
        sugg.clear()

        sugg.send_keys(ini)
        self.driver.hide_keyboard()
        time.sleep(2)

    def select_country(self, n_country):
        time.sleep(2)
        country = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                       f"//android.widget.TextView[@text='{n_country}']")
        country.click()
        time.sleep(5)

    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))
