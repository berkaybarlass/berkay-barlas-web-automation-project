# Test Automation Suite

End-to-end test automation suite covering UI, API, and Load testing for [Insider](https://insiderone.com) and [Petstore API](https://petstore.swagger.io).

---

## Projects

| Project | Type | Tech Stack | Target |
|---------|------|------------|--------|
| `ui-test` | UI / E2E | Python · Selenium · Pytest | insiderone.com |
| `api-test` | API | Python · Requests · Pytest | Petstore Swagger API |
| `load-test` | Load | Python · Locust | n11.com search module |

---

## Project Structure

```
berkay-barlas-web-automation-project/
├── ui-test/
│   ├── config/           # Timeouts, highlight settings
│   ├── data/             # URLs, expected content constants
│   ├── flows/            # Cross-page flows (cookie banner)
│   ├── locators/         # Page locators
│   ├── pages/            # Page Object Model classes
│   ├── tests/            # Test files
│   ├── utils/            # Logger, DriverFactory
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── api-test/
│   ├── api/              # BaseAPI + PetAPI HTTP client
│   ├── config/           # Base URL, SLA thresholds (env var support)
│   ├── data/             # Test data constants, ID generator
│   ├── models/           # PetBuilder — test data factory
│   ├── schemas/          # JSON schema definitions
│   ├── tests/            # Test files
│   ├── utils/            # Logger
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
└── load-test/
    ├── config/           # Base URL, SLA thresholds (env var support)
    ├── data/             # Search queries, sort options
    ├── scenarios/        # Locust TaskSets
    ├── utils/            # Logger, response validator
    ├── locustfile.py
    ├── locust.conf
    └── requirements.txt
```

---

## UI Test

### Requirements
- Python 3.9+
- Google Chrome or Firefox
- ChromeDriver / GeckoDriver (managed by Selenium 4)

### Setup

```bash
cd ui-test
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run

```bash
# Default (Chrome, headed)
pytest

# Firefox
pytest --browser=firefox

# Headless
pytest --headless=true

# Specific test file
pytest tests/test_careers_page.py -v
```

### Test Coverage

| File | Description |
|------|-------------|
| `test_home_page.py` | Homepage smoke — URL, title, main blocks |
| `test_careers_page.py` | QA job filter, card validation, Lever redirect |

### Architecture

```
BasePage
├── HomePage
└── CareersPage

SiteFlow        → Cookie banner handling
DriverFactory   → Chrome / Firefox instantiation
```

---

## API Test

### Requirements
- Python 3.9+
- Internet access to `petstore.swagger.io`

### Setup

```bash
cd api-test
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
# All tests
pytest

# Specific suite
pytest tests/test_pet_create.py -v
pytest tests/test_pet_negative.py -v

# HTML report is auto-generated to reports/report.html
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PET_API_BASE_URL` | `https://petstore.swagger.io/v2` | Override for staging/pre-prod |

```bash
PET_API_BASE_URL=https://staging-petstore.example.com/v2 pytest
```

### Test Coverage

| File | Scope | Tests |
|------|-------|-------|
| `test_pet_create.py` | POST /pet | Full payload, minimal, status parametrize, schema, response time |
| `test_pet_read.py` | GET /pet/{id} | ID/name/status match, schema, response time |
| `test_pet_update.py` | PUT /pet | Name, status, category, tags, persistence, response time |
| `test_pet_delete.py` | DELETE /pet/{id} | Delete, verify 404, double-delete, response time |
| `test_pet_negative.py` | All endpoints | Invalid ID, missing fields, wrong method, invalid status |
| `test_pet_lifecycle.py` | End-to-end | Create → Read → Update → Persist Check → Delete → Verify 404 |

### Architecture

```
BaseAPI  (requests.Session, GET / POST / PUT / DELETE)
└── PetAPI

PetBuilder          → Test data factory (full / minimal / without_name / invalid)
PET_RESPONSE_SCHEMA → JSON schema contract validation
conftest.py         → pet_api (session scope) · created_pet (function scope + teardown)
```

---

## Load Test

### Requirements
- Python 3.9+
- Internet access to `n11.com`

### Setup

```bash
cd load-test
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
# Interactive UI — browser opens at http://localhost:8089
locust

# Headless — 1 user, 2-minute run, HTML report
locust --headless --users 1 --spawn-rate 1 --run-time 2m \
       --html reports/report.html

# Override target environment
LOAD_TEST_BASE_URL=https://staging.n11.com locust --headless ...
```

### Scenarios

| Code | Scenario | Type | Description |
|------|----------|------|-------------|
| SC-01 | Popular keyword search | Weighted | High-frequency real queries |
| SC-02 | Search + pagination | Weighted | `?pg=2/3/4` browse behavior |
| SC-03 | Search + sort | Weighted | `?srt=PRICE_LOW / PRICE_HIGH / ...` |
| SC-04 | Tech category search | Weighted | Electronics-focused queries |
| SC-05 | Edge case queries | Weighted | No results, single char, long query |
| SC-06 | Full user journey | Sequential | Homepage → Search → Paginate → Sort |

### User Types

| User | Weight | Behavior |
|------|--------|----------|
| `SearchUser` | 3 (75%) | Weighted random search tasks |
| `SearchJourneyUser` | 1 (25%) | Sequential homepage-to-sort journey |

### SLA Thresholds

| Metric | Default | Override via env |
|--------|---------|-----------------|
| P95 response time | 3000 ms | `P95_THRESHOLD_MS` |
| P99 response time | 5000 ms | `P99_THRESHOLD_MS` |
| Max error rate | 1.0 % | `MAX_ERROR_RATE_PCT` |

---

## Tech Stack

| Layer | Library | Version |
|-------|---------|---------|
| UI automation | Selenium | 4.x |
| API testing | Requests | 2.31.0 |
| Load testing | Locust | 2.24.0 |
| Test runner | Pytest | 7.4.3 |
| Reporting | pytest-html | 4.1.1 |
| Schema validation | jsonschema | 4.23.0 |
