class Employers:

    def get_employers(self, employers_list: list[dict]) -> list[dict]:
        """Метод для получения данных о работодателе"""
        employers = []
        for employer in employers_list:
            if employer.get("items"):
                result = next(item for item in employer["items"])
                employers.append(
                    {
                        "employer_id": result.get("id"),
                        "employer_name": result.get("name"),
                        "company_url": result.get("alternate_url"),
                    }
                )
            else:
                employers.append({"employer_name": employer, "error": "Данные отсутствуют"})
        return employers
