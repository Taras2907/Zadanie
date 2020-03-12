from django.contrib import admin
from reservations.models import ClientModel, ReservationModel


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    pass

