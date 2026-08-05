from django.db import models

from alojamientos.models import Unidad


class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    notas = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Huésped"
        verbose_name_plural = "Huéspedes"


class Reserva(models.Model):
    ESTADO_CONSULTA = "consulta"
    ESTADO_PRE_RESERVA = "pre_reserva"
    ESTADO_RESERVADA = "reservada"
    ESTADO_SENIADA = "seniada"
    ESTADO_CANCELADA = "cancelada"
    ESTADO_FINALIZADA = "finalizada"

    ESTADOS = [
        (ESTADO_CONSULTA, "Consulta"),
        (ESTADO_PRE_RESERVA, "Pre-reserva"),
        (ESTADO_RESERVADA, "Reservada"),
        (ESTADO_SENIADA, "Señada"),
        (ESTADO_CANCELADA, "Cancelada"),
        (ESTADO_FINALIZADA, "Finalizada"),
    ]

    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, related_name="reservas")
    huesped = models.ForeignKey(Huesped, on_delete=models.PROTECT, related_name="reservas")
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    cantidad_personas = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default=ESTADO_CONSULTA)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monto_senia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.huesped} - {self.unidad} ({self.fecha_ingreso} a {self.fecha_egreso})"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_ingreso"]
