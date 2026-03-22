"""
Login tests using Page Object Model.
Can be run alongside BDD feature tests.
"""
import pytest
from playwright.sync_api import Page
import allure

from pages.login_page import LoginPage


class TestLogin:
    """Login test suite."""

    @pytest.mark.smoke
    @allure.feature("Authentication")
    @allure.story("User Login")
    @allure.title("Successful login with valid credentials")
    def test_successful_login_with_valid_credentials(self, page: Page) -> None:
        """
        Test successful login with valid credentials.

        Steps:
            1. Navigate to login page
            2. Enter valid username
            3. Enter valid password
            4. Click login button
            5. Verify success message is displayed
        """
        login_page = LoginPage(page)
        login_page.go_to_login_page()
        login_page.login("tomsmith", "SuperSecretPassword!")

        assert login_page.is_success_message_displayed(), "Success message not found"

    @pytest.mark.regression
    @allure.feature("Authentication")
    @allure.story("User Login")
    @allure.title("Failed login with invalid credentials")
    def test_failed_login_with_invalid_credentials(self, page: Page) -> None:
        """
        Test failed login with invalid credentials.

        Steps:
            1. Navigate to login page
            2. Enter invalid username
            3. Enter invalid password
            4. Click login button
            5. Verify error message is displayed
        """
        login_page = LoginPage(page)
        login_page.go_to_login_page()
        login_page.login("invaliduser", "wrongpassword")

        assert login_page.is_error_message_displayed(), "Error message not found"

    @pytest.mark.regression
    @allure.feature("Authentication")
    @allure.story("User Login")
    @allure.title("Failed login with empty username")
    def test_failed_login_with_empty_username(self, page: Page) -> None:
        """
        Test failed login with empty username.

        Steps:
            1. Navigate to login page
            2. Leave username empty
            3. Enter password
            4. Click login button
            5. Verify error message is displayed
        """
        login_page = LoginPage(page)
        login_page.go_to_login_page()
        login_page.enter_password("SuperSecretPassword!")
        login_page.click_login()

        assert login_page.is_error_message_displayed(), "Error message not found"
