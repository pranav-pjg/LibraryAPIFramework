"""
api_client.py

This file contains reusable HTTP methods.
All API requests in the framework should go through this class.

This helps with:
- Centralized request handling
- Request/response logging
- Allure request/response attachments
- Future retry logic
- Future authentication handling
"""

import json
import requests
import allure

from utilities.logger import get_logger


# Create logger object
logger = get_logger()


class APIClient:
    """
    Centralized API client class for handling HTTP methods.
    """

    @staticmethod
    def _attach_to_allure(name, content):
        """
        Attaches request/response information to Allure report.

        Args:
            name (str): Attachment name shown in Allure report
            content: Data to attach in report
        """

        # Convert dictionary/list content into pretty JSON string
        if isinstance(content, (dict, list)):
            content = json.dumps(content, indent=4)

        # Convert None to empty string
        if content is None:
            content = ""

        # Attach content to Allure report
        allure.attach(
            str(content),
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def post(url, payload=None, headers=None):
        """
        Sends a POST request.

        Args:
            url (str): Complete API URL
            payload (dict): Request body
            headers (dict): Request headers

        Returns:
            response: requests response object
        """

        # Log request details
        logger.info(f"POST Request URL: {url}")
        logger.info(f"POST Request Payload: {payload}")
        logger.info(f"POST Request Headers: {headers}")

        # Attach request details to Allure report
        APIClient._attach_to_allure("POST Request URL", url)
        APIClient._attach_to_allure("POST Request Headers", headers)
        APIClient._attach_to_allure("POST Request Payload", payload)

        # Send POST request
        response = requests.post(
            url=url,
            json=payload,
            headers=headers
        )

        # Log response details
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        # Attach response details to Allure report
        APIClient._attach_to_allure("Response Status Code", response.status_code)
        APIClient._attach_to_allure("Response Body", response.text)

        return response

    @staticmethod
    def get(url, headers=None, params=None):
        """
        Sends a GET request.

        Args:
            url (str): Complete API URL
            headers (dict): Request headers
            params (dict): Query parameters

        Returns:
            response: requests response object
        """

        # Log request details
        logger.info(f"GET Request URL: {url}")
        logger.info(f"GET Request Headers: {headers}")
        logger.info(f"GET Request Params: {params}")

        # Attach request details to Allure report
        APIClient._attach_to_allure("GET Request URL", url)
        APIClient._attach_to_allure("GET Request Headers", headers)
        APIClient._attach_to_allure("GET Request Params", params)

        # Send GET request
        response = requests.get(
            url=url,
            headers=headers,
            params=params
        )

        # Log response details
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        # Attach response details to Allure report
        APIClient._attach_to_allure("Response Status Code", response.status_code)
        APIClient._attach_to_allure("Response Body", response.text)

        return response
