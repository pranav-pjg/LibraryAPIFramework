"""
add_book_payload.py

This file builds request payloads for Add Book API.
"""

from utilities.test_data_reader import get_add_book_data


def add_book_payload(isbn, aisle):
    """
    Creates Add Book API payload using default book test data.

    Args:
        isbn (str): Book ISBN
        aisle (str): Book aisle

    Returns:
        dict: Add Book request payload
    """

    # Read Add Book test data from JSON file
    book_data = get_add_book_data()["valid_book"]

    # Build Add Book API payload
    return {
        "name": book_data["name"],
        "isbn": isbn,
        "aisle": aisle,
        "author": book_data["author"],
    }


def add_book_payload_with_author(isbn, aisle, author):
    """
    Creates Add Book API payload with custom author.

    Args:
        isbn (str): Book ISBN
        aisle (str): Book aisle
        author (str): Book author

    Returns:
        dict: Add Book request payload
    """

    # Read Add Book test data from JSON file
    book_data = get_add_book_data()["valid_book"]

    # Build Add Book API payload with custom author
    return {"name": book_data["name"], "isbn": isbn, "aisle": aisle, "author": author}
