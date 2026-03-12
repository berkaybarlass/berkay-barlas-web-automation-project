from locust import HttpUser, between

from config.config import BASE_URL, THINK_TIME_MIN, THINK_TIME_MAX
from scenarios.task_sets import BasicSearchTasks, SearchUserJourney
from utils.logger import get_logger

logger = get_logger("locustfile")
logger.info(f"Load test initialized | target={BASE_URL}")


class SearchUser(HttpUser):
    host = BASE_URL
    weight = 3
    tasks = [BasicSearchTasks]
    wait_time = between(THINK_TIME_MIN, THINK_TIME_MAX)


class SearchJourneyUser(HttpUser):
    host = BASE_URL
    weight = 1
    tasks = [SearchUserJourney]
    wait_time = between(THINK_TIME_MIN, THINK_TIME_MAX)
