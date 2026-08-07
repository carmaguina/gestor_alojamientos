from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Unidad


class UnidadListView(ListView):
    model = Unidad
    template_name = "alojamientos/unidad_list.html"
    context_object_name = "unidades"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "")

        if query:
            queryset = queryset.filter(nombre__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class UnidadDetailView(DetailView):
    model = Unidad
    template_name = "alojamientos/unidad_detail.html"
    context_object_name = "unidad"


class UnidadCreateView(LoginRequiredMixin, CreateView):
    model = Unidad
    fields = ["nombre", "descripcion", "capacidad", "activa"]
    template_name = "alojamientos/unidad_form.html"
    success_url = reverse_lazy("alojamientos:unidad_list")


class UnidadUpdateView(LoginRequiredMixin, UpdateView):
    model = Unidad
    fields = ["nombre", "descripcion", "capacidad", "activa"]
    template_name = "alojamientos/unidad_form.html"
    success_url = reverse_lazy("alojamientos:unidad_list")


class UnidadDeleteView(LoginRequiredMixin, DeleteView):
    model = Unidad
    template_name = "alojamientos/unidad_confirm_delete.html"
    success_url = reverse_lazy("alojamientos:unidad_list")
