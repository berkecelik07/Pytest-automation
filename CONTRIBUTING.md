# Contributing to Test Automation Framework

Thank you for contributing to our test automation framework! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and professional
- Write clear, descriptive commit messages
- Keep changes focused and atomic
- Test your changes locally before submitting

## Getting Started

1. Clone the repository
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Follow code quality standards (see below)
5. Write/update tests for your changes
6. Submit a pull request with a clear description

## Code Quality Standards

### Formatting

All code must be formatted with Black:

```bash
black .
```

### Linting

Code must pass Ruff linting:

```bash
ruff check .
```

### Pre-commit Hooks

Install and use pre-commit hooks to automatically check code before commit:

```bash
pre-commit install
git commit -m "Your message"
```

## Adding New Tests

### BDD Tests (Preferred for Feature Testing)

1. Create feature file in `features/`:
   ```gherkin
   Feature: Feature name
     Description here

     @smoke
     Scenario: Scenario description
       Given precondition
       When action
       Then expected result
   ```

2. Create step definitions in `steps/`:
   ```python
   from pytest_bdd import given, when, then
   
   @given("precondition")
   def step_precondition(page):
       pass
   ```

3. Create/update page object in `pages/`:
   ```python
   from pages.base_page import BasePage
   
   class MyPage(BasePage):
       SELECTOR = "selector"
   ```

### Pytest Tests (Alternative for Unit/Integration Tests)

Create test file in `tests/` following naming convention `test_*.py`:

```python
import pytest
from pages.my_page import MyPage

class TestMyFeature:
    @pytest.mark.smoke
    def test_something(self, page):
        page_obj = MyPage(page)
        # assertions
```

## Testing Your Changes

### Run All Tests
```bash
pytest tests/ features/
```

### Run Specific Tests
```bash
pytest -m smoke tests/ features/           # Smoke tests only
pytest tests/ui/test_login.py             # Specific file
pytest -k "test_login" tests/              # Tests matching pattern
```

### Run with Code Coverage
```bash
pytest --cov=pages --cov=steps tests/ features/
```

## Commit Guidelines

- Write clear, concise commit messages
- Use imperative mood: "Add feature" not "Added feature"
- Reference issues when applicable: "Fixes #123"

## Pull Request Process

1. Ensure all tests pass locally
2. Pull the latest from main branch
3. Run code quality checks: `make lint && make format`
4. Create meaningful PR title and description
5. Reference related issues
6. Request review from team members
7. Address review feedback
8. Ensure CI/CD pipeline passes

## Page Object Guidelines

### Naming
- One page per file: `login_page.py`
- Class name: `LoginPage`
- Selector constants: `UPPERCASE_WITH_UNDERSCORES`

### Selectors
1. Prefer `data-testid`: most stable
2. Avoid complex XPath: brittle and slow
3. Use meaningful names: `LOGIN_BUTTON` not `BTN_1`

### Methods
- Public methods for user actions
- Snake_case naming
- Type hints for parameters and return values
- Docstrings for public methods

## Selector Strategy

Recommend adding `data-testid` to HTML elements:

```html
<button data-testid="login-button">Login</button>
<input data-testid="username-field" name="username" />
```

Then use in page objects:
```python
LOGIN_BUTTON = "[data-testid='login-button']"
USERNAME_FIELD = "[data-testid='username-field']"
```

## Documentation

- Update README.md for major features
- Add comments for complex logic
- Keep docstrings up to date
- Document new environment variables

## Reporting Issues

When reporting issues, include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots/logs if applicable
- Environment details (OS, Python version, browser)

## Questions?

- Check existing documentation
- Review similar code examples
- Open an issue for discussion
- Contact QA team

---

Thank you for contributing! 🎉
