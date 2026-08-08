from django.contrib import admin

from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'ciudad')
    search_fields = ('usuario__username', 'telefono', 'ciudad')
    list_filter = ('ciudad',)