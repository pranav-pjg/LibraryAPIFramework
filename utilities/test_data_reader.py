"""
test_data_reader.py

This file is responsible for reading test data from JSON files.

In enterprise frameworks, test data is usually maintained separately
from automation logic to improve maintainability.
"""

import json
import os


# Get project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_json_file(file_name):
    """
    Reads a JSON file from testdata folder.

    Args:
        file_name (str): JSON file name inside testdata folder

    Returns:
        dict: JSON content as dictionary
    """

    # Build complete test data file path
    file_path = os.path.join(BASE_DIR, "testdata", file_name)

    # Validate whether file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    # Open and read JSON file
    with open(file_path, "r") as file:
        return json.load(file)


def get_add_book_data():
    """
    Returns Add Book API test data.

    Returns:
        dict: Add Book test data
    """

    return read_json_file("add_book_data.json")


def get_delete_book_data():
    """
    Returns Delete Book API test data.

    Returns:
        dict: Delete Book test data
    """

    return read_json_file("delete_book_data.json")


def get_regression_data():
    """
    Returns regression test data.

    Returns:
        dict: Regression test data
    """

    return read_json_file("regression_data.json")
