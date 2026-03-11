from models.pet_model import PetBuilder

class TestPetDelete:

    # ── Positive ──────────────────────────────────────────────

    def test_delete_existing_pet_returns_200(self, pet_api):
        payload = PetBuilder.full(name="PetToDelete")
        pet_id = pet_api.create_pet(payload).json()["id"]

        response = pet_api.delete_pet(pet_id)

        assert response.status_code == 200

    def test_deleted_pet_returns_404_on_get(self, pet_api):
        payload = PetBuilder.full(name="PetDeleteVerify")
        pet_id = pet_api.create_pet(payload).json()["id"]

        pet_api.delete_pet(pet_id)
        get_response = pet_api.get_pet(pet_id)

        assert get_response.status_code == 404

    def test_delete_same_pet_twice_returns_404(self, pet_api):
        payload = PetBuilder.full(name="PetDoubleDelete")
        pet_id = pet_api.create_pet(payload).json()["id"]

        pet_api.delete_pet(pet_id)
        second_response = pet_api.delete_pet(pet_id)

        assert second_response.status_code == 404

    def test_delete_pet_response_time_is_acceptable(self, pet_api):
        payload = PetBuilder.full(name="PetResponseTime")
        pet_id = pet_api.create_pet(payload).json()["id"]

        response = pet_api.delete_pet(pet_id)

        assert response.elapsed.total_seconds() < 2.0, \
            f"Response too slow: {response.elapsed.total_seconds()}s"