from django.urls import path, include
from .views import ReservationsListView, ReservationUpdateView ,ReservationRetrieveView

urlpatterns = [
    path("", ReservationsListView.as_view(), name="reservations-list"),

    path("reservation/<int:pk>/", ReservationRetrieveView.as_view(), name="reservation-detail"),

    path("reservation/update/<int:pk>/", ReservationUpdateView.as_view(), name="reservation-update"),

]