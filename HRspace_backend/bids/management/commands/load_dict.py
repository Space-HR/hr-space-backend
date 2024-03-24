import csv

from bids.models import (City, Country, EducationsOption, EmployeeCategory,
                         ExperienceOption, JobVacancy, RegisterAsOption,
                         ScheduleOption, Sphere, WorkFormat)
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Заполняем словари'

    def handle(self, *args, **kwargs):
        print('\nЗаполняем справочник графиков работы')
        data = [
            {'name': 'Сменный'},
            {'name': 'Вахтовый'},
            {'name': '5/2 пн - пт'},
            {'name': 'Свободный'},
            {'name': 'Другой'}]
        ScheduleOption.objects.bulk_create(
            ScheduleOption(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Графики работы успешно загруженны!\n'))

        print('\nЗаполняем справочник форматов работы')
        data = [
            {'name': 'В офисе'},
            {'name': 'Удаленно'},
            {'name': 'Гибрид'}]
        WorkFormat.objects.bulk_create(
            WorkFormat(**work) for work in data)
        self.stdout.write(self.style.SUCCESS(
            'Форматы работы успешно загруженны!\n'))

        print('\nЗаполняем справочник cпособов оформления сотрудника')
        data = [
            {'name': 'ТК РФ'},
            {'name': 'Самозанятые'},
            {'name': 'ИП'},
            {'name': 'ГПХ'}]
        RegisterAsOption.objects.bulk_create(
            RegisterAsOption(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Способы оформления сотрудника успешно загруженны!\n'))

        print('\nЗаполняем справочник особых категорий граждан')
        data = [
            {'name': 'Студентов'},
            {'name': 'От 14 лет'},
            {'name': 'От 16 лет'},
            {'name': 'Пенсионеров'},
            {'name': 'С нарушением здоровья'},
            {'name': 'Иностранных граждан'}]
        EmployeeCategory.objects.bulk_create(
            EmployeeCategory(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Категории граждан успешно загруженны!\n'))

        print('\nЗаполняем справочник требований к опыту работы')
        data = [
            {'name': 'Без опыта'},
            {'name': 'От 1 года до 3 лет'},
            {'name': 'От 3 до 6 лет'},
            {'name': 'Более 6 лет'}]
        ExperienceOption.objects.bulk_create(
            ExperienceOption(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Требования к опыту работы успешно загруженны!\n'))

        print('\nЗаполняем справочник требований к образованию')
        data = [
            {'name': 'Среднее'},
            {'name': 'Среднее специальное'},
            {'name': 'Неоконченное высшее'},
            {'name': 'Высшее'},
            {'name': 'Бакалавр'},
            {'name': 'Магистр'},
            {'name': 'Кандидат наук'},
            {'name': 'Доктор наук'}]
        EducationsOption.objects.bulk_create(
            EducationsOption(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Требования к образованию успешно загруженны!\n'))

        self.import_cites()
        print('Загрузка списка городов завершена.\n')

        self.import_job_vacancy()
        print('Загрузка списка профессий завершена.\n')

        self.import_country()
        print('Загрузка списка стран завершена.\n')

        self.import_sphere()
        print('Загрузка списка сфер деятельности завершена.\n')

    def import_sphere(self, file='sphere.csv'):
        print(f'\nЗагрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for name in reader:
                Sphere.objects.update_or_create(name=name)

    def import_country(self, file='country.csv'):
        print(f'Загрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for name in reader:
                Country.objects.update_or_create(name=name)

    def import_job_vacancy(self, file='job_vacancy.csv'):
        print(f'Загрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for name in reader:
                JobVacancy.objects.update_or_create(name=name)

    def import_cites(self, file='city.csv'):
        print(f'Загрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for name in reader:
                City.objects.update_or_create(name=name)
