"""
negative_steps.py

This file contains negative test step definitions.

Negative testing validates API behavior for:
- Missing fields
- Invalid IDs
- Invalid request data
"""

from behave import given, when, then

from payloads.delete_book_payload import delete_book_payload
from resources.api_resources import ApiResources
from utilities.api_client import APIClient
from utilities.assertions import assert_status_code


@given("user has book details without isbn")
def step_user_has_book_details_without_isbn(context):
    """
    Creates Add Book API payload without mandatory ISBN field.
    """

    # Build Add Book API URL
    context.url = context.base_url + ApiResources.ADD_BOOK

    # Create invalid payload by skipping isbn
    context.payload = {
        "name": "Learn Appium Automation with Java",
        "aisle": "9999",
        "author": "John foe",
    }


@when("user sends POST request to Add Book API with invalid payload")
def step_user_sends_post_request_with_invalid_payload(context):
    """
    Sends POST request to Add Book API using invalid payload.
    """

    # Send API request with invalid payload
    context.response = APIClient.post(
        url=context.url, payload=context.payload, headers=context.headers
    )

    # Store raw response text also because some negative APIs may not return JSON
    context.response_text = context.response.text


@then("API response status code should be 200")
def step_api_response_status_code_should_be_200(context):
    """
    Validates API response status code as 200.

    Note:
    Some APIs return HTTP 200 even for business validation errors.
    """

    assert_status_code(context.response, 200)


@then("Add Book API should return an error message")
def step_add_book_should_return_error_message(context):
    """
    Validates Add Book API returns some error response.
    """

    # Validate response is not empty
    assert (
        context.response_text.strip() != ""
    ), "Expected error response, but response was empty"


@given("user has invalid book ID for delete operation")
def step_user_has_invalid_book_id_for_delete(context):
    """
    Creates invalid book ID for Delete Book API.
    """

    # Build Delete Book API URL
    context.url = context.base_url + ApiResources.DELETE_BOOK

    # Use invalid/non-existing book ID
    context.invalid_book_id = "invalid999999"

    # Create Delete Book request payload
    context.payload = delete_book_payload(context.invalid_book_id)


@when("user sends POST request to Delete Book API with invalid ID")
def step_user_sends_delete_request_with_invalid_id(context):
    """
    Sends Delete Book API request with invalid book ID.
    """

    # Send Delete Book API request
    context.response = APIClient.post(
        url=context.url, payload=context.payload, headers=context.headers
    )

    # Store response text
    context.response_text = context.response.text


@then("API response status code should be 404")
def step_api_response_status_code_should_be_404(context):
    """
    Validates API response status code as 404.
    """

    assert_status_code(context.response, 404)


@then("Delete Book API should return an error message")
def step_delete_book_should_return_error_message(context):
    """
    Validates Delete Book API returns error response.
    """

    # Validate response is not empty
    assert (
        context.response_text.strip() != ""
    ), "Expected error response, but response was empty"


@given("user has invalid book ID for get book operation")
def step_user_has_invalid_book_id_for_get_book(context):
    """
    Creates invalid book ID for Get Book API.
    """

    # Build Get Book API URL
    context.url = context.base_url + ApiResources.GET_BOOK

    # Use invalid/non-existing book ID
    context.invalid_book_id = "invalid999999"


@when("user sends GET request to Get Book API with invalid ID")
def step_user_sends_get_request_with_invalid_id(context):
    """
    Sends Get Book API request with invalid book ID.
    """

    # Send Get Book API request with invalid ID parameter
    context.response = APIClient.get(
        url=context.url, headers=context.headers, params={"ID": context.invalid_book_id}
    )

    # Store response text
    context.response_text = context.response.text


@then("Add Book API should return empty response")
def step_add_book_should_return_empty_response(context):
    """
    Validates Add Book API returns empty response body
    when mandatory ISBN field is missing.

    Note:
    This public demo API returns HTTP 200 with empty body
    instead of a proper validation error response.
    """

    # Validate response body is empty
    assert (
        context.response_text.strip() == ""
    ), f"Expected empty response, but got: {context.response_text}"
