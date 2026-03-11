import jsonschema
from schemas.pet_schema import PET_RESPONSE_SCHEMA


class TestPetRead:

    # ── Positive ──────────────────────────────────────────────

    def test_get_existing_pet_returns_200(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert response.status_code == 200

    def test_get_existing_pet_returns_correct_id(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert response.json()["id"] == created_pet["id"]

    def test_get_existing_pet_returns_correct_name(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert response.json()["name"] == created_pet["name"]

    def test_get_existing_pet_returns_correct_status(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert response.json()["status"] == created_pet["status"]

    def test_get_pet_response_contains_required_fields(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])
        body = response.json()

        assert all(k in body for k in ["id", "name", "status", "photoUrls"])

    def test_get_pet_response_content_type_is_json(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert "application/json" in response.headers.get("Content-Type", "")

    def test_get_pet_response_time_is_acceptable(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        assert response.elapsed.total_seconds() < 2.0, \
            f"Response too slow: {response.elapsed.total_seconds()}s"

    def test_get_pet_response_matches_schema(self, pet_api, created_pet):
        response = pet_api.get_pet(created_pet["id"])

        jsonschema.validate(instance=response.json(), schema=PET_RESPONSE_SCHEMA)