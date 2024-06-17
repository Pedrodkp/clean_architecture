import pytest
from .connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_conection_handle = DBConnectionHandler()

    engine = db_conection_handle.get_engine()
    assert engine is not None
