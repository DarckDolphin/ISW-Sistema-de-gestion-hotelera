from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'hoteles', HotelViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'huespedes', HuespedViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'reserva-servicios', ReservaServicioViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'facturas', FacturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
