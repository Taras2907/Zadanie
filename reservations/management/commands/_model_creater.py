from reservations.models import ClientModel, ReservationModel


def create_client(properties:dict) -> ClientModel:
    client = ClientModel.objects.create(
        name=properties["name"],
        phone=properties["phone"],
        email=properties["email"]
    )
    client.save()
    return client


def create_reservation(properties: dict, client: ClientModel) -> ReservationModel:
    reservation = ReservationModel.objects.create(
        number=properties["number"],
        arrival=properties["arrival"],
        departure=properties["departure"],
        client_room=properties["no_of_people"],
        status=properties["status"],
        client=client
    )
    reservation.save()
    return reservation

