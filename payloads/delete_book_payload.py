"""
delete_book_payload.py

This file builds request payloads for Delete Book API.
"""


def delete_book_payload(book_id):
    """
    Creates Delete Book API payload.

    Args:
        book_id (str): Book ID to delete

    Returns:
        dict: Delete Book request payload
    """

    return {"ID": book_id}
