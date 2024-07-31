from behave import given, when, then
from tests.main_page import MainPage
from tests.drop_select import DropSelect
from tests.suggession_class import Suggession_Class
from tests.switch_tab import SwitchTab
from tests.switch_alert import SwitchAlert
from tests.table_courses import TableCourses
from tests.table_fix import TableFix
from tests.iframe_example import IframeExample
from tests.switch_window import SwitchWindow
import time

import os

if not os.path.exists('./reports'):
    os.makedirs('./reports')

@given('I open the web page')
def step_impl(context):
    time.sleep(10)
    context.main_page = MainPage(context.driver)
    context.main_page.enterUrl()


@then('I close the browser')
def step_impl(context):
    time.sleep(5)
    context.driver.quit()
    time.sleep(5)

@when('I test drop down select')
def step_impl(context):
    context.drop_select = DropSelect(context.driver)
    context.drop_select.drop_select()
    time.sleep(5)


@when('I enter "{initial}"')
def step_impl(context, initial):
    context.suggession_class = Suggession_Class(context.driver)
    context.suggession_class.enter_ini(initial)
    time.sleep(5)


@then('I select "{country}"')
def step_impl(context, country):
    context.suggession_class = Suggession_Class(context.driver)
    context.suggession_class.select_country(country)
    time.sleep(5)


@when('I enter in web page')
def step_impl(context):
    context.switch_tab = SwitchTab(context.driver)
    context.switch_tab.enter_page()
    time.sleep(5)


@when('I found the element')
def step_impl(context):
    context.switch_tab = SwitchTab(context.driver)
    context.switch_tab.found_element()
    time.sleep(5)


@then('I back')
def step_impl(context):
    context.switch_tab = SwitchTab(context.driver)
    context.switch_tab.back_page()
    time.sleep(5)


@when('I found input')
def step_impl(context):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.found_input()
    time.sleep(5)


@when('I enter the text "{name}"')
def step_impl(context, name):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.enter_text(name)
    time.sleep(5)


@when('I click the button "{btn_text}"')
def step_impl(context,btn_text):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.click_button(btn_text)
    time.sleep(5)


@then('I print the text')
def step_impl(context):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.print_text()
    time.sleep(5)


@then('I confirm')
def step_impl(context):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.confirm()
    time.sleep(5)

@then('I validate the text')
def step_impl(context):
    context.switch_alert = SwitchAlert(context.driver)
    context.switch_alert.validate_text()
    time.sleep(5)


@when('I found the table course')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.found_table()
    time.sleep(5)


@then('I count how many courses cost 25')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.count_25()
    time.sleep(5)


@then('I print how many courses cost 25')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.print_25()
    time.sleep(5)


@then('I count how many courses cost 15')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.count_15()
    time.sleep(5)


@then('I print how many courses cost 15')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.print_15()
    time.sleep(5)


@then('I print the names of courses in 25')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.print_name_courses25()
    time.sleep(5)


@then('I print the names of courses in 15')
def step_impl(context):
    context.table_course = TableCourses(context.driver)
    context.table_course.print_name_courses15()
    time.sleep(5)


@when('I found the table fix')
def step_impl(context):
    context.table_fix = TableFix(context.driver)
    context.table_fix.found_table()
    time.sleep(5)


@then('I divide the position')
def step_impl(context):
    context.table_fix = TableFix(context.driver)
    context.table_fix.div_position()
    time.sleep(5)


@when('The position is Engineer I print')
def step_impl(context):
    context.table_fix = TableFix(context.driver)
    context.table_fix.print_enginner()
    time.sleep(5)


@when('The position is Businessman I print')
def step_impl(context):
    context.table_fix = TableFix(context.driver)
    context.table_fix.print_businessman()
    time.sleep(5)


@when('I found the frame example')
def step_impl(context):
    context.iframe_example = IframeExample(context.driver)
    context.iframe_example.found_frame()
    time.sleep(5)


@then('I print the text of the frame')
def step_impl(context):
    context.iframe_example = IframeExample(context.driver)
    context.iframe_example.print_text()
    time.sleep(5)


@when('I open the window')
def step_impl(context):
    context.switch_window = SwitchWindow(context.driver)
    context.switch_window.found_button()
    time.sleep(5)


@then('I found "{text}"')
def step_impl(context,text):
    context.switch_window = SwitchWindow(context.driver)
    context.switch_window.found_text(text)
    time.sleep(5)


@then('I return to the home page')
def step_impl(context):
    current_url = "https://rahulshettyacademy.com/AutomationPractice"
    context.driver.get(current_url)
    time.sleep(5)