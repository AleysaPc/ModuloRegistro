from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro

#Buscar la explicacion del codigo 


def registrar_documento(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_documentos')
        else:
            form = RegistroForm()
        return render(request, 'registro/registrar.html', {'form': form})