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

    def test_create_pet_response_body_contains_id(self, pet_api):
        payload = PetBuilder.full()
        response = pet_api.create_pet(payload)

        assert "id" in response.json()

    def test_create_pet_with_minimal_payload_returns_200(self, pet_api):
        payload = PetBuilder.minimal(name="MinimalPet")
        response = pet_api.create_pet(payload)

        assert response.status_code == 200
        assert response.json()["name"] == "MinimalPet"

    def test_create_pet_response_content_type_is_json(self, pet_api):
        payload = PetBuilder.full()
        response = pet_api.create_pet(payload)

        assert "application/json" in response.headers.get("Content-Type", "")

    def test_create_pet_response_contains_required_fields(self, pet_api):
        payload = PetBuilder.full()
        response = pet_api.create_pet(payload)
        body = response.json()

        assert all(k in body for k in ["id", "name", "status", "photoUrls"])

    def test_create_pet_response_matches_schema(self, pet_api):
        payload = PetBuilder.full()
        response = pet_api.create_pet(payload)

        jsonschema.validate(instance=response.json(), schema=PET_RESPONSE_SCHEMA)

    def test_create_pet_response_time_is_acceptable(self, pet_api):
        payload = PetBuilder.full()
        response = pet_api.create_pet(payload)

        assert response.elapsed.total_seconds() < 2.0, \
            f"Response too slow: {response.elapsed.total_seconds()}s"

    @pytest.mark.parametrize("status", VALID_STATUSES)
    def test_create_pet_with_each_valid_status(self, pet_api, status):
        payload = PetBuilder.full(name=f"StatusPet_{status}", status=status)
        response = pet_api.create_pet(payload)

        assert response.status_code == 200
        assert response.json()["status"] == status
