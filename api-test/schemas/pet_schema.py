# JSON Schema definitions for Petstore API responses.
# Reference: https://petstore.swagger.io/#/pet

PET_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "photoUrls"],
    "properties": {
        "id": {
            "type": "integer"
        },
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            }
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {"type": "string"}
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            }
        },
        "status": {
            "type": "string",
            "enum": ["available", "pending", "sold"]
        }
    },
    "additionalProperties": False
}
