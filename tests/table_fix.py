from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class TableFix:
    isEngineer = []
    isBusinessman = []

    def __init__(self, driver):
        self.driver = driver

    def found_table(self):
        self.driver.swipe(start_x=500, start_y=1700, end_x=500, end_y=400, duration=1000)
        self.driver.swipe(start_x=1000, start_y=1300, end_x=100, end_y=1300, duration=1000)
        time.sleep(2)
        tabFix = self.wait_until_element_is_clickable(AppiumBy.XPATH, "(//android.view.View[@text='Web Table Fixed header'])[1]/android.view.View[2]")

        if tabFix:
            print("Table Courses Found")

    def div_position(self):
        tabFix = self.wait_until_element_is_clickable(AppiumBy.XPATH, "(//android.view.View[@text='Web Table Fixed header'])[1]/android.view.View[2]")

        for i in range(9):

            name_row = tabFix.find_element(AppiumBy.XPATH,
                                           f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[1]")
            position_row = tabFix.find_element(AppiumBy.XPATH,
                                               f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[2]").get_attribute(
                "text")

            if position_row == "Engineer":
                TableFix.isEngineer.append(name_row.get_attribute("text"))
            if position_row == "Businessman":
                TableFix.isBusinessman.append(name_row.get_attribute("text"))
            else:
                pass
    def print_enginner(self):
        for engineer in TableFix.isEngineer:
            print(engineer)

    def print_businessman(self):
        for businessman in TableFix.isBusinessman:
            print(businessman)
    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))