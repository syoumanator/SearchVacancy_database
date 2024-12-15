import unittest
from unittest.mock import MagicMock, patch

from src.DBManager import DBManager


class TestDBManager(unittest.TestCase):

    @patch("psycopg2.connect")
    def test_get_companies_and_vacancies_count(self, mock_connect) -> None:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Company1", 10), ("Company2", 5)]

        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        mock_connect.return_value.__enter__.return_value = mock_connection

        db_manager = DBManager()
        result = db_manager.get_companies_and_vacancies_count()

        self.assertEqual(result, [("Company1", 10), ("Company2", 5)])

    @patch("psycopg2.connect")
    def test_get_all_vacancies(self, mock_connect) -> None:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("Employer1", "Vacancy1", 50000, "url1"),
            ("Employer2", "Vacancy2", 60000, "url2"),
        ]

        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        mock_connect.return_value.__enter__.return_value = mock_connection

        db_manager = DBManager()
        result = db_manager.get_all_vacancies()

        self.assertEqual(result, [("Employer1", "Vacancy1", 50000, "url1"), ("Employer2", "Vacancy2", 60000, "url2")])

    @patch("psycopg2.connect")
    def test_get_avg_salary(self, mock_connect) -> None:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(55000.0,)]

        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        mock_connect.return_value.__enter__.return_value = mock_connection

        db_manager = DBManager()
        result = db_manager.get_avg_salary()

        self.assertEqual(result, 55000.0)

    @patch("psycopg2.connect")
    def test_get_vacancies_with_higher_salary(self, mock_connect) -> None:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("Employer1", "Vacancy1", 60000, "url1"),
            ("Employer2", "Vacancy2", 65000, "url2"),
        ]

        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        mock_connect.return_value.__enter__.return_value = mock_connection

        db_manager = DBManager()
        result = db_manager.get_vacancies_with_higher_salary()

        self.assertEqual(result, [("Employer1", "Vacancy1", 60000, "url1"), ("Employer2", "Vacancy2", 65000, "url2")])

    @patch("psycopg2.connect")
    def test_get_vacancies_with_keyword(self, mock_connect) -> None:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.side_effect = [
            [("Employer1", "Vacancy1", 50000, "url1")],
            [("Employer2", "Vacancy2", 60000, "url2")],
        ]

        mock_connection = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        mock_connect.return_value.__enter__.return_value = mock_connection

        db_manager = DBManager()
        result = db_manager.get_vacancies_with_keyword(["keyword1", "keyword2"])

        self.assertEqual(result, [("Employer1", "Vacancy1", 50000, "url1"), ("Employer2", "Vacancy2", 60000, "url2")])
