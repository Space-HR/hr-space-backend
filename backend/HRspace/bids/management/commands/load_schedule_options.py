from django.core.management import BaseCommand
from bids.models import ScheduleOption


class Command(BaseCommand):
    help = 'Создаем графики работы'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Сменный'},
            {'name': 'Вахтовый'},
            {'name': '5/2 пн - пт'},
            {'name': 'Свободный'},
            {'name': 'Другой'}]
        ScheduleOption.objects.bulk_create(
            ScheduleOption(**schedule) for schedule in data)
        self.stdout.write(self.style.SUCCESS(
            'Графики работы успешно загруженны!'))
