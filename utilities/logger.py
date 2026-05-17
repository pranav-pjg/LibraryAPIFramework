"""
logger.py

This file creates a centralized logger for the framework.
All request, response, and execution logs will be written into logs/execution.log.
"""

import logging
import os


# Get the base project directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define log file path
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "execution.log")


def get_logger():
    """
    Creates and returns a logger object.

    Returns:
        logger: Python logger object
    """

    # Get root logger
    logger = logging.getLogger()

    # Avoid adding duplicate handlers every time logger is called
    if not logger.handlers:

        # Set logging level to INFO
        logger.setLevel(logging.INFO)

        # Create file handler to write logs into execution.log
        file_handler = logging.FileHandler(LOG_FILE_PATH)

        # Define log format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # Attach formatter to file handler
        file_handler.setFormatter(formatter)

        # Add file handler to logger
        logger.addHandler(file_handler)

    return logger

