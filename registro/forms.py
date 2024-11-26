from django import forms
from .models import Registro, Destinatario

# Formulario basado en el modelo Registro
class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['codigo', 'fecha', 'hora', 'referencia', 'institucion', 'remitente', 'cargoRemitente', 'observacion', 'fojas', 'estado', 'destinatarios']

    # Validaciones personalizadas o campos adicionales pueden ir aquí
