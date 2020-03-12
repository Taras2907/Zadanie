from django.core.exceptions import ValidationError
import datetime


def validate_reservation_date_bigger_than_yesterday(reservation_time):
    current_time = datetime.date.today()
    if reservation_time < current_time:
        raise ValidationError('Date of reservation should be bigger')

