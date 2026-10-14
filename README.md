# QA Automation Framework: UI & API

A scalable test automation framework demonstrating professional QA practices, including the Page Object Model (POM), CI/CD integration, and comprehensive reporting.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **UI Testing:** Playwright
* **API Testing:** Requests
* **Framework:** Pytest
* **CI/CD:** GitHub Actions
* **Reporting:** Pytest-HTML

## 🏗️ Architecture
This project utilizes the **Page Object Model (POM)** design pattern to separate test logic from UI locators, ensuring high maintainability and scalability.

## 🚀 Features
* **Automated UI Tests:** Verifies core user flows (login, error handling) on SauceDemo.
* **Automated API Tests:** Validates GET and POST endpoints, status codes, and JSON payloads via ReqRes API.
* **Continuous Integration:** GitHub Actions automatically triggers the test suite on every push.
* **Artifact Generation:** HTML test reports are automatically generated and saved upon pipeline completion.

## 💻 How to Run Locally

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install`
6. Run all tests: `pytest`
7. Run UI tests visually: `pytest test_login.py --headed --slowmo 500`
8. Generate HTML report: `pytest --html=report.html`