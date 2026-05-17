"""
config_reader.py

This file is responsible for reading framework configuration values
from environment-specific configuration files.

Supported environments:
- qa
- stage
- prod

Example command:
behave -D env=qa
"""

import configparser
import os


# Get the base project directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_config(env="qa"):
    """
    Reads and returns configuration for the selected environment.

    Args:
        env (str): Environment name such as qa, stage, or prod

    Returns:
        configparser.ConfigParser: Loaded configuration object
    """

    # Build environment config file path dynamically
    config_file_path = os.path.join(
        BASE_DIR,
        "config",
        "environments",
        f"{env}.ini"
    )

    # Validate whether config file exists
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(
            f"Config file not found for environment: {env}. "
            f"Expected path: {config_file_path}"
        )

    # Create ConfigParser object
    config = configparser.ConfigParser()

    # Read selected environment config file
    config.read(config_file_path)

    return config


def get_base_url(env="qa"):
    """
    Reads and returns base API URL for selected environment.

    Args:
        env (str): Environment name

    Returns:
        str: Base API URL
    """

    config = get_config(env)
    return config["API"]["base_url"]


def get_timeout(env="qa"):
    """
    Reads and returns API timeout value for selected environment.

    Args:
        env (str): Environment name

    Returns:
        int: Timeout value in seconds
    """

    config = get_config(env)
    return int(config["API"]["timeout"])
