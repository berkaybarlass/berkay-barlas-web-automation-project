from config.config import RESPONSE_TIME_P95_MS
from utils.logger import get_logger

logger = get_logger(__name__)


def validate_search_response(response, query: str = "") -> bool:
    if response.status_code != 200:
        response.failure(
            f"Expected 200, got {response.status_code} | query='{query}'"
        )
        logger.error(
            f"Search failed | status={response.status_code} | query='{query}'"
        )
        return False

    elapsed_ms = response.elapsed.total_seconds() * 1000

    if elapsed_ms > RESPONSE_TIME_P95_MS:
        logger.warning(
            f"Slow response | {elapsed_ms:.0f}ms > p95 threshold {RESPONSE_TIME_P95_MS}ms "
            f"| query='{query}'"
        )

    response.success()
    return True


def validate_homepage_response(response) -> bool:
    if response.status_code != 200:
        response.failure(f"Homepage returned {response.status_code}")
        logger.error(f"Homepage failed | status={response.status_code}")
        return False

    response.success()
    return True
