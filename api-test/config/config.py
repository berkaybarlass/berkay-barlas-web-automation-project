import os

BASE_URL = os.getenv("PET_API_BASE_URL", "https://petstore.swagger.io/v2")

DEFAULT_TIMEOUT = 10  # seconds

RESPONSE_TIME_THRESHOLD = 2.0  # seconds
