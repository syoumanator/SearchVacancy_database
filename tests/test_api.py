import unittest
from unittest.mock import MagicMock, patch

from src.api import HeadHunterAPI


class TestSearchVacancies(unittest.TestCase):

    def setUp(self):
        self.search = HeadHunterAPI()

    @patch("requests.get")
    def test_successful_search(self, mock_get) -> None:

        mock_response = MagicMock()
        mock_response.json.return_value = {"items": [{"id": 1}, {"id": 2}], "pages": 10}
        mock_get.return_value = mock_response

        employers = self.search.get_data(["Test1", "Test2"])

        self.assertEqual(len(employers), 2)

    def test_get_data(self) -> None:
        with unittest.mock.patch("requests.get") as mock_get:
            mock_response = unittest.mock.MagicMock()
            mock_response.json.return_value = [{"id": 1, "name": "Employer 1"}, {"id": 2, "name": "Employer 2"}]

            mock_get.return_value = mock_response

            employers = self.search.get_data(["Employer 1", "Employer 2"])

            self.assertEqual(len(employers), 2)
            self.assertEqual(employers[0], [{"id": 1, "name": "Employer 1"}, {"id": 2, "name": "Employer 2"}])


@patch("requests.get")
def test_get_data_2(mock_get: MagicMock, company_name: list[str]) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "name": "Employer 1"}
    assert HeadHunterAPI().get_data(company_name) == [{"id": 1, "name": "Employer 1"}]
