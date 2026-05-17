"""
assertions.py

This file contains reusable assertion methods.
Using common assertion methods keeps step definitions clean and consistent.
"""

import json
from jsonschema import validate


def assert_status_code(response, expected_code):
    """
    Validates API response status code.

    Args:
        response: requests response object
        expected_code (int): Expected HTTP status code
    """

    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, " f"but got {response.status_code}"
    )


def assert_key_exists(response_json, key):
    """
    Validates whether a key exists in API response JSON.

    Args:
        response_json (dict): API response JSON
        key (str): Key to validate
    """

    assert key in response_json, f"Key '{key}' not found in response"


def assert_equals(actual, expected):
    """
    Validates whether actual value equals expected value.

    Args:
        actual: Actual value from response
        expected: Expected value
    """

    assert actual == expected, f"Expected '{expected}', but got '{actual}'"


def validate_json_schema(response_json, schema_file_path):
    """
    Validates API response JSON against a JSON schema file.

    Args:
        response_json (dict): API response JSON
        schema_file_path (str): Path of schema JSON file
    """

    # Open schema file
    with open(schema_file_path, "r") as schema_file:

        # Load schema JSON content
        schema = json.load(schema_file)

    # Validate response against schema
    validate(instance=response_json, schema=schema)
