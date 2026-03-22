"""
Utility functions for test automation framework.
"""
import logging
import os
from typing import Optional


logger = logging.getLogger(__name__)


def create_directory(path: str) -> None:
    """
    Create directory if it doesn't exist.

    Args:
        path: Directory path to create.
    """
    os.makedirs(path, exist_ok=True)
    logger.debug(f"Directory created/verified: {path}")


def ensure_reports_directories() -> None:
    """Ensure all required report directories exist."""
    directories = [
        "reports/allure-results",
        "reports/screenshots",
        "reports/traces",
    ]
    for directory in directories:
        create_directory(directory)


def get_test_data_path() -> str:
    """
    Get path to test data directory.

    Returns:
        Path to test data directory.
    """
    return os.path.join(os.path.dirname(__file__), "..", "test_data")


def load_test_data(filename: str) -> dict:
    """
    Load test data from JSON file.

    Args:
        filename: Name of JSON file in test_data directory.

    Returns:
        Dictionary with test data.
    """
    import json

    path = os.path.join(get_test_data_path(), filename)
    with open(path) as f:
        return json.load(f)


class WaitHelper:
    """Helper class for waiting operations."""

    @staticmethod
    def wait_for_condition(
        condition_func,
        max_retries: int = 10,
        delay_ms: int = 500,
        error_message: str = "Condition not met",
    ) -> bool:
        """
        Wait for condition to be true.

        Args:
            condition_func: Function that returns boolean.
            max_retries: Maximum number of retries.
            delay_ms: Delay between retries in milliseconds.
            error_message: Error message if condition not met.

        Returns:
            True if condition met, False otherwise.
        """
        import time

        for attempt in range(max_retries):
            try:
                if condition_func():
                    logger.debug(f"Condition met on attempt {attempt + 1}")
                    return True
            except Exception as e:
                logger.debug(f"Attempt {attempt + 1} failed: {e}")

            time.sleep(delay_ms / 1000)

        logger.error(error_message)
        return False
