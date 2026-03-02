# Quick Start Guide

Get up and running with the Test Automation Framework in minutes.

## Prerequisites

- Python 3.11+ installed
- Git installed
- 10 minutes of your time

## Setup (5 minutes)

### Windows (PowerShell)

```powershell
# 1. Navigate to project directory
cd path/to/Automation/Pytest

# 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Install Playwright browsers
playwright install chromium

# 5. Run example test to verify setup
.\run.ps1 test-smoke
```

### macOS/Linux (Bash/Zsh)

```bash
# 1. Navigate to project directory
cd path/to/Automation/Pytest

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Install Playwright browsers
playwright install chromium

# 5. Run example test to verify setup
make test-smoke
```

## First Test Run

After setup, run any of these commands:

### Windows
```powershell
.\run.ps1 test              # Run all tests
.\run.ps1 test-smoke        # Run smoke tests (quick)
.\run.ps1 test-headed       # See browser while running
```

### macOS/Linux
```bash
make test              # Run all tests
make test-smoke        # Run smoke tests (quick)
make test-headed       # See browser while running
```

## View Results

### Windows
```powershell
.\run.ps1 allure-serve  # Opens report in browser
```

### macOS/Linux
```bash
make allure-serve       # Opens report in browser
```

## Common Commands

### Running Tests

| Command | Windows | macOS/Linux |
|---------|---------|------------|
| All tests | `.\run.ps1 test` | `make test` |
| Smoke only | `.\run.ps1 test-smoke` | `make test-smoke` |
| Headed mode | `.\run.ps1 test-headed` | `make test-headed` |
| Parallel | `.\run.ps1 test-parallel` | `make test-parallel` |
| BDD style | `.\run.ps1 test-bdd` | `make test-bdd` |

### Code Quality

| Command | Windows | macOS/Linux |
|---------|---------|------------|
| Format code | `.\run.ps1 format` | `make format` |
| Lint check | `.\run.ps1 lint` | `make lint` |

## Using Direct Pytest Commands

If you prefer pytest directly (without wrapper scripts):

```bash
# Run all tests
pytest tests/ features/

# Run specific marker
pytest -m smoke tests/ features/

# Parallel execution
pytest -n auto tests/ features/

# Show browser (headed mode)
HEADLESS=false pytest tests/ features/

# Verbose output
pytest -v tests/ features/

# Specific environment
ENVIRONMENT=staging pytest tests/ features/
```

## Project Layout

```
. 
├── pages/              # Page Object Models
├── features/           # BDD feature files (.feature)
├── steps/              # BDD step definitions
├── tests/ui/           # Pytest test files
├── config/             # Configuration management
├── reports/            # Test results (generated)
└── conftest.py         # Pytest fixtures
```

## Key Locations

- **Page Objects**: `pages/base_page.py`, `pages/login_page.py`
- **Example Test BDD**: `features/login.feature`, `steps/login_steps.py`
- **Example Test Pytest**: `tests/ui/test_login.py`
- **Configuration**: `.env` file (copy from `.env.example`)
- **Fixtures**: `conftest.py`

## Configuration

Edit `.env` to change settings:

```bash
ENVIRONMENT=dev              # dev, staging, or prod
HEADLESS=true               # false to see browser
BROWSER=chromium            # chromium, firefox, or webkit
TIMEOUT=30000               # Wait timeout in milliseconds
SCREENSHOT_ON_FAILURE=true  # Auto screenshot on failure
```

## Troubleshooting

### "playwright: command not found"
```bash
# Install Playwright
pip install playwright

# Install browsers
playwright install chromium
```

### Tests won't run
```bash
# Verify pytest installed
pytest --version

# Check Python version (needs 3.11+)
python --version

# Try with explicit module
python -m pytest tests/
```

### Can't view Allure report
```bash
# Install allure command-line tool
# macOS: brew install allure
# Windows: Download from https://github.com/allure-framework/allure2/releases

# Generate report
allure generate reports/allure-results -o allure-report --clean

# View in browser
allure open allure-report
```

## Next Steps

1. ✅ Complete setup above
2. 📖 Read full [README.md](README.md) for detailed documentation
3. ✍️  Add your first test following [Adding New Tests](README.md#adding-new-tests)
4. 🔧 Configure your application URL in `.env`
5. 🚀 Run tests against your application

## Tips

- Run `.\run.ps1 help` (Windows) or `make help` (macOS/Linux) for all commands
- Use `pytest --tb=short` for cleaner error output
- Use `pytest -k "keyword"` to run tests matching a pattern
- Use `pytest --pdb` to drop to debugger on failure
- Enable `HEADLESS=false` to watch tests run in real-time

## Still Stuck?

1. Check [README.md Troubleshooting](README.md#troubleshooting) section
2. Review test logs in `reports/` folder
3. Try running a simple test: `pytest tests/ui/test_login.py::TestLogin::test_successful_login_with_valid_credentials`

---

**Happy Testing! 🎉**
