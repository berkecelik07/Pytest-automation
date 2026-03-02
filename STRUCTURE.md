# Repository Structure Guide

Complete documentation of the test automation framework repository structure.

## Directory Tree

```
.
├── .github/                             # GitHub configuration
│   └── workflows/
│       └── test.yml                    # GitHub Actions CI/CD pipeline
├── config/                              # Configuration module
│   ├── __init__.py
│   └── config.py                       # Environment configuration & settings
├── features/                            # BDD Feature files
│   ├── conftest.py                     # BDD-specific fixtures
│   └── login.feature                   # Example feature file (Gherkin syntax)
├── pages/                               # Page Object Models
│   ├── __init__.py
│   ├── base_page.py                    # Base class with common methods
│   └── login_page.py                   # Example login page object
├── steps/                               # BDD Step Definitions
│   ├── __init__.py
│   └── login_steps.py                  # Step implementations for login.feature
├── tests/                               # Pytest test files
│   ├── __init__.py
│   ├── conftest.py                     # Test-level fixtures
│   └── ui/                              # UI tests
│       ├── __init__.py
│       ├── conftest.py                 # UI-specific fixtures
│       └── test_login.py               # Example pytest-style test file
├── utils/                               # Utility functions
│   └── __init__.py                     # Helper utilities
├── reports/                             # Test reports (generated at runtime)
│   ├── allure-results/                 # Allure report data
│   ├── screenshots/                    # Failure screenshots
│   └── traces/                         # Playwright traces (optional)
├── .editorconfig                        # Editor configuration (IDE consistency)
├── .env                                 # Environment variables (local)
├── .env.example                         # Environment variables template
├── .github/                             # GitHub configuration
├── .gitignore                           # Git ignore rules
├── .pre-commit-config.yaml              # Pre-commit hooks configuration
├── conftest.py                          # Root pytest fixtures & hooks
├── CONTRIBUTING.md                      # Contributing guidelines
├── Makefile                             # Commands for macOS/Linux
├── pyproject.toml                       # Project metadata & dependencies (modern)
├── pytest.ini                           # Pytest configuration
├── QUICK_START.md                       # Quick start guide
├── README.md                            # Main documentation
├── requirements.txt                     # Dependencies (legacy format)
├── run.ps1                              # Commands for Windows PowerShell
├── setup.py                             # Setup script (editable install)
├── STRUCTURE.md                         # This file
└── tox.ini                              # Tox testing configuration
```

---

## File Descriptions

### Configuration Files

#### `.env` & `.env.example`
- **Purpose**: Environment-specific settings
- **Content**: 
  - Environment selection (dev, staging, prod)
  - Base URLs
  - Playwright settings (browser, headless, timeout)
  - Reporting options
- **Usage**: Copy `.env.example` to `.env` and customize for your environment

#### `pyproject.toml`
- **Purpose**: Modern Python project configuration (PEP 517/518)
- **Content**:
  - Project metadata (name, version, description)
  - Dependencies (production & dev)
  - Build system configuration
  - Tool configuration (black, ruff, pytest-bdd)
- **Usage**: `pip install -e .`

#### `setup.py`
- **Purpose**: Alternative setup script for editable installation
- **Content**: Same as pyproject.toml but in setuptools format
- **Usage**: `pip install -e .`

#### `requirements.txt`
- **Purpose**: Alternative dependency listing (legacy format)
- **Content**: Direct pip-compatible dependency list
- **Usage**: `pip install -r requirements.txt`

#### `pytest.ini`
- **Purpose**: Pytest configuration
- **Content**:
  - Test discovery patterns
  - Test markers (smoke, regression, ui)
  - Report generation options (Allure)
  - Output formatting

#### `tox.ini`
- **Purpose**: Tox testing automation configuration
- **Content**:
  - Test environments (Python versions, lint, format)
  - Test commands for different scenarios
  - Pytest configuration

