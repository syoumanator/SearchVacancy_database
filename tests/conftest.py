import pytest


@pytest.fixture
def company_name() -> list[str]:
    return ["Тест"]


@pytest.fixture
def company_data() -> list[dict]:
    return [
        {
            "items": [
                {
                    "id": "80",
                    "name": "Альфа-Банк",
                    "url": "https://api.hh.ru/employers/80",
                    "alternate_url": "https://hh.ru/employer/80",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/663873.png",
                        "240": "https://img.hhcdn.ru/employer-logo/3096625.png",
                        "90": "https://img.hhcdn.ru/employer-logo/3096624.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=80",
                    "open_vacancies": 2010,
                },
                {
                    "id": "534346",
                    "name": "АЛЬФА-БАНК",
                    "url": "https://api.hh.ru/employers/534346",
                    "alternate_url": "https://hh.ru/employer/534346",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/878490.png",
                        "240": "https://img.hhcdn.ru/employer-logo/3954836.png",
                        "90": "https://img.hhcdn.ru/employer-logo/3954835.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=534346",
                    "open_vacancies": 84,
                },
                {
                    "id": "5730209",
                    "name": "Шаповалова Ольга Юрьевна",
                    "url": "https://api.hh.ru/employers/5730209",
                    "alternate_url": "https://hh.ru/employer/5730209",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1245742.jpg",
                        "240": "https://img.hhcdn.ru/employer-logo/6603398.jpeg",
                        "90": "https://img.hhcdn.ru/employer-logo/6603397.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5730209",
                    "open_vacancies": 0,
                },
                {
                    "id": "5845941",
                    "name": "ФСЗС АО Альфа-Банк",
                    "url": "https://api.hh.ru/employers/5845941",
                    "alternate_url": "https://hh.ru/employer/5845941",
                    "logo_urls": None,
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5845941",
                    "open_vacancies": 0,
                },
            ],
            "found": 4,
            "pages": 1,
            "page": 0,
            "per_page": 10,
        },
        {
            "items": [
                {
                    "id": "78638",
                    "name": "Т-Банк",
                    "url": "https://api.hh.ru/employers/78638",
                    "alternate_url": "https://hh.ru/employer/78638",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1285309.png",
                        "240": "https://img.hhcdn.ru/employer-logo/6761535.png",
                        "90": "https://img.hhcdn.ru/employer-logo/6761534.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=78638",
                    "open_vacancies": 11003,
                }
            ],
            "found": 1,
            "pages": 1,
            "page": 0,
            "per_page": 10,
        },
    ]
