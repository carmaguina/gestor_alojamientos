from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo