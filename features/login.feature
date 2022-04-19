Feature: Login

  Scenario Outline: Login on application
    Given launch application
    Then verify home page
    When click on sign in button
    Then user redirected to sign in page
    And user enters "<email>" and "<password>"
    And click on log in button
    And verify label page
    And logged out from the application
    Then verify home page

    Examples:
    | email  | password |
      | qa@mementia.com | Testpass1    |
