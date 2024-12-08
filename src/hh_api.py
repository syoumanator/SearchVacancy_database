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

    def get_vacancies(self, employers_id):
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
                    data_d.append(vacancy)
        print(employers_id)
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
            "vacancy_id": vacancy["id"],
            "employer_id": vacancy["employer"]["id"],
            "vacancy_name": vacancy["name"],
            "salary": salary,
            "vacancy_url": vacancy.get("alternate_url", ""),}
        return transformed_vacancy


# default_companies_list = [
#          "Альфа-Банк", "Т-Банк", "Самокат (ООО Умный ритейл)", "СОГАЗ", "ПАО Ростелеком",
#         "Rusprofile", "Контур", "Нетология", "РМК", 'УГМК']

# example ={'id': '102029313', 'premium': False, 'name': 'Boдитель с легковым автомобилем', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '70', 'name': 'Оренбург', 'url': 'https://api.hh.ru/areas/70'},
#           'salary': 2344,
#           'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-12-06T08:04:22+0300', 'created_at': '2024-12-06T08:04:22+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=102029313', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/102029313?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/102029313', 'relations': [], 'employer': {'id': '4598057', 'name': 'УГМК-Телеком', 'url': 'https://api.hh.ru/employers/4598057', 'alternate_url': 'https://hh.ru/employer/4598057', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1147822.png', '240': 'https://img.hhcdn.ru/employer-logo/6211854.png', '90': 'https://img.hhcdn.ru/employer-logo/6211853.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4598057', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Boдители с личным легковым автомобилем. — Наличие водительского удостоверения категории В. — Пользователь ПК. — Рассмотрим кандидатов без опыта работы или на подработку. — ', 'responsibility': 'Водитель – оператор систем фотовидеофиксации для работы с комплексом на участках дорог. Фиксация нарушений правил дорожного движения. Режим дня: — Выезд, установка...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': True, 'professional_roles': [{'id': '21', 'name': 'Водитель'}], 'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}


# vacancies_data = HeadHunterAPI().get_vacancies(default_companies_list)
# employers_data = HeadHunterAPI().get_employers(default_companies_list)
# edit = HeadHunterAPI().change_data(example)
