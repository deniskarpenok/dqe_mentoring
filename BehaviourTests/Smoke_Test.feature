Feature: Google Page Smoke Test

  Scenario: Open Google page and search
    Given main page was opened
    When search for "epam"
    Then link "https://careers.epam.by" on the result page


  Scenario: Open Google page and search
    Given main page was opened
    When search for "something else"
    And do something else
    Then link "https://epam.by" on the result page