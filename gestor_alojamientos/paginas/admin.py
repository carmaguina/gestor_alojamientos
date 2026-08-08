from django.contrib import admin

from .models import MensajeContacto


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_creacion', 'leido')
    list_filter = ('leido', 'fecha_creacion')
    search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('fecha_creacion',)
