import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import pytest
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "12"
options.device_name = "joyeuse"
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"

host = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(host, options=options)

@pytest.fixture(scope="module")
def setup():
    url = "https://rahulshettyacademy.com/AutomationPractice"
    input = driver.find_element(AppiumBy.XPATH,
                                "//android.widget.EditText[@resource-id='com.android.chrome:id/search_box_text']")
    input.clear()
    input.send_keys(url)
    driver.implicitly_wait(5)
    driver.press_keycode(66)
    time.sleep(5)

    yield driver
    driver.quit()

def test_suggestion_class(setup):
    def suggestionClass(ini, name):
        sugg = driver.find_element(AppiumBy.XPATH,
                                   "(//android.view.View[@text='Suggession Class Example'])[1]/android.widget.EditText")
        sugg.clear()
        sugg.click()
        sugg.send_keys(ini)
        driver.implicitly_wait(10)
        country = driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{name}']")
        country.click()
        driver.implicitly_wait(100)
        sugg.clear()

    suggestionClass("Me", "Mexico")
    suggestionClass("Uni", "United Arab Emirates")

def test_dropdown_select(setup):
    def dropdownSelect():
        driver.swipe(1000, 800, 100, 800, 1000)
        time.sleep(2)
        button = driver.find_element(AppiumBy.XPATH, "//android.view.View[@text='Select']")
        button.click()
        driver.find_element(AppiumBy.XPATH,
                            "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Option2']").click()
        time.sleep(5)
        button.click()
        driver.find_element(AppiumBy.XPATH,
                            "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Option3']").click()
        time.sleep(5)
        driver.swipe(100, 800, 1000, 800, 1000)

    dropdownSelect()

def test_open_new_window(setup):
    def openNewWindow():
        search_text = ["30 DAY MONEY BACK GUARANTEE",
                       "SELF PACED ONLINE TRAINING",
                       "IN DEPTH MATERIAL",
                       "LIFETIME INSTRUCTOR SUPPORT",
                       "RESUME PREPARATION",
                       "a"]

    openNewWindow()

def test_switch_tab(setup):
    def switchTab():
        button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Open Window']")
        button.click()
        time.sleep(10)
        for _ in range(1):
            try:
                driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=500, duration=1000)
                time.sleep(2)
                element = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='']")
                print("Elemento encontrado")
                element.click()
                screenshot_path = 'C:/Users/cesar/PycharmProjects/Stori-QA-Automation-Challenge/ss/screenshot.png'
                driver.get_screenshot_as_file(screenshot_path)
            except:
                print("Elemento no encontrado")

            driver.back()

    switchTab()

def test_switch_to_alert(setup):
    def switchToAlert():
        driver.swipe(start_x=30, start_y=500, end_x=1000, end_y=500, duration=1000)
        driver.swipe(start_x=500, start_y=350, end_x=500, end_y=2200, duration=1000)

        driver.swipe(start_x=1000, start_y=500, end_x=500, end_y=500, duration=1000)
        validText = "Hello Stori Card, Are you sure you want to confirm?"
        for _ in range(2):
            try:
                inputText = driver.find_element(AppiumBy.XPATH,
                                                "(//android.view.View[@text='Switch To Alert Example'])[1]/android.widget.EditText")
                if inputText:
                    inputText.send_keys("Stori Card")
            except:
                print("Element not found in this screen")
                driver.swipe(start_x=1000, start_y=500, end_x=100, end_y=500, duration=1000)

        driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Alert']").click()

        alertText = driver.find_element(AppiumBy.XPATH,
                                        "//android.widget.TextView[@resource-id='com.android.chrome:id/message_paragraph_1']").text
        print(alertText)

        time.sleep(3)
        driver.find_element(AppiumBy.XPATH,
                            "//android.widget.Button[@resource-id='com.android.chrome:id/positive_button']").click()
        time.sleep(1)

        inputText.send_keys("Stori Card")

        driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Confirm']").click()
        time.sleep(1)
        confirmText = driver.find_element(AppiumBy.XPATH,
                                          "//android.widget.TextView[@resource-id='com.android.chrome:id/message_paragraph_1']").text

        print(validText)
        print(confirmText)

        if validText == confirmText:
            print("Is te same text")
            time.sleep(3)
        else:
            print("The texts aren't same")

        driver.find_element(AppiumBy.XPATH,
                            "//android.widget.Button[@resource-id='com.android.chrome:id/positive_button']").click()

    switchToAlert()

