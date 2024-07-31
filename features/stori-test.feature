Feature: Web Page Automation Iteration
    Background:
        Given I open the web page

    @open_page
    Scenario: Open the web page

    @drop_select
    Scenario: Test Drop Select
    When I test drop down select

    @suggession_class
    Scenario: Enter initial country
    When I enter "Me"
    Then I select "Mexico"
    When I enter "Uni"
    Then I select "United Arab Emirates"
    When I enter "Uni"
    Then I select "United States (USA)"
    When I enter "Ca"
    Then I select "Canada"
    When I enter "Ja"
    Then I select "Japan"

    @switch_window
    Scenario: Test Switch Window
    When I open the window
    Then I found "30 day money back guarantee"
    And I back

    @switch_tab
    Scenario: Test Switch Tab Example
    When I enter in web page
    And I found the element
    Then I back

    @switch_alert
    Scenario: Test Switch Alert
    When I found input
    And I enter the text "Stori Card"
    And I click the button "Alert"
    Then I print the text
    And I confirm
    When I enter the text "Stori Card"
    And I click the button "Confirm"
    Then I print the text
    And I confirm

    @table_courses
    Scenario: Print the course in 15 and 25
    When I found the table course
    Then I count how many courses cost 25
    And I print how many courses cost 25
    Then I count how many courses cost 15
    And I print how many courses cost 15
    Then I print the names of courses in 25
    And I print the names of courses in 15

    @table_fix
    Scenario: Print Engineer and Businessman
    When I found the table fix
    Then I divide the position
    When The position is Engineer I print
    And The position is Businessman I print

    @iframe_example
    Scenario: Found a text in the frame
    When I found the frame example
    Then I print the text of the frame