#### `.editorconfig`
- **Purpose**: Editor configuration for IDE consistency
- **Content**: Indentation, line endings, charset settings
- **Supported by**: VS Code, PyCharm, Sublime, etc.

#### `.pre-commit-config.yaml`
- **Purpose**: Git pre-commit hooks configuration
- **Content**:
  - Code formatting (black)
  - Linting (ruff, flake8)
  - Common checks (trailing whitespace, YAML validity)
- **Usage**: `pre-commit install`

#### `.gitignore`
- **Purpose**: Git ignore rules
- **Content**:
  - Python cache (`__pycache__`, `.pyc`)
  - Virtual environments
  - Build artifacts
  - IDE files (`.vscode`, `.idea`)
  - Test reports and artifacts

---

### Source Code Files

#### `config/config.py` + `config/__init__.py`
- **Purpose**: Configuration management module
- **Classes**: `Settings` (Pydantic model for type-safe config)
- **Functions**: 
  - `get_settings()` - Get cached settings instance
  - `get_base_url()` - Get URL based on environment
- **Features**:
  - Reads from `.env` file automatically
  - Type validation with Pydantic
  - Environment-aware configuration

#### `pages/base_page.py`
- **Purpose**: Base page object with common methods
- **Class**: `BasePage`
- **Key Methods**:
  - `navigate_to(url)` - Navigate to URL
  - `find_element(selector)` - Find by CSS selector
  - `find_element_by_testid(testid)` - Find by data-testid
  - `click_element(selector)` - Click element
  - `fill_input(selector, text)` - Fill text input
  - `get_text(selector)` - Get element text
  - `is_visible(selector)` - Check visibility
  - `wait_for_element(selector)` - Wait for element
  - `take_screenshot(filename)` - Take screenshot
- **Usage**: Extend this class for page-specific objects

#### `pages/login_page.py`
- **Purpose**: Page object for login functionality
- **Class**: `LoginPage(BasePage)`
- **Selectors**: Username, password, button, messages
- **Methods**: Login actions and assertions
- **Example**: Demonstrates proper POM usage

#### `pages/__init__.py`
- **Purpose**: Package initialization
- **Content**: Exports for convenient importing

#### `features/login.feature`
- **Purpose**: BDD feature file (Gherkin syntax)
- **Content**:
  - Feature description
  - Scenarios with Given-When-Then steps
  - Markers (@smoke, @regression)
- **Executed by**: pytest-bdd plugin
- **Links to**: Step definitions in `steps/login_steps.py`

#### `steps/login_steps.py`
- **Purpose**: BDD step definitions
- **Implementation**: Given/When/Then functions
- **Markers**: pytest_bdd decorators (@given, @when, @then)
- **Parameters**: Parsed from feature file scenarios
- **Uses**: Page objects for interactions

#### `steps/__init__.py`
- **Purpose**: Package initialization for steps

#### `tests/ui/test_login.py`
- **Purpose**: Pytest-style UI tests (alternative to BDD)
- **Classes**: Test classes grouping related tests
- **Methods**: Individual test functions
- **Markers**: @pytest.mark decorators
- **Fixtures**: page fixture from conftest
- **Assertions**: Standard pytest assertions

#### `tests/__init__.py` & `tests/ui/__init__.py`
- **Purpose**: Package initialization

#### `utils/__init__.py`
- **Purpose**: Utility functions module
- **Functions**:
  - `create_directory(path)` - Create directory safely
  - `ensure_reports_directories()` - Create report dirs
  - `load_test_data(filename)` - Load JSON test data
- **Classes**: `WaitHelper` - Retry/wait utilities

---

### Test Configuration Files

#### `conftest.py` (root)
- **Purpose**: Pytest configuration and fixtures (session-scoped)
- **Key Fixtures**:
  - `browser` - Playwright browser instance
  - `context` - Browser context for page isolation
  - `page` - Playwright page instance
  - `browser_type` - Gets browser from config
  - `is_headless` - Gets headless setting
