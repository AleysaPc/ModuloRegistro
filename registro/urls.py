from django.urls import path
from .import views

urlpatterns = [
    path('registrar/', views.registrar_documento, name='registrar_documento'),
    path('', views.lista_documentos, name='lista_documentos'),
]