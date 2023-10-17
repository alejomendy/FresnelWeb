from django.urls import path
from . import views

urlpatterns = [
    path('', views.fresnel_calculator, name='fresnel_calculator'),
]
