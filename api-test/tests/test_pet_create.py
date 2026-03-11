import jsonschema
import pytest
from data.pet_data import VALID_STATUSES
from models.pet_model import PetBuilder
from schemas.pet_schema import PET_RESPONSE_SCHEMA


class TestPetCreate:

    # ── Positive ──────────────────────────────────────────────

    def test_create_pet_with_full_payload_returns_200(self, pet_api):
        payload = PetBuilder.full(name="FullPet", status="available")
        response = pet_api.create_pet(payload)

        assert response.status_code == 200

    def test_create_pet_response_body_contains_correct_name(self, pet_api):
        payload = PetBuilder.full(name="NameCheckPet")
        response = pet_api.create_pet(payload)

        assert response.json()["name"] == "NameCheckPet"
