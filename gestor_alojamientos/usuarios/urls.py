from django.urls import path

from .views import PerfilUpdateView, RegistroUsuarioView

app_name = 'usuarios'

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/', PerfilUpdateView.as_view(), name='perfil'),
]