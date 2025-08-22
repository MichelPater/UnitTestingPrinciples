# Python Unit Testing Principles Project

This project demonstrates comprehensive testing concepts in Python using pytest. It's designed for developers new to testing who want to learn best practices.

## Project Structure

```
UnitTestingPrinciples/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── weather_service/
│   │   ├── __init__.py
│   │   └── weather_service.py
│   └── user_management/
│       ├── __init__.py
│       ├── user.py
│       └── user_repository.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_weather_service.py
│   └── test_user_management.py
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

### 2. Weather Service (Mocking & Exception Handling)
- **Purpose**: Shows how to test external dependencies and exceptions
- **Concepts**: Mocking, HTTP requests, exception testing
- **Location**: `src/weather_service/weather_service.py`

### 3. User Management (Advanced Testing Concepts)
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