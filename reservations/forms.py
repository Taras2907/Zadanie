from django import forms
from .models import ReservationModel


class ReservationForm(forms.ModelForm):

    def clean_arrival(self):
        arrival = self.cleaned_data["arrival"]
        departure = self.instance.departure
        if arrival > departure:
            raise forms.ValidationError("Departure date should be bigger than arrival")
        return arrival

    class Meta:
        model = ReservationModel
        fields = ['arrival', 'departure', 'status']

