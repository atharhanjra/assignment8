# FastAPI Calculator

A web calculator built with FastAPI for Module 8. You enter two numbers in the browser and click Add, Subtract, Multiply, or Divide. The page sends the numbers to the FastAPI server, which calculates the result and sends it back.

## Features

- Add, subtract, multiply, and divide through a web page
- REST API endpoints for each operation
- Error message for dividing by zero or invalid input
- Logging of every calculation and error
- Unit, integration, and end-to-end tests
- GitHub Actions runs all tests on every push

## Setup

```
git clone https://github.com/atharhanjra/assignment8.git
cd assignment8
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m playwright install --with-deps chromium
```

The last line installs the browser used by the end-to-end tests.

## Running the App

```
python main.py
```

Then open http://127.0.0.1:8000 in your browser. Press Ctrl+C in the terminal to stop the app.

## API Endpoints

Each endpoint takes JSON like `{"a": 10, "b": 5}` and returns `{"result": ...}`.

| Endpoint | Method | What it does |
|---|---|---|
| `/` | GET | Shows the calculator page |
| `/add` | POST | Adds a and b |
| `/subtract` | POST | Subtracts b from a |
| `/multiply` | POST | Multiplies a and b |
| `/divide` | POST | Divides a by b (returns an error if b is 0) |

## Logging

Every operation is logged with Python's `logging` module. Successful calculations are logged at INFO level (for example, `Add: 2 + 3 = 5`), and errors like dividing by zero are logged at ERROR level. The log messages appear in the terminal while the app is running.

## Running the Tests

Run all tests:

```
pytest
```

Or run each type separately:

```
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/
```

- **Unit tests** check each function in `app/operations` and its logging.
- **Integration tests** send requests to each API endpoint in `main.py`.
- **End-to-end tests** use Playwright to open the page in a browser, type numbers, and click the buttons.

## GitHub Actions

The workflow in `.github/workflows/test.yml` runs on every push and pull request to `main`. It installs the dependencies and the Playwright browser, then runs the unit, integration, and end-to-end tests.