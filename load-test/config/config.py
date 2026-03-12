import os

BASE_URL = os.getenv("LOAD_TEST_BASE_URL", "https://www.n11.com")
SEARCH_ENDPOINT = "/arama"
RESPONSE_TIME_P95_MS = int(os.getenv("P95_THRESHOLD_MS", "3000"))
RESPONSE_TIME_P99_MS = int(os.getenv("P99_THRESHOLD_MS", "5000"))
MAX_ERROR_RATE_PCT = float(os.getenv("MAX_ERROR_RATE_PCT", "1.0"))
THINK_TIME_MIN = float(os.getenv("THINK_TIME_MIN", "1.0"))
THINK_TIME_MAX = float(os.getenv("THINK_TIME_MAX", "3.0"))
