import pytest
import database
import sqlite3

@pytest.fixture
def test_db(monkeypatch, tmp_path):
    db_path = tmp_path / "test_task.db"
    
    monkeypatch.setattr(
        database, 
        "get_connection",
        lambda: sqlite3.connect(db_path)
    )
    
    database.init_db()
    
    return db_path