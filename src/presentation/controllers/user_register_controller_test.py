from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.tests.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {"first_name": "meuTeste", "last_name": "test", "age": 10}

def test_handle():
    http_request_mock = HttpRequestMock()
    user_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(user_case)

    response = user_register_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
