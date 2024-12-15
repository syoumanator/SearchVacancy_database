import requests


class HeadHunterAPI:
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {}

    def get_data(self, employers_list: list[str]) -> list[dict]:
        """Метод для получения данных"""
        employers = []
        self.__url = "https://api.hh.ru/employers"
        self.__params["sort_by"] = "by_vacancies_open"
        self.__params["per_page"] = 10
        for employer in employers_list:
            self.__params["text"] = employer
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            data = response.json()
            employers.append(data)
        return employers
