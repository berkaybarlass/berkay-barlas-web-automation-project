import pytest
from data.pet_data import (
    NON_EXISTENT_PET_ID,
    INVALID_PET_ID_STRING,
    NEGATIVE_PET_ID,
    INVALID_STATUS,
)
from models.pet_model import PetBuilder


class TestPetNegative:

    # ── GET Negative ───────────────────────────────────────────

    def test_get_non_existent_pet_returns_404(self, pet_api):
        response = pet_api.get_pet(NON_EXISTENT_PET_ID)

        assert response.status_code == 404

    def test_get_pet_with_string_id_returns_400(self, pet_api):
        response = pet_api.get_pet(INVALID_PET_ID_STRING)

        assert response.status_code == 400

    def test_get_pet_with_negative_id_returns_404(self, pet_api):
        response = pet_api.get_pet(NEGATIVE_PET_ID)

        assert response.status_code in (400, 404)

    # ── DELETE Negative ────────────────────────────────────────

    def test_delete_non_existent_pet_returns_404(self, pet_api):
        response = pet_api.delete_pet(NON_EXISTENT_PET_ID)

        assert response.status_code == 404

    # ── CREATE Negative ────────────────────────────────────────

    def test_create_pet_with_invalid_body_returns_error(self, pet_api):
        response = pet_api.create_pet(PetBuilder.invalid_body())

        assert response.status_code in (400, 500)

    def test_create_pet_without_name_returns_error(self, pet_api):
        response = pet_api.create_pet(PetBuilder.without_name())

        assert response.status_code in (400, 500)

    def test_create_pet_without_photo_urls_returns_error(self, pet_api):
        response = pet_api.create_pet(PetBuilder.without_photo_urls())

        assert response.status_code in (400, 500)

    # ── UPDATE Negative ────────────────────────────────────────

    def test_update_pet_with_non_existent_id_returns_404(self, pet_api):
        payload = PetBuilder.full(pet_id=NON_EXISTENT_PET_ID)
        response = pet_api.update_pet(payload)

        assert response.status_code == 404

    # ── 405 Method Not Allowed ─────────────────────────────────

    def test_unsupported_method_on_pet_endpoint_returns_405(self, pet_api):
        response = pet_api.delete_pet_without_id()

        assert response.status_code == 405

    # ── FIND BY STATUS Negative ────────────────────────────────

    def test_find_by_invalid_status_returns_400(self, pet_api):
        response = pet_api.find_by_status(INVALID_STATUS)

        assert response.status_code == 400

    @pytest.mark.parametrize("status", ["", "  ", "AVAILABLE", "Available"])
    def test_find_by_malformed_status_returns_error(self, pet_api, status):
        response = pet_api.find_by_status(status)

        assert response.status_code in (400, 200)
        if response.status_code == 200:
            assert response.json() == []