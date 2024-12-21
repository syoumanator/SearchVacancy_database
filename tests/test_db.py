import unittest
from unittest.mock import MagicMock, patch

from src.db import DBCreate


class TestDBCreate(unittest.TestCase):

    @patch("psycopg2.connect")
    def test_create_database(self, mock_connect) -> None:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        db_creator = DBCreate(database_name="test_db")
        db_creator.create_database()
        mock_cursor.execute.assert_any_call("DROP DATABASE IF EXISTS test_db")
        mock_cursor.execute.assert_any_call("CREATE DATABASE test_db")
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called()
