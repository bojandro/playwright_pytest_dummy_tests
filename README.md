## Installation Guide

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

(Optional) Install Allure (Arch)
```shell
yay -S allure-commandline
```

## Running the Tests
Simple test run
```shell
pytest
```

Run and generate Allure report
```shell
pytest --alluredir run_artifacts/allure_results
```

Serve test report
```shell
allure serve run_artifacts/allure_results
```

Report should be available at `http://127.0.0.1:40939`.
