import requests


class Vacancies:

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {}

    def get_id(self, data_list: list[dict]) -> list[str]:
        """Метод для получения id компаний"""

        employers_id = []
        for employer_id in data_list:
            if employer_id.get("items"):
                result = next(item for item in employer_id["items"])
                employers_id.append(result.get("id"))
        return employers_id

    def get_vacancies(self, employer_id: str) -> list[dict]:
        """Метод для получения данных о вакансиях по id"""
        list_vacancies = []
        self.__params = {}
        self.__url = "https://api.hh.ru/vacancies"
        self.__params["employer_id"] = employer_id
        self.__params["per_page"] = 10
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        data = response.json().get("items", [])
        for vacancy in data:
            if isinstance(vacancy.get("salary"), dict):
                if vacancy.get("salary").get("from") is None and vacancy.get("salary").get("to") is None:
                    salary = "Зарплата не указана"
                elif vacancy.get("salary").get("from") and vacancy.get("salary").get("to") is None:
                    salary = f"от {vacancy.get("salary").get('from')}"
                elif vacancy.get("salary").get("from") is None and vacancy.get("salary").get("to"):
                    salary = f"до {vacancy.get("salary").get('to')}"
                elif vacancy.get("salary").get("from") and vacancy.get("salary").get("to"):
                    salary = f"{vacancy.get("salary").get('from')} - {vacancy.get("salary").get('to')}"
            elif vacancy.get("salary") is None:
                salary = "Зарплата не указана"
            else:
                salary = vacancy.get("salary")

            transformed_vacancy = {
                "vacancy_id": vacancy["id"],
                "employer_id": vacancy["employer"]["id"],
                "vacancy_name": vacancy["name"],
                "salary": salary,
                "vacancy_url": vacancy.get("alternate_url"),
            }
            list_vacancies.append(transformed_vacancy)
        return list_vacancies
