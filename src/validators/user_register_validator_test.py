from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from .user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator():
    request = MockRequest()
    request.json = {
        "first_name": 123,
        "last_name": "algumaCoisa",
        "age": 23
    }
    try:
        user_register_validator(request)
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
