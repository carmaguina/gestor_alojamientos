from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repetir contraseña',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        datos = self.cleaned_data

        if datos.get('password') != datos.get('password2'):
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return datos.get('password2')

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('telefono', 'ciudad', 'fecha_nacimiento', 'bio')
        labels = {
            'telefono': 'Teléfono',
            'ciudad': 'Ciudad',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'bio': 'Biografía',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }