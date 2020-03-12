from django.db import models


class ClientModel(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=35)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ReservationModel(models.Model):
    number = models.IntegerField(unique=True)
    arrival = models.DateField()
    departure = models.DateField()
    client_room = models.IntegerField()
    client = models.ForeignKey('ClientModel', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('CANCELLED', "CANCELLED")
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="NEW")

    def __str__(self):
        return f'Reservation number {self.number}'
