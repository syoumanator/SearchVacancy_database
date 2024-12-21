import unittest

from src.employers import Employers


class TestEmployers(unittest.TestCase):

    def setUp(self) -> None:
        self.employer = Employers()

    def test_get_employers_with_data(self) -> None:
        employers_list = [
            {"items": [{"id": 1, "name": "Google", "alternate_url": "google.com"}]},
            {"items": [{"id": 2, "name": "Microsoft", "alternate_url": "microsoft.com"}]},
        ]
        result = self.employer.get_employers(employers_list)
        expected_result = [
            {"employer_id": 1, "employer_name": "Google", "company_url": "google.com"},
            {"employer_id": 2, "employer_name": "Microsoft", "company_url": "microsoft.com"},
        ]
        self.assertEqual(result, expected_result)

    def test_get_employers_without_data(self) -> None:
        employers_list = [{"items": []}, {"items": [{"id": 3, "name": "Amazon", "alternate_url": "amazon.com"}]}]
        result = self.employer.get_employers(employers_list)
        expected_result = [
            {"employer_name": {"items": []}, "error": "Данные отсутствуют"},
            {"employer_id": 3, "employer_name": "Amazon", "company_url": "amazon.com"},
        ]
        self.assertEqual(result, expected_result)

    def test_get_employers_empty_list(self) -> None:
        employers_list = []
        result = self.employer.get_employers(employers_list)
        expected_result = []
        self.assertEqual(result, expected_result)
