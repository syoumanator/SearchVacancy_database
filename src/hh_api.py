# from typing import Any

import requests


class HeadHunterAPI:
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {}

    def _get_response(self) -> bool:
        """Метод подключения к API"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return True
        else:
            print(f"Ошибка при запросе: {response.status_code}")
            return False

    def get_employers(self, employers_list: list[str]) -> list[dict]:
        """Метод для получения данных о работодателе"""
        employers = []
        if self._get_response():
            self.__url = "https://api.hh.ru/employers"
            self.__params["sort_by"] = "by_vacancies_open"
            self.__params["per_page"] = 10
        for employer in employers_list:
            self.__params["text"] = employer
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            data = response.json()
            if data.get('items'):
                result = next(item for item in data['items'])
                employers.append({"employer_id": result.get('id'), "employer_name": result.get('name'), "company_url": result.get('alternate_url')})
            else:
                employers.append({'employer_name': employer, 'error': 'Данные отсутствуют'})
        return employers

    def get_vacancies(self, employers_id, company_url, employer_name):
        """Метод для получения данных о вакансиях по id"""
        data_d = []
        if self._get_response():
                self.__params = {}
                self.__url = "https://api.hh.ru/vacancies"
                self.__params["employer_id"] = employers_id
                self.__params["per_page"] = 10
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                data = response.json().get('items', [])
                for vacancy in data:
                    vacancy['company_url'] = company_url
                    vacancy['employer_name'] = employer_name

                    data_d.append(vacancy)
        return data_d

    @classmethod
    def change_data(cls, vacancy: dict):
        """Метод для преобразования вакансии в подходящий формат"""
        if isinstance(vacancy.get("salary"), dict):
            if vacancy.get("salary").get('from') is None and vacancy.get("salary").get('to') is None:
                salary = "Зарплата не указана"
            elif vacancy.get("salary").get('from') and vacancy.get("salary").get('to') is None:
                salary = f"от {vacancy.get("salary").get('from')}"
            elif vacancy.get("salary").get('from') is None and vacancy.get("salary").get('to'):
                salary = f"до {vacancy.get("salary").get('to')}"
            elif vacancy.get("salary").get('from') and vacancy.get("salary").get('to'):
                salary = f"{vacancy.get("salary").get('from')} - {vacancy.get("salary").get('to')}"
        elif vacancy.get("salary") is None:
            salary = "Зарплата не указана"
        else:
            salary = vacancy.get("salary")

        transformed_vacancy = {
            "name_company": vacancy["employer_name"],
            "vacancy_id": vacancy["id"],
            "employer_id": vacancy["employer"]["id"],
            "vacancy_name": vacancy["name"],
            "salary": salary,
            "company_url": vacancy["company_url"],
            "vacancy_url": vacancy.get("alternate_url"),}
        return transformed_vacancy
