@negative
Feature: Library API Negative Test Scenarios

  @add_book @negative
  Scenario: Verify Add Book API behavior when ISBN is missing
    Given user has book details without isbn
    When user sends POST request to Add Book API with invalid payload
    Then API response status code should be 200
    And Add Book API should return empty response

  @delete_book @negative
  Scenario: Verify Delete Book API behavior with invalid book ID
    Given user has invalid book ID for delete operation
    When user sends POST request to Delete Book API with invalid ID
    Then API response status code should be 404
    And Delete Book API should return an error message

  @get_book @negative
  Scenario: Verify Get Book API behavior with invalid book ID
    Given user has invalid book ID for get book operation
    When user sends GET request to Get Book API with invalid ID
    Then API response status code should be 404
