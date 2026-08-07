from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistroUsuarioForm


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