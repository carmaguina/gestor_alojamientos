from django.conf import settings
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    telefono = models.CharField(max_length=30, blank=True)
    ciudad = models.CharField(max_length=80, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    