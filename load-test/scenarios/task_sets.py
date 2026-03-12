import random

from locust import SequentialTaskSet, TaskSet, task

from config.config import SEARCH_ENDPOINT
from data.search_data import (
    EDGE_CASE_QUERIES,
    HIGH_VOLUME_QUERIES,
    POPULAR_QUERIES,
    SORT_OPTIONS,
    TECH_QUERIES,
)
from utils.logger import get_logger
from utils.response_validator import validate_homepage_response, validate_search_response

logger = get_logger(__name__)


# ── Scenario 1: Weighted Random Search ──

class BasicSearchTasks(TaskSet):

    @task(5)
    def search_popular_keyword(self):
        query = random.choice(POPULAR_QUERIES)

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": query},
            name=f"{SEARCH_ENDPOINT}?q=[popular]",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=query)
            logger.info(
                f"Popular search | query='{query}' "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task(3)
    def search_with_pagination(self):
        query = random.choice(HIGH_VOLUME_QUERIES)
        page = random.choice([2, 3, 4])

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": query, "pg": page},
            name=f"{SEARCH_ENDPOINT}?q=[keyword]&pg=[n]",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=f"{query} (pg={page})")
            logger.info(
                f"Paginated search | query='{query}' page={page} "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task(2)
    def search_with_sort(self):
        query = random.choice(POPULAR_QUERIES)
        sort = random.choice(SORT_OPTIONS)

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": query, "srt": sort},
            name=f"{SEARCH_ENDPOINT}?q=[keyword]&srt=[sort]",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=f"{query} srt={sort}")
            logger.info(
                f"Sorted search | query='{query}' sort='{sort}' "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task(2)
    def search_tech_category(self):
        query = random.choice(TECH_QUERIES)

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": query},
            name=f"{SEARCH_ENDPOINT}?q=[tech]",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=query)
            logger.info(
                f"Tech search | query='{query}' "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task(1)
    def search_edge_cases(self):
        query = random.choice(EDGE_CASE_QUERIES)

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": query},
            name=f"{SEARCH_ENDPOINT}?q=[edge_case]",
            catch_response=True,
        ) as response:
            if response.status_code in (200, 301, 302):
                response.success()
                logger.info(
                    f"Edge case | query='{query}' "
                    f"| status={response.status_code} "
                    f"| {response.elapsed.total_seconds():.2f}s"
                )
            else:
                response.failure(
                    f"Unexpected status for edge case | "
                    f"status={response.status_code} | query='{query}'"
                )

    def on_stop(self):
        logger.info("BasicSearchTasks user session ended.")


# ── Scenario 2: Full User Journey ──

class SearchUserJourney(SequentialTaskSet):
    _current_query: str = "laptop"

    def on_start(self):
        logger.info("SearchUserJourney session started.")

    @task
    def visit_homepage(self):
        with self.client.get(
            "/",
            name="/ (homepage)",
            catch_response=True,
        ) as response:
            validate_homepage_response(response)
            logger.info(
                f"Homepage | status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task
    def perform_search(self):
        self._current_query = random.choice(POPULAR_QUERIES)

        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": self._current_query},
            name=f"{SEARCH_ENDPOINT}?q=[keyword] (journey:1)",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=self._current_query)
            logger.info(
                f"Journey step 1 | search | query='{self._current_query}' "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task
    def browse_next_page(self):
        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": self._current_query, "pg": 2},
            name=f"{SEARCH_ENDPOINT}?q=[keyword]&pg=2 (journey:2)",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=f"{self._current_query} pg=2")
            logger.info(
                f"Journey step 2 | paginate | query='{self._current_query}' "
                f"| {response.elapsed.total_seconds():.2f}s"
            )

    @task
    def apply_price_sort(self):
        with self.client.get(
            SEARCH_ENDPOINT,
            params={"q": self._current_query, "srt": "PRICE_LOW"},
            name=f"{SEARCH_ENDPOINT}?q=[keyword]&srt=PRICE_LOW (journey:3)",
            catch_response=True,
        ) as response:
            validate_search_response(response, query=self._current_query)
            logger.info(
                f"Journey step 3 | sort | query='{self._current_query}' "
                f"| status={response.status_code} "
                f"| {response.elapsed.total_seconds():.2f}s"
                f" — Journey complete."
            )
        self.interrupt(reschedule=True)