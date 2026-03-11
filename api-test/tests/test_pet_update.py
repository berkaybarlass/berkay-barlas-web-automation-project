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

    def test_update_pet_status_returns_200(self, pet_api, created_pet):
        payload = {**created_pet, "status": "sold"}
        response = pet_api.update_pet(payload)

        assert response.status_code == 200

    def test_update_pet_status_reflected_in_response(self, pet_api, created_pet):
        payload = {**created_pet, "status": "pending"}
        response = pet_api.update_pet(payload)

        assert response.json()["status"] == "pending"

    def test_update_persists_on_subsequent_get(self, pet_api, created_pet):
        payload = {**created_pet, "name": "PersistCheck"}
        pet_api.update_pet(payload)

        get_response = pet_api.get_pet(created_pet["id"])

        assert get_response.json()["name"] == "PersistCheck"

    def test_update_pet_category_reflected_in_response(self, pet_api, created_pet):
        payload = {**created_pet, "category": {"id": 2, "name": "Cats"}}
        response = pet_api.update_pet(payload)

        assert response.status_code == 200
        assert response.json()["category"]["name"] == "Cats"

    def test_update_pet_tags_reflected_in_response(self, pet_api, created_pet):
        payload = {**created_pet, "tags": [{"id": 99, "name": "updated-tag"}]}
        response = pet_api.update_pet(payload)

        assert response.status_code == 200
        assert response.json()["tags"][0]["name"] == "updated-tag"

    def test_update_pet_response_time_is_acceptable(self, pet_api, created_pet):
        payload = {**created_pet, "name": "ResponseTimeCheck"}
        response = pet_api.update_pet(payload)

        assert response.elapsed.total_seconds() < 2.0, \
            f"Response too slow: {response.elapsed.total_seconds()}s"