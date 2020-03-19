from django.core.management.base import BaseCommand
from django.conf import settings
from reservations.models import ClientModel, ReservationModel
from ._csv_decorators import csv_reader

BASE_DIR = settings.BASE_DIR


def create_model(**kwargs):
    model = kwargs.get("model")
    model_props = dict()

    for field in model._meta.fields:
        model_props[field.name] = kwargs.get(field.name)

    instance = model.objects.create(**model_props)
    instance.save()

    return instance


class Command(BaseCommand):

    @csv_reader(f'{BASE_DIR}/res_data.csv')
    def handle(self, **options):

        for reserv in options.get("data"):
            client = create_model(**reserv, model=ClientModel)
            reservation = create_model(**reserv, client=client, model=ReservationModel)

            self.stdout.write(f'Reservation number {reservation.number} was successfully added to the database')
        self.stdout.write('Importing was successfully ended')

