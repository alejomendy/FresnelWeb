from django.contrib import admin
from django.urls import path
from .views import main_page,prueba

urlpatterns = [
    path('',prueba, name='calcular'),
    path('resultado/',main_page, name='resultado'),    
]