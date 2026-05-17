# Library API Automation Framework

This is an enterprise-style REST API automation framework built using Python, Behave BDD, Requests, and Allure Reporting.

The framework validates Library API operations such as:

- Add Book
- Get Book by ID
- Get Book by Author
- Delete Book
- Negative API behavior
- JSON schema validation

---

## Tech Stack

| Area | Tool |
|---|---|
| Programming Language | Python |
| BDD Framework | Behave |
| API Client | Requests |
| Reporting | Allure |
| Schema Validation | jsonschema |
| Environment | Ubuntu / WSL |
| IDE | VS Code / PyCharm |
| Execution | Shell Scripts |
| CI/CD Ready | Jenkins |

---

## Project Structure

```text
LibraryAPIFramework/
│
├── config/
│   └── environments/
│       ├── qa.ini
│       ├── stage.ini
│       └── prod.ini
│
├── features/
│   ├── add_book/
│   ├── get_book/
│   ├── delete_book/
│   ├── negative/
│   ├── regression/
│   ├── steps/
│   └── environment.py
│
├── payloads/
├── resources/
├── schemas/
├── scripts/
├── testdata/
├── utilities/
├── reports/
├── logs/
├── regression/
├── requirements.txt
├── behave.ini
├── pytest.ini
├── README.md
└── Jenkinsfile

---

## Git Workflow

This project follows a feature branch based Git workflow.

Recommended process:

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name



---

## Step 23.4 — Check Changes

Run:

```bash id="d4bsbq"
git status
---

## Makefile Commands

Install dependencies:

```bash
make install

---

## Framework Completion Summary

This framework is designed as an enterprise-style API automation framework using Python Behave BDD.

### Completed Capabilities

- BDD-based test automation using Behave
- REST API automation using Requests
- Add Book, Get Book, and Delete Book API coverage
- Smoke, regression, functional, and negative test suites
- JSON schema validation
- Environment-specific execution using `-D env=qa`
- Externalized test data using JSON files
- Centralized API resources and payloads
- Centralized utilities for API calls, logging, assertions, config, and test data
- Allure reporting with request and response attachments
- Local report hosting for WSL using Python HTTP server
- Shell scripts for execution
- Makefile shortcuts
- Code quality checks using Black and Flake8
- GitHub repository with feature branch workflow
- Jenkinsfile prepared for future CI/CD integration

### Recommended Daily Commands

Activate environment:

```bash
source .venv/bin/activate
