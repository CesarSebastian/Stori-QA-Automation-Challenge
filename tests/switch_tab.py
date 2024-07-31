from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
import time


class SwitchTab:
    def __init__(self, driver):
        self.driver = driver

    def enter_page(self):
        button = self.wait_until_element_is_clickable(AppiumBy.XPATH, "//android.widget.Button[@text='Open Window']")
        button.click()
        time.sleep(10)

    def found_element(self):
        for _ in range(1):
            try:
                # Intenta encontrar el elemento en la pantalla actual
                self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=100, duration=1000)
                time.sleep(2)  # Espera un poco para que la pantalla se desplace
                element = self.wait_until_element_is_clickable(AppiumBy.XPATH, "//android.view.View[@content-desc='']")
                print("Elemento encontrado")
                element.click()
                screenshot_path = 'C:/Users/cesar/PycharmProjects/Stori-QA-Automation-Challenge/ss/screenshot.png'
                self.driver.get_screenshot_as_file(screenshot_path)
            except:
                print("Elemento no encontrado")

    def back_page(self):
            self.driver.back()

    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))