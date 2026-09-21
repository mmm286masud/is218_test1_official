# Test 1

## Name
Masud Mohammad Amin

## Purpose
This project is a simple Python calculator that implements and tests addition and subtraction operations.

## Setup

Create the virtual environment:

    python -m venv .venv

Activate the virtual environment in PowerShell:

    .\.venv\Scripts\Activate.ps1

Install the requirements:

    python -m pip install -r requirements.txt

## Testing

Run the student tests:

    python -m pytest tests

Run the complete test suite:

    python -m pytest

Run the student tests and supplied acceptance cases:

    python -m pytest tests checks -v

## Test Assertion Explanation

One subtraction test uses `5` and `3` as inputs and expects the result to be `2`.

    assert subtract(5, 3) == 2

The assertion checks that the value returned by the `subtract` function is equal to the expected value of `2`. If it is not equal to `2`, the test fails.

## Virtual Environment

The `.venv` directory is ignored by Git because it contains locally installed Python packages and environment files. These files can be recreated using `requirements.txt`, so they should not be stored in the repository.

## Issues

- Issue 1: [Environment and project setup](PASTE-ISSUE-1-LINK-HERE)
- Issue 2: [Implement and test addition](PASTE-ISSUE-2-LINK-HERE)
- Issue 3: [Implement and test subtraction](PASTE-ISSUE-3-LINK-HERE)
- Issue 4: [Document, verify, and deliver](PASTE-ISSUE-4-LINK-HERE)