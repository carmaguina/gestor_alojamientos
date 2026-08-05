from django.urls import path
from . import views

app_name = "alojamientos"

urlpatterns = [
    path("", views.UnidadListView.as_view(), name="unidad_list"),
    path("<int:pk>/", views.UnidadDetailView.as_view(), name="unidad_detail"),
    path("crear/", views.UnidadCreateView.as_view(), name="unidad_create"),
    path("<int:pk>/editar/", views.UnidadUpdateView.as_view(), name="unidad_update"),
    path("<int:pk>/eliminar/", views.UnidadDeleteView.as_view(), name="unidad_delete"),
]