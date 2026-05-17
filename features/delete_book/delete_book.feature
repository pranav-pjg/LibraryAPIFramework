@delete_book @functional @smoke @regression
Feature: Delete Book API Validation

  Scenario: Verify user can delete an existing book successfully
    Given user has added a book for delete operation
    When user sends POST request to Delete Book API
    Then Delete Book API response status code should be 200
    And Delete Book API response schema should be valid
    And delete response message should be "book is successfully deleted"
