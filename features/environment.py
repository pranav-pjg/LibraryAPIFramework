"""
environment.py

This file contains Behave hooks.
Behave automatically executes this file during test execution.

Hooks are used for:
- Setup before test execution
- Cleanup after test execution
- Sharing common data through context
- Reading environment value from command line
"""
import allure
from utilities.config_reader import get_base_url
from utilities.logger import get_logger


def before_all(context):
    """
    Runs once before all feature files.

    Args:
        context: Behave context object
    """

    # Initialize logger
    context.logger = get_logger()

    # Read environment from command line.
    # Example: behave -D env=qa
    # If no env is provided, default will be qa.
    context.env = context.config.userdata.get("env", "qa")

    # Store base URL globally in context based on selected environment
    context.base_url = get_base_url(context.env)

    # Common API headers
    context.headers = {"Content-Type": "application/json"}

    context.logger.info("Test execution started")
    context.logger.info(f"Selected Environment: {context.env}")
    context.logger.info(f"Base URL: {context.base_url}")


def before_scenario(context, scenario):
    """
    Runs before each scenario.

    Args:
        context: Behave context object
        scenario: Current scenario object
    """

    # Log scenario start in framework logs
    context.logger.info(f"Starting scenario: {scenario.name}")

    # Add Allure behavior labels.
    # These labels help Allure generate behavior-related report files like behaviors.json.
    # This can fix the Jenkins Allure overview widget issue:
    # 500 Unexpected token '<', "<!DOCTYPE..." is not valid JSON
    allure.dynamic.epic("Library API Automation")
    allure.dynamic.feature(context.feature.name)
    allure.dynamic.story(scenario.name)


def after_scenario(context, scenario):
    """
    Runs after each scenario.

    Args:
        context: Behave context object
        scenario: Current scenario object
    """

    context.logger.info(f"Completed scenario: {scenario.name}")
    context.logger.info(f"Scenario status: {scenario.status}")


def after_all(context):
    """
    Runs once after all feature files.
    """

    context.logger.info("Test execution completed")
