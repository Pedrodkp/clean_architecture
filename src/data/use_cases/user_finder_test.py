from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = "meunome"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = "meunome123"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False #erro por não ter exception
    except Exception as exception:
        assert str(exception) == "Nome inválido para a busca"

def test_find_error_in_too_long_name():
    first_name = "meunomemeunomemeunomemeuno"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False #erro por não ter exception
    except Exception as exception:
        assert str(exception) == "Nome muito grande para busca"

def test_find_error_user_not_found():
    first_name = "teste"

    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False #erro por não ter exception
    except Exception as exception:
        assert str(exception) == "Usuário não encontrado"
