from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea
    )

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')

        if len(mensaje.strip()) < 10:
            raise forms.ValidationError(
                'El mensaje debe tener al menos 10 caracteres.'
            )

        return mensaje