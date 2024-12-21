import psycopg2

from config.config import config


class DBCreate:
    """Класс создает и заполняет таблицы PostgreSQL"""

    def __init__(self, database_name: str = "hh_ru") -> None:
        self.database_name = database_name
        self.__params = config()
        self.__conn = psycopg2.connect(dbname="postgres", **self.__params)

    def create_database(self) -> None:
        """Метод создает базу данных и таблицы"""
        conn = self.__conn
        conn.autocommit = True
        cur = conn.cursor()
        try:
            cur.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
            cur.execute(f"CREATE DATABASE {self.database_name}")
        except Exception as e:
            print(f"Произошла ошибка при удалении базы данных: {e}")
        finally:
            cur.close()
            conn.close()

        conn = psycopg2.connect(dbname=self.database_name, **self.__params)
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE employees (
                        employer_id INT PRIMARY KEY,
                        employer_name VARCHAR(255) NOT NULL,
                        company_url TEXT NOT NULL
                    )
                """
                )
                cur.execute(
                    """
                    CREATE TABLE vacancies (
                        vacancy_id VARCHAR(255) NOT NULL,
                        employer_id INT REFERENCES employees(employer_id),
                        vacancy_name VARCHAR NOT NULL,
                        salary VARCHAR,
                        vacancy_url TEXT
                    )
                """
                )
                conn.commit()
        except Exception as e:
            print(f"Произошла ошибка при создании таблиц: {e}")
        finally:
            conn.close()

    def save_data_to_database(self, employers_data: list[dict], vacancy_data: list[dict]) -> None:
        """Метод заполняет таблицы данными"""
        if employers_data and vacancy_data:
            conn = self.__conn = psycopg2.connect(dbname=self.database_name, **self.__params)

            with conn.cursor() as cur:
                for employer in employers_data:
                    cur.execute(
                        """
                        INSERT INTO employees (employer_id, employer_name, company_url)
                        VALUES (%s, %s, %s) ON CONFLICT DO NOTHING
                        RETURNING employer_id""",
                        (employer["employer_id"], employer["employer_name"], employer["company_url"]),
                    )
                for vacancy in vacancy_data:
                    cur.execute(
                        """
                        INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name,
                        salary, vacancy_url)
                        VALUES (%s, %s, %s, %s, %s)""",
                        (
                            vacancy["vacancy_id"],
                            vacancy["employer_id"],
                            vacancy["vacancy_name"],
                            vacancy["salary"],
                            vacancy["vacancy_url"],
                        ),
                    )
            conn.commit()
            conn.close()
        else:
            print("Нет данных")
