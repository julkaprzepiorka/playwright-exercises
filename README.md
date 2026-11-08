# Playwright Exercises

Automated UI tests for the AGH Faculty of Computer Science website using Playwright and pytest.

## Tests

- Opening the homepage
- Navigating to the "O Wydziale" page
- Navigating to the study programmes page
- Verifying URL changes after navigation

## Installation

```bash
pip install pytest-playwright
playwright install
```

## Running tests

Chromium:
```bash
pytest -v --browser chromium test_playwright.py
```

Firefox:
```bash
pytest -v --browser firefox test_playwright.py
```

Headed mode:
```bash
pytest -v --browser chromium --headed test_playwright.py
```

All four tests passed in Chromium and Firefox.