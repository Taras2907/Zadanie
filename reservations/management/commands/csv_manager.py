from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from ._model_creater import create_client, create_reservation

BASE_DIR = settings.BASE_DIR

#10000000,2020-05-05,2020-05-16,Danielle Webb,+1-125-476-8450x273,kemperik@simpson.info,5,NEW


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
        reservations = import_from_cv(f'{BASE_DIR}/res_data.csv')
        for reserv in reservations:
            client = create_client(reserv)
            reservation = create_reservation(reserv, client)

            self.stdout.write(f'Reservation number {reservation.number} was successfully added to the database')
        self.stdout.write('Importing was successfully ended')

