"""
Step definitions for login feature.
"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page

from pages.login_page import LoginPage


@given("I am on the login page")
def step_navigate_to_login(page: Page) -> None:
    """Navigate to the login page."""
    login_page = LoginPage(page)
    login_page.go_to_login_page()


@when(parsers.parse('I enter username "{username}"'))
def step_enter_username(page: Page, username: str) -> None:
    """Enter username."""
    login_page = LoginPage(page)
    login_page.enter_username(username)


@when(parsers.parse('I enter password "{password}"'))
def step_enter_password(page: Page, password: str) -> None:
    """Enter password."""
    login_page = LoginPage(page)
    login_page.enter_password(password)


@when("I click the login button")
def step_click_login(page: Page) -> None:
    """Click the login button."""
    login_page = LoginPage(page)
    login_page.click_login()


@then("I should see the success message")
def step_verify_success_message(page: Page) -> None:
    """Verify success message is displayed."""
    login_page = LoginPage(page)
    assert login_page.is_success_message_displayed(), "Success message not found"


@then("I should see the error message")
def step_verify_error_message(page: Page) -> None:
    """Verify error message is displayed."""
    login_page = LoginPage(page)
    assert login_page.is_error_message_displayed(), "Error message not found"
