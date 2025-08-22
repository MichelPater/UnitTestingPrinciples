# Python Unit Testing Principles Project

This project demonstrates comprehensive testing concepts in Python using pytest. It's designed for developers new to testing who want to learn best practices.

# This project will be added to over time
For now only the example code for the Calculator is added, no tests or other example code.

## Project Structure

```
UnitTestingPrinciples/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── calculator.py
|   |   └── calculator_with_history.py
│   ├── weather_service/
│   │   ├── __init__.py
│   │   └── weather_service.py
│   └── user_management/
│       ├── __init__.py
│       ├── user.py
│       └── user_repository.py
├── tests/
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── test_calculator.py
|   |   └── test_calculator_with_history.py
│   ├── weather_service/
│   │   ├── __init__.py
│   │   └── test_weather_service.py
│   └── user_management/
│       ├── __init__.py
│       ├── test_user.py
│       └── test_user_repository.py
└── conftest.py
```

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run tests with verbose output
pytest -v
```

## Test Cases Overview

### 1. Calculator (Basic Unit Testing)
- **Purpose**: Demonstrates basic unit testing principles
- **Concepts**: AAA pattern, edge cases, code coverage pitfalls
- **Location**: `src/calculator/calculator.py`

### 2. Calculator with History (Introduction with mocking)
- **Purpose**: Using the learned basic unit test principles and applying them
- **Concepts**: Mocking, AAA pattern, edge cases, code coverage pitfalls
- **Location**: `src/calculator/calculator_with_history.py`

### 3. Weather Service (Mocking & Exception Handling)
- **Purpose**: Shows how to test external dependencies and exceptions
- **Concepts**: Mocking, HTTP requests, exception testing
- **Location**: `src/weather_service/weather_service.py`

### 4. User Management (Advanced Testing Concepts)
- **Purpose**: Demonstrates fixtures, parametrized tests, and test organization
- **Concepts**: Fixtures, parametrization, test classes, database mocking
- **Location**: `src/user_management/`

## Key Testing Concepts Demonstrated

1. **AAA Pattern** (Arrange, Act, Assert)
2. **Test Fixtures** and setup/teardown
3. **Mocking external dependencies**
4. **Exception testing**
5. **Parametrized tests**
6. **Code coverage vs. test quality**
7. **Test organization and structure**