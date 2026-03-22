"""
Login page object for the-internet.herokuapp.com/login.
"""
from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    """Page object for login functionality."""

    # Selectors using both data-testid and fallback CSS selectors
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    SUCCESS_MESSAGE = "div.flash.success"
    ERROR_MESSAGE = "div.flash.error"

    def __init__(self, page: Page) -> None:
        """
        Initialize login page.

        Args:
            page: Playwright page instance.
        """
        super().__init__(page)

    def go_to_login_page(self) -> None:
        """Navigate to the login page."""
        login_url = f"{self.settings.base_url_dev}/login"
        self.navigate_to(login_url)

    def enter_username(self, username: str) -> None:
        """
        Enter username.

        Args:
            username: Username to enter.
        """
        self.fill_input(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        """
        Enter password.

        Args:
            password: Password to enter.
        """
        self.fill_input(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        """Click the login button."""
        self.click_element(self.LOGIN_BUTTON)

    def is_success_message_displayed(self) -> bool:
        """
        Check if success message is displayed.

        Returns:
            True if success message is visible, False otherwise.
        """
        return self.is_visible(self.SUCCESS_MESSAGE)

    def is_error_message_displayed(self) -> bool:
        """
        Check if error message is displayed.

        Returns:
            True if error message is visible, False otherwise.
        """
        return self.is_visible(self.ERROR_MESSAGE)

    def get_success_message_text(self) -> str:
        """
        Get the text of the success message.

        Returns:
            Success message text.
        """
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message_text(self) -> str:
        """
        Get the text of the error message.

        Returns:
            Error message text.
        """
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username: str, password: str) -> None:
        """
        Perform login action.

        Args:
            username: Username for login.
            password: Password for login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
