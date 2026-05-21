import os
from unittest.mock import MagicMock, patch
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from src.load import load_to_db

# some tests require invocation of functionality that depends on global settings or involves network access
# monkeypatch allows for the safe set/delete of a attribute, dictionary item, or environmental variable, or can modify sys.path
def setup_db_env(monkeypatch):
    monkeypatch.setenv("DB_USERNAME", "user")
    monkeypatch.setenv("DB_PASSWORD", "pass")
    monkeypatch.setenv("DB_HOST", "host")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_DATABASE_NAME", "database")
    monkeypatch.setenv("DB_TABLE_NAME", "weather")


def test_database_connection(monkeypatch):
    setup_db_env(monkeypatch)

    # MagicMock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
    mock_engine = MagicMock()
    mock_engine.url = "postgresql://host"

    with patch("src.load.create_engine", return_value=mock_engine) as create_engine_mock, \
         patch("src.load.database_exists", return_value=True), \
         patch("src.load.create_database"):
        load_to_db(MagicMock())

    create_engine_mock.assert_called_once_with(
        "postgresql+psycopg2://user:pass@host:5432/database"
    )


def test_database_creation(monkeypatch):
    setup_db_env(monkeypatch)
    mock_engine = MagicMock()
    mock_engine.url = "postgresql://host"
    mock_conn = MagicMock()
    mock_engine.begin.return_value.__enter__.return_value = mock_conn
    mock_df = MagicMock()

    # replace real database calls with mocked patch ones
    with patch("src.load.create_engine", return_value=mock_engine), \
         patch("src.load.database_exists", return_value=False), \
         patch("src.load.create_database") as create_database_mock:
        load_to_db(mock_df)

    create_database_mock.assert_called_once_with(mock_engine.url)
    mock_df.to_sql.assert_called_once_with("weather", mock_conn, if_exists="append", index=False)


def test_dataframe_loading(monkeypatch):
    setup_db_env(monkeypatch)
    mock_engine = MagicMock()
    mock_engine.url = "postgresql://host"
    mock_conn = MagicMock()

    # mock the context manager behavior of engine.begin()
    mock_engine.begin.return_value.__enter__.return_value = mock_conn
    mock_df = MagicMock()

    with patch("src.load.create_engine", return_value=mock_engine), \
         patch("src.load.database_exists", return_value=True), \
         patch("src.load.create_database"):
        load_to_db(mock_df)

    mock_df.to_sql.assert_called_once_with("weather", mock_conn, if_exists="append", index=False)


def test_sql_error_handling(monkeypatch):
    setup_db_env(monkeypatch)
    mock_engine = MagicMock()
    mock_engine.url = "postgresql://host"
    mock_engine.begin.return_value.__enter__.return_value = MagicMock()
    mock_df = MagicMock()
    mock_df.to_sql.side_effect = SQLAlchemyError("load failed")

    with patch("src.load.create_engine", return_value=mock_engine), \
         patch("src.load.database_exists", return_value=True), \
         patch("src.load.create_database"), \
         patch("src.load.logger.error") as error_logger:
        load_to_db(mock_df)

    error_logger.assert_called_once()
    assert "load failed" in str(error_logger.call_args[0][1])


def test_invalid_credentials(monkeypatch):
    setup_db_env(monkeypatch)
    mock_df = MagicMock()

    with patch("src.load.create_engine", side_effect=SQLAlchemyError("invalid credentials")), \
         patch("src.load.logger.error") as error_logger:
        load_to_db(mock_df)

    error_logger.assert_called_once()
    assert "invalid credentials" in str(error_logger.call_args[0][1])
