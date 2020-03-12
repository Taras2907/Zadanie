from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from .models import ClientModel, ReservationModel
from .forms import ReservationForm


class ReservationsListView(generic.ListView):
    model = ReservationModel
    template_name = "reservations/index.html"
    context_object_name = "reservations"
    paginate_by = 10


class ReservationRetrieveView(generic.DetailView):
    model = ReservationModel
    template_name = "reservations/reservation_detail.html"
    context_object_name = "reservation"


class ReservationUpdateView(generic.UpdateView):
    context_object_name = "form"
    form_class = ReservationForm
    template_name = 'reservations/reservation_form.html'
    model = ReservationModel

    def get_success_url(self):
        return reverse('reservation-detail', kwargs={'pk': self.object.pk})
