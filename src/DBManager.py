import psycopg2


class DBManager:
    """Класс для работы с БД"""
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """Выводит список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()
        





