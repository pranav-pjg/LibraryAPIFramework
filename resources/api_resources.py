"""
api_resources.py

This file stores all API endpoint paths in one place.
If endpoint changes in future, update only this file.
"""


class ApiResources:
    """
    Centralized API resource paths for Library API.
    """

    # Endpoint to add a new book
    ADD_BOOK = "/Library/Addbook.php"

    # Endpoint to get book by ID or author
    GET_BOOK = "/Library/GetBook.php"

    # Endpoint to delete an existing book
    DELETE_BOOK = "/Library/DeleteBook.php"
