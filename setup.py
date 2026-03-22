"""
Setup configuration for test automation framework.
Can install using: pip install -e .
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="test-automation-framework",
    version="1.0.0",
    author="QA Team",
    author_email="qa@example.com",
    description="Production-ready test automation framework using Pytest, Playwright, and BDD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/test-automation-framework",
    python_requires=">=3.11",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.3",
        "pytest-asyncio==0.21.1",
        "pytest-bdd==6.1.1",
        "pytest-xdist==3.5.0",
        "allure-pytest==2.13.2",
        "playwright==1.40.0",
        "python-dotenv==1.0.0",
        "pydantic==2.5.0",
        "pydantic-settings==2.1.0",
    ],
    extras_require={
        "dev": [
            "black==23.12.1",
            "ruff==0.1.8",
            "pre-commit==3.5.0",
        ],
    },
)
