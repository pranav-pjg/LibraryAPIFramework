@get_book @functional @regression
Feature: Get Book API Validation

  Scenario: Verify user can get book details by book ID
    Given user has already added a book to the library
    When user sends GET request to Get Book API using book ID
    Then Get Book API response status code should be 200
    And Get Book API response schema should be valid
    And response should contain correct book isbn and aisle

  Scenario: Verify user can get book details by author name
    Given user has already added a book to the library
    When user sends GET request to Get Book API using author name
    Then Get Book API response status code should be 200
    And response should contain book list for the author
