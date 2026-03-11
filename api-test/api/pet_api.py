import requests
from api.base_api import BaseAPI


class PetAPI(BaseAPI):

    def create_pet(self, payload: dict) -> requests.Response:
        return self.post("/pet", json=payload)

    def get_pet(self, pet_id) -> requests.Response:
        return self.get(f"/pet/{pet_id}")

    def update_pet(self, payload: dict) -> requests.Response:
        return self.put("/pet", json=payload)

    def delete_pet(self, pet_id: int) -> requests.Response:
        return self.delete(f"/pet/{pet_id}")

    def find_by_status(self, status: str) -> requests.Response:
        return self.get("/pet/findByStatus", params={"status": status})

    def delete_pet_without_id(self) -> requests.Response:
        return self.delete("/pet")
