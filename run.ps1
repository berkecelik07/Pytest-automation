param(
    [Parameter(Position = 0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Test Automation Framework - Available Commands" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Setup:" -ForegroundColor Yellow
    Write-Host "  .\run.ps1 install              Install production dependencies"
    Write-Host "  .\run.ps1 install-dev         Install development dependencies"
    Write-Host "  .\run.ps1 clean               Remove build artifacts, cache, and reports"
    Write-Host ""
    Write-Host "Testing:" -ForegroundColor Yellow
    Write-Host "  .\run.ps1 test                Run all tests"
    Write-Host "  .\run.ps1 test-bdd            Run BDD tests with Gherkin terminal reporter"
    Write-Host "  .\run.ps1 test-smoke          Run smoke tests only"
    Write-Host "  .\run.ps1 test-regression     Run regression tests only"
    Write-Host "  .\run.ps1 test-headed         Run tests in headed mode (browser visible)"
    Write-Host "  .\run.ps1 test-parallel       Run tests in parallel"
    Write-Host ""
    Write-Host "Code Quality:" -ForegroundColor Yellow
    Write-Host "  .\run.ps1 format              Format code with black and ruff"
    Write-Host "  .\run.ps1 lint                Run linting checks"
    Write-Host "  .\run.ps1 pre-commit          Install pre-commit hooks"
    Write-Host ""
    Write-Host "Reporting:" -ForegroundColor Yellow
    Write-Host "  .\run.ps1 allure-report       Generate Allure report"
    Write-Host "  .\run.ps1 allure-serve        Generate and serve Allure report"
}

function Install-Dependencies {
    Write-Host "Installing production dependencies..." -ForegroundColor Green
    pip install -e .
}

function Install-DevDependencies {
    Write-Host "Installing development dependencies..." -ForegroundColor Green
    pip install -e ".[dev]"
    Write-Host "Installing Playwright browsers..." -ForegroundColor Green
    playwright install chromium firefox webkit
}

function Clean-Artifacts {
    Write-Host "Cleaning build artifacts, cache, and reports..." -ForegroundColor Green
    
    # Remove __pycache__ directories
    Get-ChildItem -Path . -Directory -Filter __pycache__ -Recurse | Remove-Item -Recurse -Force
    
    # Remove .pyc files
    Get-ChildItem -Path . -File -Filter "*.pyc" -Recurse | Remove-Item -Force
    
    # Remove build directories
    Remove-Item -Path "build", "dist", ".egg-info" -Recurse -Force -ErrorAction SilentlyContinue
    
    # Remove test cache
    Remove-Item -Path ".pytest_cache", ".coverage", "htmlcov" -Recurse -Force -ErrorAction SilentlyContinue
    
    # Remove reports
    Remove-Item -Path "reports", ".allure" -Recurse -Force -ErrorAction SilentlyContinue
    
    Write-Host "Clean complete!" -ForegroundColor Green
}

function Run-Tests {
    Write-Host "Running all tests..." -ForegroundColor Green
    pytest tests/ features/
}

function Run-BDD-Tests {
    Write-Host "Running BDD tests..." -ForegroundColor Green
    pytest --gherkin-terminal-reporter tests/ features/
}

function Run-Smoke-Tests {
    Write-Host "Running smoke tests..." -ForegroundColor Green
    pytest -m smoke tests/ features/
}

function Run-Regression-Tests {
    Write-Host "Running regression tests..." -ForegroundColor Green
    pytest -m regression tests/ features/
}

function Run-Headed-Tests {
    Write-Host "Running tests in headed mode..." -ForegroundColor Green
    $env:HEADLESS = "false"
    pytest tests/ features/
    Remove-Item env:HEADLESS
}

function Run-Parallel-Tests {
    Write-Host "Running tests in parallel..." -ForegroundColor Green
    pytest -n auto tests/ features/
}

function Format-Code {
    Write-Host "Formatting code..." -ForegroundColor Green
    black .
    ruff check . --fix
    Write-Host "Code formatted!" -ForegroundColor Green
}

function Run-Lint {
    Write-Host "Running linting checks..." -ForegroundColor Green
    ruff check .
    black --check .
}

function Install-PreCommit {
    Write-Host "Installing pre-commit hooks..." -ForegroundColor Green
    pre-commit install
    Write-Host "Pre-commit hooks installed!" -ForegroundColor Green
}

function Generate-Allure-Report {
    Write-Host "Generating Allure report..." -ForegroundColor Green
    allure generate reports/allure-results -o allure-report --clean
    Write-Host "Allure report generated in ./allure-report" -ForegroundColor Green
}

function Serve-Allure-Report {
    Write-Host "Serving Allure report..." -ForegroundColor Green
    allure serve reports/allure-results
}

# Execute command
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "install" { Install-Dependencies }
    "install-dev" { Install-DevDependencies }
    "clean" { Clean-Artifacts }
    "test" { Run-Tests }
    "test-bdd" { Run-BDD-Tests }
    "test-smoke" { Run-Smoke-Tests }
    "test-regression" { Run-Regression-Tests }
    "test-headed" { Run-Headed-Tests }
    "test-parallel" { Run-Parallel-Tests }
    "format" { Format-Code }
    "lint" { Run-Lint }
    "pre-commit" { Install-PreCommit }
    "allure-report" { Generate-Allure-Report }
    "allure-serve" { Serve-Allure-Report }
    default { Write-Host "Unknown command: $Command" -ForegroundColor Red; Write-Host "Run '.\run.ps1 help' for available commands."; exit 1 }
}
