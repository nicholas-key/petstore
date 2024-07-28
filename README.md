# Overview of this work
## Packages and tools required
1. `Python`
2. `pytest`
3. `requests` library
4. `pip`
5. `pytest-html`

## Setting up the python environment
1. Go to `petstore` directory (this work)
```
cd <the_path_this_repo_is_checked_out>/petstore
```
2. Create separate python development environment so that the global environment is not tainted
```
/usr/bin/python3 -m venv pytest-env
```
3. Initialize the test environment
```
source pytest-env/bin/activate
```
4. Install the python packages
```
pip install pytest
pip install requests
pip install pytest-html
```
5. Run `pytest` in the test suite in the `petstore` directory, eg
```
(pytest-env) petstore$ pytest -v -s -p no:warnings --html=report.html
```

## Thoughts and approaches in implementing this automated test suite
1. `Pytest` is chosen due to its simplicity and the ease of implementing test cases
2. Test cases were initially identified based on the scenarios for the `pet` endpoint
3. Test cases that exercise the same HTTP method are merged and simplified into a more universal test case with the usage of test parameters. For example, the scenarios of `find pets by status` and `find a single pet by ID` are identified to run with HTTP `GET` method.
4. The other scenarios are marked as `SKIPPED` and backlogged
5. HTML reporting is configured so that test failures can be intepreted more easily. Sample report is as below: 

<img width="1430" alt="Screenshot 2024-07-29 at 2 15 28 AM" src="https://github.com/user-attachments/assets/2d9de25b-d736-4c81-8cc1-49b50dcee110">

## To-do list
1. Integrate with CI (eg CircleCI)
2. Increase test coverage