def test_web_table_exam(setup):
    def webTableExam():
        driver.swipe(start_x=30, start_y=500, end_x=1000, end_y=500, duration=1000)
        driver.swipe(start_x=500, start_y=350, end_x=500, end_y=2200, duration=1000)

        driver.swipe(start_x=500, start_y=1700, end_x=500, end_y=400, duration=1000)
        tabExample = driver.find_element(AppiumBy.XPATH, "(//android.view.View[@text='Web Table Example'])[1]")

        name25 = []
        price25 = []

        name15 = []
        price15 = []

        for i in range(10):
            rowName = tabExample.find_element(AppiumBy.XPATH, f"//android.widget.GridView/android.view.View[{i+2}]/android.view.View[2]")
            rowPrice = tabExample.find_element(AppiumBy.XPATH, f"//android.widget.GridView/android.view.View[{i+2}]/android.view.View[3]")

            priceResult = rowPrice.get_attribute("text")

            if priceResult == "25":
                name25.append(rowName.get_attribute("text"))
                price25.append(priceResult)
            if priceResult == "15":
                name15.append(rowName.get_attribute("text"))
                price15.append(priceResult)
            else:
                pass

        print("We have ", len(price25), " courses in 25")

        for nametf in name25:
                print(nametf)

        print("We have ", len(price15), " courses in 15")

        for nameft in name15:
                print(nameft)

    webTableExam()

def test_web_table_fix(setup):
    def webTableFix():
        driver.swipe(start_x=1000, start_y=500, end_x=100, end_y=500, duration=1000)
        isEngineer = []
        isBusinessman = []

        tabFix = driver.find_element(AppiumBy.XPATH, "(//android.view.View[@text='Web Table Fixed header'])[1]/android.view.View[2]")

        for i in range(9):
            name_row = tabFix.find_element(AppiumBy.XPATH, f"//android.widget.GridView/android.view.View[{i+2}]/android.view.View[1]")
            position_row = tabFix.find_element(AppiumBy.XPATH, f"//android.widget.GridView/android.view.View[{i+2}]/android.view.View[2]").get_attribute("text")

            if position_row == "Engineer":
                isEngineer.append(name_row.get_attribute("text"))
            if position_row == "Businessman":
                isBusinessman.append(name_row.get_attribute("text"))
            else:
                pass

        for engineer in isEngineer:
            print(engineer)
        for businessman in isBusinessman:
            print(businessman)

    webTableFix()

def test_iframe_exam(setup):
    def iframeExam():
        driver.press_keycode(82)  # Abre el menú de Chrome
        time.sleep(1)
        driver.find_element(AppiumBy.XPATH,
                            "//android.widget.TextView[@text='Refresh']").click()  # Selecciona "Refresh"
        time.sleep(5)

        driver.swipe(start_x=500, start_y=2200, end_x=500, end_y=300, duration=1000)
        driver.swipe(start_x=500, start_y=1770, end_x=500, end_y=300, duration=1000)
        driver.swipe(start_x=1000, start_y=1330, end_x=50, end_y=1330, duration=1000)
        driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        driver.swipe(start_x=800, start_y=1330, end_x=800, end_y=450, duration=1000)
        driver.swipe(start_x=800, start_y=1330, end_x=500, end_y=1330, duration=1000)

        textSelect = driver.find_element(AppiumBy.XPATH,
                            "//android.view.View[@text='His mentorship program is most after in the software testing community with long waiting period.']")

        print(textSelect.get_attribute("text"))

    iframeExam()