- **Hooks**:
  - `pytest_runtest_makereport()` - Screenshot on failure
  - `setup_allure_environment()` - Allure environment setup
- **Features**:
  - Automatic browser cleanup
  - Automatic screenshot capture on failures
  - Allure environment properties generation

#### `conftest.py` (tests/, features/)
- **Purpose**: Sub-package conftest files
- **Content**: Imports from root conftest for fixture availability

#### `tests/ui/conftest.py`
- **Purpose**: UI-specific fixtures and setup
- **Content**: Imports from root for fixture availability

#### `features/conftest.py`
- **Purpose**: BDD-specific fixtures and setup
- **Content**: Imports from root for fixture availability

---

### Documentation Files

#### `README.md`
- **Purpose**: Main project documentation
- **Sections**:
  - Features overview
  - Installation instructions (Windows, macOS, Linux)
  - Project structure explanation
  - Configuration guide
  - Running tests (various methods)
  - Page Object Model examples
  - Selector strategy guidelines
  - Adding new tests (BDD and Pytest)
  - Reporting (Allure) instructions
  - Code quality tools (Black, Ruff, pre-commit)
  - Parallel execution
  - GitHub Actions CI/CD
  - Troubleshooting guide
  - Contributing guidelines

#### `QUICK_START.md`
- **Purpose**: Fast setup and basic commands
- **Content**:
  - Prerequisites checklist
  - Step-by-step setup (5 minutes)
  - Common command examples
  - Troubleshooting quick tips
- **Audience**: New users/quick reference

#### `CONTRIBUTING.md`
- **Purpose**: Guidelines for contributors
- **Sections**:
  - Code of conduct
  - Setup instructions
  - Code quality standards
  - Adding new tests
  - Testing procedures
  - Commit guidelines
  - PR process
  - Page object guidelines
  - Documentation requirements

#### `STRUCTURE.md`
- **Purpose**: This file - explains repository organization

---

### Automation Script Files

#### `run.ps1` (Windows)
- **Purpose**: PowerShell command wrapper for testing tasks
- **Commands**:
  - `install` - Install dependencies
  - `install-dev` - Install with dev dependencies
  - `clean` - Clean build artifacts
  - `test` - Run all tests
  - `test-smoke` - Smoke tests only
  - `test-regression` - Regression tests only
  - `test-headed` - Run with visible browser
  - `test-parallel` - Parallel execution
  - `format` - Format code
  - `lint` - Check code quality
  - `allure-serve` - Serve Allure report
- **Usage**: `.\run.ps1 <command>`

#### `Makefile` (macOS/Linux)
- **Purpose**: Make command wrapper for testing tasks
- **Commands**: Same as run.ps1 (Unix flavor)
- **Usage**: `make <command>`

#### `.github/workflows/test.yml`
- **Purpose**: GitHub Actions CI/CD pipeline
- **Triggers**:
  - Push to main/develop
  - Pull requests to main/develop
  - Daily schedule (2 AM UTC)
- **Jobs**:
  - Checkout code
  - Setup Python 3.11
  - Install dependencies
  - Install Playwright browsers
  - Run tests (with xdist parallel)
  - Generate Allure report
  - Upload artifacts
  - Deploy to GitHub Pages (main branch)
- **Features**:
  - Pip caching
  - Automatic browser installation
  - Screenshot artifacts
  - Allure report hosting

---

## Dependency Structure

### Production Dependencies
```
pytest                  # Test framework
pytest-bdd             # BDD with Gherkin
pytest-xdist           # Parallel execution
playwright             # Browser automation
allure-pytest          # Reporting
python-dotenv          # Environment variables
pydantic               # Configuration validation
```

### Development Dependencies
```
black                  # Code formatter
ruff                   # Linter
pre-commit             # Git hooks
```

---

## Fixture Architecture

