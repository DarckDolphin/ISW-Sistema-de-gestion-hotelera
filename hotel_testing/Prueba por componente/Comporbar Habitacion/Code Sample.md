# models.py
from django.db import models
from django.db.models import Q

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Simple'),
        ('double', 'Doble'),
        ('suite', 'Suite'),
    )
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)

    def __str__(self):
        return f"Hab {self.number} ({self.get_room_type_display()})"

    def is_available(self, start_date, end_date):
        """
        Devuelve True si no existe ninguna reserva que se solape
        con el rango [start_date, end_date].
        """
        overlap = self.reservations.filter(
            Q(check_in__lte=end_date) & Q(check_out__gte=start_date)
        ).exists()
        return not overlap

class Reservation(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Reserva {self.id} | {self.room} | {self.check_in}–{self.check_out}"


# services.py
from .models import Room

class RoomAvailabilityService:
    @staticmethod
    def is_available(room_id, start_date, end_date):
        room = Room.objects.get(pk=room_id)
        return room.is_available(start_date, end_date)


# views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .services import RoomAvailabilityService

def check_availability(request, room_id):
    """
    Endpoint: /rooms/<room_id>/availability/?start=YYYY-MM-DD&end=YYYY-MM-DD
    Devuelve JSON con la disponibilidad de la habitación.
    """
    start = request.GET.get('start')
    end = request.GET.get('end')
    room = get_object_or_404(Room, pk=room_id)
    available = room.is_available(start, end)
    return JsonResponse({
        'room': room.number,
        'available': available
    })


## Fragmento de Codigo Desarrolado por: Frank Ernesto Cortiñas Peña
## Proyecto: ISW-Sistema de Gestion Hotelera
## Equipo: DarckDolphin
## Revisado por: Maydelín del Carmen Ibarra Núñez 