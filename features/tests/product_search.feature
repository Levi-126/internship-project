Feature: Test cases for Product Search on Target


  Scenario: User can edit personal info in settings
    Given Open Reely main page
    When Login to the Page
    When Click on Settings Option
    And Click on Edit Profile Option
    Then Enter test information
    Then Check the right information is present
    And Check the Close and Save Changes buttons are Available


