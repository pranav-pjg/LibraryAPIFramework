"""
get_book_steps.py

This file contains step definitions for Get Book API scenarios.

Covered scenarios:
- Get book details by book ID
- Get book details by author name

Important:
Some Library API responses return JSON as a list of objects.
So we handle response carefully instead of assuming it is always a dictionary.
"""

from behave import given, when, then

from payloads.add_book_payload import add_book_payload_with_author
from resources.api_resources import ApiResources
from utilities.api_client import APIClient
from utilities.assertions import assert_status_code, assert_equals
from utilities.random_generator import generate_isbn, generate_aisle


@given("user has already added a book to the library")
def step_user_has_already_added_book(context):
    """
    Adds a new book before validating Get Book API.

    This makes the test independent and avoids using hardcoded old test data.
    """

    # Generate unique ISBN and aisle to avoid duplicate book errors
    context.isbn = generate_isbn()
    context.aisle = generate_aisle()

    # Use author name without spaces to avoid API response issues
    context.author = "Johnfoe"

    # Build Add Book API URL
    add_book_url = context.base_url + ApiResources.ADD_BOOK

    # Create Add Book request payload
    payload = add_book_payload_with_author(
        isbn=context.isbn, aisle=context.aisle, author=context.author
    )

    # Send POST request to add a new book
    add_response = APIClient.post(
        url=add_book_url, payload=payload, headers=context.headers
    )

    # Validate Add Book API status code
    assert_status_code(add_response, 200)

    # Convert Add Book response into JSON
    add_response_json = add_response.json()

    # Store generated book ID for Get Book API
    context.book_id = add_response_json["ID"]


@when("user sends GET request to Get Book API using book ID")
def step_user_sends_get_request_using_book_id(context):
    """
    Sends GET request to fetch book details using generated book ID.
    """

    # Build Get Book API URL
    context.url = context.base_url + ApiResources.GET_BOOK

    # Send GET request with ID query parameter
    context.response = APIClient.get(
        url=context.url, headers=context.headers, params={"ID": context.book_id}
    )

    # Convert response into JSON
    context.response_json = context.response.json()


@when("user sends GET request to Get Book API using author name")
def step_user_sends_get_request_using_author_name(context):
    """
    Sends GET request to fetch book details using author name.
    """

    # Build Get Book API URL
    context.url = context.base_url + ApiResources.GET_BOOK

    # Send GET request with AuthorName query parameter
    context.response = APIClient.get(
        url=context.url, headers=context.headers, params={"AuthorName": context.author}
    )

    # Print response text for debugging if API does not return valid JSON
    print("Author API Response:", context.response.text)

    # Convert response into JSON
    context.response_json = context.response.json()


@then("Get Book API response status code should be 200")
def step_get_book_status_code_should_be_200(context):
    """
    Validates Get Book API response status code.
    """

    assert_status_code(context.response, 200)


@then("response should contain correct book isbn and aisle")
def step_response_should_contain_correct_book_details(context):
    """
    Validates that Get Book by ID response contains correct isbn and aisle.

    API may return response as:
    - dictionary
    - list containing one dictionary

    So we handle both formats safely.
    """

    # If response is a list, take the first book object
    if isinstance(context.response_json, list):
        book_details = context.response_json[0]
    else:
        book_details = context.response_json

    # Validate ISBN
    assert_equals(book_details["isbn"], context.isbn)

    # Validate aisle
    assert_equals(str(book_details["aisle"]), str(context.aisle))


@then("response should contain book list for the author")
def step_response_should_contain_book_list_for_author(context):
    """
    Validates that Get Book by Author response contains at least one book.

    Also verifies that the recently added book is present in the response.
    """

    # Validate response is a list
    assert isinstance(context.response_json, list), "Expected response to be a list"

    # Validate author has at least one book
    assert len(context.response_json) > 0, "Expected at least one book for author"

    # Check whether the recently added book is available in author response
    matching_books = [
        book
        for book in context.response_json
        if book.get("isbn") == context.isbn
        and str(book.get("aisle")) == str(context.aisle)
    ]

    # Validate matching book exists
    assert len(matching_books) > 0, "Added book was not found in author search response"


@then("Get Book API response schema should be valid")
def step_get_book_response_schema_should_be_valid(context):
    """
    Validates Get Book API response against JSON schema.

    Note:
    Get Book by ID API may return either:
    - List containing one book object
    - Single book object

    So we normalize the response before schema validation.
    """

    import os
    from utilities.assertions import validate_json_schema

    # Build schema file path
    schema_path = os.path.join(os.getcwd(), "schemas", "get_book_response_schema.json")

    # If response is a list, validate first object
    if isinstance(context.response_json, list):
        book_details = context.response_json[0]
    else:
        book_details = context.response_json

    # Validate response JSON against schema
    validate_json_schema(book_details, schema_path)
