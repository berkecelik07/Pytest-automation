# Setup & Execution Guide

Complete guide to setting up and running the test automation framework locally and in CI/CD.

---

## Complete Setup Instructions

### Windows (PowerShell)

#### Step 1: Prerequisites
```powershell
# Verify Python 3.11+ is installed
python --version

# Verify pip is available
pip --version

# Verify git is available
git --version
```

#### Step 2: Clone Repository
```powershell
git clone <repository-url>
cd path/to/Automation/Pytest
```

#### Step 3: Create Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Verify virtual environment is active (should see (venv) in prompt)
```

#### Step 4: Install Dependencies
```powershell
# Upgrade pip first
pip install --upgrade pip

# Install project with dev dependencies
pip install -e ".[dev]"
```

#### Step 5: Install Playwright Browsers
```powershell
# Install all browsers
playwright install chromium firefox webkit

# Or just chromium (minimum)
playwright install chromium
```

#### Step 6: Verify Installation
```powershell
# Check pytest
pytest --version

# Check playwright
playwright --version

# Try importing key packages
python -c "import pytest; import playwright; import allure"
```

#### Step 7: Configure Environment (Optional)
```powershell
# Copy example to create local config
Copy-Item .env.example .env

# Edit .env with your settings (optional)
notepad .env
```

---

### macOS/Linux (Bash/Zsh)

#### Step 1: Prerequisites
```bash
# Verify Python 3.11+ is installed
python3 --version

# Verify pip is available
pip3 --version

# Verify git is available
git --version
```

#### Step 2: Clone Repository
```bash
git clone <repository-url>
cd path/to/Automation/Pytest
```

#### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

# Verify virtual environment is active (should see (venv) in prompt)
```

#### Step 4: Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install project with dev dependencies
pip install -e ".[dev]"
```

#### Step 5: Install Playwright Browsers
```bash
# Install all browsers
playwright install chromium firefox webkit

# Or just chromium (minimum)
playwright install chromium
```

#### Step 6: Verify Installation
```bash
# Check pytest
pytest --version

# Check playwright
playwright --version

# Try importing key packages
python -c "import pytest; import playwright; import allure"
```

#### Step 7: Configure Environment (Optional)
```bash
# Copy example to create local config (already exists)
cp .env.example .env

# Edit .env with your settings (optional)
nano .env
```

---

## Running Tests Locally

### Windows - Using PowerShell Script

```powershell
# View all available commands
.\run.ps1 help

# Run tests with full output
.\run.ps1 test

# Run only smoke tests (quick validation)
.\run.ps1 test-smoke

# Run regression tests (comprehensive)
.\run.ps1 test-regression

# Run with visible browser (headed mode)
.\run.ps1 test-headed

# Run in parallel (faster)
.\run.ps1 test-parallel

# Run BDD tests with Gherkin terminal reporter
.\run.ps1 test-bdd

# Format code
.\run.ps1 format

# Check code quality
.\run.ps1 lint

# View Allure report (opens in browser)
.\run.ps1 allure-serve
```

### macOS/Linux - Using Makefile

```bash
# View all available commands
make help

# Run tests with full output
make test

# Run only smoke tests (quick validation)
make test-smoke

# Run regression tests (comprehensive)
make test-regression

# Run with visible browser (headed mode)
make test-headed

# Run in parallel (faster)
make test-parallel

# Run BDD tests with Gherkin terminal reporter
make test-bdd

# Format code
make format

# Check code quality
make lint

# View Allure report (opens in browser)
make allure-serve
```

### Direct Pytest Commands (Cross-platform)

```bash
# Run all tests
pytest tests/ features/

# Run with verbose output
pytest -v tests/ features/

# Run specific test file
pytest tests/ui/test_login.py

# Run specific test class
pytest tests/ui/test_login.py::TestLogin

# Run specific test method
pytest tests/ui/test_login.py::TestLogin::test_successful_login_with_valid_credentials

# Run tests matching pattern
pytest -k "login" tests/ features/

