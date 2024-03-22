import csv

from django.core.management.base import BaseCommand
from bids.models import Country


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.import_cites()
        print('Загрузка списка стран завершена.')

    def import_cites(self, file='country.csv'):
        print(f'Загрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                Country.objects.update_or_create(row)
