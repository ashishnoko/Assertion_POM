
Feature: Login functionality

  Scenario: Valid User
    Given the browser is open
    When the user navigates to the login page
    And enters valid credentials
    Then the user should be redirected to the homepage