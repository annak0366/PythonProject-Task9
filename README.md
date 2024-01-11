## Description

This repository contains automated tests created for the https://automationexercise.com website. 
These tests are implemented using Playwright and the pytest testing frameworks. 
Additionally, the project integrates Allure reports, with the results showcased on GitHub Pages.

## Requirements
Before running or contributing to this project, ensure that you have the necessary dependencies installed.

- Download Python from [python.org](https://www.python.org/downloads/).

## Steps to install
Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/your-repo.git
```

### 2. Install dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Upgrade pip (Optional but Recommended)

Upgrade `pip` to the latest version using the following command:

```bash
python -m pip install --upgrade pip
```

## Run tests:
To run all set of tests, use:
```bash
pytest
```

To run one particular test:
```bash
pytest -k <name of the test>
```

## Steps to generate report
1. Run the command:
```bash
  pytest --alluredir=./reports
```

2. To see generated reports - run the command:
```bash
    allure serve ./reports
``` 