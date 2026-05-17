"""
random_generator.py

This file generates dynamic test data.

Dynamic data is useful because APIs may reject duplicate records.
Example: same ISBN and aisle combination may already exist.
"""

import random
import string


def generate_isbn(length=5):
    """
    Generates a random ISBN string.

    Args:
        length (int): Number of characters to generate

    Returns:
        str: Random lowercase ISBN value
    """

    # Generate random lowercase letters
    return "".join(random.choices(string.ascii_lowercase, k=length))


def generate_aisle():
    """
    Generates a random aisle number.

    Returns:
        str: Random aisle number as string
    """

    # Generate random 4-digit aisle number
    return str(random.randint(1000, 9999))
