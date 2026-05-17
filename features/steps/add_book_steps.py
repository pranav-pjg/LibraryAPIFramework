"""
add_book_steps.py

This file contains step definitions for Add Book API scenarios.
"""

import os
from behave import given, when, then

from payloads.add_book_payload import add_book_payload
from resources.api_resources import ApiResources
from utilities.api_client import APIClient
from utilities.assertions import (
    assert_status_code,
    assert_equals,
    assert_key_exists,
    validate_json_schema,
)
from utilities.random_generator import generate_isbn, generate_aisle


@given("user has valid book details")
def step_user_has_valid_book_details(context):
    """
    Prepares valid request payload for Add Book API.
    """

    # Generate unique ISBN and aisle to avoid duplicate book errors
    context.isbn = generate_isbn()
    context.aisle = generate_aisle()

    # Build complete Add Book API URL
    context.url = context.base_url + ApiResources.ADD_BOOK

    # Create request payload
    context.payload = add_book_payload(context.isbn, context.aisle)


@when("user sends POST request to Add Book API")
def step_user_sends_post_request_to_add_book_api(context):
    """
    Sends POST request to Add Book API.
    """

    # Send POST request using centralized API client
    context.response = APIClient.post(
        url=context.url, payload=context.payload, headers=context.headers
    )

    # Convert response into JSON
    context.response_json = context.response.json()


@then("Add Book API response status code should be 200")
def step_add_book_status_code_should_be_200(context):
    """
    Validates Add Book API status code.
    """

    assert_status_code(context.response, 200)


@then('response message should be "successfully added"')
def step_response_message_should_be_successfully_added(context):
    """
    Validates success message in response.
    """

    assert_equals(context.response_json["Msg"], "successfully added")


@then("response should contain generated book ID")
def step_response_should_contain_generated_book_id(context):
    """
    Validates generated book ID exists in response.
    """

    # Validate ID key exists
    assert_key_exists(context.response_json, "ID")

    # Expected ID is isbn + aisle
    expected_book_id = context.isbn + context.aisle

    # Validate actual ID
    assert_equals(context.response_json["ID"], expected_book_id)


@then("Add Book API response schema should be valid")
def step_add_book_response_schema_should_be_valid(context):
    """
    Validates Add Book API response against JSON schema.
    """

    # Build schema file path
    schema_path = os.path.join(os.getcwd(), "schemas", "add_book_response_schema.json")

    # Validate response JSON against schema
    validate_json_schema(context.response_json, schema_path)
