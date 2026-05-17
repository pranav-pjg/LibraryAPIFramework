@regression
Feature: Library API Regression Suite

  @add_book @functional
  Scenario: Verify user can add a new book successfully
    Given user has valid book details
    When user sends POST request to Add Book API
    Then Add Book API response status code should be 200
    And response message should be "successfully added"
    And response should contain generated book ID
    And Add Book API response schema should be valid

  @get_book @functional
  Scenario: Verify user can get book details by book ID
    Given user has already added a book to the library
    When user sends GET request to Get Book API using book ID
    Then Get Book API response status code should be 200
    And Get Book API response schema should be valid
    And response should contain correct book isbn and aisle

  @get_book @functional
  Scenario: Verify user can get book details by author name
    Given user has already added a book to the library
    When user sends GET request to Get Book API using author name
    Then Get Book API response status code should be 200
    And response should contain book list for the author

  @delete_book @functional
  Scenario: Verify user can delete an existing book successfully
    Given user has added a book for delete operation
    When user sends POST request to Delete Book API
    Then Delete Book API response status code should be 200
    And Delete Book API response schema should be valid
    And delete response message should be "book is successfully deleted"
