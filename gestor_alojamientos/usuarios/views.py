from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .forms import PerfilForm, RegistroUsuarioForm
from .models import Perfil


class RegistroUsuarioView(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()

        messages.success(
            self.request,
            'Registro exitoso. Ahora podés iniciar sesión.'
        )

        return super().form_valid(form)

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'usuarios/perfil_form.html'
    success_url = reverse_lazy('usuarios:perfil')

    def get_object(self, queryset=None):
        perfil, creado = Perfil.objects.get_or_create(
            usuario=self.request.user
        )
        return perfil