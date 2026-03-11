import random

VALID_STATUSES = ["available", "pending", "sold"]
INVALID_STATUS = "invalid_status"

NON_EXISTENT_PET_ID = 999999999
INVALID_PET_ID_STRING = "not-a-number"
NEGATIVE_PET_ID = -1


def generate_pet_id() -> int:
    return random.randint(100000, 999999)
