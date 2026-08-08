from django.db import models


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'mensaje de contacto'
        verbose_name_plural = 'mensajes de contacto'

    def __str__(self):
        return f'{self.nombre} - {self.email}'
