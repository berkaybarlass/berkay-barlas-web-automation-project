import requests
from utils.logger import get_logger


class BaseAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url} | params={kwargs.get('params')}")
        response = self.session.get(url, **kwargs)
        self.logger.info(f"← {response.status_code} | {len(response.content)} bytes")
        return response

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url} | body={kwargs.get('json')}")
        response = self.session.post(url, **kwargs)
        self.logger.info(f"← {response.status_code}")
        return response

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PUT {url} | body={kwargs.get('json')}")
        response = self.session.put(url, **kwargs)
        self.logger.info(f"← {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")
        response = self.session.delete(url, **kwargs)
        self.logger.info(f"← {response.status_code}")
        return response
