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
        vacancies.extend(HeadHunterAPI().get_vacancies(employer['employer_id'], employer["company_url"], employer["employer_name"]))

    for i in vacancies:
        # print(i)
        edit = HeadHunterAPI().change_data(i)
        print(edit)


if __name__ == '__main__':
    main()

#
# s = {'id': '112867974', 'premium': False, 'name': 'Стажёр менеджер проектов', 'department': {'id': '80-80-bank', 'name': 'Альфа-Банк'}, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-12-10T14:48:57+0300', 'created_at': '2024-12-10T14:48:57+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=112867974', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': {'id': '32631', 'url': 'https://hh.ru/interview/32631?employerId=80'}, 'url': 'https://api.hh.ru/vacancies/112867974?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/112867974', 'relations': [], 'employer': {'id': '80', 'name': 'Альфа-Банк', 'url': 'https://api.hh.ru/employers/80', 'alternate_url': 'https://hh.ru/employer/80', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/663873.png', '240': 'https://img.hhcdn.ru/employer-logo/3096625.png', '90': 'https://img.hhcdn.ru/employer-logo/3096624.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=80', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Хорошее владение PowerPoint, умение работать с Eхcel. Ответственность, умение грамотно распоряжаться временем на рабочие задачи. Навыки презентации, отличные коммуникативные и...', 'responsibility': 'Подготавливать материалы для презентаций ко встречам. Работать с отчетностью, сводными таблицами. Взаимодействовать с командой аналитиков в рамках технических заданий на...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '107', 'name': 'Руководитель проектов'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None, 'company_url': 'https://hh.ru/employer/80'}
#
# print(s.get('department').get('name'))
