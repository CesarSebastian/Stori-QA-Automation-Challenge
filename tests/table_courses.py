from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait


class TableCourses:
    name25 = []
    price25 = []

    name15 = []
    price15 = []

    def __init__(self, driver):
        self.driver = driver

    def found_table(self):
        self.driver.swipe(start_x=500, start_y=1700, end_x=500, end_y=400, duration=1000)
        time.sleep(2)
        tabExample = self.wait_until_element_is_clickable(AppiumBy.XPATH, "(//android.view.View[@text='Web Table Example'])[1]")

        if tabExample:
            print("Table Courses Found")

    def count_25(self):
        tabExample = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                          "(//android.view.View[@text='Web Table Example'])[1]")
        for i in range(10):
            rowName = tabExample.find_element(AppiumBy.XPATH,
                                              f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[2]")
            rowPrice = tabExample.find_element(AppiumBy.XPATH,
                                               f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[3]")

            priceResult = rowPrice.get_attribute("text")

            if priceResult == "25":
                TableCourses.name25.append(rowName.get_attribute("text"))
                TableCourses.price25.append(priceResult)

    def count_15(self):
        tabExample = self.wait_until_element_is_clickable(AppiumBy.XPATH,
                                                          "(//android.view.View[@text='Web Table Example'])[1]")
        for i in range(10):
            rowName = tabExample.find_element(AppiumBy.XPATH,
                                              f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[2]")
            rowPrice = tabExample.find_element(AppiumBy.XPATH,
                                               f"//android.widget.GridView/android.view.View[{i + 2}]/android.view.View[3]")

            priceResult = rowPrice.get_attribute("text")

            if priceResult == "15":
                TableCourses.name15.append(rowName.get_attribute("text"))
                TableCourses.price15.append(priceResult)

    def print_25(self):
        print(len(TableCourses.price25))

    def print_15(self):
        print(len(TableCourses.price15))

    def print_name_courses25(self):
        for nametf in TableCourses.name25:
                print(nametf)

    def print_name_courses15(self):
        for nameft in TableCourses.name15:
            print(nameft)
    def wait_until_element_is_clickable(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, locator)))