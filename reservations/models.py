from django.db import models
from .validators import validate_reservation_date_bigger_than_yesterday


class ClientModel(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=35)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ReservationModel(models.Model):
    number = models.IntegerField(unique=True)
    arrival = models.DateField(validators=[validate_reservation_date_bigger_than_yesterday])
    departure = models.DateField(validators=[validate_reservation_date_bigger_than_yesterday])
    client_room = models.IntegerField()
    client = models.ForeignKey('ClientModel', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('CANCELLED', "CANCELLED")
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="NEW")

    def __str__(self):
        return f'Reservation number {self.number}'
