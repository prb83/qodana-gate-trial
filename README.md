# qodana-gate-trial

A small Python project for trying Qodana on pull requests.

The workflow `.github/workflows/quality.yml` runs the tests with coverage and then Qodana in pull-request mode.
It keeps the Qodana results and the coverage reports as artifacts of the run.

## Run the tests

```sh
python -m pip install -r requirements-dev.txt
python -m coverage run -m pytest
python -m coverage report
```

## The coverage report for Qodana

Qodana reads one coverage report from the directory `.qodana/code-coverage`.
Write it after the tests:

```sh
python -m coverage xml -o .qodana/code-coverage/coverage.xml
```
