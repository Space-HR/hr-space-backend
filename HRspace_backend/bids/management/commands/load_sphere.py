import csv

from django.core.management.base import BaseCommand
from bids.models import Sphere


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.import_cites()
        print('Загрузка списка городов завершена.')

    def import_cites(self, file='sphere.csv'):
        print(f'Загрузка данных из {file}')
        path = f'./data/{file}'
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                Sphere.objects.update_or_create(row)
