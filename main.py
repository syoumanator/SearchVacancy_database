from src.hh_api import HeadHunterAPI


def main():
    """Основная функция проекта, которая взаимодействует с пользователем"""
    default_companies_list = [
         "Альфа-Банк", "Т-Банк", "Самокат (ООО Умный ритейл)", "СОГАЗ", "ПАО Ростелеком",
        "Rusprofile", "Контур", "Нетология", "РМК", 'УГМК']
    vacancies = []
    check_response = HeadHunterAPI()._get_response()
    print(check_response)

    employers_data = HeadHunterAPI().get_employers(default_companies_list)
    for employer in employers_data:
        vacancies.extend(HeadHunterAPI().get_vacancies(employer['employer_id']))
    for i in vacancies:
        edit = HeadHunterAPI().change_data(i)
        print(edit)


if __name__ == '__main__':
    main()
