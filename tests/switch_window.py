from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
import time
class SwitchWindow:
    def __init__(self, driver):
        self.driver = driver

    def found_button(self):
        self.wait_until_element_is_clickable(AppiumBy.XPATH, "//android.widget.Button[@resource-id='openwindow']").click()


    def found_text(self,text):
        text_found = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{text}").instance(0))'
        try:
          element = self.wait_until_element_is_clickable(AppiumBy.ANDROID_UIAUTOMATOR, text_found)
          if element:
            print("We found: ",element.get_attribute("text"))
          else:
            print("No found the text: ",text," here")

        except:
          print("Text no found")

    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))