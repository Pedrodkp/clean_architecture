from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from .user_finder_validator import user_finder_validator

class MockRequest:
    def __init__(self) -> None:
        self.args = None

def test_user_finder_validator():
    request = MockRequest()
    request.args = {
        "first_name": 123
    }
    try:
        user_finder_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
