from typing import Optional, List

from data.pet_data import generate_pet_id


class PetBuilder:

    @staticmethod
    def full(
        pet_id: Optional[int] = None,
        name: str = "TestDog",
        status: str = "available",
        photo_urls: Optional[List[str]] = None,
    ) -> dict:
        return {
            "id": pet_id or generate_pet_id(),
            "name": name,
            "status": status,
            "photoUrls": photo_urls or ["https://berkaytest.com/photo.jpg"],
            "category": {"id": 1, "name": "Dogs"},
            "tags": [{"id": 1, "name": "test-tag"}],
        }

    @staticmethod
    def minimal(name: str = "MinimalPet") -> dict:
        return {
            "name": name,
            "photoUrls": ["https://berkaytest.com/photo.jpg"],
        }

    @staticmethod
    def without_name() -> dict:
        return {
            "id": generate_pet_id(),
            "photoUrls": ["https://berkaytest.com/photo.jpg"],
            "status": "available",
        }

    @staticmethod
    def without_photo_urls() -> dict:
        return {
            "id": generate_pet_id(),
            "name": "NoPhotosPet",
            "status": "available",
        }

    @staticmethod
    def invalid_body() -> dict:
        return {"random_key": "random_value", "number": 999}
