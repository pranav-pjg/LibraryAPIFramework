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