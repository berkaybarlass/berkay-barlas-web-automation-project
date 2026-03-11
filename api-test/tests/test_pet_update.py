class TestPetUpdate:

    # ── Positive ──────────────────────────────────────────────

    def test_update_pet_name_returns_200(self, pet_api, created_pet):
        payload = {**created_pet, "name": "UpdatedName"}
        response = pet_api.update_pet(payload)

        assert response.status_code == 200

    def test_update_pet_name_reflected_in_response(self, pet_api, created_pet):
        payload = {**created_pet, "name": "ReflectedName"}
        response = pet_api.update_pet(payload)

        assert response.json()["name"] == "ReflectedName"