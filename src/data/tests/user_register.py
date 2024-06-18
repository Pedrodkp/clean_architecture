from typing import Dict

class UserRegisterSpy:

    def __init__(self) -> None:
        self.registry_attributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.registry_attributes["first_name"] = first_name
        self.registry_attributes["last_name"] = last_name
        self.registry_attributes["age"] = age

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                {"first_name": first_name, "last_name": last_name, "age": age}
            ]
        }