# Run with specific marker
pytest -m smoke tests/ features/

# Run in parallel (8 workers)
pytest -n 8 tests/ features/

# Run with detailed output on failure
pytest -vv --tb=long tests/ features/

# Run and stop on first failure
pytest -x tests/ features/

# Run with detailed coverage report
pytest --cov=pages --cov=steps tests/ features/

# Show local variables on failure
pytest -l tests/ features/

# Drop to debugger on failure
pytest --pdb tests/ features/

# Show print statements during test
pytest -s tests/ features/

# Run specific environment
ENVIRONMENT=staging pytest tests/ features/

# Run in headed mode (see browser)
HEADLESS=false pytest tests/ features/

# Use different browser
BROWSER=firefox pytest tests/ features/
```

---

## Parallel Execution

### Windows
```powershell
# Use all available CPUs
.\run.ps1 test-parallel

# Or directly with pytest
pytest -n auto tests/ features/
```

### macOS/Linux
```bash
# Use all available CPUs
make test-parallel

# Or directly with pytest
pytest -n auto tests/ features/
```

### Pytest Direct (Cross-platform)
```bash
# Auto-detect number of workers
pytest -n auto tests/ features/

# Use specific number of workers
pytest -n 4 tests/ features/

# Distribute by test module scope
pytest -n auto --dist loadscope tests/ features/

# Distribute by test file
pytest -n auto --dist loadfile tests/ features/
```

---

## Reporting

### Generate Allure Report

#### Windows
```powershell
.\run.ps1 allure-report  # Generate only
.\run.ps1 allure-serve   # Generate and serve
```

#### macOS/Linux
```bash
make allure-report       # Generate only
make allure-serve        # Generate and serve
```

#### Direct Commands (Cross-platform)
```bash
# Generate report
allure generate reports/allure-results -o allure-report --clean

# Serve report (opens http://localhost:4040)
allure serve reports/allure-results

# Open existing report
allure open allure-report
```

### Report Location
- **Results Data**: `reports/allure-results/`
- **Generated HTML**: `allure-report/`
- **Screenshots**: `reports/screenshots/`
- **Environment Info**: `reports/allure-results/environment.properties`

---

## Code Quality

### Windows
```powershell
# Format code (black + ruff)
.\run.ps1 format

# Check code quality
.\run.ps1 lint

# Install pre-commit hooks
.\run.ps1 pre-commit
```

### macOS/Linux
```bash
# Format code (black + ruff)
make format

# Check code quality
make lint

# Install pre-commit hooks
make pre-commit
```

### Direct Commands (Cross-platform)
```bash
# Format with black
black .

# Fix with ruff
ruff check . --fix

# Check with ruff
ruff check .

# Check with black (no changes)
black --check .

# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files

# Update pre-commit tools
pre-commit autoupdate
```

---

## Configuration

### Using .env File

Copy template and customize:
```bash
cp .env.example .env
```

Edit `.env`:
```bash
# Environment selection
ENVIRONMENT=dev              # dev, staging, or prod

# Application URLs
BASE_URL_DEV=https://the-internet.herokuapp.com
BASE_URL_STAGING=https://staging.example.com
BASE_URL_PROD=https://example.com

# Playwright Browser Configuration
HEADLESS=true                # false to see browser
BROWSER=chromium             # chromium, firefox, webkit
TIMEOUT=30000                # milliseconds

# Reporting
SCREENSHOT_ON_FAILURE=true   # Auto-capture on failure
TRACE_ON_FAILURE=false       # Advanced: capture Playwright trace
```

### Environment Variables (Override .env)

```bash
# Windows PowerShell
$env:ENVIRONMENT="staging"
$env:HEADLESS="false"
$env:BROWSER="firefox"

# macOS/Linux Bash
export ENVIRONMENT="staging"
export HEADLESS="false"
export BROWSER="firefox"

