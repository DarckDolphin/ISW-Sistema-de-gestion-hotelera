# Generated by Django 5.1.7 on 2025-04-11 06:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('clasificacion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('numero_habitaciones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento_identidad', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('precio_por_noche', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada'), ('mantenimiento', 'Mantenimiento')], default='disponible', max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='hotel_app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('numero_huespedes', models.IntegerField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=50)),
                ('habitacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservas', to='hotel_app.habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='hotel_app.huesped')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField()),
                ('importe_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facturas', to='hotel_app.reserva')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios', to='hotel_app.reserva')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='hotel_app.servicio')),
            ],
        ),
    ]
