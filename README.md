# FA26-IS601851-Assignment10-Pydantic_Validation

## Overview

This project is a Python web application built with FastAPI, Pydantic, and SQLAlchemy. It provides a browser-based calculator backed by JSON API endpoints, plus a PostgreSQL-backed user model with Pydantic validation and password hashing.

The calculator supports addition, subtraction, multiplication, and division. The `/divide` endpoint returns a client error for division by zero. The user model enforces unique usernames and email addresses, stores password hashes rather than plain-text passwords, and includes registration and authentication helpers.

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── test.yml          # CI tests, security scan, and Docker Hub deployment
├── app/
│   ├── auth/                 # Authentication dependencies
│   ├── models/               # SQLAlchemy user model
│   ├── operations/           # Calculator operations
│   ├── schemas/              # Pydantic validation and response schemas
│   ├── config.py             # Application settings
│   ├── database.py           # SQLAlchemy engine and sessions
│   └── database_init.py      # Database table initialization
├── templates/
│   └── index.html            # Browser calculator interface
├── tests/
│   ├── unit/                 # Isolated model, schema, and calculator tests
│   ├── integration/          # API and PostgreSQL-backed tests
│   └── e2e/                  # Browser-driven UI tests
├── Dockerfile
├── docker-compose.yml
├── main.py                   # FastAPI application entry point
├── pytest.ini
└── requirements.txt
```

The main calculator API endpoints are `POST /add`, `POST /subtract`, `POST /multiply`, and `POST /divide`. `GET /` serves the calculator page, and `GET /health` is used for container health checks.

## Run tests locally

Use Python 3.10, start the PostgreSQL service, and install the project dependencies:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
docker compose up -d db
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db"
```

Run the test suites:

```bash
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/
```

Unit tests do not require PostgreSQL. Integration tests use the configured database, and end-to-end tests require Playwright's Chromium browser and port 8000 to be available.

## Docker Hub

The GitHub Actions workflow publishes the image to the [Docker Hub repository](https://hub.docker.com/r/anutale/fa26-is601851-assignment10-pydantic_validation) after successful tests and security checks on `main`.

```bash
docker pull anutale/fa26-is601851-assignment10-pydantic_validation:latest
```
