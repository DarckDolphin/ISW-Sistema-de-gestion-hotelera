from django.contrib import admin
from .models import (
    Hotel, Habitacion, Huesped, Reserva,
    Servicio, ReservaServicio, Empleado, Factura
)

admin.site.register([
    Hotel, Habitacion, Huesped, Reserva,
    Servicio, ReservaServicio, Empleado, Factura
])
