# QA Automation Project

This project contains automated tests for both API and UI layers using Python, pytest, Playwright, and Allure reporting.

## Features
- API testing with `requests`
- UI testing with `playwright`
- Unified test execution via `pytest`
- Allure reporting integration
- Easy-to-run test suite

## Project Structure
project/
│
├── tests/
│   ├── api/
│   ├── ui/
│   └── conftest.py
│
├── requirements.txt
├── README.md
└── LICENSE

## Installation
Install all dependencies:
pip install -r requirements.txt

## Running Tests

### Run all tests:
pytest

### Run only API tests:
pytest tests/api

### Run only UI tests:
pytest test/ui

## Allure Report
Generate and open Allure report:

pytest --alluredir=allure-results
allure serve allure-results

## Technologies Used
- Python
- pytest
- Playwright
- requests
- Allure

## License
This project is licensed under the MIT License.
