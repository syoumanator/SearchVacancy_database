import unittest
from unittest.mock import patch, MagicMock
from src.hh_api import HeadHunterAPI

api = HeadHunterAPI()


class TestResponses(unittest.TestCase):

    @patch.object(HeadHunterAPI, '_get_response')
    def test_get_response_success(self, mock_get_response):
        mock_get_response.return_value = True
        result_success = api._get_response()

        self.assertTrue(result_success)
        mock_get_response.assert_called_once_with()

    @patch.object(HeadHunterAPI, '_get_response')
    def test_get_response_fail(self, mock_get_response):
        mock_get_response.return_value = False
        result_fail = api._get_response()

        self.assertFalse(result_fail)
        mock_get_response.assert_called_once_with()


class TestEmployers(unittest.TestCase):

    @patch('requests.get')
    def test_get_employers_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'items': [{'id': '123', 'name': 'Test Employer', 'alternate_url': 'https://example.com'}]}
        mock_get.return_value = mock_response
        result = api.get_employers(['Test Employer'])

        # Проверка результата
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0],
                         {'employer_id': '123', 'employer_name': 'Test Employer', 'company_url': 'https://example.com'})

    @patch('requests.get')
    def test_get_employers_fail(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'items': []}
        mock_get.return_value = mock_response

        result = api.get_employers(['Test Employer'])

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0], {'employer_name': 'Test Employer', 'error': 'Данные отсутствуют'})


class TestVacancies(unittest.TestCase):

    @patch('requests.get')
    def test_get_vacancies_fail(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404)
        result = api.get_vacancies('123', 'https://example.com/company', 'Test Employer')

        self.assertEqual(result, [])



