from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    nombre             = models.CharField(max_length=100)
    direccion          = models.TextField()
    clasificacion      = models.IntegerField(
                            validators=[MinValueValidator(1), MaxValueValidator(5)]
                        )
    numero_habitaciones= models.IntegerField()

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupada',    'Ocupada'),
        ('mantenimiento', 'Mantenimiento'),
    ]

    numero_habitacion = models.IntegerField()
    tipo               = models.CharField(max_length=50)
    precio_por_noche   = models.DecimalField(max_digits=10, decimal_places=2)
    estado             = models.CharField(
                            max_length=50,
                            choices=ESTADO_CHOICES,
                            default='disponible'
                        )
    hotel              = models.ForeignKey(
                            Hotel,
                            on_delete=models.CASCADE,
                            related_name='habitaciones'
                        )

    def __str__(self):
        return f"{self.hotel.nombre} - Hab. {self.numero_habitacion}"


class Huesped(models.Model):
    nombre               = models.CharField(max_length=50)
    apellido             = models.CharField(max_length=50)
    documento_identidad  = models.CharField(max_length=20, unique=True)
    telefono             = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico   = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada','Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    fecha_entrada    = models.DateField()
    fecha_salida     = models.DateField()
    numero_huespedes = models.IntegerField()
    estado           = models.CharField(
                          max_length=50,
                          choices=ESTADO_CHOICES,
                          default='pendiente'
                       )
    huesped          = models.ForeignKey(
                          Huesped,
                          on_delete=models.CASCADE,
                          related_name='reservas'
                       )
    habitacion       = models.ForeignKey(
                          Habitacion,
                          on_delete=models.SET_NULL,
                          null=True,
                          blank=True,
                          related_name='reservas'
                       )

    def __str__(self):
        return f"Reserva #{self.id} — {self.huesped}"


class Servicio(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio      = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class ReservaServicio(models.Model):
    reserva  = models.ForeignKey(
                  Reserva,
                  on_delete=models.CASCADE,
                  related_name='servicios'
               )
    servicio = models.ForeignKey(
                  Servicio,
                  on_delete=models.CASCADE,
                  related_name='reservas'
               )
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}×{self.servicio.nombre} en Reserva {self.reserva.id}"


class Empleado(models.Model):
    nombre             = models.CharField(max_length=50)
    apellido           = models.CharField(max_length=50)
    puesto             = models.CharField(max_length=100)
    telefono           = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} — {self.puesto}"


class Factura(models.Model):
    fecha_emision = models.DateField()
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago   = models.CharField(max_length=50, blank=True, null=True)
    reserva       = models.ForeignKey(
                        Reserva,
                        on_delete=models.SET_NULL,
                        null=True,
                        blank=True,
                        related_name='facturas'
                    )

    def __str__(self):
        return f"Factura #{self.id} — {self.importe_total} €"
