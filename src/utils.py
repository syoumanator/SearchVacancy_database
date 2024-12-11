import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создание баз данных и таблиц для сохранения данных о работодателе и его вакансиях"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(database_name, **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS employers_data (
        employers_id VARCHAR PRIMARY KEY,
        employers_name VARCHAR(255) NOT NULL,
        company_url VARCHAR
        );
        """
        )

        cur.execute("""CREATE TABLE IF NOT EXISTS vacancies_data (
        vacancy_id VARCHAR(20) PRIMARY KEY,
        employers_id VARCHAR(20) NOT NULL,
        vacancy_name VARCHAR NOT NULL,
        salary REAL,
        vacancy_url TEXT,
        
        CONSTRAIN fk_vacancies_employers FOREIGN KEY (employers_id) REFERENCES employers_data(employers_id)
        );
        """
        )

    conn.close()


def save_data_to_db(
    vacancy_data: list[dict], database_name: str, params: dict
) -> None:
    conn = None
    try:
        conn = psycopg2.connect(database_name, **params)
        conn.autocommit = True
        with conn.cursor() as cur:
            for employer in vacancy_data:
                cur.execute(
                    """
                    INSERT INTO employers_list (employer_id, employer_name, company_url)
                    VALUES (%s, %s, %s)
                    """,
                    (employer["employer_id"], employer["name_company"], employer["company_url"]),
                )
            for vacancy in vacancy_data:
                cur.execute(
                    """
                    INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, salary, vacancy_url)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        vacancy['vacancy_id'],
                        vacancy["employer_id"],
                        vacancy['name'],
                        vacancy["salary"],
                        vacancy["vacancy_url"],
                    ),
                )
                print("Таблица создана!")
    except Exception as error:
        print(f'Ошибка {error}')
    finally:
        if conn:
            conn.close()