# Then run
pytest tests/ features/
```

---

## Continuous Integration (GitHub Actions)

### Workflow Location
`.github/workflows/test.yml`

### Workflow Triggers
- **Push**: To `main` or `develop` branches
- **Pull Request**: Against `main` or `develop`
- **Schedule**: Daily at 2 AM UTC

### What It Does
1. Checks out code
2. Sets up Python 3.11
3. Caches pip dependencies
4. Installs project with dependencies
5. Installs Playwright browsers
6. Runs tests in parallel (`-n auto`)
7. Generates Allure report
8. Uploads results as artifacts
9. Deploys to GitHub Pages (main branch only)

### Viewing CI Results

1. Go to "Actions" tab in GitHub
2. Select workflow run
3. View test results in "Run tests" step
4. Download artifacts from "test-results"
5. View Allure report in GitHub Pages (after deployment)

### CI/CD Environment Variables

Set in GitHub: Settings → Secrets and variables → Actions

```
ENVIRONMENT=dev
HEADLESS=true
BROWSER=chromium
```

---

## Common Workflows

### First Time Developer Setup

```powershell
# Windows PowerShell
git clone <repo>
cd Automation/Pytest
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e ".[dev]"
playwright install chromium
.\run.ps1 test-smoke          # Quick validation
.\run.ps1 allure-serve        # View results
```

```bash
# macOS/Linux Bash
git clone <repo>
cd Automation/Pytest
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
make test-smoke               # Quick validation
make allure-serve             # View results
```

### Before Committing

```powershell
# Windows PowerShell
.\run.ps1 format        # Format code
.\run.ps1 lint          # Check quality
.\run.ps1 test          # Run all tests
git add .
git commit -m "message"
```

```bash
# macOS/Linux Bash
make format             # Format code
make lint               # Check quality
make test               # Run all tests
git add .
git commit -m "message"
```

### Running Specific Test Types

```bash
# Smoke tests only (quick)
pytest -m smoke tests/ features/

# Regression tests only (comprehensive)
pytest -m regression tests/ features/

# UI tests only
pytest -m ui tests/ features/

# Tests matching keyword
pytest -k "login" tests/ features/
```

### Debugging Test Failure

```bash
# Run with max verbosity
pytest -vv --tb=long tests/ui/test_login.py

# Show print statements
pytest -s tests/ui/test_login.py

# Drop to debugger on failure
pytest --pdb tests/ui/test_login.py

# Show local variables
pytest -l tests/ui/test_login.py

# Keep browser open on failure (headed mode)
HEADLESS=false pytest --pdb tests/ui/test_login.py
```

### Testing Different Environments

```bash
# Dev environment (default)
ENVIRONMENT=dev pytest tests/ features/

# Staging environment
ENVIRONMENT=staging pytest tests/ features/

# Production environment
ENVIRONMENT=prod pytest tests/ features/
```

### Testing Different Browsers

```bash
# Chromium (default)
BROWSER=chromium pytest tests/ features/

# Firefox
BROWSER=firefox pytest tests/ features/

# WebKit
BROWSER=webkit pytest tests/ features/
```

---

## Troubleshooting Commands

### Verify Python Setup
```bash
# Check Python version
python --version              # Should be 3.11+

# Check virtual environment is active
# Windows: prompt should show (venv)
# macOS/Linux: prompt should show (venv)

# Check Python path
python -c "import sys; print(sys.executable)"

# Check installed packages
pip list
```

### Verify Playwright Setup
```bash
# Check Playwright installation
python -c "import playwright; print(playwright.__version__)"

# List installed browsers
playwright install --list

# Re-install browsers
playwright install chromium firefox webkit
```

### Verify pytest Setup
```bash
# Check pytest version
pytest --version

# Check pytest can find tests
pytest --collect-only tests/ features/

# Check plugins
pytest --version -v
```

### Verify Allure Setup
```bash
# Check Allure command-line tool
allure --version

# Check allure-pytest plugin
python -c "import allure; print(allure.__version__)"
```

### Check Configuration
```bash
# Verify .env file exists and is readable
cat .env            # macOS/Linux
type .env           # Windows

