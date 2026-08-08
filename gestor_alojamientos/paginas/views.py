from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactoForm


def inicio(request):
    return render(request, 'paginas/inicio.html')


def acerca(request):
    return render(request, 'paginas/acerca.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            messages.success(
                request,
                'Tu mensaje fue enviado correctamente.'
            )
            return redirect('paginas:contacto')
    else:
        form = ContactoForm()

    return render(request, 'paginas/contacto.html', {'form': form})