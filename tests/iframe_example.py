from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class IframeExample:

    def __init__(self, driver):
        self.driver = driver

    def found_frame(self):
        self.driver.swipe(start_x=500, start_y=2200, end_x=500, end_y=300, duration=1000)
        self.driver.swipe(start_x=500, start_y=1770, end_x=500, end_y=300, duration=1000)
        self.driver.swipe(start_x=1000, start_y=1330, end_x=50, end_y=1330, duration=1000)
        self.driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        self.driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        self.driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        self.driver.swipe(start_x=800, start_y=1330, end_x=500, end_y=1330, duration=1000)

        textSelect = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                         "//android.view.View[@text='His mentorship program is most after in the software testing community with long waiting period.']")
        if textSelect:
            print("Frame Found")

    def print_text(self):
        textSelect = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                         "//android.view.View[@text='His mentorship program is most after in the software testing community with long waiting period.']")

        print(textSelect.get_attribute("text"))


    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))