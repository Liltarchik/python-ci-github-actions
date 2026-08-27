# Python CI Pipeline with GitHub Actions ⚙️

![Python CI]

A showcase repository demonstrating automated continuous integration (CI) workflows for Python applications using GitHub Actions and pytest.

## 🚀 Key Features

* **Automated CI Workflow:** Triggers tests automatically on every `push` and `pull_request` to the `main` branch.
* **Environment Provisioning:** Configures an isolated `ubuntu-latest` runner with Python 3.11 (`actions/setup-python@v5`).
* **Test Automation:** Validates core arithmetic operations and edge cases via `pytest`.

## 📁 Repository Structure

```text
├── .github/workflows/
│   └── tests.yml         # GitHub Actions workflow configuration
├── ARIT/
│   ├── arit.py           # Core business logic / arithmetic functions
│   └── test_arit.py      # Unit test suites
└── README.md
