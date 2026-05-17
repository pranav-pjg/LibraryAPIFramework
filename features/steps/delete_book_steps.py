"""
delete_book_steps.py

This file contains step definitions for Delete Book API scenarios.

Test flow:
1. Add a new book
2. Capture generated book ID
3. Delete the generated book ID
4. Validate delete response
"""

from behave import given, when, then

from payloads.add_book_payload import add_book_payload
from payloads.delete_book_payload import delete_book_payload
from resources.api_resources import ApiResources
from utilities.api_client import APIClient
from utilities.assertions import assert_status_code, assert_equals
from utilities.random_generator import generate_isbn, generate_aisle


@given("user has added a book for delete operation")
def step_user_has_added_book_for_delete_operation(context):
    """
    Adds a new book before deleting it.

    This avoids deleting hardcoded or existing test data.
    """

    # Generate unique ISBN and aisle
    context.isbn = generate_isbn()
    context.aisle = generate_aisle()

    # Build Add Book API URL
    add_book_url = context.base_url + ApiResources.ADD_BOOK

    # Create Add Book request payload
    payload = add_book_payload(isbn=context.isbn, aisle=context.aisle)

    # Send Add Book API request
    add_response = APIClient.post(
        url=add_book_url, payload=payload, headers=context.headers
    )

    # Validate Add Book API response status
    assert_status_code(add_response, 200)

    # Convert Add Book response into JSON
    add_response_json = add_response.json()

    # Store generated book ID for delete operation
    context.book_id = add_response_json["ID"]


@when("user sends POST request to Delete Book API")
def step_user_sends_post_request_to_delete_book_api(context):
    """
    Sends POST request to Delete Book API using generated book ID.
    """

    # Build Delete Book API URL
    context.url = context.base_url + ApiResources.DELETE_BOOK

    # Create Delete Book payload
    context.payload = delete_book_payload(context.book_id)

    # Send Delete Book API request
    context.response = APIClient.post(
        url=context.url, payload=context.payload, headers=context.headers
    )

    # Convert Delete Book response into JSON
    context.response_json = context.response.json()


@then("Delete Book API response status code should be 200")
def step_delete_book_status_code_should_be_200(context):
    """
    Validates Delete Book API response status code.
    """

    assert_status_code(context.response, 200)


@then('delete response message should be "book is successfully deleted"')
def step_delete_response_message_should_be_success(context):
    """
    Validates Delete Book API success message.
    """

    assert_equals(context.response_json["msg"], "book is successfully deleted")


@then("Delete Book API response schema should be valid")
def step_delete_book_response_schema_should_be_valid(context):
    """
    Validates Delete Book API response against JSON schema.
    """

    import os
    from utilities.assertions import validate_json_schema

    # Build schema file path
    schema_path = os.path.join(
        os.getcwd(), "schemas", "delete_book_response_schema.json"
    )

    # Validate response JSON against schema
    validate_json_schema(context.response_json, schema_path)
