import pytest
from api.pet_api import PetAPI
from config.config import BASE_URL
from models.pet_model import PetBuilder
from utils.logger import get_logger

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def pet_api() -> PetAPI:
    return PetAPI(base_url=BASE_URL)


@pytest.fixture
def created_pet(pet_api):

    payload = PetBuilder.full(name="FixturePet", status="available")
    response = pet_api.create_pet(payload)

    assert response.status_code == 200, \
        f"Fixture: pet oluşturulamadı → {response.status_code} | {response.text}"

    pet = response.json()
    logger.info(f"Fixture created pet | id={pet['id']}")

    yield pet

    pet_api.delete_pet(pet["id"])
    logger.info(f"Fixture deleted pet | id={pet['id']}")
