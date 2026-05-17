@add_book @functional @smoke @regression
Feature: Add Book API Validation

  Scenario: Verify user can add a new book successfully
    Given user has valid book details
    When user sends POST request to Add Book API
    Then Add Book API response status code should be 200
    And response message should be "successfully added"
    And response should contain generated book ID
    And Add Book API response schema should be valid
