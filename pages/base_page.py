"""
Base page object containing common functionality for all pages.
"""
from typing import Optional

from playwright.sync_api import Page, Locator
from config import get_settings


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page) -> None:
        """
        Initialize base page object.

        Args:
            page: Playwright page instance.
        """
        self.page = page
        self.settings = get_settings()

    def navigate_to(self, url: str) -> None:
        """
        Navigate to a specific URL.

        Args:
            url: URL to navigate to.
        """
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def find_element(self, selector: str) -> Locator:
        """
        Find element by selector.

        Args:
            selector: CSS selector for the element.

        Returns:
            Locator object.
        """
        return self.page.locator(selector)

    def find_element_by_testid(self, testid: str) -> Locator:
        """
        Find element by data-testid attribute.

        Args:
            testid: Value of data-testid attribute.

        Returns:
            Locator object.
        """
        return self.page.locator(f"[data-testid='{testid}']")

    def click_element(self, selector: str) -> None:
        """
        Click an element.

        Args:
            selector: CSS selector for the element.
        """
        self.find_element(selector).click()

    def fill_input(self, selector: str, text: str) -> None:
        """
        Fill text input field.

        Args:
            selector: CSS selector for the input element.
            text: Text to fill.
        """
        self.find_element(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """
        Get text content of an element.

        Args:
            selector: CSS selector for the element.

        Returns:
            Text content.
        """
        return self.find_element(selector).text_content() or ""

    def is_visible(self, selector: str) -> bool:
        """
        Check if element is visible.

        Args:
            selector: CSS selector for the element.

        Returns:
            True if element is visible, False otherwise.
        """
        return self.find_element(selector).is_visible()

    def wait_for_element(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Wait for element to be visible.

        Args:
            selector: CSS selector for the element.
            timeout: Timeout in milliseconds. Uses config timeout if not specified.
        """
        timeout_ms = timeout or self.settings.timeout
        self.find_element(selector).wait_for(state="visible", timeout=timeout_ms)

    def take_screenshot(self, filename: str) -> None:
        """
        Take a screenshot of the current page.

        Args:
            filename: Name for the screenshot file (without extension).
        """
        screenshots_dir = "reports/screenshots"
        import os
        os.makedirs(screenshots_dir, exist_ok=True)
        self.page.screenshot(path=f"{screenshots_dir}/{filename}.png")
