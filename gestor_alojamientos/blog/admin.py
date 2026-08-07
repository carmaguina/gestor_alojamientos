from django.contrib import admin

from .models import Post


@admin.action(description='Marcar posts seleccionados como publicados')
def publicar_posts(modeladmin, request, queryset):
    queryset.update(publicado=True)


@admin.action(description='Marcar posts seleccionados como ocultos')
def ocultar_posts(modeladmin, request, queryset):
    queryset.update(publicado=False)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'publicado')
    list_filter = ('publicado', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    actions = [publicar_posts, ocultar_posts]