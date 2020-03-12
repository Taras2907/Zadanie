from django.core.management.base import BaseCommand
from django.conf import settings
import csv

BASE_DIR = settings.BASE_DIR


def import_from_cv(filepath: str) -> list:
    try:
        with open(filepath) as f:
            row_data = csv.DictReader(f)
            data = [{k:v for k, v in row.items()} for row in row_data]
            return data
    except FileNotFoundError:
        print(f'file {filepath} is not found please check is the path correct')


class Command(BaseCommand):
    def handle(self, **options):
        data = import_from_cv(f'{BASE_DIR}/res_data.csv')
        self.stdout.write(f'Successfully ended {BASE_DIR}')

