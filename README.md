# qa-python-api-tests

API test automation project written in **Python** using **pytest** and **requests**.
Includes CI execution via **GitHub Actions** and basic HTML reporting.

## Tech stack
- Python 3.11
- pytest
- requests
- GitHub Actions (CI)

## Project structure
```text
qa-python-api-tests/
├── .github/workflows/tests.yml   # CI pipeline
├── tests/                        # API test cases
├── utils/                        # API client & helpers
├── pytest.ini                    # pytest configuration
├── requirements.txt              # dependencies
└── README.md