### Scope Hierarchy
```
session:
├── browser_type      # Browser selection (read from config)
└── is_headless       # Headless mode (read from config)

function:
├── browser           # Browser instance (session-managed)
├── context           # Browser context (per test)
└── page              # Page instance (per test - PRIMARY)
```

### Fixture Dependencies
```
page fixture:
  ↓
context (new per test)
  ↓
browser (session-wide)
  ↓
browser_type & is_headless (from config)
```

---

## Configuration Flow

```
.env file
  ↓
Pydantic Settings (config.py)
  ↓
get_settings() → cached Settings instance
  ↓
conftest.py fixtures use settings
  ↓
Page objects access settings
```

---

## Test Execution Flow

### BDD Tests
```
Feature file (.feature)
  ↓
pytest-bdd discovers scenarios
  ↓
Matches steps to step definitions
  ↓
Step functions create page objects
  ↓
Page objects use base page methods
  ↓
Base page uses page fixture
  ↓
Results → Allure report
```

### Pytest Tests
```
Test file (test_*.py)
  ↓
pytest discovers test classes/functions
  ↓
Injects fixtures (page, browser, etc.)
  ↓
Test code creates page objects
  ↓
Page objects interact with application
  ↓
Assertions check results
  ↓
On failure: screenshot captured automatically
  ↓
Results → Allure report
```

---

## Adding New Components

### To Add New Page Object
1. Create `pages/new_page.py`
2. Inherit from `BasePage`
3. Define selectors as class attributes
4. Add methods for page interactions
5. Export in `pages/__init__.py`

### To Add New BDD Feature
1. Create `features/new_feature.feature`
2. Write scenarios in Gherkin
3. Create `steps/new_steps.py` with step implementations
4. Run: `pytest features/new_feature.feature`

### To Add New Pytest Test
1. Create `tests/ui/test_new.py`
2. Create `TestClassName` class
3. Add `test_method_name` functions
4. Use page fixture
5. Run: `pytest tests/ui/test_new.py`

---

## Configuration Loading Priority

1. `.env` file (highest priority)
2. Environment variables (OS-level)
3. Default values in Settings class (lowest priority)

This allows:
- Local `.env` for local development
- Environment variables for CI/CD
- Defaults for basic functionality

---

## Report Generation

### During Test Execution
```
conftest.py pytest hook:
  ↓
allure_results directory
  (test data, screenshots, attachments)
```

### Report Generation
```
allure generate reports/allure-results
  ↓
allure-report/ directory (HTML)
```

### Report Serving
```
allure serve reports/allure-results
  ↓
Opens http://localhost:4040
```

---

## CI/CD Flow

```
GitHub Push/PR
  ↓
GitHub Actions triggered
  ↓
test.yml workflow
  ↓
Setup Python & dependencies
  ↓
Install Playwright browsers
  ↓
pytest -n auto   (parallel)
  ↓
Allure report generated
  ↓
Results uploaded as artifacts
  ↓
(On main) Deploy to GitHub Pages
```

---

## Quick Reference

| Need | File | How |
|------|------|-----|
| Add test | `tests/ui/test_*.py` | Class + test methods |
| Add feature | `features/*.feature` | Gherkin scenarios |
| Add steps | `steps/*_steps.py` | @given/@when/@then |
| Add page | `pages/*_page.py` | Inherit BasePage |
| Change config | `.env` | Edit variables |
| Change timeout | `.env` or conftest.py | TIMEOUT setting |
| Run tests | Terminal | `pytest tests/ features/` |
| View reports | Terminal | `allure serve reports/allure-results` |

---

This structure supports:
- ✅ Scalability (add tests as needed)
- ✅ Maintainability (clear organization)
- ✅ Reusability (page objects, fixtures)
- ✅ Documentation (inline + files)
- ✅ Automation (CI/CD integration)
- ✅ Quality (linting, formatting, testing)
