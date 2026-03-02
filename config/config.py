"""
Configuration module for test automation framework.
Reads from environment variables via .env file.
"""
import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Environment
    environment: str = "dev"

    # Base URLs
    base_url_dev: str = "https://the-internet.herokuapp.com"
    base_url_staging: str = "https://staging.example.com"
    base_url_prod: str = "https://example.com"

    # Playwright Configuration
    headless: bool = True
    browser: str = "chromium"  # chromium, firefox, webkit
    timeout: int = 30000  # milliseconds

    # Test Execution
    log_level: str = "INFO"
    screenshot_on_failure: bool = True
    trace_on_failure: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


def get_base_url() -> str:
    """Get base URL based on current environment."""
    settings = get_settings()
    env = settings.environment.lower()

    if env == "staging":
        return settings.base_url_staging
    elif env == "prod":
        return settings.base_url_prod
    else:  # dev is default
        return settings.base_url_dev


# Export settings for easy import
settings = get_settings()