# Check environment variables are set
# Windows: echo %ENVIRONMENT%
# macOS/Linux: echo $ENVIRONMENT
```

### View Test Results
```bash
# Check if reports directory exists
ls reports/allure-results/       # macOS/Linux
dir reports\allure-results\      # Windows

# Check screenshots
ls reports/screenshots/          # macOS/Linux
dir reports\screenshots\         # Windows
```

---

## Performance Tips

### Run Tests Faster

1. **Use Parallel Execution**
   ```bash
   pytest -n auto tests/ features/
   ```

2. **Run Only Smoke Tests During Development**
   ```bash
   pytest -m smoke tests/ features/
   ```

3. **Stop on First Failure**
   ```bash
   pytest -x tests/ features/
   ```

4. **Use Specific Browser (Firefox is faster than Chromium)**
   ```bash
   BROWSER=firefox pytest tests/ features/
   ```

5. **Increase Timeout in Headless Mode**
   - Headless mode can be slower on some systems

### Reduce Memory Usage

1. **Limit parallel workers to available cores**
   ```bash
   pytest -n 2 tests/ features/  # Use 2 workers instead of auto
   ```

2. **Run serially (no parallelism)**
   ```bash
   pytest tests/ features/
   ```

### Speed Up CI/CD

1. **Cache dependencies** (GitHub Actions) - Already configured
2. **Use minimal test set first** - Run smoke tests only
3. **Parallelize** - Already configured in workflows

---

## Advanced Usage

### Custom Pytest INI Options

Edit `pytest.ini` to customize:

```ini
[pytest]
addopts = -v --strict-markers --tb=short --alluredir=reports/allure-results
markers =
    smoke: Smoke test
    regression: Regression test
    ui: UI test
```

### Using Tox for Multiple Environments

```bash
# Run tests in all configured environments
tox

# Run specific environment
tox -e py311

# Run linting environment
tox -e lint

# Run formatting environment
tox -e format
```

### Using Docker (Optional)

If Docker is available, you can run tests in isolated environment:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -e ".[dev]"
RUN playwright install chromium

CMD ["pytest", "tests/", "features/"]
```

---

## Support & Help

### Getting Help

1. **Check Documentation**
   - [README.md](README.md) - Main documentation
   - [QUICK_START.md](QUICK_START.md) - Quick setup
   - [STRUCTURE.md](STRUCTURE.md) - Repository structure
   - [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines

2. **Check Logs**
   - Test output in terminal
   - Screenshots in `reports/screenshots/`
   - Allure report in `reports/allure-results/`

3. **Debug Test**
   ```bash
   pytest -vv -s --tb=long tests/ui/test_login.py
   ```

4. **Check Test Examples**
   - `tests/ui/test_login.py` - Pytest style
   - `features/login.feature` - BDD style
   - `steps/login_steps.py` - Step implementations

---

## Quick Command Reference

| Task | Windows | macOS/Linux | Direct |
|------|---------|------------|--------|
| **Setup** | `pip install -e ".[dev]"` | `pip install -e ".[dev]"` | `pip install -e ".[dev]"` |
| **Browsers** | `playwright install chromium` | `playwright install chromium` | `playwright install chromium` |
| **Run All** | `.\run.ps1 test` | `make test` | `pytest tests/ features/` |
| **Run Smoke** | `.\run.ps1 test-smoke` | `make test-smoke` | `pytest -m smoke tests/ features/` |
| **Run Headed** | `.\run.ps1 test-headed` | `make test-headed` | `HEADLESS=false pytest tests/ features/` |
| **Run Parallel** | `.\run.ps1 test-parallel` | `make test-parallel` | `pytest -n auto tests/ features/` |
| **Format** | `.\run.ps1 format` | `make format` | `black . && ruff check . --fix` |
| **Lint** | `.\run.ps1 lint` | `make lint` | `ruff check . && black --check .` |
| **Report** | `.\run.ps1 allure-serve` | `make allure-serve` | `allure serve reports/allure-results` |

---

**You're ready to go! Start with the Quick Start commands above.** 🚀
