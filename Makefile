.PHONY: help install install-dev clean test test-smoke test-regression test-headed test-parallel format lint pre-commit allure-report allure-serve

help:
	@echo "Test Automation Framework - Available Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install           Install production dependencies"
	@echo "  make install-dev       Install development dependencies"
	@echo "  make clean             Remove build artifacts, cache, and reports"
	@echo ""
	@echo "Testing:"
	@echo "  make test              Run all tests"
	@echo "  make test-smoke        Run smoke tests only"
	@echo "  make test-regression   Run regression tests only"
	@echo "  make test-headed       Run tests in headed mode (browser visible)"
	@echo "  make test-parallel     Run tests in parallel"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format            Format code with black and ruff"
	@echo "  make lint              Run linting checks"
	@echo "  make pre-commit        Install pre-commit hooks"
	@echo ""
	@echo "Reporting:"
	@echo "  make allure-report     Generate Allure report"
	@echo "  make allure-serve      Generate and serve Allure report"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	playwright install chromium firefox webkit

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .coverage htmlcov/
	rm -rf reports/
	rm -rf .allure/

test:
	pytest tests/ features/

test-bdd:
	pytest --gherkin-terminal-reporter tests/ features/

test-smoke:
	pytest -m smoke tests/ features/

test-regression:
	pytest -m regression tests/ features/

test-headed:
	HEADLESS=false pytest tests/ features/

test-parallel:
	pytest -n auto tests/ features/

format:
	black .
	ruff check . --fix

lint:
	ruff check .
	black --check .

pre-commit:
	pre-commit install

allure-report:
	allure generate reports/allure-results -o allure-report --clean

allure-serve:
	allure serve reports/allure-results

.DEFAULT_GOAL := help
