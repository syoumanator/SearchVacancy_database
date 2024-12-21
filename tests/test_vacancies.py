import unittest
from unittest.mock import MagicMock, patch

from src.vacancies import Vacancies


@patch("requests.get")
def test_get_id(mock_get: MagicMock, company_data) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = ["80", "78638"]
    assert Vacancies().get_id(company_data) == ["80", "78638"]


class TestVacancies(unittest.TestCase):

    def setUp(self):
        self.vacancies = Vacancies()

    @patch("requests.get")
    def test_get_vacancies(self, mock_get) -> None:
        mock_response = {
            "items": [
                {
                    "id": 112867974,
                    "name": "Стажёр менеджер проектов",
                    "salary": {"from": None, "to": None},
                    "employer": {"id": 80},
                }
            ]
        }

        mock_get.return_value.json.return_value = mock_response

        result = self.vacancies.get_vacancies("80")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["vacancy_id"], 112867974)
        self.assertEqual(result[0]["vacancy_name"], "Стажёр менеджер проектов")
        self.assertEqual(result[0]["salary"], "Зарплата не указана")
