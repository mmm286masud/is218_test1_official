# IS 218 Test 1 Calculator

**Author:** Masud

This project is a small Python calculator assignment for implementing and testing integer addition and subtraction.

## Setup on Windows PowerShell

Create the local environment with Python 3.13. On Windows, use the Python launcher if it detects your 3.13 installation:

```powershell
py -3.13 -m venv .venv
```

The launcher did not detect Python 3.13 in this environment, so I used its installed executable directly. Another developer can substitute the path to their Python 3.13 installation.

```powershell
& 'C:\Users\polo1\AppData\Local\Programs\Python\Python313\python.exe' -m venv .venv
```

Install the pinned dependencies and select `.venv\Scripts\python.exe` as the editor's Python interpreter. The commands below call that interpreter directly, so PowerShell activation is not required.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m pytest tests checks -v
```

The first test command runs the student tests selected by `pytest.ini`. The second runs the student tests and supplied acceptance checks. In `test_add`, the inputs are `2` and `3`; its assertion checks that `add` returns the expected result, `5`.

The pinned `requirements.txt` is committed so another developer and CI can install the same dependencies. `.venv` stays local and ignored because it contains machine-specific executable paths and installed packages.

## Task issues

- [Issue 1: Setup](https://github.com/mmm286masud/is218_test1_official/issues/1)
- [Issue 2: Addition](https://github.com/mmm286masud/is218_test1_official/issues/2)
- [Issue 3: Subtraction](https://github.com/mmm286masud/is218_test1_official/issues/3)
- [Issue 4: Delivery](https://github.com/mmm286masud/is218_test1_official/issues/4)
