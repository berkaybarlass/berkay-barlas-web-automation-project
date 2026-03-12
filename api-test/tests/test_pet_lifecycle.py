from models.pet_model import PetBuilder


class TestPetLifecycle:

    def test_full_pet_lifecycle_create_read_update_delete(self, pet_api):
        # ── Create ────────────────────────────────────────────
        payload = PetBuilder.full(name="LifecyclePet", status="available")
        create_response = pet_api.create_pet(payload)

        assert create_response.status_code == 200
        pet_id = create_response.json()["id"]

        # ── Read ──────────────────────────────────────────────
        get_response = pet_api.get_pet(pet_id)

        assert get_response.status_code == 200
        assert get_response.json()["name"] == "LifecyclePet"
        assert get_response.json()["status"] == "available"

        # ── Update ────────────────────────────────────────────
        updated_payload = {**create_response.json(), "name": "UpdatedLifecyclePet", "status": "sold"}
        update_response = pet_api.update_pet(updated_payload)

        assert update_response.status_code == 200
        assert update_response.json()["name"] == "UpdatedLifecyclePet"
        assert update_response.json()["status"] == "sold"

        # ── Update Persist Check ──────────────────────────────
        get_after_update = pet_api.get_pet(pet_id)

        assert get_after_update.json()["name"] == "UpdatedLifecyclePet"

        # ── Delete ────────────────────────────────────────────
        delete_response = pet_api.delete_pet(pet_id)

        assert delete_response.status_code == 200

        # ── Verify Deleted ────────────────────────────────────
        get_after_delete = pet_api.get_pet(pet_id)

        assert get_after_delete.status_code == 404