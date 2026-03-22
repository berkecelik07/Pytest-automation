"""
Pytest configuration and fixtures.
"""
import os
import logging
from typing import Generator

import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from allure import attach, attachment_type

from config import get_settings
from pytest_bdd import parsers


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser_type():
    """Get browser type from settings."""
    return get_settings().browser


@pytest.fixture(scope="session")
def is_headless() -> bool:
    """Check if headless mode is enabled."""
    return get_settings().headless


@pytest.fixture(scope="function")
def browser(browser_type: str) -> Generator[Browser, None, None]:
    """
    Create and yield browser instance.

    Args:
        browser_type: Type of browser (chromium, firefox, webkit).

    Yields:
        Browser instance.
    """
    settings = get_settings()

    with sync_playwright() as p:
        if browser_type.lower() == "firefox":
            browser_obj = p.firefox.launch(headless=settings.headless)
        elif browser_type.lower() == "webkit":
            browser_obj = p.webkit.launch(headless=settings.headless)
        else:  # chromium is default
            browser_obj = p.chromium.launch(headless=settings.headless)

        yield browser_obj
        browser_obj.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """
    Create and yield browser context instance.

    Args:
        browser: Browser instance.

    Yields:
        BrowserContext instance.
    """
    context_obj = browser.new_context()
    yield context_obj
    context_obj.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """
    Create and yield page instance.

    Args:
        context: BrowserContext instance.

    Yields:
        Page instance.
    """
    page_obj = context.new_page()

    # Set default timeout from settings
    settings = get_settings()
    page_obj.set_default_timeout(settings.timeout)

    yield page_obj

    page_obj.close()


@pytest.fixture
def pytest_bdd_parse_example(request):
    """Parse examples for parametrized scenarios."""
    return parsers.parse


def pytest_runtest_makereport(item, call):
    """
    Hook for pytest to create test report.
    Used for attaching screenshots on failure.
    """
    if call.when == "call" and call.excinfo is not None:
        # Test failed
        settings = get_settings()

        if settings.screenshot_on_failure:
            # Try to attach screenshot if page fixture exists
            if "page" in item.fixturenames:
                try:
                    page = item.funcargs.get("page")
                    if page:
                        screenshot_path = "reports/screenshots"
                        os.makedirs(screenshot_path, exist_ok=True)
                        filename = f"{screenshot_path}/{item.name}.png"
                        page.screenshot(path=filename)

                        # Attach to Allure report
                        attach.file(
                            filename,
                            name=f"Screenshot: {item.name}",
                            attachment_type=attachment_type.PNG,
                        )
                        logger.info(f"Screenshot saved: {filename}")
                except Exception as e:
                    logger.warning(f"Failed to take screenshot: {e}")

        if settings.trace_on_failure:
            # Try to attach trace if page fixture exists
            if "page" in item.fixturenames:
                try:
                    page = item.funcargs.get("page")
                    if page and hasattr(page.context, "tracing"):
                        trace_path = "reports/traces"
                        os.makedirs(trace_path, exist_ok=True)
                        filename = f"{trace_path}/{item.name}.zip"
                        # Note: Tracing needs to be started in fixture
                        # This is a placeholder for trace attachment
                        logger.info(f"Trace would be saved: {filename}")
                except Exception as e:
                    logger.warning(f"Failed to save trace: {e}")


@pytest.fixture(scope="session", autouse=True)
def setup_allure_environment() -> None:
    """
    Set up Allure environment variables.
    """
    settings = get_settings()
    os.makedirs("reports/allure-results", exist_ok=True)

    # Create environment.properties for Allure
    env_properties = f"""OS={os.name}
Environment={settings.environment}
Browser={settings.browser}
Headless={settings.headless}
"""
    with open("reports/allure-results/environment.properties", "w") as f:
        f.write(env_properties)
